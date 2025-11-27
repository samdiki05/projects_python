#position , name, age, level, salary
se1 =[ "Software Engineer", " Max", 20, "Junoir", 500]
se2 =[ "Software Engineer", " Lisa", 24, "Senoir", 700]
d1 = ["Designer", "Philipp"]
# class


class SoftwareEngineer:

    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    # instance method
    def code(self):
        print(f"{self.name} is writing code...")
        
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")
    
    def information(self):
        information = f"{self.name} , age = {self.age}, level = {self.level}"
        return information
    
        #dunder method
    def __str__(self):
        information = f"{self.name} , age = {self.age}, level = {self.level}"
        return information
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

    
#imstance:
se1 = SoftwareEngineer(" Max", 20, "Junoir", 500)
se2 = SoftwareEngineer(" Lisa", 24, "Senoir", 700)
se3 = SoftwareEngineer(" Lisa", 24, "Senoir", 700)

#se1 = SoftwareEngineer(" Max", 20, "Junoir", 500)
#print(se1.name, se1.age)
#print(SoftwareEngineer.alias)
#se2 = SoftwareEngineer(" Lisa", 24, "Senoir", 700)
#print(SoftwareEngineer.alias)

se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("Javascript")
#print(se1.information())
print(SoftwareEngineer.entry_salary(27))

# Recap
# create a class (blueprint)
# create a instance(object)
# class vs instance
# instance attributes: defined in __int__(self)

# class attributes
