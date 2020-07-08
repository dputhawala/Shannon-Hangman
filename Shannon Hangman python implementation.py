from random import*

# Shannon Hangman

# This script was written by Daniel Puthawala the OSU LING 3801 course, Code Making and Code Breaking.
# This script can be freely used for personal and educational purposes.
# If you want to use it, or anything herein for some other or nefaroius purposes, please ask me first.
# Thanks, Daniel
# puthawala.1@osu.edu






plaintexts = [
    "The animals commonly known as pythons, from the Greek word python, are a family of nonvenomous snakes found in Africa, Asia, and Australia.",
    "Noted for having founded information theory with a landmark paper, A Mathematical Theory of Communication, that he published in nineteen forty eight.",
    "Linguistics is the scientific study of language, and involves an analysis of language form, language meaning, and language in context.",
    "She said that she told Damian to go to the store and get three pounds of top round roast. but chuck was on sale so he got that. what am I supposed to do now",
    "Purple lions gaze slovenly on lazy grasses rustling in the breeze. The gazelle may sleep safe tonight.",
    "The weather forecast calls for three to six inches of snow this evening, turning to freezing rain tonight into early morning. Be careful on the roads tomorrow.",
    "Two days ago, I saw a man lounging in his field. Though he looked lazy, his farm was well kept and his wheat grew tall. An admirable man then, that farmer."
]



# basic version like battleship
# initiate target text
plain_number = randrange(len(plaintexts))
print "plain_number = ",plain_number

input_text = plaintexts[plain_number]  # The text we will use as an input.  A test sentence for now
# input_text = "hello world you world"
# input_text = "Two days ago, I saw a man lounging in his field."
clean_text = ""                 # A cleaned-up version of he input text
gameboard_text = []             # a list that holds the information of what the game board text will actually look like on a given turn
letter_guess_count = []        # a list that will keep track of the number of guesses made per letter
total_guesses = 0               #A number that just keeps track ot the total number of guesses so far.
current_letter_guesses = 0
victory = False                 #to check if the game is over yet, this will change to True when the gameboard_text == clean_text
current_letter = 0              #The index of the current letter in the message being guessed
uppered = input_text.upper()
# print(uppered)     #make sure all the input text is upper-case
for x in uppered:
    if x.isalpha() == True: #if the character is a letter or space, we leave it in, this gets rid of punctuation
        clean_text += x
    if x == " ":
        clean_text +="_"
print(clean_text)
for x in clean_text:
    gameboard_text.append(x)
    letter_guess_count.append(0)

# print "len(clean_text)",len(clean_text)


# print gameboard_text

reconstructed_text = []         #The text that has been thus far reconstructed by the players
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]
current_alpha = []

# current_alpha = alphabet
# current_alpha[4] = " "
# output_alpha = ""

# print gameboard_text

def Get_Current_Alpha(working_alpha):
    global alphabet
    working_alpha = []
    for x in alphabet:
        working_alpha.append(x)
    return working_alpha

Get_Current_Alpha(current_alpha)


for x in range(len(letter_guess_count)):
    reconstructed_text.append("-")



def List_To_Text(lst):
    output_string = ""
    for x in lst:
        output_string += str(x)
        output_string += " "
    return output_string


current_alpha = Get_Current_Alpha(current_alpha)

print "Gameboard_text: ",gameboard_text
print "reconstructed_text: ",reconstructed_text
print "letter_guess_count: ", letter_guess_count
print "List_To_Text(alphabet) ",List_To_Text(alphabet)
print "List_To_Text(current_alpha) ",List_To_Text(current_alpha)


# print current_alpha

def Print_Gameboard():
    for i in range(30):
        print
    # global reconstructed_text
    # print "           ","gameboard_text ",List_To_Text(gameboard_text)
    for x in range(20,1000,20):
        if len(reconstructed_text) >= x:
            print "           ", List_To_Text(reconstructed_text[x-20:x])
            print "           ", List_To_Text(letter_guess_count[x-20:x])
            print
        else:
            print "           ", List_To_Text(reconstructed_text[x - 20:len(reconstructed_text)])
            print "           ", List_To_Text(letter_guess_count[x - 20:len(reconstructed_text)])
            break

            # for y in range(20):
        #     if len(reconstructed_text) <= x+y:
        #         print "           ",List_To_Text(reconstructed_text)[x+y]
        #         print "           ",List_To_Text(letter_guess_count)[x+y]
    # output_alpha = ""
    # print
    # print
    # for x in current_alpha:
    #     output_alpha += x
    print "           ",List_To_Text(current_alpha)
    print
    print "           Total Guesses so far: ",total_guesses
    global current_letter
    if current_letter >> 0:
        average_guess = float(total_guesses) / float(current_letter)
        print "           Average Guesses per letter: ",average_guess

Print_Gameboard()

# ask for input each turn.


def Get_Letter():
    letter_guess = raw_input("Guess a letter! > ")
    if letter_guess.isalpha() == True:
        capital_guess = letter_guess.upper()
    elif letter_guess == "" or " " or "_" or None:
        print "Changing blank input to '_'"
        capital_guess = "_"
    global total_guesses
    global current_letter_guesses
    # print capital_guess
    # print "total_guesses is a: ",type(total_guesses)
    # game = 3
    # print "total_guesses: ",total_guesses
    # print "current_letter_guesses: ",current_letter_guesses
    if str.isalpha(capital_guess) == False and capital_guess != "_":
        print"That's not a valid option.  Try again."
        return
    elif capital_guess not in current_alpha:
        print "You already guessed that letter or typed something weird.  Try again."
        return
    else:
        current_letter_guesses += 1
        total_guesses += 1
        return capital_guess


# while victory == False:
# for i in range(4):
#     print Get_Letter()

# keep track of guesses per letter
# keep track of total number of turns

for i in range(len(clean_text)):
    got_letter = False
    # global current_alpha
    current_alpha = Get_Current_Alpha(current_alpha)
    while got_letter == False:
    # for j in range(2):
        print "i = ",i, #"j = ",j
        current_guess = Get_Letter()
        print
        print "current guess is: ",current_guess
        print
        if current_guess != "" or " " or "_":
            # global letter_guess_count
            if current_guess in current_alpha:
                letter_guess_count[i] += 1
            print "current guess: ",current_guess
            print "clean_text[current_letter]: ",clean_text[current_letter]
        # else:
        #     current_guess = "_"
        if current_guess == clean_text[current_letter]:
            got_letter = True
            print "You got the letter  Yahooooo!"
            # global reconstructed_text
            reconstructed_text[i] = current_guess
            current_letter += 1
            # global alphabet
            # global current_alpha
            # current_alpha = []
            current_alpha = Get_Current_Alpha(current_alpha)
            Print_Gameboard()
            break
        else:
            # current_alpha.index(current_guess)
            print "Incorrect guess.  Try again!"
            if current_guess in current_alpha:
                current_alpha[current_alpha.index(current_guess)] = " "
            Print_Gameboard()

# give victory message when finished

# if gameboard_text == clean_text:
victory = True
for i in range(30):
    print
print "Congratulations, you won!"
print
print List_To_Text(reconstructed_text)
print List_To_Text(letter_guess_count)
print
average_guess = float(total_guesses) / float(len(reconstructed_text))
print "You took on average ",average_guess, " guesses to get each letter."