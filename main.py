import os
# import requests
# from bs4 import BeautifulSoup

def scrape_travel_deals():
    # 喺度寫你嘅爬蟲邏輯
    return "✈️ 今日精選優惠：\n1. 沖繩機票半價..."

def send_whatsapp(message):
    # 呢度可以用 Twilio API 發送 WhatsApp
    # 記得用 os.environ 讀取 API Key，千萬唔好直接寫喺 code 入面！
    twilio_sid = os.environ.get("TWILIO_SID")
    twilio_token = os.environ.get("TWILIO_TOKEN")
    print(f"Sending WhatsApp: {message}")

if __name__ == "__main__":
    deals = scrape_travel_deals()
    send_whatsapp(deals)
