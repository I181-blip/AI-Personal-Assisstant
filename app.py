import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)
print("Key ends with:", api_key[-4:])

print("AI Assistant ready. Type 'exit' to quit.")
while True:
    try:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=user_input,
        )
        print("Assistant:", response.text, "\n")

    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}\n")
