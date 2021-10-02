import base64

print("Created by: FaezFM212")
print("Version: 1")

#Choose and open an input file
sourcePath = input("Open file: ")

try:
  FileInput = open(sourcePath, "rb")
except FileNotFoundError:
  print("File not found!")
  exit()

#Encode or Decode
mode = input("Encode / Decode: ")

#Writing to the output file
savePath = input("Save as: ")
FileOutput = open(savePath, "wb")

if mode == "Encode":
  FileOutput.write(base64.b64encode(FileInput.read()))
  print("File writed successfully")
elif mode == "Decode":
  FileOutput.write(base64.b64decode(FileInput.read()))
  print("File writed successfully")
else:
  print("Please choose \"Encode\" or \"Decode\"")

#Close File
FileInput.close()
FileOutput.close()