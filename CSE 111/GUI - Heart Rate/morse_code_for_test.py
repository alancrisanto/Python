from playsound import playsound
import time
import pyttsx3 as pyttsx


def main():
    select = 0
    option = ["Decode", "Encode", "Quit"]

    #Displays the options in order
    for i in range(len(option)):
        print(f"{i + 1}. {option[i]}")

    
    while select!= 3:

        select = int(input("\nPlease select one option: "))

        if select == 1:
            
            text = input("Enter your message: ")
            morse_dict = morse_code_dict()
            encode_message = encode_morse(text, morse_dict)
            print(encode_message)
            print("thank you!")
            break
        
        elif select == 2:

            morse_code = input("Enter your morse code: ")
            morse_dict = morse_code_dict()
            decode_message = decode_morse(morse_code, morse_dict)            
            print(f"{decode_message}")
            print("thank you!")
            break

        elif select == 3:

            print("\nThank you")

        else:
            print("Please enter a number")


def morse_code_dict():

    morse_dict = {  "A" : ".-", 
                    "B" : "-...", 
                    "C" : "-.-.", 
                    "D" : "-..", 
                    "E" : ".", 
                    "F" : "..-.", 
                    "G" : "--.", 
                    "H" : "....", 
                    "I" : "..", 
                    "J" : ".---", 
                    "K" : "-.-", 
                    "L" : ".-..", 
                    "M" : "--", 
                    "N" : "-.", 
                    "O" : "---", 
                    "P" : ".--.", 
                    "Q" : "--.-", 
                    "R" : ".-.", 
                    "S" : "...", 
                    "T" : "-", 
                    "U" : "..-", 
                    "V" : "...-", 
                    "W" : ".--", 
                    "X" : "-..-", 
                    "Y" : "-.--", 
                    "Z" : "--..", 
                    "0" : "-----", 
                    "1" : ".----", 
                    "2" : "..---", 
                    "3" : "...--", 
                    "4" : "....-", 
                    "5" : ".....", 
                    "6" : "-....", 
                    "7" : "--...", 
                    "8" : "---..", 
                    "9" : "----.",
                    "," :"--..--",
                    ":": "---...",
                    "." :".-.-.-",
                    "!" :"-.-.--",
                    "'": ".----.",
                    "?" :"..--..",
                    "/" :"-..-.",
                    "-" :"-....-",
                    "(" :"-.--.",
                    ")" :"-.--.-",
                    '@': ".--.-.",
                    "=": "-...-",
                    "+": ".-.-.",
                    '"': ".-..-.",
                    '&': ".-...",
                    " " :"|"          # This is to ignore spaces
                    }
    
    return morse_dict

def encode_morse(text, morse_dict):

    encode = ""

    #Iterates through the text, and obtain each letter of the text

    for letter in text:

        letter = letter.upper()

        if letter != " ":

            encode += morse_dict[letter] + " "

        else:

            encode += " "
    
    return encode
    # Iterates through every symbol and reproduces the sound of it
    # print(f"\n{encode}")

    # for i in encode:
        
    #     if i == ".":
    #         playsound("dit.wav")
        
    #     elif i == "-":
    #         playsound("dah.wav")
    
    # # is there is space, the sound is mute for 0.5 seconds
    #     else: 
    #         time.sleep(0.5)
    
    

def decode_morse(code, morse_dict):
    
    key_list = list(morse_dict.keys())
    val_list = list(morse_dict.values())

    code += " "
    morse = ""
    normal_text = ""
    


    for letters in code:
        
        if letters != " ":
            morse += letters
            space_found = 0
        
        else:
            space_found += 1
            
            if space_found == 2:
                
                normal_text += " "
                
            else:
                normal_text += key_list[val_list.index(morse)]

                morse = ""
    return normal_text.strip()


if __name__ == "__main__":
    main()
