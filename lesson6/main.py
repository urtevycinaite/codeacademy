# # Simple print
# print("hello world")

# # Gets the same result but slightly different:
# print("hello", "world")

# # Gets the same result but is even more different:
# print(*["hello", "world"])

# # let's play with separator:
# print("hello world", sep=",")

# # some more
# print("hello", "world", sep=" amazing ", end=" .\n", flush=)

# greet = "Hello World"
# print(type(greet))

# number = 2022
# print(type(number))

# my_list = [1, 2, 3]
# print(type(my_list))

# print(type(my_list[0]))

# my_dictionary = {"name": "Albert"}
# print(type(my_dictionary))

# print(round(1.999))

# print(round(1.5555, 2))

# my_list = [45, 20, 14, 55]
# sorted_list = sorted(my_list)

# print(sorted_list)

# sorted_reverse_list = sorted(my_list, reverse=True)

# print(sorted_reverse_list)


# my_list = [45, 20, 14, 55]
# my_list = sorted(my_list)

# print(*my_list, sep="-")

# 1. Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:

# greet = "Hello World"
# print(type(greet))

# number = 2022
# print(type(number))

# my_list = [1, 2, 3]
# print(type(my_list))

# print(type(my_list[0]))

# name = "Urte"
# print(type(name))

# age = 23
# print(type(age))

# my_list = [555, "Jonas", "Febas", 1010]
# print(type(my_list))

# my_dictionary = {"name": "urte", "surname": "vycinaite"}
# print(type(my_dictionary))

# my_tuple = [1, 5, 8]
# print(type(my_tuple))

# 2. print all the items separated with "|"


# my_list = [555, "Jonas", "Febas", 1010]
# print(*my_list, sep="|")

# 3. create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

# my_list = [8.8813, 3]
# print(round(8.8813, 3))


# my_second_list = [2.776, 2]
# print(round(2.776, 2))

# 4. Create a list with student names and sort them, print the result to the terminal.

# my_list = ["Deividas", "Febas", "Urte", "Andrius"]
# sorted_list = sorted(my_list)

# print(sorted_list)

# sorted_reverse_list = sorted(my_list, reverse=True)
# print(sorted_reverse_list)

# 5. write a program that allows user to write in any float number and then round it.

# number = float(input("Enter your number:"))
# print(round(number))

# if number > 10:
#     print("Cool")
# else:
#     print("Wtf") 

# number = input("Enter nr:")
# print(round(number))

# if number == (type(float)):
#     print(round(number, 3))