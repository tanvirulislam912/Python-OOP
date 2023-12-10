class Vaccine:
    def __init__(self, name, md_in, intrvl):
        self.name = name
        self. md_in = md_in
        self.intrvl = intrvl

class Person:
    def __init__(self, pname, age, ptype ="General Citizen"):
        self.pname = pname
        self. age = age
        self.ptype = ptype
        self.vac = ""         
        self.firstdose = False
        self.secdose = False

    def pushVaccine(self, vacN, dose = "1st dose"):
        if dose == "1st dose":
            if self.age >=25 or self.ptype == "student":
                self.vac = vacN        #storing object of vaccine/memory location
                self.firstdose = True
                print("1st dose done for", self.pname)
            else:
                print("Sorry", self.pname,"Minimum age for taking vaccine is 25 years now")

        else:
            if self.vac.name != vacN.name:
                print("Sorry", self.pname, "you cannot take 2 different vaccine")
            elif self.firstdose == True:
                self.secdose = True
                print("2nd dose done for", self.pname)
                            
    def showDetail(self):
        print("Name:",self.pname, "Age:",self.age, "Type:",self.ptype)
        print("Vaccine Name:", self.vac.name)
        if self.secdose == True:
            print("1st dose given")
            print("2nd dose given")
        elif self.firstdose == True:
            print("1st dose given")
            print("2nd dose:Please come after", self.vac.intrvl,"days")



astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)

p1 = Person("Bob", 21, "Student")
print("######################################")
p1.pushVaccine(astra)
print("######################################")
p1.showDetail()
print("######################################")
p1.pushVaccine(sin, "2nd Dose")
print("######################################")
p1.pushVaccine(astra, "2nd Dose")
print("######################################")
p1.showDetail()
print("######################################")
p2 = Person("Carol", 23, "Actor")
print("######################################")
p2.pushVaccine(sin)
print("######################################")
p3 = Person("David", 34)
print("######################################")
p3.pushVaccine(modr)
print("######################################")
p3.showDetail()
print("######################################")
p3.pushVaccine(modr,"2nd Dose")

