import os.path

save_path = 'C:\\Users\\jsmul\\Desktop\\College Year 3\\Semester 2\\3D3 Computer Networks\\Project 2\\project 2 repo\\Joes work\\p2p\\P2P with threads\\p2p 4 peers\\rcvd_A\\DATABASE.TXT' 

file1 = open(save_path, "wb")

toFile = input("Write what you want into the field ")

file1.write(toFile)

file1.close()