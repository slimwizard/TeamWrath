import socket
import time
from binascii import hexlify
from time import sleep


# this program creates a simple messaging server. When a client connects
# a message is transmitted. The characters of the message are sent in time 
# intervals mapping to 0 and 1, allowing us to send a covert binary message 
# to our friend on the other side. 


# change IP and PORT constants to those of your own machine
ZERO = 0.025
ONE = 0.1
PORT = 8000
IP = "192.168.0.101"

# creats socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

#listen for clients
server.listen(10)



while True:   
    try:        
        # client connects
        client, addr = server.accept()
        msg = "Hello, I am writing to you to let you in on a really amazing"
        msg += " secret. Trust me, you're gonna wanna know this..."
        msg += "Okay okay. The secret is ........   "
        msg += "............................................................... "
        msg += "Yeah sorry there is no secret. Really sorry about that. "
        msg += "I hope you can forgive me. Honestly though, if not oh well."
        msg += "No skin off my back! Well, anyway...I guess I'll talk to you later"
        covert = "This is my covert message! Hell Yeah!!" + "EOF"
        covert_bin = ""

        # translate covert message to binary
        for i in covert:
            covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)
                

        n = 0
        # sends overt message character then waits certain time interval depending 
        # on whether current character in the covert message is a 0 or 1
        for i in msg:       
            client.send(i)
            if covert_bin[n] == "0":
                time.sleep(ZERO)
            else:
                time.sleep(ONE)
            n = (n+1) % len(covert_bin)
        client.send("EOF")
        client.close()
    except:
        if KeyboardInterrupt:
            exit()
        

        