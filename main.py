from cryptography.fernet import Fernet
from keygen import getKey
import os
import tkinter as tk
from tkinter import filedialog


def encrypt(key, file):
    with open(file,"rb") as f:
        message = f.read()
        f.close()
    fernet = Fernet(getKey(key))
    cipherTxt = fernet.encrypt(message)
    with open(file+".encrypted" ,"wb") as f:
        f.write(cipherTxt)
        f.close()

def decrypt(key,file):
    with open(file,"rb") as f:
        message = f.read()
        f.close()
    fernet = Fernet(getKey(key))
    # Check if its the right key
    try:
        base = os.path.splitext(file)[0]
        plainTxt = fernet.decrypt(message)
        with open(base+".decrypted","wb") as f:
            f.write(plainTxt)
            f.close()
    except:
        print("Invalid key")

root = tk.Tk()

method = int(input("1 - Encription\n2 - Decryption\nChose method: "))
key = input("Key: ")

if method == 1:
    files = filedialog.askopenfilenames()
    for file in files:
        if file.endswith(".encrypted"):
            print(file, " is Already encrypted")
        else:
            encrypt(key, file)

elif method == 2:
    files = filedialog.askopenfilenames(filetypes=(("Encrypted","*.encrypted"),))
    for file in files:
        decrypt(key, file)


