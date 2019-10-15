#Introducting List

motorcycles = ['honda', 'yamaha', 'sujuki']

#accessing element in a list

'''
print (motorcycles)
print (motorcycles[0])
print (motorcycles[1])
print (motorcycles[2])


#updating element in list
motorcycles[0] = 'hero'

print(motorcycles)

fruits = []
fruits.append('orenge')
fruits.append('mango')
fruits.append('banana')
fruits.insert(1,'apple')

print(fruits)
fruits.sort()
print (fruits)

print ('After Reverse Sort :')
fruits.sort(reverse = True)
print (fruits)

fruits.reverse()
print(fruits)

print ('After renove : ')

fruits.remove ('apple')
print (fruits)

print ('After Delete :')
del fruits [0]
print (fruits)

print
'''
#print (dir(fruits))
#print (help(fruits.remove))

cars = ['bmw','audi','toyota','audi','subaru','audi','cortina']
'''
print('Count Number of Occurences : ')
print(cars.count('audi'))

print(cars.index('audi'))

print ("\nHere is the sorted list:")
print(sorted(cars))



print("\nHere is the Original list")

print(cars)

print ("/nTotal number of car :")
print(len(cars))

print ("/nTotal number of car: ",end="")
print(len(cars))
'''
print (cars[0:3])

print (cars[-1])

print('='*30)