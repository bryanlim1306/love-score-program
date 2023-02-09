# "Love Score" Program
# Takes both people's names and checks for the number of times the letters in the word "TRUE" occur
# Then check both people for the number of times the letters in the word "LOVE" occur. 
# Combine the two numbers to make a 2 digit number, the love score. 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

up_name1 = name1.upper()
up_name2 = name2.upper()
true_counter = 0
love_counter = 0
for letter1 in up_name1:
    if letter1 == "T":
        true_counter += 1
    elif letter1 == "R":
        true_counter += 1
    elif letter1 == "U":
        true_counter += 1
    elif letter1 == "E":
        true_counter += 1

for letter2 in up_name2:
    if letter2 == "T":
        true_counter += 1
    elif letter2 == "R":
        true_counter += 1
    elif letter2 == "U":
        true_counter += 1
    elif letter2 == "E":
        true_counter += 1

for letter2 in up_name2:
    if letter2 == "L":
        love_counter += 1
    elif letter2 == "O":
        love_counter += 1
    elif letter2 == "V":
        love_counter += 1
    elif letter2 == "E":
        love_counter += 1

for letter1 in up_name1:
    if letter1 == "L":
        love_counter += 1
    elif letter1 == "O":
        love_counter += 1
    elif letter1 == "V":
        love_counter += 1
    elif letter1 == "E":
        love_counter += 1

love_string = str(true_counter) + str(love_counter)
love_score = int(love_string)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else: print(f"Your score is {love_score}.")