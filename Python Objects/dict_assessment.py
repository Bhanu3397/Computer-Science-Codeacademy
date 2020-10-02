# (https://www.youtube.com/watch?v=WjVJcCBazNI&feature=emb_title)
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "]=0
# print(letter_to_points)
# print(letter_to_points.keys())
# print(letter_to_points.values())
# print("B" in letter_to_points.keys())
def score_word(word):
  point_total =0
  for point in word:
    # print(point)
    if point in letter_to_points.keys():
      point_total +=letter_to_points[point]
  return point_total
brownie_points = score_word("BROWNIE")
print(brownie_points)
player_to_words = {"player1":["BLUE","EARTH","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":['ERASER','BELLY','HUSKY'],"Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points={}
for player,words in player_to_words.items():
  player_points =0
  for word in words:
    player_points+=score_word(word)
  player_to_points[player]=player_points
print(player_to_points)

def play_word(player,word):
  player_to_words[player].append(word)

play_word("player1","Code")
print(player_to_words)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30))

# combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[3]) #Key error
