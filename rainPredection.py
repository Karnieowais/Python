class PrintingDetails:
    def __init__(self, name, designaton):
        self.name = None
        self.designation = None

    def displayName(self, name, designation):
        print(f"My name is {name} and i am working as a {designation}")


details = PrintingDetails("Owais", "Big Data engineer")
