# Write your sum_values function here:
def sum_values(my_dictionary):
  total=0
  for value in my_dictionary.values():
    total+=value
  return total
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total=0
  for key in my_dictionary.keys():
      if key %2 ==0:
        total+=my_dictionary[key]
  return total
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Write your add_ten function here:
def add_ten(my_dictionary):
  new_dict={}
  for key,val in my_dictionary.items():
    new_val= val+10
    new_dict.update({key:new_val})
  return new_dict
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  my_list=[]
  keys=my_dictionary.keys()
  # print(keys)
  for val in my_dictionary.values():
    # print(val)
    if val in keys:
      my_list.append(val)
  return my_list
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


def word_length_dictionary(words):
  new_dict={}
  for word in words:
    new_dict.update({word:len(word)})
  return new_dict
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
# def count_first_letter(names):
#   letters = {}
#   for key in names:
#     first_letter = key[0]
#     if first_letter not in letters:
#       letters[first_letter] = 0
#     letters[first_letter] += len(names[key])
#   return letters
def count_first_letter(names):
  my_dict = {}
  for key, value in names.items():
    if key[0] not in my_dict:
      my_dict.update({key[0] : len(value)})
    else:
      my_dict[key[0]] += len(value)
  return my_dict
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

myd={"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
mydl=len(myd["Stark"]) # My dict length 
print(mydl)

