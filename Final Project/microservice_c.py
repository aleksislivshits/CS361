# Daily Reminder Microservice

from flask import Flask, jsonify, request
import json
import datetime
import os

app = Flask(__name__)

# Path to store reminder settings
REMINDER_TIME_FILE = 'reminder_time.json'


# Function to load the reminder time from file (if exists)
def load_reminder_time():
    if not os.path.exists(REMINDER_TIME_FILE):
        return None  # Default: no reminder set
    with open(REMINDER_TIME_FILE, 'r') as f:
        return json.load(f).get('reminder_time', None)


# Function to save the reminder time to a file
def save_reminder_time(reminder_time):
    with open(REMINDER_TIME_FILE, 'w') as f:
        json.dump({"reminder_time": reminder_time}, f)


@app.route('/set-reminder-time', methods=['POST'])
def set_reminder_time():
    """Endpoint to set the user's preferred reminder time"""
    data = request.get_json()
    reminder_time = data.get('reminder_time')

    if reminder_time:
        save_reminder_time(reminder_time)
        return jsonify({"message": f"Reminder time set to {reminder_time}."}), 200
    return jsonify({"error": "Invalid time format."}), 400


@app.route('/daily-reminder', methods=['GET'])
def daily_reminder():
    """Endpoint to send daily reminder at the user’s set time"""
    reminder_time = load_reminder_time()

    if reminder_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == reminder_time:
            reminder_message = f"Reminder: Don't forget to track your spending today!"
        else:
            reminder_message = f"Your next reminder is at {reminder_time}."
    else:
        reminder_message = "No reminder time set. Please set a reminder time."

    return jsonify({"reminder": reminder_message})


if __name__ == '__main__':
    app.run(port=5003)
