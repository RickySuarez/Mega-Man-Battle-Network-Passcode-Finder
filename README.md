# Passcode Finder – Mega Man Battle Network

A **Streamlit** app that helps you find the correct passcodes in **Mega Man Battle Network**! This interactive tool uses a guided guessing system to quickly identify the passcode in the game.

## Features
- Efficient binary search algorithm to narrow down passcodes.
- Handles second-digit verification failures.
- Automatically updates guesses based on your feedback.
- Intuitive interface with easy-to-use buttons.
- Alerts if an impossible state is detected.
- Restart option to start over anytime.

## How It Works
1. Enter the number displayed in your game into the app.  
2. Click the button that matches the feedback from the game:
   - **Passcode too high**
   - **Passcode too low**
   - **Second digit verification failure**
   - **Passcode accepted**
   - **Reset passcode**
3. The app automatically adjusts its guesses and guides you to the correct passcode.