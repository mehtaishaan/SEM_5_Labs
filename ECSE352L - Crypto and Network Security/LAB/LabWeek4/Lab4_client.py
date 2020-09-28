
# coding: utf-8

import socket
import math
#Ishaan Mehta E18CSE069 LabWeek4
#Vigenere Cipher

def ende(text,key,choice):
    #choice 2 for decrypt, 1 for encrypt
    text = text.upper()
    key = key.upper()
    
    #functions to change letter to respective int value and vice versa
    to_num = lambda x: ord(x)-65
    to_str = lambda x: chr(x+65)

    #converting key to list of numbers and extending it as much is required for text
    key_list = list(map(to_num,list(key)))                
    key_list = key_list * math.ceil(len(text)/len(key_list))
    
    #converting text to list of number(" " will become -33(32-65))
    text_list = list(map(to_num,list(text)))               
    final_list = []
    counter = 0              #counter for key list
    
    for i in text_list:
        if(i == -33):        #for space(" ")
            appen = -33
        else:
            if(choice == 1):
                appen = (i + key_list[counter]) % 26       #encryption formula
            else:
                appen = (i - key_list[counter] + 26) % 26  #decryption formula

            counter += 1
        final_list.append(appen)
    return "".join(list(map(to_str,final_list)))    #joining final list after converting all values to letter


key = "crypto"
client = socket.socket()

client.connect(("localhost", 9999))

print(client.recv(1024).decode())
while True:
    txt = input("Enter something: ")
    enc = ende(txt, key, 1)

    client.send(bytes(enc,"utf-8"))
    dec = client.recv(1024).decode()
    print(f"Decrypted: {dec}")
    if(dec == "EXIT"):
        break
client.close()

