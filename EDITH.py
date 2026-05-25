import webbrowser
import datetime
import random
import os
import requests
import pyautogui

print("===================================")
print("         EDITH ASSISTANT")
print("===================================")
print("Type 'exit' to close Edith")

while True:

    command = input("\nEnter Command: ").lower()

    # EXIT
    if command == "bye edith":
        print("Shutting down Edith...")
        break

    # HELLO
    elif "hello" in command:
        print("Hello")

    # TIME
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)

    # DATE
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Today's Date:", current_date)

    # OPEN YOUTUBE
    elif "open youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    # OPEN GOOGLE
    elif "open google" in command:
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    # GOOGLE SEARCH
    elif "search" in command:
        search_query = command.replace("search", "")
        print("Searching for", search_query)

        webbrowser.open(
            f"https://www.google.com/search?q={search_query}"
        )

    # OPEN NOTEPAD
    elif "open notepad" in command:
        print("Opening Notepad...")
        os.system("notepad")

    # SCREENSHOT
    elif "screenshot" in command:

        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")

        print("Screenshot saved as screenshot.png")

    # JOKE
    elif "joke" in command:

        try:
            url = "https://official-joke-api.appspot.com/random_joke"

            response = requests.get(url)

            joke = response.json()

            print("\nJOKE\n")

            print(joke["setup"])

            print(joke["punchline"])

        except:
            print("Unable to fetch joke")

    # WEATHER
    elif "weather" in command:

        city = input("Enter city name: ")

        try:
            url = f"https://wttr.in/{city}?format=3"

            data = requests.get(url)

            print(data.text)

        except:
            print("Unable to fetch weather")

    # LIVE CRICKET SCORE
    elif "cricket" in command:

        try:
            url = "https://cricket-api.vercel.app/cri.php"

            response = requests.get(url)

            print("\nLIVE CRICKET SCORE\n")

            print(response.text)

        except:
            print("Unable to fetch cricket score")

    # NEWS
    elif "news" in command:

        print("Opening Google News...")

        webbrowser.open("https://news.google.com")

    # CALCULATOR
    elif "calculate" in command:

        try:
            expression = input("Enter calculation: ")

            result = eval(expression)

            print("Result:", result)

        except:
            print("Invalid Calculation")

    # UNKNOWN COMMAND
    else:
        print("Sorry, command not recognized.")