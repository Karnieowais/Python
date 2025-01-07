class PrintingDetails:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def display_details(self):
        print(f"My name is {self.name} and i am working as a {self.designation}")

    def get_details(self):
        return self.name, self.designation

details = PrintingDetails("Owais", "Big Data engineer")
details.get_details()
details.display_details()
