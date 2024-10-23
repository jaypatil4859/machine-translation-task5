import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

def load_translations(english_file, french_file, hindi_file):
    with open(english_file, 'r', encoding='utf-8') as file:
        english_sentences = file.read().strip().split('\n')
    with open(french_file, 'r', encoding='utf-8') as file:
        french_sentences = file.read().strip().split('\n')
    with open(hindi_file, 'r', encoding='utf-8') as file:
        hindi_sentences = file.read().strip().split('\n')
    return dict(zip(english_sentences, french_sentences)), dict(zip(english_sentences, hindi_sentences))

def translate_to_french_and_hindi(sentence, english_to_french, english_to_hindi):
    if len(sentence) != 10:
        return "Error: Word length must be exactly 10 letters.", "", ""
    french_translation = english_to_french.get(sentence)
    hindi_translation = english_to_hindi.get(sentence)
    if french_translation and hindi_translation:
        return f"French Translation: {french_translation}", f"Hindi Translation: {hindi_translation}", ""
    else:
        return "", "", "Translation not found."

def on_translate_click():
    sentence = entry.get()
    english_to_french, english_to_hindi = load_translations("data5/english.txt", "data5/french.txt", "data5/hindi.txt")
    french, hindi, error = translate_to_french_and_hindi(sentence, english_to_french, english_to_hindi)
    if error:
        messagebox.showerror("Error", error)
    else:
        french_label.config(text=french)
        hindi_label.config(text=hindi)

# Load model (example file path)
model = load_model("translation_model.h5")

# GUI setup
root = tk.Tk()
root.title("Translator GUI")

tk.Label(root, text="Enter a 10-letter English word:").grid(row=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Button(root, text="Translate", command=on_translate_click).grid(row=1, columnspan=2)

french_label = tk.Label(root, text="")
french_label.grid(row=2, columnspan=2)

hindi_label = tk.Label(root, text="")
hindi_label.grid(row=3, columnspan=2)

root.mainloop()



