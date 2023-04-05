while True:
    num= input("number: ")    
    try:
        val=int(num)       
        if val < 0 or val > 100:
            print("Number should be between 0-100.")
            continue
        break
    except ValueError:
        print("Not a number!")
print("Pressed number: ",val)
