# apply same function to each element of a sequence
# return new list

simple_list = [1,2,3,4,5]

def new_list(x):
    return x*2

new_list = map(new_list, simple_list)

print(new_list)

# useing lambda function
new_list = map(lambda x:x*2, simple_list)

print(new_list)


def square(list1):
    list2 = []
    for i in list1:
        list2.append(i**2)
    return list2

print(square([2,3,4,5]))

print[i**2 for i in [2,3,4,5]]

