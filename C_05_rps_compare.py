# Check that users have entered a valid
# option bases on a list
def rps_compare(user , comp):

    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        results = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result


# Automating testing is below in the form(test_case, expecting_value)
to_test = [
    ('Rock', 'rock', 'tie'),
    ('rock', 'paper', 'lose'),
    ('rock', 'paper', 'win'),
    ('PAPER', 'paper', 'tie'),
    ('paper', 'rock', 'win'),
    ('paper', 'scissors', 'lose'),
    ('scissors', 'scissors', 'tie'),
    ('scissors', 'rock', 'lose'),
    ('scissors', 'paper', 'win'),
]

# run test!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get atual value (ie: test ticket function
    actual = rps_compare(user, comp)

# compare actual and expected output pass / fail
if actual == expected:
    print(f" ✔️✔️✔️ Passed! Case: {user} vs {comp}, expecte: {expected}, received: {actual} ✔️✔️✔️")
else:
    print(f" 👎👎👎 Failed! Case: {user} vs {comp}, expected: {expected}, received: {actual} 👎👎👎")
# Main routine goes here

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = rps_compare("Do you want to see the instructions? 🤨")

print("You chose: ", want_instructions)

user_choice = rps_compare("Choose: ", rps_list)
print("You chose: ", user_choice)
