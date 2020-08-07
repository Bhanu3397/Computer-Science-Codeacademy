#A list is an ordered set of objects in Python. 
#Lists can contain more than just numbers.
mixed_list = ['Jenny', 61]
'''We’ve seen that the items in a list can be numbers or strings. They can also be other lists!'''
# Example:- heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]
#Zip:-If we wanted to create a list of lists that paired each name with a height, we could use the command zip.
#zip takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. 
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)
print(names_and_heights) # You won’t be able to see much about this object from just printing it,because it will return the location of this object in memory.
#To see the nested lists, you can convert the zip object to a list first
print(list(names_and_heights))

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names =zip(names,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

'''Empty Lists:-A list doesn’t have to contain anything! You can create an empty list like this:
empty_list = []
Growing a List: Append
We can add a single element to a list using .append().'''
orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

'''Growing a List: Plus (+):-When we want to add multiple items to a list, we can use + to combine two lists.
We can only use + with other lists. If we want to add a single element using +, we have to put it into a list with brackets ([]):
Example:- my_list + [4]'''
items_sold = ['cake', 'cookie', 'bread']
#Suppose the bakery wants to start selling 'biscuit' and 'tart':
items_sold_new = items_sold + ['biscuit', 'tart']
print(items_sold_new) #['cake', 'cookie', 'bread', 'biscuit', 'tart']

orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
# Create new orders here:
new_orders =orders+['lilac','iris']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

'''Range I:-Often, we want to create a list of consecutive numbers. For example, suppose we want a list containing the numbers 0 through 9:
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Python gives us an easy way of creating these lists using a function called range. 
The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9'''
list1 = range(0,9)
list2= range(0,8)
print(list1,list2) # prints range(0, 9) range(0, 8)
print(list1) # prints range(0, 9)
print(list(list1)) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list(list1),list(list2))

'''Range II:-For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
my_range2 = range(2, 9, 2)
print(list(my_range2)) #[2, 4, 6, 8]'''
list1 = range(5, 15, 3)
list2 = range(0,40,5)
print(list(list1))
print(list(list2))

first_names=['Ainsley','Ben','Chani','Depak']
age=[] #Empty list
age.append(42) # appending to empty list
all_ages=[32, 41, 29]+age # combining two lists
name_and_age=zip(first_names,all_ages) # zipping two lists together
ids=range(0,4) # creating ids with range

#Grade Book:- 
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects =["physics","calculus","poetry","history"]
grades=[98,97,85,88]
gradebook=list(zip(subjects,grades))
subjects.append('computer science')
grades.append(100)
gradebook.append(("visual arts", 93))
full_gradebook =last_semester_gradebook+gradebook
print(full_gradebook)

#Operations on Lists:-
''' Length of a List:-Often, we’ll need to find the number of items in a list, usually called its length.'''
list1 = range(2, 20, 3)
list1_len =len(list1) # Assigning length of list to list1_len variable
print(list1_len) # prints 9
'''Selecting List Elements I:-In Python, we call the order of an element in a list its index.
Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.'''
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4=employees[4] 
print(index4) # prints Ryan
print(len(employees))
print(employees[5])

'''Selecting List Elements II:-What if we want to select the last element of a list?
We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.'''
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element=shopping_list[-1]
element5=shopping_list[5]
print(last_element,element5)

'''Slicing Lists:- suitcase[start:end] here start can start or middle or end or even backwards like -1'''
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
print(beginning)
middle=suitcase[2:4]
print(middle)

#Slicing Lists II:-
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start=suitcase[:3]
end=suitcase[4:]
#If we want to select the last 3 elements of suitcase, we can also use this syntax:
last3=suitcase[-3:]
'''Counting elements in a list:-Suppose we have a list called letters that represents the letters in the word “Mississippi”:
letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
If we want to know how many times i appears in this word, we can use the function count:
num_i = letters.count('i')
print(num_i)
This would print out:
4'''
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes=votes.count('Jake')
print(jake_votes)

'''Sorting Lists I:-Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order. 
with sort we can't assign new variable with existing list, if you do it'll return None'''
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
# Sort addresses here:
print(addresses.sort()) #None
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort() 
print(names) # ['Albus', 'Harry', 'Hermione', 'Ron', 'Sirius']
### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
sorted_cities = cities.sort()
print(sorted_cities) #None

'''Sorting Lists II:-A second way of sorting a list is to use sorted. sorted is different from .sort() in several ways:
It comes before a list, instead of after.
It generates a new list.'''
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted=sorted(games)
print(games_sorted) # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']

##########################################
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len= len(inventory)
first=inventory[0] # First element in inventory
last=inventory[-1] # Last element in inventory
inventory_2_6= inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count('twin bed') # Checks how many twin bed's are in inventory
inventory.sort() # sort inventory
print(inventory) 
##########################################

# Make Some Pizzas:-
#https://www.youtube.com/watch?v=CINEiX_Y0K8&feature=emb_title
toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices=[2,6,1,3,2,7,2]
num_pizzas=len(toppings)
print("We sell {} different kinds of pizza!".format(num_pizzas))
pizzas=list(zip(prices,toppings))
#print(pizzas) # Unsorted ;ist
pizzas.sort()
print(pizzas) # sort list
cheapest_pizza= pizzas[0]
print(cheapest_pizza)
priciest_pizza= pizzas[-1]
print(priciest_pizza)
three_cheapest=pizzas[0:3]
print(three_cheapest)
num_two_dollar_slices= prices.count(2)
print(num_two_dollar_slices)

##############Some Examples using lists###########
#Write your function here
#For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
'''Write a function named larger_list that has two parameters named lst1 and lst2.
The function should return the last element of the list that contains more elements. 
If both lists are the same size, then return the last element of lst1.'''
#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10,5], [-10, 2, 5, 10]))
'''Create a function named more_than_n that has three parameters named lst, item, and n.
The function should return True if item appears in the list more than n times. 
The function should return False otherwise.'''
#Write your function here
def more_than_n(lst1,item,n):
  item_lst=lst1.count(item) 
  if item_lst > n:
    return True
  return False
#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

'''Create a function called append_size that has one parameter named lst.
The function should append the size of lst (inclusive) to the end of lst. 
The function should then return this new list.
For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.'''
#Write your function here
def append_size(lst1):
  size=len(lst1)
  lst1.append(size)
  return lst1
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

'''Write a function named combine_sort that has two parameters named lst1 and lst2.
The function should combine these two lists into one new list and sort the result. Return the new sorted list.'''
#Write your function here
def combine_sort(lst1,lst2):
  combine_set= lst1+lst2
  combine_set.sort()
  return combine_set
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

'''Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
If start is greater than 100, the function should return an empty list.'''
#Write your function here
def every_three_nums(start):
  if start >100:
    return []
  else:
    lst1=range(start,101,3)
    return list(lst1)
#Uncomment the line below when your function is done
print(every_three_nums(91))

'''Create a function named remove_middle which has three parameters named lst, start, and end.
The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed: '''
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

'''Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
Return either item1 or item2 depending on which item appears more often in lst.
If the two items appear the same number of times, return item1.'''
#Write your function here
def more_frequent_item(lst,item1,item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

'''Create a function named double_index that has two parameters: a list named lst and a single number named index.
The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.
If index is not a valid index, the function should return the original list.
For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
double_index([1, 2, 3, 4], 2)
After writing your function, un-comment the call to the function that we’ve provided for you to test your results.'''
'''  try:    
    new_value = lst[index]
    print(new_value)
    doubled_value=new_value*2
    print(doubled_value)
  except IndexError:
    return lst'''

#Write your function here
def double_index(lst,index):
  if index+1 > len(lst):
    return lst
  else:
    double=lst[index]*2
    lst[index]=double
    return lst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

'''Create a function called middle_element that has one parameter named lst.
If there are an odd number of elements in lst, the function should return the middle element. 
If there are an even number of elements, the function should return the average of the middle two elements.'''
#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

#Tuples:- https://www.youtube.com/watch?time_continue=60&v=yDvRR8nWMNI&feature=emb_title
