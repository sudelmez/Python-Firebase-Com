decimal = input("Sayı: ")
binary = bin(int(decimal)).replace("0b", "")
# binary = bin(int(decimal))

print("Binary: {}".format(binary))