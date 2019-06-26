import os
#key is a python file for encryption
from key import enc

filename = input("Enter file name to Encrypt - ")

try:
	with open('ReportData/'+filename) as f:
		with open("Encryption/enc.txt", "w") as f1:
			for line in f:
				for ch in line:
					#enc from import statements
					if ch in enc:
						f1.write(enc[ch])

except EnvironmentError:
    print("File Not Found")
    exit()

print("Encrypted Successfully")
os.remove('ReportData/'+filename)