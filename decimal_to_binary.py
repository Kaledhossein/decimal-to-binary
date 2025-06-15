"""
file: decimaltobinary.py
Converts a decimal int to a string of bits
 """

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
   bitString = ""
while decimal > 0: 
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
print(f"Binary number: {bitString}")

