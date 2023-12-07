# from folder_name import class_name

from PythonOOP import Book                                 #Not same folder

b1=Book.Book("Opekka", "Humayun Ahmed") 
b1.details()       
b1.set_price(250)
print(b1)
# b1.details()   
x= b1.get_price()
print(x)   


b2=Book.Book("sahitto", "Rabindronath Takur") 
b2.details()       
b2.set_price(350)
print(b2)
#b2.details()   
y= b2.get_price()
print(y)  