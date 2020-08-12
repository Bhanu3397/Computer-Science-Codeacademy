# break
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]
print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
# for dog_breed in dog_breeds_available_for_adoption:
  # print(dog_breed)
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed==dog_breed_I_want:
    print("They have the dog I want!")
    break

# Continue:- Let’s say we want to print out all of the numbers in a list, unless they’re negative.
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i < 0:
    continue
  print(i)

# Your computer is the doorman at a bar in a country where the drinking age is 21.
# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print the age.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age < 21:
    continue
  print(age)

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []
for word in words:
  if word[0] == '@':
    usernames.append(word)

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student) 
print(students_in_poetry)

# Nested Loops:-
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  for student in team:
    print(student)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold=0
for data in sales_data:
  for index in data:
    scoops_sold+=index
print(scoops_sold)

# List Comprehension:-
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster =[height for height in heights if height>161]
print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit =[cel * 9/5 + 32 for cel in celsius]
print(fahrenheit)

single_digits = range(0,10)
squares=[]
# for digit in single_digits:
  # squares.append(digit*digit)
# print(squares)
squares=[square*square for square in single_digits]
print(squares)
cubes=[cube**3 for cube in single_digits]
print(cubes)