# Python Alarm Clock ⏰

This is a Python-based command-line alarm clock that allows users to set alarms and plays a custom sound at the specified time. It uses Python's `datetime` module to track the time and `pygame` to play audio when the alarm goes off.

## Features

- Set an alarm in the format `HH:MM:SS`.
- Continuously checks the current time and triggers an alarm at the set time.
- Plays an alarm sound using `pygame`.

## How to Use

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/rabin20-04/Python-Codex.git
   ```
2. Navigate to the Alarm Clock project directory:
   ```bash
   cd Python-Codex/Projects/CLI/Alarm\ Clock
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```
4. Run the Python script:
   ```bash
   python alarm_clock.py
   ```
5. Enter the alarm time in the `HH:MM:SS` format when prompted:
   ```bash
   Enter the time in format HH:MM:SS =
   ```
6. The script will print the current time every second and trigger the alarm at the set time.
