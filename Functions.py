def create_spreadsheet(title,row_count= 1000): 
    #Here row_count set to default to 1000, and we can change the value later in the function 
  print("Creating a spreadsheet called "+title+" with "+str(row_count)+" rows")
# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
# Prints "Creating a spreadsheet called Downloads with 1000 rows"
create_spreadsheet("Applications",row_count =10)
# Prints "Creating a spreadsheet called Applications with 10 rows"

#Functions can also return a value to the user so that this value can be modified or used later.

def divide_by_four(input_number):
  return input_number/4
result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
my_age=calculate_age(2049,1993)
dads_age = calculate_age(2049,1953)
print("I am "+ str(my_age)+" and "+"my "+str(dads_age))

def get_boundaries(target,margin):
  low_limit = target-margin
  high_limit = margin + target
  return low_limit,high_limit
low,high= (get_boundaries(100,20))
print(low)
print(high)

# Scope: Variables defined outside of the function can use inside the function, but variables defined inside the 
#function can't be used outside, Because the variable which defined inside the function is limited to only
#that functon, where variable defind outside can be used anywhere.
current_year = 2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age
print(calculate_age(1970))

def repeat_stuff(stuff,num_repeates=10):
  return (stuff*num_repeates)
#Here we are concatinating repeat_stuff with "Your Boat. "
lyrics=repeat_stuff("Row ",3)+"Your Boat. "
#Here we are calling lyrics variable in the "repeat_stuff" function where lyrics variable multiplies with default num_repeates
song = repeat_stuff(lyrics)
print(song)

time = "3pm"
mood = "good"
def report():
  print("The current time is " + time)
  print("The mood is " + mood)
print("Beginning of report")
report()