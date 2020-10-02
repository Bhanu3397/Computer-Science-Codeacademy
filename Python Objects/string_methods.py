poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)
poem_author_fixed=poem_author.upper()
print(poem_author_fixed)
line_one = "The sky has given over"
line_one_words  = line_one.split()
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')
print(chorus_lines)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one=' '.join(reapers_line_one_words)
print(reapers_line_one)

def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc
my_beard_description= poem_description(1974,"Shel Silverstein","My Beard", "Where the Sidewalk Ends")
print(my_beard_description)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

god_wills_it_line_one = "The very earth will disown you"
disown_placement= god_wills_it_line_one.find('disown')
print(disown_placement)
