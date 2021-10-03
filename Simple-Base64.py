import base64
import time

print("Created by: FaezFM212")
print("Version: 1.1\n")

#Choose and open an input file
sourcePath = input("Open file: ")

try:
  File = open(sourcePath, "rb")
except FileNotFoundError:
  print("File not found!")
  time.sleep(1)
  exit()

#Encode or Decode
mode = input("Encode / Decode: ")

#Processing
base64String = ""

if mode == "Encode":
  base64String = base64.b64encode(File.read())
elif mode == "Decode":
  base64String = base64.b64decode(File.read())
else:
  print("Please choose \"Encode\" or \"Decode\"")
  time.sleep(1)
  exit()

#Close File
File.close()

#Write to output file
savePath = input("Save as: ")
File = open(savePath, "wb")

File.write(base64String)
print("File writed successfully")

#Close File
File.close()