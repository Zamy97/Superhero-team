
class Dog:
    greeting = "woof!"

    def __init__(self, name):
        self.name = name



    def bark(self):
        print(self.greeting)


if __name__ == "__main__":
    my_dog = Dog("Spot")
    print(my_dog.name)
