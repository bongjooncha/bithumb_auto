import os
from dotenv import load_dotenv
load_dotenv()
import python_bithumb
import logging
logging.getLogger().setLevel(logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# GRPC 로깅 비활성화
os.environ['GRPC_PYTHON_LOG_LEVEL'] = 'error'
os.environ['GRPC_VERBOSITY'] = 'ERROR'

# 1. 빗썸 차트 데이터 가져오기 (30일 일봉)
df = python_bithumb.get_ohlcv("KRW-BTC", interval="day", count=30)

import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(
    f"""You are an expert in Bitcoin investing. Here is the Bitcoin OHLCV data for the last 30 days:

{df.to_json()}

Based on this chart data, tell me whether to buy, sell, or hold at the moment. Response in json format.

Response Example:
{{"decision": "buy", "reason": "some technical reason"}}
{{"decision": "sell", "reason": "some technical reason"}}
{{"decision": "hold", "reason": "some technical reason"}}"""
)

import json
result = json.loads(response.text)
print(result['decision'])

print(result['reason'])


result = json.loads(result)
access = os.getenv("BITHUMB_ACCESS_KEY")
secret = os.getenv("BITHUMB_SECRET_KEY")
bithumb = python_bithumb.Bithumb(access, secret)

print(result["decision"])
print(result["reason"])

result["decision"] = "buy"

if result["decision"] == "buy":
    print(bithumb.buy_market_order("KRW-BTC", 10000))
elif result["decision"] == "sell":
    print(bithumb.sell_market_order("KRW-BTC", 10000))