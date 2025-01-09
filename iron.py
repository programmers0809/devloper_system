import pyttsx3

# Ovozli chiqish uchun ovoz sozlamalari
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Erkak ovozi
engine.setProperty('rate', 150)  # Ovoz tezligi

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Asosiy dastur
if __name__ == "__main__":
    print("Salom! Menga biror narsa yozing, men ovoz chiqarib javob beraman.")
    while True:
        user_input = input("Sizning so'rovingiz: ")
        if user_input.lower() in ["xayr", "chiq", "tugat"]:
            print("Xayr, yaxshi kun tilayman!")
            speak("Xayr, yaxshi kun tilayman!")
            break
        else:
            print(f"Siz yozdingiz: {user_input}")
            speak(user_input)
