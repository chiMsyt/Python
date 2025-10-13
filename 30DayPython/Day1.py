'''
addition (+)
subtraction (-)
multiplication (*)
division (/)
exponential (**)
modulus (%)
floor division operator (//)

data types: check with type()
10 - int
3.14 - float
1 + 3j - complex number
"Tim" - string
[1, 2, 3] - list
{"name":"Tim"} - dictionar : unordered, key value pair format
{9.8, 3.14, 2.7} - set : not ordered, only stores unique items
(9.8, 3.14, 2.7) - tuple : ordered, cannot be modified, immutable
'''

# Exercise 1

num1 = 3
num2 = 4

firstOperation = num1 + num2
secondOperation = num1 - num2
thirdOperation = num1 * num2
fourthOperation = num1 % num2
fifthOperation = num1 / num2
sixthOperation = num1 ** num2
seventhOperation = num1 // num2

operations = f"addition : {firstOperation}, subtraction : {secondOperation}, multiplication : {thirdOperation}, modulus : {fourthOperation}, division : {fifthOperation}, exponentional : {sixthOperation}, floor division : {seventhOperation}."

print(operations)

myName = "Tim"
lastName = "T"
myCountry = "Philippines"
message = f"My name is {myName} {lastName}, I am from the {myCountry}. I am enjoying 30 days of Python."

print(message)

dataOne = 10
dataTwo = 9.8
dataThree = 3.14
dataFour = 4 - 4j
dataFive = ['Tim', 'Chanel', 'Marsella']
dataSix = myName
dataSeven = lastName
dataEight = myCountry

checkTypes = f"{type(dataOne), type(dataTwo), type(dataThree), type(dataFour), type(dataFive), type(dataSix), type(dataSeven), type(dataEight)}"
print(checkTypes)

# Exercise 3

'''
1. write an example for different python data types such as number(int, float, complex), str, bool, list, tuple, set, and dict
2. find the Euclidian distance between (2, 3) and (10, 8)
'''

number1 = 10
number2 = 3.14
number3 = 1 + 3j
thisIsString = "Hello"
thisIsBool = True
thisIsList = [123, 456, 789]
thisIsTuple = (123, 456, 789)
thisIsSet = {123, 456, 789}
thisIsDict = {'numbers' : "1234567890"}

print(type(number1))
print(type(number2))
print(type(number3))
print(type(thisIsString))
print(type(thisIsBool))
print(type(thisIsList))
print(type(thisIsTuple))
print(type(thisIsSet))
print(type(thisIsDict))

findEuclidian = int(input("First number: "))