# print("hello, world")
"""This is a comment written in more than just one line"""
print("cheers, mate!")

# create a list
list = ["bike", "car", "truck"]
print(list)
# lenght
list = ["a", "b", "c"]
print(len(list))

# list of data types
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]
list3 = [True, False, True]

print(list1)
print(list2)
print(list3)


list = ["car", "jeep", "bus", "bike", "plane", "cycle"]
print(list[2:4])


list = ["car", "jeep", "bus", "bike", "plane", "cycle"]
print(list[-1])


list = ["car", "jeep", "bus", "bike", "plane", "cycle"]
print(list[:4])


list = ["car", "jeep", "bus", "bike", "plane", "cycle"]
print(list[2:])

# change item
list = ["a", "b", "c"]
list[2] = "e"
print(list)

list = ["a", "b", "c", "d"]
list[2:3] = ["e", "f"]
print(list)

# check if "football" is present in the list

list = ["football", "cricket", "hockey"]
if "hockey" in list:
    print("yes, 'hockey' is in the games list")

    # using append
    list = ["football", "cricket", "hockey"]
    list.append("cricket")
    print(list)

    # using remove
    list = ["football", "cricket", "hockey"]
    list.remove("football")
    print(list)

    # pop()
    list= ["car", "bike", "bus"]
    list.pop(1)
    print(list)

    #del
    list = ["football", "cricket", "hockey"]
    del list[0]
    print(list)

    # clear
    list = ["car", "bike", "bus"]
    list.clear()
    print(list)

    # loop through a list
    list = ["cat", "rat", "dog"]
    for x in list:
        print(x)

        # while loop
        i = 1
        while i <= 11:
            print(i)
            i = i + 1

            # list comprehension
            animal = ["cat", "rat", "dog"]
            newlist = []

            for x in animal:
                if "a" in x:
                    list.append(x)
            print(list)


