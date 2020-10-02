first_name = "Rodrigo"
last_name = "Villanueva"
new_account =last_name[:5]
temp_password = last_name[2:6]
print(temp_password,last_name)

fruit_prefix = "blue"
fruit_suffix = "berries"
# We can create a new string by concatenating them together as follows:
favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit)

first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name,last_name):
  return first_name[:3]+last_name[:3] # First three letters
new_account=account_generator(first_name,last_name)
print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  return first_name[-3:]+last_name[-3:] #last three letters
temp_password=password_generator(first_name,last_name)
print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2] # 2nd word from last
final_word=company_motto[-4:] # Last 4 words
print(second_to_last,final_word)

first_name = "Bob"
last_name = "Daily"
# first_name[0] = "R"
fixed_first_name= "R"+ first_name[1:] #from 1st index, not including 0 index
print(fixed_first_name)

#Escape Characters
password = "theycallme\"crazy\"91"
print(password)

def get_length(string):
  count = 0
  for word in string:
    count +=1
  return count
print(get_length('Hello'))

# Above can written as
def get_length(string):
    return len(string)
print(get_length('Hello'))

def letter_check(word,letter):
  for i in word:
    if i  in letter:
      return True
  return False
print(letter_check('Hiytur','l'))

def contains(big_string, little_string):
  return little_string in big_string
print(contains("watermelon", "berry"))
print(contains("watermelon", "melon"))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("banana", "cream"))
print(common_letters("hyder", "cream"))


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
print(username_generator("abe", "simp"))
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
print(password_generator('abesimp'))