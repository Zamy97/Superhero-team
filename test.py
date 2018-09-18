# class Cat:
#
#     def crying(self):
#         print("Meow!")
#
# my_cats = list()
#
# my_cats.append(Cat())
# my_cats.append(Cat())
#
# for cat in my_cats:
#     cat.crying()

# class Cat:
#
#     def crying(self):
#         print("Meow!")
#
# my_cats = Cat()
# my_cats.crying()



# class Animal:
#
#     def __init__(self, name, sleep_time):
#         self.name = name
#         self.sleep_time = sleep_time
#
#     def sleep(self):
#         print("{} sleeps for {} hours.".format(
#              self.name, self.sleep_time ))
#
# kiddo = Animal("Spot", 16)
# kiddo.sleep()

class Animal:
    def __init__(self, name, nap_time):
        self.name = name
        self.nap_time = nap_time

    def sleep(self):
        print("{} slepps for {} hours.".format(
        self.name, self.nap_time))

class Dog(Animal):
    def bark(self):
        print("woof! Woof!")

my_doggo = Dog("Spot", 23)
my_doggo.sleep()
my_doggo.bark()
