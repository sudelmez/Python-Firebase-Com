binary_string = input("2' lik Sistemde Sayı :")
 
try:
    decimal = int(binary_string,2)  
    print("Girilen Sayı 10' luk Sistemde :", decimal)    
    
except ValueError:
    print("Geçersiz Giriş")