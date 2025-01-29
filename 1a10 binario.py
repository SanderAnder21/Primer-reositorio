print("decimal  binario  octal  hexadecimal")
for i in range (1, 11, 1):
   binario=bin(i)[2:]
   octal=oct(i)[2:]
   hexadecimal=hex(i)[2:]
   print(i, binario, octal, hexadecimal)
   