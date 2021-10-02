import base64

#Choose and open an input file
sourceFile = input("Open file: ")

try:
  FileInput = open(sourceFile, "rb")
except FileNotFoundError:
  print("File not found!")
  exit()

#Encode or Decode
mode = input("Encode / Decode: ")

#Writing to the output file
FileOutput = open("output.txt", "wb")

if mode == "Encode":
  FileOutput.write(base64.b64encode(FileInput.read()))
  print("File writed successfully, the result is in \"output.txt\"")
elif mode == "Decode":
  FileOutput.write(base64.b64decode(FileInput.read()))
  print("File writed successfully, the result is in \"output.txt\"")
else:
  print("Please choose \"Encode\" or \"Decode\"")

#Close File
FileInput.close()
FileOutput.close()