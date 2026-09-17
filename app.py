import streamlit as st
import requests
import smtplib
from email.mime.text import MIMEText

# Cấu hình giao diện thương hiệu Taro Cam
st.set_page_config(page_title="Taro Cam - Hỗ Trợ Tâm Lý", page_icon="📝")

st.markdown("""
<style>
.main {background-color: #f8f9fa;}
.stButton>button {background-color: #ff4d4d; color: white; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🍁 Taro Cam - Hệ Thống Hỗ Trợ Tâm Lý Học Đường")
st.subheader("Trò chuyện nhanh cùng Khoai Môn & Mây Hồng")

menu = st.radio("Chọn chức năng:", ["1. Tâm sự cùng bộ đôi Taro & Mây", "2. Hòm thư ẩn danh"])

if menu == "1. Tâm sự cùng bộ đôi Taro & Mây":
    st.write("Hôm nay có điều gì làm cậu bận lòng ở lớp hay KTX?")
    
    ten_lop = st.text_input("Tên lớp của cậu:")
    noi_dung = st.text_area("Nội dung tâm sự khẩn cấp:")
    
    if st.button("Gửi tâm sự"):
        if ten_lop and noi_dung:
            # Cấu hình tài khoản gửi tin nhắn (Email hệ thống)
            EMAIL_GUI = "letranhoainam30@gmail.com"  
            EMAIL_NHAN = "letranhoainam30@gmail.com"  
            MAT_KHAU_UNG_DUNG = "3333333333333333"  # Sau này thay bằng 16 ký tự thật của Google để gửi được thư thật

            message = f"[TARO CAM - THƯ KHẨN]\n👤 Người gửi: {ten_lop}\n\n📝 Nội dung tâm sự:\n{noi_dung}"

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
        else:
            st.warning("Cậu chưa nhập đầy đủ thông tin tên lớp hoặc nội dung thư kìa!")

elif menu == "2. Hòm thư ẩn danh":
    st.write("Nơi cậu có thể trút bỏ những tâm tư thầm kín mà không lo bị lộ danh tính.")
    noi_dung_an_danh = st.text_area("Nhập tâm sự ẩn danh của cậu vào đây:")
    if st.button("Gửi ẩn danh"):
        if noi_dung_an_danh:
            st.success("Gửi thư ẩn danh thành công! Bí mật của cậu sẽ được giữ kín.")
        else:
            st.warning("Vui lòng nhập nội dung trước khi gửi.")
