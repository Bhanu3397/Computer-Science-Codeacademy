print(type(5))
my_dict={}
print(type(my_dict))
my_list=[]
print(type(my_list))

class Facade:
  pass
Facade1=Facade() #Class Instantiation
facade_1_type=type(Facade1)
print(facade_1_type)

class Dog:
  dog_time_dilation = 7

  def time_explanation(self):# Method
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()

class Rules:
  pass
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

Rule=Rules() # Instantiation
print(Rule.washing_brushes())

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)

class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)
print(pizza_area,teaching_table_area,round_room_area)

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"
shout2 = Shouter()
# prints "HELLO?!"

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"
shout2 = Shouter("shout")
# prints "SHOUT"
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

class Circle:
  pi = 3.14
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

class FakeDict:
  pass
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)

class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(codecademy.url)
# prints "www.codecademy.com"
print(wikipedia.url)
# prints "www.wikipedia.org"

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry('www.wikipedia.com')
print(codecademy.secure()) # prints "https://www.codecademy.com"
print(wikipedia.secure()) # prints "https://www.wikipedia.org"

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    self.radius = diameter / 2
  def area(self):
    return self.pi * self.radius ** 2
  def circumference(self):
    return self.pi * 2 * self.radius
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
