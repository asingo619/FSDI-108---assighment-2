class Dog:
    def __init__(self, name):
        self.name = name


me = {
    "name" :"Andrew",
    "last" : "Singo",
    "email" : "test@email.com",
    "age" : 32,
    "hobbies" : [],
    "address" : {
        "street" : "main",
        "number" : "100"
    }

}

def print_data ():
    print(me["name"])
    print(me["name"] + " " + me["last"])

    # creat an object of Dog class
    fido = Dog("Fido")
    print(fido.name)

    print_data()

    