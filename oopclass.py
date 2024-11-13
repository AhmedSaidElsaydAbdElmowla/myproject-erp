class pepole:

    unumber = 0 
    

    not_allowed = ["sera" , "jera"]

    def __init__(self, name, age, phone, gender):
    
        self.fname = name
        self.age = age
        self.phone = phone
        self.gender = gender
        pepole.unumber += 1 

    
    def full(self):

        if self.fname in pepole.not_allowed:
            return ValueError("name is not allowed")
        
        else:
            return f"{self.fname} {self.age} {self.phone} {self.gender}"
    
    
    def title(self):
        if self.gender == "male" :
            return f"Hello mr {self.fname} "
        
        elif self.gender == "female":
            return f"Hello miss {self.fname} "
        
    
    def all(self):
        return f"{self.title()}, your All info Is: {self.full()}"


personOne = pepole("ahmed", "25", "011", "male")
personTwo = pepole("sera", "30", "010", "male")
personThree = pepole("soso", "30", "012", "female")


#print(personThree.title())

print("////////////////////////////////////////")
print(personOne.all())
print(personTwo.all())
print(personThree.all())
print("////////////////////////////////////////")
print(pepole.unumber)




# print(personOne.fname, personOne.age)
# print(personTwo.fname, personTwo.age)
# print(personThree.fname, personThree.age)