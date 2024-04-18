#lists - using index place
lst = [10,20,30,40,50]
lst.append(7)
lst.append(6)
lst.append(5)
print(lst)

lst.remove(40)
print(lst)
lst.pop(2)
print(lst)

#reverse the list
lst.reverse()
print(lst)

#add 500 to the beginning 
lst[0] = 500
print(lst)

#start at index 1 and go to the end 
lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20)    #HELPFUL FOR HOMEWORK 2
print(count20)

#copy a list
copy_lst = lst
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)

#safer copy
new_copy = lst.copy()
print(new_copy)
new_copy[0] = 500
print(new_copy)
print(lst)

#slicing
new_copy = lst[:] #defaults to index placed 0 through the end of the list

#practice for loop
empty_lst = []
for val in lst:
    empty_lst.append(val)
print(empty_lst)

empty_lst = [0] * 10
print(empty_lst)
empty_lst[0] = 10

#squaring nums 1 to 9 with for loop
squares = []
for i in range(1, 10):
    squares.append(i**2)
print(squares)

#list comprehensions 
'''
squares = [x * x for x in range(1,10)]
print(squares)
'''
plus_5 = [val + 5 for x in lst]
print(plus_5)

#comprehension filters
small_vals = [val for val in lst if val < 20]
print(small_vals)


######################################################


#dictionaries - holds keys and values
    #use {} for dictionaries
fav_foods = {"Kathleen" : "pizza", "Hannah" : "pasta",
             "Kush" : "fries", "Yamill" : "fries"}
print(fav_foods)

hff = fav_foods["Hannah"] #Hannah = key
print(hff)

#2 ways to iterate through the dict.
for key in fav_foods:
   print(f"{key}'s favorite food is {fav_foods[key]}") #f = way to print string and imbed variables within

for person, food in fav_foods.items(): #.items returns person and food
   print(f"{person}'s favorite food is {food}")  #f = way to print string and imbed variables within

#bff = fav_foods["Bob"], not in program
if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)

#alternate way
if "Bob" not in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)
