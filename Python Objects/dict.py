animals_in_zoo={}
animals_in_zoo["zebras"]=8
animals_in_zoo["monkeys"]=12
animals_in_zoo["dinosaurs"]=0
print(animals_in_zoo)

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
# If we wanted to add 3 new rooms, we could use:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739})
print(user_ids)

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# zipped_drinks =zip(drinks,caffeine)
# print(zipped_drinks)
drinks_to_caffeine = {key:value for key, value in zip(drinks,caffeine)}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays={key:value for key, value in zip(songs,playcounts)}
# print(plays)
plays["Purple Haze"]=1
plays.update({"Respect":94})
# print(plays)
library ={"The Best Songs":plays,"Sunday Feelings":{}}
print(library)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120,"matcha":30}
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

# getting a key:-
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id=user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash",100000 )
print(stack_id )

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users=user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for value in num_exercises.values():
  total_exercises+=value
print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for key,value in pct_women_in_occupation.items():
  print('Women make up {} percent of {}s.'.format(value,key))

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {"past":"Death"}
tarot.pop(13)
tarot.pop(22)
spread["present"]= "The Fool"
tarot.pop(10)
spread["future"]= "Wheel of Fortune"
for key,value in spread.items():
  print("Your {} is the {} card.".format(key,value))
  