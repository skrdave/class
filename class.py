class person:
    #class variables
    head = 1
    legs = 2
    hands = 2
    nose = 1

    #instance varibles
    #contructor
    def __init__(self,name,age,bank_balance):
        self.name = name
        self.age = age
        self.bank_balance = bank_balance


    #methods
    def details(self):
        print("my name is",self.name)
        print("I am",self.age,"years old")


    #modify
    def  modify(self):
        print("my old name is",self.name)
        new = input("enter new name")
        self.name = new
        print("my new name is",self.name)

#instances/objects
person1 = person("Bob",25,6)
person2 = person("johhnathan stanley",30,10000)
person3 = person("Bod.jr",5,10000000000)




person1.modify()
print(person3.bank_balance)