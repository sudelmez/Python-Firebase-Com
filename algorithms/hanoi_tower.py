def Hanoi(n,kaynak,hedef,yedek):
    if n==1:
        print ("Disk 1 Taşı, Kaynak:",kaynak," Hedef:",hedef)
        return
    Hanoi(n-1, kaynak, yedek, hedef)    
    print ("Disk",n,"Taşı, Kaynak:",kaynak," Hedef:",hedef)
    Hanoi(n-1, yedek, hedef, kaynak)

n = 4
Hanoi(n,'A','B','C')