class Pet:
    
    def init(self, name="", type="", age=0):
        self.name = name
        self.type = type
        self.age = age

    
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age

    # Accessors (Getters)
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


def main():
    
    inputName = input("Enter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))

   
    Animal = Pet()

 
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

  
    print(f"The pet name is {Animal.getName()}")
    print(f"The pet type is {Animal.getType()}")
    print(f"The pet age is {Animal.getAge()}")


if __name__ == "main":
    main()
