import streamlit as st
import requests

# Cấu hình giao diện thương hiệu Taro Cam
st.set_page_config(page_title="Taro Cam - Ho Trợ Tâm Lý", page_icon="🍠")

st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {background-color: #ff4b4b; color: white; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🍠☁️ Taro Cam - Hệ Thống Hỗ Trợ Tâm Lý Học Đường")
st.subheader("'Taro Chào các bạn Chuyên NTTer!'")

menu = st.radio("Chọn chức năng:", ["1. Tâm sự cùng bộ đôi Taro & Mây", "2. Hòm thư ẩn danh gửi nhà trường"])

if menu == "1. Tâm sự cùng bộ đôi Taro & Mây":
    st.markdown("### 💬 Trò chuyện nhanh cùng Khoai Môn & Mây Hồng")
    user_input = st.text_area("Hôm nay có điều gì làm cậu bận lòng ở lớp hay KTX?")
    
    if st.button("Gửi tâm sự"):
        if user_input:
            st.markdown("---")
            st.markdown("☁️ **Mây Hồng:** *Ôi giời ơi, mới kiểm tra điểm kém hơn bạn bè một chút mà đã than thở thế này à? Tưởng nhà vô địch Olympic sinh ra là biết bay chắc?*")
            st.markdown("🍠 **Khoai Môn:** *Đúng rồi đó cậu! Thua kém lúc nay không phải để tự ti hay buông xuôi, mà để thấy mình còn rất nhiều khoảng trống bứt phá. Bình tĩnh, lên lịch chiến đấu lại!*")
            st.info("🍃 [CHIẾC LÁ PHẢN HỒI]: Đừng so sánh chặng đua của mình với vạch đích của người khác. Cậu đang cố gắng từng ngày và thế là quá tuyệt rồi!")
        else:
            st.warning("Cậu nhớ nhập tâm sự trước khi gửi nha!")

elif menu == "2. Hòm thư ẩn danh gửi nhà trường":
    st.markdown("### ✉️ Hòm Thư Kết Nối Giáo Viên / Phòng Tư Vấn")
    ten_lop = st.text_input("Tên / Lớp của cậu (có thể để ẩn danh):")
    noi_dung = st.text_area("Nội dung thư gửi thầy cô / phòng tư vấn:")
    
    # Số điện thoại cố định của em
    sdt_mac_dinh = "+84357158572"
    st.text(f"Số điện thoại liên hệ gắn kèm: {sdt_mac_dinh}")

    if st.button("Gửi bức thư đặc biệt"):
        if noi_dung:
            # -------------------------------------------------------------
            # PHẦN GỬI THẬT QUA TELEGRAM BOT (Đã có thể tích hợp thực tế)
            # -------------------------------------------------------------
           import smtplib
from email.mime.text import MIMEText

# Cấu hình tài khoản gửi tin nhắn (Email hệ thống)
EMAIL_GUI = "letranhoainam30@gmail.com"  # Email giả lập hệ thống
EMAIL_NHAN = "letranhoainam30@gmail.com"  # Thay bằng Gmail nhận của giáo viên
MAT_KHAU_UNG_DUNG = "30032011@Nam"  # Mật khẩu ứng dụng tạo từ Gmail gửi

message = f"[TARO CAM - THƯ KHẨN]\n👤 Người gửi: {ten_lop}\n\n📝 Nội dung tâm sự:\n{noi_dung}"

# Đoạn code tự động kết nối và gửi Gmail
# Đoạn code tự động kết nối và gửi Gmail
try:
    msg = MIMEText(message, _charset="utf-8")
    msg["Subject"] = "Taro Cam - Thông báo tâm sự khẩn từ học sinh"
    msg["From"] = EMAIL_GUI
    msg["To"] = EMAIL_NHAN

    with smtplib.SMTP_SSL("://gmail.com", 465) as server:
        server.login(EMAIL_GUI, MAT_KHAU_UNG_DUNG)
        server.sendmail(EMAIL_GUI, EMAIL_NHAN, msg.as_string())
    
    st.success("🔔 ĐÃ GỬI THƯ THÀNH CÔNG! Chiếc lá đặc biệt đã bay đến phòng tư vấn.")
    st.balloons()
except Exception as e:
    st.error(f"Lỗi gửi thư: {e}")
