import requests
from bs4 import BeautifulSoup
import re
import os  # 引入內建的作業系統模組，用來讀取雲端保險箱密碼

# ================= 1. LINE 機器人設定區 =================
# 改從 GitHub 的環境變數（保險箱）讀取密鑰，確保安全
LINE_TOKEN = os.environ.get("LINE_TOKEN")
USER_ID = os.environ.get("USER_ID")

# ================= 2. 爬蟲抓取資料函式 =================
def get_discount_info():
    print("開始爬取最新優惠資訊...")
    # 稍微客製化一下你的專屬推播開頭
    message = "☕ Silas 的專屬優惠整理來囉！\n-------------------\n"
    
    for page in range(1, 3):
        url = f"https://info.talk.tw/page/{page}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            articles = soup.select("article.entry-card")
            
            for article in articles:
                title = article.select_one("h2.entry-title").get_text()
                a_tag = article.select_one("h2.entry-title a")
                time = article.select_one("ul.entry-meta li.meta-date").get_text()
                
                # 清洗時間字串
                time = re.sub(r"2026 年", "", time).strip()
                
                # 將每一筆資料排版並接在 message 後面
                message += f"📅 {time}\n📌 {title}\n🔗 {a_tag['href']}\n\n"
                
    return message

# ================= 3. LINE 發送訊息函式 =================
def send_line_message(msg):
    print("準備將優惠資訊推播至 LINE...")
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": msg
            }
        ]
    }
    
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
    
    if response.status_code == 200:
        print("✅ 發送成功！請檢查手機 LINE！")
    else:
        print(f"❌ 發送失敗，錯誤碼: {response.status_code}")
        print("錯誤訊息:", response.text)

# ================= 4. 主程式執行區 =================
if __name__ == "__main__":
    # 步驟一：先去抓資料
    final_discount_text = get_discount_info()
    
    # 步驟二：把抓到的資料傳出去
    send_line_message(final_discount_text)