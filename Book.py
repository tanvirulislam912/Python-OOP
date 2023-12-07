class Book:
    def __init__(self, name, author):
        self.name= name
        self.author= author
        self.price= 0


    # get_set method
    def set_price(self, price):                #price update
        self.price= price

    def get_price(self):                       #show updated price(return)
        return self.price        
    
    def details(self):
        print("Book Name:", self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price, "Taka")
        

# b1= Book("Opekka", "Humayun Ahmed") 
# b1.details()       
# b1.set_price(250)
# print(b1)
# # b1.details()   
# x= b1.get_price()
# print(x)    


# b2= Book("sahitto", "Rabindronath Takur") 
# b2.details()       
# b2.set_price(350)
# print(b2)
# #b2.details()   
# y= b2.get_price()
# print(y)  
