class Person:
    def __init__(self, name, age, gender, religion, genotype, state, education, hobbies, physical_characteristics, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.religion = religion
        self.genotype = genotype
        self.state = state
        self.education = education
        self.hobbies = hobbies
        self.physical_characteristics = physical_characteristics
        self.occupation = occupation

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Religion: {self.religion}\n"
                f"Genotype: {self.genotype}\n"
                f"State: {self.state}\n"
                f"Education: {self.education}\n"
                f"Hobbies: {', '.join(self.hobbies)}\n"
                f"Physical Characteristics: {self.physical_characteristics}\n"
                f"Occupation: {self.occupation}")

# Create an instance of Person with sample data
person = Person(
    name="John Doe",
    age=30,
    gender="Male",
    religion="Christianity",
    genotype="AA",
    state="California",
    education="Bachelor's Degree in Computer Science",
    hobbies=["Reading", "Hiking", "Gaming"],
    physical_characteristics="6 feet tall, brown hair, blue eyes",
    occupation="Software Engineer"
)

# Print the details of the person
print(person)
