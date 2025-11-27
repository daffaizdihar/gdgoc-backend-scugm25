from google import genai

GEMINI_API_KEY = "AIzaSyCjw0L7x9EKfP2MgjnYlcLc_zWsquj02Lo"
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
   model="gemini-2.5-flash", contents="who are you?"
)
print(response.text)