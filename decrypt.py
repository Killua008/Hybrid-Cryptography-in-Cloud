import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random 
import hybrid

def decryptAES(cipherAESd,cipherText):
    dec= cipherAESd.decrypt(cipherText)
    return dec

def decrypt(pk, ciphertext):
    d, n = pk
    m = [chr((char ** d) % n) for char in ciphertext]
    return m

pri = tuple(int(item) for item in input("Enter the Private Key: ").split(','))
cipherKey=[int(item) for item in input("Enter the AES Symmetric Key: ").split(',')]
cipherText=b'\t\x9d\x82\xe4\xc0\x16\xb1\xc6'
nonce= b'dim\xb9\xe6\x07\x95\xc7\xb9Op\xfb\xfdt\xf96'
decriptedKey=''.join(decrypt(pri,cipherKey))
print("Decrypting the AES Symmetric Key...")

decriptedKey=decriptedKey.encode('utf-8')
cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
decrypted=decryptAES(cipherAESd,cipherText)
print("\nDecrypting the message using the AES symmetric key.....")
print("decrypted message: ", decrypted)
