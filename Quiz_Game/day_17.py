class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Arun")
user_2 = User("002", "Anju")
user_3 = User("003", "Ankit")

# print(user_1.id, user_1.username)
# print(user_2.id, user_2.username)
# print(user_3.id, user_3.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print()
print(user_2.followers)
print(user_2.following)


# creating your own class day_27_TKINTER 17
# id is the attribute that will be passed everytime
# when we create an object of the respective class.
# pass will bypass the need of class definition, we can define the class
# without getting the indentation error.
# this (id) is an attribute made by using the user_1 object.
# a constructor in python is made by the __init__() function means initialization
# function. this is a special function
# declared by
# class Car:
#   def __init__(self):
# self.id will be replaced by object_name.id whenever we create an object.
#         in this function we will create the starting values of our attributes.
# if we want some parameter not to be given with every object created,
# then we can just write its initial value inside the __init__() function
