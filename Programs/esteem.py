from typing import Counter


def main():

    print("""\nThis program is an implementation of the Rosenberg Self-Esteem Scale.
This program will show you ten statements that you could possibly
apply to yourself. Please rate how much you agree with each of the
statements by responding with one of these four letters:\n""")

    print("""D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.\n""")


    final_score = []

    print("1. I feel that I am a person of worth, at least on an equal plane with others") #Positive
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(possitive_answers(answer))

    print("2. I feel that I have a number of good qualities.") #Positive
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(possitive_answers(answer))

    print("3. All in all, I am inclined to feel that I am a failure.")
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(negative_answers(answer))

    print("4. I am able to do things as well as most other people.") #Positive
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(possitive_answers(answer))

    print("5. I feel I do not have much to be proud of.")
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(negative_answers(answer))

    print("6. I take a positive attitude toward myself.") #Positive
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(possitive_answers(answer))

    print("7. On the whole, I am satisfied with myself.") #Positive
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(possitive_answers(answer))

    print("8. I wish I could have more respect for myself.")
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(negative_answers(answer))

    print("9. I certainly feel useless at times.")
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(negative_answers(answer))

    print("10. At times I think I am no good at all.")
    answer = (input("Enter D, d, a, or A: "))
    final_score.append(negative_answers(answer))

    count = 0

    for i in final_score:
        count += i

    print(f"\nYour score is {count}.")
    print(f"A score bellow 15 may indicate problematic low self-esteem.\n")

#----------------------------------------------------------------------------------

def possitive_answers(answer):

    pos_score = []

    if answer == "D":           #Strongly Disagree
        pos_score.append(0)
    
    elif answer == "d":         # Disagree
        pos_score.append(1)

    elif answer == "a":         # Agree
        pos_score.append(2)
    
    else:                       # Strongly agree
        pos_score.append(3)
    
    count = 0
    
    for i in pos_score:
        count += i
    
    return count

#---------------------------------------------------------------------------
def negative_answers(answer):

    neg_score = []

    if answer == "D":           #Strongly Disagree        
        neg_score.append(3)
    
    elif answer == "d":         # Disagree
        neg_score.append(2)

    elif answer == "a":         # Agree
        neg_score.append(1)
    
    else:                       # Strongly agree
        neg_score.append(0)
    
    count = 0

    for i in neg_score:
        count += i
    
    return count


main()