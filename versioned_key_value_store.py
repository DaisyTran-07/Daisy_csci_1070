class Person():
    
    def __init__(self, name, occupation, country, age):
        self.name = name
        self.occupation = occupation
        self.country = country
        self.age = age
        
    def display(self):
        print(f"I am {self.name}, a {self.age} years old college student in {self.country}.")

p1 = Person("Daisy", "St.Louis", "USA", 18)
p1.display()

