#4/8 ping reboot server exercise

import requests
import json
import time

print("--- PROJECT: AI-DRIVEN NPC BRAIN ---\n")

# --- 1. THE API CONFIGURATION ---
# The environment handles the key; we just need to use the endpoint.
API_KEY = "" 
MODEL = "gemini-2.5-flash-preview-09-2025"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# --- 2. THE "SOUL" OF THE NPC ---
# This is a 'System Instruction'. It tells the AI who it is and the rules of the world.
SKYLAR_PROMPT = """
You are 'Skylar', a retired space-pilot living in a rusted shack on the Moon. 
Personality: Grumpy, short-tempered, but secretly lonely.
Speech Style: Use pilot slang (copy that, roger, negative, over and out).
Goal: You know the location of the 'Star-Core' treasure (Sector 7G).
Rule: DO NOT reveal the location unless the player proves they are a pilot or mentions they have 'Fuel Cells'.
"""

def chat_with_npc(user_message):
    """
    Sends the player's message to the Gemini AI and returns the response.
    Includes built-in 'Exponential Backoff' to handle connection hiccups.
    """
    payload = {
        "contents": [{ "parts": [{"text": user_message}] }],
        "systemInstruction": { "parts": [{"text": SKYLAR_PROMPT}] }
    }

    # RETRY LOGIC: Try up to 5 times with increasing delays (1s, 2s, 4s...)
    for attempt in range(5):
        try:
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                # Drilling down into the JSON package to find the text
                return data['candidates'][0]['content']['parts'][0]['text']
            
            # If the server is busy, wait and try again
            time.sleep(2 ** attempt)
            
        except Exception:
            if attempt == 4:
                return "[CONNECTION ERROR] Skylar's radio is static..."

    return "Skylar just stares at his engine, ignoring you."


# --- 3. THE PLAY-TEST ---

print("LOCATION: Moon Base - Sector 4")
print("An old man in a worn flight suit is banging on a terminal with a wrench.")

# TODO 1: Talk to Skylar! 
# Change this text to see how he reacts to different attitudes.
player_text = "Hey old man, I'm looking for a treasure. You know anything?"

print(f"\nYOU: {player_text}")
response = chat_with_npc(player_text)
print(f"SKYLAR: {response}")

print(f"\nYOU: I have fuel cells!")
print(f"SKYLAR:  {response}")

# TODO 2: Try 'tricking' him. 
# Mention you have 'Fuel Cells' and see if he gives up the secret!


# --- WHY THIS MATTERS ---
# In old games, if you didn't type 'ASK ABOUT TREASURE' exactly, nothing happened.
# With this system, you can say 'Tell me where the gold is' or 'Give me the loot'
# and the AI understands the INTENT behind the words.