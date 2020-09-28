
# coding: utf-8


import socket
import math
#Ishaan Mehta E18CSE069 LabWeek4 EB02
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

server = socket.socket() #ipv4 and tcp if not passed

#we now have to bind the socket with a port number
server.bind(("localhost", 9999)) #localhost coz we're doing in our pc only


server.listen()
print("Waiting")
client, address = server.accept() #client's host & address
print(f"Client {address} appeared")
client.send(b"Hey, Welcome")

while True:
    enc = client.recv(1024).decode()
    print(f"Encrypted: {enc}")
    dec = ende(enc, key, 2)
    client.send(bytes(dec, "utf-8") )
    if(dec == "EXIT"):
        break
client.close()

