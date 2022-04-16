import os, random

from Crypto.Cipher import AES

from Crypto.Hash import SHA256

from Crypto import Random

import getpass


#encrypt Function
def encryptaes(key, filename,Ofilename1):

	blocksize = 64*1024

	Ofilename = Ofilename1 #Set Output File Name
	
	#Zfill pads left in the string with zeros to complete the width 
	filesize = str(os.path.getsize(filename)).zfill(16)
	
	#Initialization Vector
	InitVector=Random.new().read(16)


	encryptor = AES.new(key, AES.MODE_CBC, InitVector)

	
	#open the file(rb-It reads the file in binary mode)
	with open(filename, 'rb') as infile:

		with open(Ofilename, 'wb') as outfile: #write the file in binary mode

			outfile.write(filesize.encode("utf-8"))

			outfile.write(InitVector)

			while True:

				size = infile.read(blocksize)

				

				if len(size) == 0:

					break

				elif len(size) % 16 != 0:

					size += b"{" * (16 - (len(size) % 16))

				outfile.write(encryptor.encrypt(size))





def decryptaes(key, filename,Ofilename1):

	blocksize = 64*1024

	#Ofilename = filename #Set Output File Name
	Ofilename=Ofilename1

	
	#open the file(rb-It reads the file in binary mode)
	with open(filename, 'rb') as infile:

		filesize = int(infile.read(16))

		InitVector = infile.read(16)



		decryptor = AES.new(key, AES.MODE_CBC, InitVector)



		with open(Ofilename, 'wb') as outfile:

			while True:

				size = infile.read(blocksize)



				if len(size) == 0:

					break



				outfile.write(decryptor.decrypt(size))

			outfile.truncate(filesize)





def getKey(password):

	hasher = SHA256.new(password.encode("utf-8"))

	return hasher.digest()



