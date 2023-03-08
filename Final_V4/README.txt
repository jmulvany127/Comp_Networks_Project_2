README
SETUP
python , filepath, token . how token and peer lines work
We wrote our program in python. You will need to have python downloaded and installed into path for the most optimal experience. Anytime that you want to  
how to run locally and externally

COMPILE



RUN TESTCASES
TESTCASES
communication between another peer
SEND A MESSAGE
VIEW DATA
ADD TO DATABASE
SEND DATABASE
VIEW MODIFIED ON OTHER PEER

Testcase 1 instructions :
Instructions for Windows.
Open the testcases folder and go into the testcase1 folder.You should see two different folders,token_1 and token_2. It is going to be necessary to open two seperate command prompts.
We are going to want to run the p2p.py file in token_1, this can be run command prompt on windows by typing cmd into the file directory at the top of file explorer and then using the command python p2p.py in the prompt.
We are then going to want to run the p2p1.py in token_2. type cmd in token_2 and use "python p2p1.py" in the prompt.
Hopefully this should have opened both programs in seperate command prompts


Sending a message from 1 peer to another

Type cnct to begin the connection proccess in the prompt.
When asked about the peer number to connect to check which program is being run.
if you are running p2p.py and want to connect to p2p1.py, you need to input "2".
if you are running p2p1.py and want to connect to p2p.py, you need to input "1".
Then at this point the program should then ask you want you would like to send. We are sending a message, so type msg.
The receiving peer should react to this and say listening as message server ('127.0.0.1',50023)
Then on the sending peer type a message and hopefully it should come up on other command prompt

The database cannot be viewed or modified when the program has begun to connect.
Viewing the database
type "view" when prompted to by the program.
this should print out the database as how it currently is.

Adding a new entry into the database
Type "add" when prompted to by the program.
Type 'y' when prompted.
Fill in the data as it is requested one by one.
After completely filling in the data, you can now view the database and see the changes that you have made.

Sending your database to another peer.
I recommend having added to the database before sending it so that you can visually see a difference, you should also view the database on the receiving peer before you send the new database to it.

After adding to the database, type cnct to connect to other peer, type the token value of the receiving peer (1 or 2), this should get you to the place you were when sending a message. Except this time type file instead.
This should hopefully send the database to other peer, to check just type view on the receiving peer to ensure that the database was received.

This now is end of our demostration of our program, Feel free to type the wrong thing into the each and every prompt and try to break it. We would like to hear how it was broken as we wouldn't have much experience breaking program.
Try putting anything else into the program's main page.
Connection
Put the wrong peer number in while connecting, type a name in, put a number larger than the ammount of users in the token.txt file, 

try changing the token value of your peer in the token.txt file (it is the third value on any line, assuming that you are peer 1 you would need to change the token value on first line of the token.txt file).
try sending a message to peer 2 using it. Peer 2 should reject the connection as the token value is not on its list.
 


How to connect to another device
The program right now is hardcoded so that it can only connect to itself. If you would like to connect it to another device.You will need to get the ip of both devices that you want to connect together.
You need to change the token.txt file for both peers to do so.
In the token.txt file there are 3 pieces of data per line, ip address,port number,token value, which are in that order.
As we are changing the ip address, we are going to be changing the first piece of data. 
Lets just try to change line 1 and 2 as they are associated with peer number 1 and peer number 2. Both ip address in line 1 and line 2 are going to needed to be swapped out with the new ones for both token.txt files.
this should work






