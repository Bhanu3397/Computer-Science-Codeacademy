#Boolean Expressions
#We can create boolean expressions by comparing two values using these operators:
1 == 1 #True
2 != 4 #True
3 == 5 #False
#If Statements:-
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"
# Enter a user name here, make sure to make it a string
user_name = "Dave"
print(dave_check(user_name))

#Relational Operators II
def greater_than(x,y):
  if x == y:
    return "These numbers are the same"
  if x>y:
    return x
  if x<y:
    return y
print(greater_than(2,-2))

def graduation_reqs(credits):
  if credits <120:
    return "You don't have enough credits to graduate!"
  if credits >=120:
    return "You have enough credits to graduate!"
print(graduation_reqs(130))

#Boolean Operators: and
statement_one =(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two =(4 * 2 <= 8) and (7 - 1 == 6)
print(statement_one)
print(statement_two)
def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >=2.0:
    return "You meet the requirements to graduate!"
print(graduation_reqs(120,2.0))

#Boolean Operators: or
statement_one =(2 - 1 > 3) or (-5 * 2 == -10)
print(statement_one)
statement_two =(9 + 5 <= 15) or (7 != 4 + 3)
print(statement_two)
def graduation_mailer(gpa,credits):
  if gpa >=2.0 or credits >= 120:
    return True
print(graduation_mailer(1.9,120))

#Boolean Operators: not "The final boolean operator we will cover is not. 
#This operator is straightforward: when applied to any boolean expression it reverses the boolean value.
#So if we have a True statement and apply a not operator we get a False statement.
not True == False
not False == True
statement_one =not (4 + 5 <= 9)
print(statement_one)
statement_two =not (8 * 2) != 20 - 4
print(statement_two)
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not(credits >= 120):
    return "You do not have enough credits to graduate."
  if not(gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not(gpa >= 2.0) and not(credits >= 120):
    return "You do not meet either requirement to graduate!"
print(graduation_reqs(2.0, 120))
print(graduation_reqs(2.0, 100))
print(graduation_reqs(1.0, 120))
print(graduation_reqs(1.0, 100))

#Else Statements:-
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

print(graduation_reqs(0.0,0))

#Else If Statements:-We can use elif statements to control the order we want our program to check each of our conditional statements.
#First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.
def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >=3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa>=1.0:
    return "D"
  else:
    return "F"
print(grade_converter(3.2))

'''Try and Except Statements:-if, elif, and else statements aren’t the only way to build a control flow into your program. You can use try and except statements to check for possible errors that a user might encounter.
The general syntax of a try and except statement is
try:
    # some statement
except ErrorName:
    # some statement
First, the statement under try will be executed. If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement, then the try statement will terminate and the except statement will execute.
'''
def raises_value_error():
  try:
    raise ValueError
  except ValueError:
    print('You raised a ValueError!')
raises_value_error()

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")
divides(1,0)

def divide_two_numbers(x, y):
  result = x / y
  return result
try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")


def applicant_selector(gpa,ps_score,ec_count):
  if gpa>= 3.0 and ps_score >= 90 and ec_count >=3:
    return "This applicant should be accepted."
  elif (gpa>=3.0 and ps_score>=90) and  ec_count!=3:
    return "This applicant should be given an in-person interview."
  else:
      return "This applicant should be rejected."
  
print(applicant_selector(0.2,50,0))

'''Create a function named large_power() that takes two parameters named base and exponent.
If base raised to the exponent is greater than 5000, return True, otherwise return False'''
def large_power(base,exponent):
  if base**exponent > 5000:
    return True
  return False
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

def over_budget(budget, food_bill, electricity_bill, internet_bill,rent): 
  if (budget < electricity_bill+internet_bill+rent+food_bill):
    return True
  return False
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# Write your twice_as_large function here:
def twice_as_large(num1,num2):
  if num1 > num2*2:
    return True
  return False
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if num % 10 ==0:
    return True
  return False
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
#Return True if num1 and num2 do not sum to 10. Return False otherwise.
# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1,num2):
  if num1+num2 !=10:
    return True
  return False
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False