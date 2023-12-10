# class my_calculator:
#                                     #default constructor
#     def product(self, num1, num2=None, num3=None):                    #Limited Number
#         if num1 != None and num2 !=None and num3 != None:
#             print(num1 * num2 * num3)
#         elif num1 != None and num2 !=None:
#             print(num1 * num2)
#         else:
#             print(1 * num1)        


#     # def product(self, num1, num2, num3):                   #methodOverloading
#     #     print(num1 * num2 *num3)


# c1= my_calculator()
# c1.product(4)  
# c1.product(4,5)      
# c1.product(4,5,6)  



class my_calculator:
                                    #default constructor
    def product(self, *nums):                                #number of N
        pro = 1
        print(nums)
        for x in nums:
            pro = pro * x
        print(pro)    
        


c1= my_calculator()
c1.product(4 )  
c1.product(4,5)      
c1.product(4,5,6)  
c1.product(4,5,6,7)  
c1.product(4,5,6,7,8, 300)  

