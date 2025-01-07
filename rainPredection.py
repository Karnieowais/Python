class PrintingDetails:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def display_name(self):
        print(f"My name is {self.name} and i am working as a {self.designation}")


details = PrintingDetails("Owais", "Big Data engineer")
details.display_name()