import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests

# load_dotenv()

# # Gemini API 설정
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # 모델 설정
# model = genai.GenerativeModel('gemini-pro')

# # 테스트 실행
# response = model.generate_content("안녕하세요!")
# print(response.text)


fearAndGreed = requests.get("https://api.alternative.me/fng/").json()['data'][0]
print(fearAndGreed)