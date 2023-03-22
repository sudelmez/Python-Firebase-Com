file=open("dosya.txt","r") #read file

veri = file.read()
print(veri)

#file.seek(10)...starts reading after 10 characters on file
for satir in file:
    print(satir)

file.close()