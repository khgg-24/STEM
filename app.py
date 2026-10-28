import streamlit as st
from config import inject_custom_css, init_session_state
from modules.learning_hub import render_learning_hub
from modules.career_navigator import render_career_navigator
from modules.community_qa import render_community_qa
from modules.teacher_lms import render_teacher_lms
from modules.telemetry_sensor import render_telemetry_and_triage

# ==============================================================================
# 1. CẤU HÌNH TRANG & KHỞI TẠO TRẠNG THÁI
# ==============================================================================
st.set_page_config(
    page_title="ED-ODYSSEY NEXUS | Hệ sinh thái Học tập Đa môn & Định hướng Tuyển sinh",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_session_state()
inject_custom_css()

# ==============================================================================
# 2. THANH ĐIỀU HƯỚNG SIDEBAR GLASSMORPHISM
# ==============================================================================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 8px 0 4px 0;">
            <div style="font-size: 2.1rem;">🚀</div>
            <h2 style="margin: 0; font-weight: 800; background: linear-gradient(90deg, #00F5D4, #00BBF9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ED-ODYSSEY NEXUS
            </h2>
            <p style="font-size: 0.76rem; color: #94A3B8; margin-top: 2px;">
                Multi-Subject EdTech & Holistic Career Engine
            </p>
            <span class="status-badge badge-safe">● SYSTEM ONLINE • v5.0 NEXUS</span>
        </div>
        <hr style="border-color: rgba(255,255,255,0.08); margin: 12px 0;">
    """, unsafe_allow_html=True)

    st.markdown("#### 👤 Hồ sơ Học sinh / Thí sinh")
    st.session_state.student_name = st.text_input("Họ và tên:", value=st.session_state.student_name)
    st.session_state.school_name = st.text_input("Trường THCS / THPT:", value=st.session_state.school_name)
    st.session_state.grade_level = st.selectbox(
        "Cấp học hiện tại:",
        [
            "Lớp 12 (Tuyển sinh Đại học Toàn quốc)",
            "Lớp 10 - 11 (Định hình Tổ hợp GDPT 2018)",
            "Lớp 6 - 9 THCS (Lộ trình Ôn thi vào 10)"
        ]
    )

    st.markdown(f"""
    <div class="glass-card" style="padding:10px 14px; margin-top:8px;">
        <div style="display:flex; justify-content:space-between; font-size:0.8rem;">
            <span>✨ Điểm Trí tuệ (WP):</span>
            <b style="color:#00F5D4;">{st.session_state.wisdom_points} WP</b>
        </div>
        <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin-top:4px;">
            <span>⚡ Chỉ số Tập trung AEI:</span>
            <b style="color:#34D399;">{st.session_state.aei_score:.1f}%</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🧭 Điều hướng 5 Phân hệ Cốt lõi")
    selected_module = st.radio(
        "Chọn Mô-đun Chức năng:",
        [
            "📚 1. Công cụ Học tập Đa môn & Bảo tàng Sai lầm",
            "🧭 2. Định hướng Đa chiều & Tuyển sinh (Lớp 6–12)",
            "🤝 3. Cộng đồng Hỏi-Đáp & Odyssey Squads",
            "👨‍🏫 4. Phân hệ Giáo viên & Đề thi Chuẩn Bộ GD&ĐT",
            "⏱️ 5. Cảm biến Chống Treo máy (AEI) & Sơ cứu Tâm lý"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 12px 0;'>", unsafe_allow_html=True)
    github_url = "https://github.com/ed-odyssey-team/ed-odyssey-nexus"
    st.markdown(f"""
        <div style="font-size: 0.75rem; color: #94A3B8; margin-bottom: 6px;">
            🔓 Minh bạch mã nguồn (Phụ lục 8 - KHKT):
        </div>
        <a href="{github_url}" target="_blank" class="github-btn">
            View Repository on GitHub ↗
        </a>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. BANNER HEADER TỔNG QUAN
# ==============================================================================
st.markdown(f"""
<div class="glass-card" style="padding: 16px 22px; margin-bottom: 18px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center;">
    <div>
        <div style="font-size: 0.76rem; color: #00F5D4; font-weight: 700; letter-spacing: 0.8px;">
            HỆ SINH THÁI HỌC TẬP TƯƠNG TÁC ĐA MÔN, ĐỊNH HƯỚNG ĐA CHIỀU & ĐIỀU HƯỚNG HÀNH VI HỌC ĐƯỜNG
        </div>
        <h2 style="margin: 2px 0 0 0; font-size: 1.45rem; font-weight: 800;">
            ED-ODYSSEY NEXUS — Kiến tạo kỷ luật từ sự thấu cảm & Bình đẳng hóa công cụ học tập
        </h2>
    </div>
    <div style="text-align: right;">
        <div style="font-size: 0.84rem; color: #E2E8F0;">
            Học sinh: <b>{st.session_state.student_name}</b> | <code>{st.session_state.grade_level.split('(')[0].strip()}</code>
        </div>
        <div style="font-size: 0.76rem; color: #94A3B8;">
            Đơn vị: {st.session_state.school_name}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. ĐIỀU HƯỚNG TỚI TỪNG MÔ-ĐUN CHỨC NĂNG
# ==============================================================================
try:
    if selected_module.startswith("📚 1."):
        render_learning_hub()
    elif selected_module.startswith("🧭 2."):
        render_career_navigator()
    elif selected_module.startswith("🤝 3."):
        render_community_qa()
    elif selected_module.startswith("👨‍🏫 4."):
        render_teacher_lms()
    elif selected_module.startswith("⏱️ 5."):
        render_telemetry_and_triage()
except Exception as err:
    st.error(f"Đã xảy ra lỗi ngoại lệ trong quá trình hiển thị mô-đun: {err}")

# ==============================================================================
# 5. FOOTER MINH BẠCH SỬ DỤNG AI (TUÂN THỦ PHỤ LỤC 8 - KHKT 2026-2027)
# ==============================================================================
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
with st.expander("📋 Nhật ký Minh bạch Sử dụng AI & Kiểm chứng Khoa học (Tuân thủ Phụ lục 8 - Cuộc thi KHKT 2026–2027)"):
    st.markdown("""
    - **Cam kết Liêm chính Học thuật:** Toàn bộ mô hình toán học **Ma trận Tương thích Đa biến (Holistic Fit Score)**, **Hàm Dự báo Trúng tuyển Đa phương thức ($\text{Hope Score}_{\text{Multi}}$)**, **Chỉ số Tập trung Chủ động chống treo máy ($\text{AEI}$)** và dữ liệu thực nghiệm *Shadowing* được nhóm học sinh trực tiếp thiết kế, kiểm thử và ghi chép trong Sổ nhật ký nghiên cứu (Phụ lục 3).
    - **Khai báo Sử dụng Công cụ AI Tạo sinh (Mục II.7 - Phụ lục 8):** Sử dụng AI hỗ trợ cấu trúc giao diện CSS Glassmorphism và khung mã mô-đun Streamlit/Plotly ban đầu; nhóm tác giả trực tiếp rà soát thuật toán, chuẩn hóa cấu trúc đề thi 4 dạng thức của Bộ GD&ĐT và kiểm chứng độ chính xác.
    """)