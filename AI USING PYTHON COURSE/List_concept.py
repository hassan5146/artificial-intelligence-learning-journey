#List
fruits=["Banana","Apple","Orange","Mango","Banana"]

print(fruits)

#Accessing elements
print(fruits[1])
print(fruits[-2])

#List method (Most Important)

fruits.append("5_Apple")     #append add item
print(fruits)

fruits.insert(1,"Grapes")    #insert add new item with your choice index
print(fruits)

fruits.remove("Banana")      #remove item one first remove not remove all duplicate item with same name .
print(fruits)

fruits.pop()                 #remove list last item
print(fruits)

fruits.sort()                #sort  list           
print(fruits)


for fruit in fruits:         #looping throught list
    print(fruit)