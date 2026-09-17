import streamlit as st
import requests

# Cấu hình giao diện thương hiệu Taro Cam
st.set_page_config(page_title="Taro Cam - Hỗ Trợ Tâm Lý", page_icon="📝")

st.markdown("""
<style>
.main {background-color: #f8f9fa;}
.stButton>button {background-color: #ff4d4d; color: white; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🍁 Taro Cam - Hệ Thống Hỗ Trợ Tâm Lý Học Đường")
st.subheader("Trò chuyện thông minh cùng Khoai Môn & Mây Hồng (AI)")

menu = st.radio("Chọn chức năng:", ["1. Tâm sự cùng bộ đôi Taro & Mây", "2. Hòm thư ẩn danh"])

if menu == "1. Tâm sự cùng bộ đôi Taro & Mây":
    st.write("Hôm nay có điều gì làm cậu bận lòng ở lớp hay KTX? Hãy chia sẻ với tớ nhé.")
    
    ten_lop = st.text_input("Tên lớp của cậu:")
    noi_dung = st.text_area("Nội dung tâm sự của cậu:")
    
    if st.button("Gửi tâm sự và Trò chuyện cùng AI"):
        if ten_lop and noi_dung:
            with st.spinner("Bộ đôi Taro & Mây đang lắng nghe và suy nghĩ lời khuyên cho cậu..."):
                
                # Sử dụng Public AI Server miễn phí không cần API Key
                url = "https://pollinations.ai"
                prompt = (
                    f"Bạn là bộ đôi chuyên gia tâm lý học đường Taro và Mây Hồng. "
                    f"Hãy đọc tâm sự sau của một bạn học sinh lớp {ten_lop}: '{noi_dung}'. "
                    f"Hãy đưa ra lời khuyên, sự an ủi thật ấm áp, thân thiện, đồng cảm dưới danh nghĩa là người bạn Taro và Mây Hồng. "
                    f"Cách xưng hô: Gọi học sinh là 'cậu' hoặc 'bạn', xưng là 'Taro & Mây' hoặc 'tớ'. Trả lời hoàn toàn bằng tiếng Việt mượt mà."
                )
                
                try:
                    response = requests.post(url, json={"messages": [{"role": "user", "content": prompt}]})
                    if response.status_code == 200:
                        ai_reply = response.text
                        
                        # Hiển thị câu trả lời của AI ra màn hình
                        st.subheader("💌 Lời khuyên từ bộ đôi Taro & Mây dành cho cậu:")
                        st.info(ai_reply)
                        st.balloons()
                    else:
                        st.error("Hệ thống AI đang bận, cậu vui lòng thử lại sau chút nhé!")
                except Exception as e:
                    st.error(f"Lỗi kết nối AI: {e}")
        else:
            st.warning("Cậu chưa nhập đầy đủ thông tin tên lớp hoặc nội dung thư kìa!")

elif menu == "2. Hòm thư ẩn danh":
    st.write("Nơi cậu có thể trút bỏ những tâm tư thầm kín mà không lo bị lộ danh tính.")
noi_dung_an_danh = st.text_area("Nhập tâm sự ẩn danh của cậu vào đây:")
    if st.button("Gửi ẩn danh"):
        if noi_dung_an_danh:
            st.success("Gửi thư ẩn danh thành công! Bí mật của cậu sẽ được giữ kín.")
            st.balloons()
        else:
            st.warning("Vui lòng nhập nội dung trước khi gửi.")
import streamlit as st
import requests

# Cấu hình giao diện thương hiệu Taro Cam
st.set_page_config(page_title="Taro Cam - Hỗ Trợ Tâm Lý", page_icon="📝")

st.markdown("""
<style>
.main {background-color: #f8f9fa;}
.stButton>button {background-color: #ff4d4d; color: white; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🍁 Taro Cam - Hệ Thống Hỗ Trợ Tâm Lý Học Đường")
st.subheader("Trò chuyện thông minh cùng Khoai Môn & Mây Hồng (AI)")

menu = st.radio("Chọn chức năng:", ["1. Tâm sự cùng bộ đôi Taro & Mây", "2. Hòm thư ẩn danh"])

if menu == "1. Tâm sự cùng bộ đôi Taro & Mây":
    st.write("Hôm nay có điều gì làm cậu bận lòng ở lớp hay KTX? Hãy chia sẻ với tớ nhé.")
    
    ten_lop = st.text_input("Tên lớp của cậu:")
    noi_dung = st.text_area("Nội dung tâm sự của cậu:")
    
    if st.button("Gửi tâm sự và Trò chuyện cùng AI"):
        if ten_lop and noi_dung:
            with st.spinner("Bộ đôi Taro & Mây đang lắng nghe và suy nghĩ lời khuyên cho cậu..."):
                
                # Sử dụng Public AI Server miễn phí không cần API Key
                url = "https://pollinations.ai"
                prompt = (
                    f"Bạn là bộ đôi chuyên gia tâm lý học đường Taro và Mây Hồng. "
                    f"Hãy đọc tâm sự sau của một bạn học sinh lớp {ten_lop}: '{noi_dung}'. "
                    f"Hãy đưa ra lời khuyên, sự an ủi thật ấm áp, thân thiện, đồng cảm dưới danh nghĩa là người bạn Taro và Mây Hồng. "
                    f"Cách xưng hô: Gọi học sinh là 'cậu' hoặc 'bạn', xưng là 'Taro & Mây' hoặc 'tớ'. Trả lời hoàn toàn bằng tiếng Việt mượt mà."
                )
                
                try:
                    response = requests.post(url, json={"messages": [{"role": "user", "content": prompt}]})
                    if response.status_code == 200:
                        ai_reply = response.text
                        
                        # Hiển thị câu trả lời của AI ra màn hình
                        st.subheader("💌 Lời khuyên từ bộ đôi Taro & Mây dành cho cậu:")
                        st.info(ai_reply)
                        st.balloons()
                    else:
                        st.error("Hệ thống AI đang bận, cậu vui lòng thử lại sau chút nhé!")
                except Exception as e:
                    st.error(f"Lỗi kết nối AI: {e}")
        else:
            st.warning("Cậu chưa nhập đầy đủ thông tin tên lớp hoặc nội dung thư kìa!")

elif menu == "2. Hòm thư ẩn danh":
    st.write("Nơi cậu có thể trút bỏ những tâm tư thầm kín mà không lo bị lộ danh tính.")
noi_dung_an_danh = st.text_area("Nhập tâm sự ẩn danh của cậu vào đây:")
    if st.button("Gửi ẩn danh"):
        if noi_dung_an_danh:
            st.success("Gửi thư ẩn danh thành công! Bí mật của cậu sẽ được giữ kín.")
            st.balloons()
        else:
            st.warning("Vui lòng nhập nội dung trước khi gửi.")
