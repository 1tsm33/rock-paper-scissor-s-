# Check that users have entered a valid
# option bases on a list
def string_checker(question, valid_ans=["yes", "no"]):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a word in the list
             if item == user_response:
                 return item

             # check if the user response is the same as
             # the first letter of an item in the list
             elif user_response == item[0]:
                 return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Display instructions

def instructions():
    print ("""
    
*** Instructions ***

(To begin, choose the number of rounds (or p...
infinant mode.)

Then play against the computer you need to choose between R (rock) P (paper) or S (scissors).

The rules are as follow
o   Paper beats rock
o   Rock beats scissors
o   Sissors beats rock

Press <xxx> to end the game at anytime.

Good Luck!
    """)


# Main routine
print()
print("🪨🗞️✂ Rock / Paper / Scissors Game ✂🗞️🪨")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (no)
if want_instructions == "yes":
    instructions()

print("Program continues")