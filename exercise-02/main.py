name = ["ram", "laxman", "bahrat", "shatrugun", 1]
print(name[0])
name[0] = "Hari"
print(name[:])

list1=[4,5,7,2,6]

    # find max value in an array
max = 0
for num in list1:
    if num > max:
        max = num

print(max)

# print "Max value element : ", max(list1)

    # lists in python
# matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[0])
print(matrix[2][1])

for row in matrix:
    for item in row:
        print(item)


number = [1,5,2,7,2,1]
number.append(7)
print(number)
number.insert(0,6)
print(number)
number.remove(5)
print(number)
print (9 in number)
print(number.count(6))
number.sort()
print(number)
number.reverse()
print(number)

    # remove duplicacy in array using loop
res = []
for i in number:
    if i not in res:
        res.append(i)

print ("The list after removing duplicates : " + str(res))

    # remove duplicacy in array using list comprehension
res = []
[res.append(x) for x in number if x not in res]

print ("The list after removing duplicates : " + str(res))


        # tuples in python
tuple = (2,4,3)
print(tuple.count(2))

print(tuple.index(3))


    # Dictionary in python
customer = {
    "name": "alex",
    "age": 22,
    "party": True
}

print(customer["name"])
customer["name"] = "saurav"
print(customer)
customer["address"] = "koteshwor"
print(customer)
print(customer.get("name"))
print(customer.get("city", "kathmandu"))



# number = input("enter your number: ")
# num_text = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five"
# }

# output =""
# for num in number:
#     output += num_text.get(num,"!") + " "
# print(output) 



        # functions in python
def greet_user(f_name, l_name):
    print(f"Hi {f_name} {l_name}")
    print("How are you?")


print("start")
greet_user("ram", "poudel")
greet_user(l_name="yadav", f_name="raju")
print("end")

# functions with return value
def square(number):
    return number * number

print(square(3))


            # Assignment
    # use function with dictionary with user input as above dictionary example