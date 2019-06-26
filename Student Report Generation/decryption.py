import os
#key is a python file for encryption
from key import enc

filename = input("Enter file name to Decrypt - ")

dec = {v: k for k, v in enc.items()}

try:
	with open('Encryption/'+filename) as f:
		with open("Decryption/dec.txt", "w") as f1:
			for line in f:
				for ch in line:
					if ch in dec:
						f1.write(dec[ch])

except EnvironmentError:
    print("File Not Found")
    exit()

print("Decrypted Successfully")
os.remove('Encryption/'+filename)