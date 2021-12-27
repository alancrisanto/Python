import tkinter as tk
from playsound import playsound
import time
import pyttsx3 as pyttsx
import sys


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Morse Decoder")
    frm_main.pack()

    

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    morse_main_frame(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def morse_main_frame(frm_main):
    
    # Print Welcome message

    wlcme_msg = tk.Label(frm_main, text="Welcome to Morse Decoder", font="times 20 bold", fg="#007ACC")
    wlcme_msg.grid(row=0, column=0, pady=20, padx=20)

    # Middle Message
    middle_msg = tk.Label(frm_main, text="Enter your message", font="times 15")
    middle_msg.grid(row=1, column=0, pady=20)
    
    #Message Input

    msge_code = tk.Text(frm_main, bg="white", height=3, width=50)
    msge_code.grid(row=2, column=0, pady=20, padx=20)
    msge_code.focus()

    ########  Create a buttons that displays "Encode and decode"  ###################

    #Encode
    encode_btn = tk.Button(frm_main, text="Encode", font="times 13", fg="#008080", command=lambda: encode_morse(msge_code.get('1.0', tk.END), morse_code_dict()))
    encode_btn.grid(row=3, column=0, pady=20, padx=100, sticky="w")
    
    #Decode
    decode_btn = tk.Button(frm_main, text="Decode", font="times 13", fg="#008080", command=lambda: decode_morse(msge_code.get("1.0", "end-1c"), morse_code_dict()))
    decode_btn.grid(row=3, column=0, pady=20, padx=100, sticky="e")
    
    #######  Bottom message ###########

    dcode_message = tk.Label(frm_main, text="Your message is", font="times 15")
    dcode_message.grid(row=4, column=0, pady=20)

    #########  Decode Output  ##############

    dcode_box = tk.Text(frm_main, bg="white", height=3, width=50)
    dcode_box.grid(row=5, column=0, pady=20, padx=30)

    ##########  Clear button  #############

    clear_btn = tk.Button(frm_main, text="Clear", font="times 13", fg="#008080")
    clear_btn.grid(row=6,column=0, pady=20, padx=100, sticky="w")

    #########  Quit button  ##############

    quit_btn = tk.Button(frm_main, text="Quit", font="times 13", fg="#FF2424", command=quit_function)
    quit_btn.grid(row=6, column=0, pady=20, padx=100, sticky="e")

    # def get_code():

    #     code_message = encode_morse(msge_code.get(msge_code.get('1.0', tk.END), morse_code_dict()))

    #     dcode_box.insert(0.0, code_message)

    #     return code_message

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
                    " " : ""          # This is to ignore spaces
                    }
    
    return morse_dict

def encode_morse(text, morse_dict):

    encode = ""

    #Iterates through the text, and obtain each letter of the text
    for letter in text:
        letter = letter.upper()
        if letter in morse_dict:

            encode += (morse_dict[letter]+ " ")

        else:

            encode += " "

    # Iterates through every symbol and reproduces the sound of it
    print(f"\n{encode}")

    for i in encode:
        
        if i == ".":
            playsound("dit.wav")
        
        elif i == "-":
            playsound("dah.wav")
    
    # is there is space, the sound is mute for 0.5 seconds
        else: 
            time.sleep(0.2
            )
    
    return encode

def decode_morse(code, morse_dict):

    key_list = list(morse_dict.keys())
    val_list = list(morse_dict.values())

    morse = ""
    normal_text = ""
    code += " "

    for letters in code:
        
        if letters != " ":
            morse += letters
            space_found = 0
        
        else:
            space_found += 1
            
            if space_found == 2:
                
                normal_text += " "
                
            else:
                normal_text = normal_text + key_list[val_list.index(morse)]

                morse = ""
    
    print(normal_text)


    #This reproduce the text to voice
    engine = pyttsx.init()
    engine.say(normal_text)
    engine.runAndWait()
    
    return ""

def quit_function():
    sys.exit(0)

if __name__ == "__main__":
    main()
