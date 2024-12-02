import google.generativeai as genai

genai.configure(api_key="erm no")
model = genai.GenerativeModel('gemini-1.5-flash')

def ask(c):
    print("🔵|Proszę czekać...")
    response = model.generate_content(c)
    return response.text