import speech_recognition as sr
import requests
import base64

# Replace with your actual MonsterAPI key
API_KEY = "dummy-api-key"
URL = "https://api.monsterapi.ai/v1/generate"

def speak_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak the image description...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        print("❌ Could not recognize speech.")
        return None

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "steps": 20,
        "guidance_scale": 7.5
    }

    print("🧠 Sending request to AI...")
    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        image_base64 = response.json()["image"]
        with open("generated_image.png", "wb") as img_file:
            img_file.write(base64.b64decode(image_base64))
        print("✅ Image saved as 'generated_image.png'")
    else:
        print("❌ API Error:", response.text)

if __name__ == "__main__":
    prompt = speak_to_text()
    if prompt:
        generate_image(prompt)
