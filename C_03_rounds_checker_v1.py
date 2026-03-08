# Checks that users enter an integer
# that is more than 13
def int_check():


    while True:
        error = "Please enter an integer more than / equal to 13."

        try:
            response = int(input("Enter an integer: "))

            # Checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine starts here
game_goal = int_check()
print(game_goal)

# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("No", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("Maybe", "invalid"),
]

# run test!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, ["yes", "no"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✔️✔️✔️Passed! Case: {case}, expected: {expected}, received: {actual}✔️✔️✔️")
    else:
        print(f"👎👎👎Failed! Case: {case}, expected: {expected}, received: {actual}👎👎👎")