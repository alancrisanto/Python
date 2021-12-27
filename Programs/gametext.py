import sys

question = ""

while question.lower() != "yes" and question.lower() != "no":
    question = input("Do you want to play? ")
    print()
    if question.lower() == "yes":

        while question.lower() != "bottle" and question.lower() != "castle":
            question = input("You are alone in a island an you saw a BOTTLE an a CASTLE\n Which one do you choose?\n")
            print()

            if question.lower() == "bottle":
                while question.lower() != "sea" and question.lower() != "trees":
                    question = input("The bottle has a message: \"No one leaves this island without proving their worth to themselves\", you can try the SEA or the TREES\n Which one do you choose?")
                    print()

                    if question.lower() == "sea":
                        
                        print("Is already night, and you were ate by a whale \U0001F40B in the blink of an eye.\n")
                        print()
                        sys.exit()
                    elif question.lower() == "trees":
                        while question.lower() != "meat" and question.lower() != "broccoli":
                            question = input("You are walking trhough the forest and you saw a piece of MEAT and a BROCCOLI\n Which one do you choose?\n")
                            print()

                            if question.lower() == "meat":
                                while question.lower() != "meat" and question.lower() != "run":
                                    question = input("finally you enetred into the castle and found a hungry dragon \U0001F432\n Do you want to give it the MEAT or RUN?\n")
                                    if question.lower() == "meat":
                                        print("Sorry the dragon is vegetarian, you lose!")
                                        print()
                                        sys.exit()

                                    elif question.lower() == "run":
                                        print("That was close, you are safe!")
                                        print()
                                        sys.exit()
                                        
                                    else:
                                        print("Invalid answer, try again")
                                        print()
                            elif question.lower() == "broccoli":
                                print("You are lucky, this dragon loves broccoli. you are safe")
                                print()
                                sys.exit()
                            else:
                                print("Invalid answer, try again")
                                print()
                    else:
                        print("Invalid answer, try again!")
                        print()
            elif question.lower() == "castle":
                while question.lower() != "ball" and question.lower() != "feather":
                    question = input("You are in the forest on your way to the castle \U0001F3F0 and found a BALL and a FEATHER \n Which one do  you choose?\n")
                    if question.lower() == "ball":
                        while question.lower() != "ball" and question.lower() != "dance":
                            question = input("You are inside the castle and you saw a whizard\n Do you want to give him the BALL or DANCE?\n")
                            if question.lower() == "ball":
                                print("You are lucky, that's his magic ball. You are alive!")
                                print()
                                sys.exit()
                            elif question.lower() == "dance":
                                print("You dance so bad, he bewitches yu and turns you into a frog")
                                print()
                                sys.exit()
                            else:
                                print("Invalid answer, try again")
                                print()
                    elif question.lower() == "feather":
                        while question.lower() != "tickles" and question.lower() != "hide":
                            question = input("You are now face to face with a big griffin\n Do you want to make it TICKLES with the feather or HIDE?\n")
                            print()
                            if question.lower() == "tickles":
                                print("You are lucky, it likes tickles, you are alive!")
                                print()
                                sys.exit()
                            elif question.lower() == "hide":
                                print("I'm sorry it found you. You lose!")
                                print()
                                sys.exit()
                            else:
                                print("Invalid answer, try again")
                    else:
                        print("invalid answer, try again")
                        print()
            else:
                print("Invalid answer, try again!")
                print()
    elif question.lower() == "no":
        print("That's too bad!")
        print()
    else:
        print("Invalid answer, try again!")