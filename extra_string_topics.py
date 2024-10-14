# operations with strings and values

character_class = "wizard"
character_race = "gnome"
character_mana = 50

# I want to print the string "Your character is a wizard gnome with 50 mana"

# by joining strings and values with addition (concatenation)
print("Your character is a " + character_class + " " + character_race + " with " + str(character_mana) + " mana.")
# by joining strings and values with commas

#use str( ) to typecast a value to a string type
print("Your Character is a",character_class,character_race,"with",character_mana,"mana.")

print(f"Your character is a {character_class} {character_race} with {character_mana} mana.")
#f strings
# multiplication
print("a"*20)
long_string = "abc"*10
print(long_string)
print(f"Yer a {character_class} "*4)
print("There is an","echo "*5)
# print the following
# ask the user how many times they want to cast their spell if each cast is 10 mana
# if they use more than 50 mana, just default to 5 casts
casts = int(input("How many times would you like to cast your fire spell? "))
if casts > 5:
    casts = 5
if casts < 0:
    casts = 0

# print the following (if n were 3)
# "The {class} {race} cast a fire spell {n} times" (use any method you want)
# |===o  ~~ x x x ~~    ~~ x x x ~~    ~~ x x x ~~ (use multiplication)
print(f"The {character_class} {character_race} cast a fire spell {casts} times!")
print(f"|==o" ," ~~ x x x ~~   "*casts)

