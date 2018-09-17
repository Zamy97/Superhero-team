
class Dog:
    greeting = "woof!"

    def __init__(self, name):
        self.name = name



    def bark(self):
        print(self.greeting)


# if __name__ == "__main__":
#     my_dog = Dog("Spot")
#     my_other_dog = Dog("Mac")
#     print(my_dog.name)
#     print(my_other_dog.name)

my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")

print(my_first_dog.name)
print(my_second_dog.name)

my_first_dog.bark()
my_second_dog.bark()



class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
