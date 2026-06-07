#############-Advanced python functions-##############
# 1.------------Lambda function------------
##It is small anonymous function . Anonymous means the function does not have a name
##It is useful when a function is needed only once and does not need to be reused elsewhere
#syntax: lambda arguments:expression

#for example
#--adding two numbers--
add=lambda a,b:a+b
print(add(3,2))  #output is 5

#----squaring----
square=lambda x:x*x
print(square(4)) #output is 16

#why use lambda function--
#reduces code length, easy to use for simple operations
#commonly used with ***map(),filter(),and sorted()***

#real life example--->imagine an online shopping application that needs to calculate an 18% GST
gst=lambda amount:amount*0.18  #18% means 0.18 because % is per hundred 18% = 18/100 = 0.18
print(gst(1000))      #output is 180.0




# 2.------------Map function----------
#it is applies the same operation to every item in a collection
#syntax: map(function,iterable)
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))     #output [2, 4, 6, 8, 10]



# 3.-----------Filter function--------
#it is selects only the items that satisfy a condition
#syntax: filter(function,iterable)
numbers=[1,2,3,4,5,6]
even_numbers=filter(lambda x:x%2==0,numbers)
print(list(even_numbers))    #[2, 4, 6]



# 4.----------Reduce function--------
#it is combines all values into a single value,  it repeatedly performs an operation until only one result remains
#syntax: from functools import reduce
from functools import reduce
numbers=[1,2,3,4]
result=reduce(lambda x,y:x+y,numbers)
print(result)               #output : 10




# 5.----------Zip function----------
#it is combines multiple collections together
name=["raju","ravi","rani"]
marks=[80,90,99]
result=list(zip(name,marks))
print(result)                #output: [('raju', 80), ('ravi', 90), ('rani', 99)]



# 6.----------Enumerate function-------
# it is automatically adds the index numbers
fruits=["apple","banana","mango"]
for index,fruits in enumerate(fruits):
    print(index,fruits)          #output : 0 apple
                                 #         1 banana
                                 #         2 mango
    


# 7.----------Sorted function---------
# it is sorts data in ascending or descending order
numbers=[3,2,5,1]
print(sorted(numbers))               #output : [1, 2, 3, 5]
print(sorted(numbers,reverse=True))  #output : [5, 3, 2, 1]



# 8.----------Any function------------
# it is returns true if at least one value is true
values=[False,False,True]
print(any(values))                  #output : True



# 9.----------All function------------
#it is returns true only when every value is true
marks=[70,80,90]
print(all(mark>50 for mark in marks))  #output : True


# 10.---------isinstance function----------
#it is checks whether a variable belongs to a particular data type
age=21
print(isinstance(age,int))          #output : True
