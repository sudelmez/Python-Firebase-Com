class Account:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("İsim: ",self.name)


acc=Account("Sude Ölmez")      
acc.info()