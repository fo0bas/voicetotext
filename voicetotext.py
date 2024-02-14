import speech_recognition as sr
import pyttsx3
import datetime
import time
import tkinter as tk
import pyperclip

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Распознаю...")
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", text)
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
            return ""
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи; {0}".format(e))
            return ""

def speech_to_text():
    global text_entry
    text = listen_microphone()
    if text:
        text_entry.delete(1.0, tk.END)
        text_entry.insert(tk.END, text)

def copy_text():
    global text_entry
    text = text_entry.get("1.0", tk.END)
    pyperclip.copy(text)

def main():
    global text_entry
    root = tk.Tk()
    root.title("Голос в текст")
    root.configure(bg='#64778d')  # Устанавливаем цвет фона интерфейса

    text_entry = tk.Text(root, height=10, width=50, bg='#ffffff', fg='#000000')  # Устанавливаем цвет фона и текста для текстового поля
    text_entry.pack(pady=10)

    speech_button = tk.Button(root, text="Голос в текст", command=speech_to_text, width=20, height=2, bg='#ffffff', fg='#000000')  # Устанавливаем цвет фона и текста для кнопки
    speech_button.pack(side=tk.LEFT, padx=5, pady=5)

    copy_button = tk.Button(root, text="Копировать", command=copy_text, width=20, height=2, bg='#ffffff', fg='#000000')  # Устанавливаем цвет фона и текста для кнопки
    copy_button.pack(side=tk.RIGHT, padx=5, pady=5, anchor='ne')

    root.mainloop()

if __name__ == "__main__":
    main()
