from tkinter import *
import base64

# Initialize tkinter


root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Message Encode & Decode")

# Define variables


text = StringVar()
private_key = StringVar()
mode = StringVar()  # encode or decode
result = StringVar()

# Define Encode function


def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        # convert integer unicode value from the remainder of division of ord(message[i]) + ord(key_c)) by 256, to string and store to enc
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    # return decoded string of utf-8 encoded message of string
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Define Encode function


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Define mode function


def Mode():
    if (mode.get() == "e"):
        result.set(Encode(private_key.get(), text.get()))
    elif (mode.get() == "d"):
        result.set(Decode(private_key.get(), text.get()))
    else:
        result.set("Invalid Mode")

# Define Exit function


def Exit():
    root.destroy()

# Define Reset function


def Reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")

# Set Labels & Buttons #


# Header & Footer
Label(root, text="ENCODE x DECODE", font="arial 20 bold").pack()
Label(root, text="~ Welcome to Cyphertext ~",
      font="arial 20 bold").pack(side=BOTTOM)

# MESSAGE
Label(root, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
Entry(root, font="arial 10", textvariable=text,
      bg="ghost white").place(x=310, y=60)

# KEY
Label(root, font="arial 12 bold", text="KEY").place(x=60, y=90)
Entry(root, font="arial 10", textvariable=private_key,
      bg="ghost white").place(x=310, y=90)

# MODE
Label(root, font="arial 12 bold",
      text="MODE('e'=encode, 'd'=decode)").place(x=60, y=120)
Entry(root, font="arial 10", textvariable=mode,
      bg="ghost white").place(x=310, y=120)

# RESULT
Button(root, font="arial 10 bold", text="RESULT",
       bg="light grey", padx=2, command=Mode).place(x=60, y=150)
Entry(root, font="arial 10 bold", textvariable=result,
      bg="ghost white").place(x=310, y=150)

# RESET BUTTON
Button(root, font="arial 11 bold", text="RESET", width=6,
       command=Reset, bg="LimeGreen", padx=2).place(x=170, y=200)

# EXIT BUTTON
Button(root, font="arial 11 bold", text="EXIT", width=6, command=Exit,
       bg="OrangeRed", padx=2, pady=2).place(x=280, y=200)

root.mainloop()
