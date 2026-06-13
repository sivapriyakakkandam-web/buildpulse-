import requests
from datetime import datetime

def get_weather(location="Thiruvananthapuram"):
    try:
        url = f"https://wttr.in/{location}?format=j1"
        data = requests.get(url, timeout=10).json()
        current = data["current_condition"][0]
        return {
            "location": location,
            "temperature": current["temp_C"],
            "condition": current["weatherDesc"][0]["value"]
        }
    except Exception as e:
        return {"location": location, "temperature": "N/A", "condition": f"Error: {e}"}

def get_quote():
    try:
        data = requests.get("https://zenquotes.io/api/random", timeout=10).json()
        return data[0]["q"] + " — " + data[0]["a"]
    except Exception:
        return "Stay positive and keep learning."

def create_summary():
    weather = get_weather()
    quote = get_quote()

    summary = f"""
DAILY PULSE
Date: {datetime.now().strftime("%d %B %Y")}

Weather:
Location: {weather['location']}
Temperature: {weather['temperature']}°C
Condition: {weather['condition']}

Quote:
"{quote}"

Generated automatically by Pulse.
"""
    return summary

def save_summary():
    summary = create_summary()
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("daily_summary.txt created successfully")

if __name__ == "__main__":
    save_summary()
