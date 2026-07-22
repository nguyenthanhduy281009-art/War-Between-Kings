import requests
import time
import random

TOKEN = "447107892283877624:oedSMfxhfckBEqlvlEiGvrIVJbLxWHOppZmApWCoNeyKYKqwuVMHPWpTMiotWUpS
"
API_URL = f"https://bot.zapps.me/api/v1/bot{TOKEN}"

Dữ liệu giả lập (Sau này bạn cần dùng Database thực tế để lưu trữ)
danh_sach_thanh_vien = ["Duy", "Thắng", "Nam", "An"]
thong_ke_tin_nhan = {"Duy": 150, "Thắng": 12, "Nam": 85, "An": 40}

def get_updates(offset=None):
url = f"{API_URL}/getUpdates"
try:
return requests.get(url, params={"offset": offset, "timeout": 30}).json()
except:
return None

def send_message(chat_id, text):
requests.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})

def process_event(chat_id, text, event_type):
# 1. Xử lý các sự kiện tự động
if event_type == "member_join":
send_message(chat_id, "Chào thành viên mới.")
return
elif event_type == "member_leave":
send_message(chat_id, "Tạm biệt khi ai đó rời nhóm.")
return

text = str(text).strip()

# 2. Xử lý lệnh từ người dùng
if text == "/start":
send_message(chat_id, "Xin chào, tôi là chat bot của nhóm Sky Dodge, tôi sẽ giải thích một số thông tin hữu ích về nhóm cho bạn.")

elif text == "/parky":
send_message(chat_id, "Theo tôi được biết Thắng là 1 con chó súc vật, chỉ biết cong đuôi khi anh em khó khăn, nên hạn chế tiếp xúc với người này.")

elif text == "/asuna":
# Gửi kèm link ảnh (có thể đổi thành API gửi ảnh riêng của Zalo)
send_message(chat_id, "Gửi bạn hình Asuna ngẫu nhiên: https://example.com/asuna_random.jpg")

elif text == "/game":
send_message(chat_id, "Link các web của Duy:\n- War Between Kings: [link]\n- Angry Fat - Random Map Edition: [link]")

elif text == "/random":
nguoi = random.choice(danh_sach_thanh_vien)
send_message(chat_id, f"Người ngẫu nhiên được chọn là: {nguoi}")

elif text == "/chain":
send_message(chat_id, "Thống kê chuỗi nhắn tin của nhóm: Đang duy trì chuỗi 7 ngày liên tiếp.")

elif text.startswith("/statistical"):
parts = text.split(" ", 1)
if len(parts) > 1:
ten = parts[1]
so_tin = thong_ke_tin_nhan.get(ten, 0)
send_message(chat_id, f"Thống kê: {ten} đã gửi {so_tin} tin nhắn.")
else:
send_message(chat_id, "Vui lòng nhập tên. Ví dụ: /statistical Duy")

def main():
print("Bot đang chạy...")
offset = None
while True:
updates = get_updates(offset)
if updates and "result" in updates:
for update in updates["result"]:
offset = update["update_id"] + 1

message = update.get("message", {})
chat_id = message.get("chat", {}).get("id")
text = message.get("text", "")

# Giả định Zalo API trả về loại sự kiện trong webhook/polling
event_type = message.get("event_type", "chat")

if chat_id:
process_event(chat_id, text, event_type)

# Chức năng tự động thống kê tin nhắn hôm qua (cần dùng thư viện schedule để chạy đúng 0:00 mỗi ngày, ở đây là giả lập)
# if thoi_gian_hien_tai == "00:00":
# send_message(chat_id_nhom, "Thống kê tin nhắn của mọi người hôm qua: ...")

time.sleep(1)

if name == "main":
main()

