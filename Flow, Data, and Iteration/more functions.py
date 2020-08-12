#Write your function here
def divisible_by_ten(nums):
  count=0
  for num in nums:
    if num % 10 == 0:
      count+=1
  return count
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, "+name)
  return greeting
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Write your function here
def odd_indices(lst):
  new_list=[]
  i=0
  for lst[i] in lst:
    if i%2 ==1:
      new_list.append(lst[i])
    i+=1
  return new_list
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Write your function here
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Write your function here
def exponents(bases, powers):
  result=[]
  for base in bases:
    for power in powers:
       result.append(base**power)
  return result

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#Write your function here
def larger_sum(lst1, lst2):
  total1=0
  total2=0
  for num in lst1:
    total1 += num
  for num in lst2:
    total2+=num
  if total1 == total2:
    return lst1
  if total1 > total2:
    return lst1
  if total1 < total2:
    return lst2
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  if lst == []:
    return 0
  for num in lst:
    sum +=num
    if sum >= 9000:
      break
  if sum >= 9000:
    return sum
  else:
    return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

def over_nine_thousand(lst):
  sum = 0
  if lst == []:
    return 0
  for num in lst:
    sum +=num
    if sum > 9000:
      break
  if sum >= 9000:
    return sum
  else:
    return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 120,1000, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([120,1000, 5000]))

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1, lst2):
  index=0
  newlst=[]
  for val in lst1:
    if lst1[index] == lst2[index]:
      newlst.append(index)
    index+=1
  return newlst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 10, -10, 3, 3], [5, 10, -10, 3, 5]))

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))