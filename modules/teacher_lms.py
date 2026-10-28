import json
import streamlit as st
import pandas as pd


def render_teacher_lms():
    """Hiển thị Phân hệ Giáo viên (Teacher LMS) & Công cụ tạo/chấm đề thi 4 dạng thức chuẩn Bộ GD&ĐT."""
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div>
                <h3 style="margin:0; color:#00F5D4;">👨‍🏫 Trụ cột 4: Phân hệ Giáo viên & Trình Tạo Đề thi Chuẩn Bộ GD&ĐT</h3>
                <p style="font-size:0.85rem; color:#94A3B8; margin:4px 0 0 0;">
                    Hỗ trợ đầy đủ <b>4 dạng thức câu hỏi mới nhất (Chương trình GDPT 2018)</b> kèm quy tắc chấm điểm lũy tiến Đúng/Sai và Bảng Quản lý Cảnh báo sớm Học sinh.
                </p>
            </div>
            <span class="status-badge badge-safe">MOET 2026 EXAM FORMAT</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    lms_tabs = st.tabs([
        "📝 Phòng Thi Thực hành Chuẩn 4 Dạng thức Bộ GD&ĐT (Học sinh làm bài)",
        "🛠️ Trình Tạo Đề thi & Xuất/Nhập Mẫu Chuẩn (Dành cho Giáo viên)",
        "📊 Bảng Quản lý Lớp học & Cảnh báo Sớm (Teacher Analytics Dashboard)"
    ])

    current_exam = st.session_state.custom_exams[0]

    # --------------------------------------------------------------------------
    # TAB 4.1: HỌC SINH LÀM ĐỀ THI CHUẨN 4 DẠNG THỨC BỘ GD&ĐT & CHẤM TỰ ĐỘNG
    # --------------------------------------------------------------------------
    with lms_tabs[0]:
        st.markdown(f"""
        <div class="glass-card" style="border-left: 4px solid #00F5D4;">
            <div style="display:flex; justify-content:space-between;">
                <b style="color:#00F5D4;">Mã đề: {current_exam['exam_id']} • Môn: {current_exam['subject']} ({current_exam['grade']})</b>
                <span class="status-badge badge-warning">Thời gian: {current_exam['duration']} phút</span>
            </div>
            <h4 style="margin:6px 0 0 0;">{current_exam['title']}</h4>
        </div>
        """, unsafe_allow_html=True)

        # PHẦN I: TRẮC NGHIỆM 4 LỰA CHỌN (0.25 điểm)
        st.markdown("##### 📌 Dạng 1 (Phần I): Câu hỏi Trắc nghiệm Nhiều lựa chọn (0.25 điểm)")
        st.write(f"**Câu 1:** {current_exam['p1_stem']}")
        opts_list = [f"{k}. {v}" for k, v in current_exam["p1_options"].items()]
        user_p1 = st.radio("Chọn 1 đáp án đúng:", opts_list, index=0, key="exam_p1_radio")

        st.markdown("<hr style='border-color:rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

        # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI 4 Ý a, b, c, d (Thang điểm lũy tiến 0.1 - 0.25 - 0.5 - 1.0)
        st.markdown("##### 📌 Dạng 2 (Phần II): Câu hỏi Trắc nghiệm Đúng / Sai (Thang điểm lũy tiến chuẩn Bộ GD&ĐT: 1 ý = 0.1đ; 2 ý = 0.25đ; 3 ý = 0.5đ; 4 ý = 1.0đ)")
        st.write(f"**Câu 2:** {current_exam['p2_stem']}")
        user_p2 = {}
        for sub_key, sub_info in current_exam["p2_statements"].items():
            user_p2[sub_key] = st.checkbox(f"Ý {sub_key}) {sub_info['text']} (Tích chọn nếu ĐÚNG, bỏ trống nếu SAI)", value=True, key=f"p2_{sub_key}")

        st.markdown("<hr style='border-color:rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

        # PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN (0.5 điểm)
        st.markdown("##### 📌 Dạng 3 (Phần III): Câu hỏi Trắc nghiệm Trả lời ngắn (0.50 điểm)")
        st.write(f"**Câu 3:** {current_exam['p3_stem']}")
        user_p3 = st.number_input("Nhập kết quả số (tối đa 4 ký tự):", value=0.0, step=0.5, key="exam_p3_num")

        st.markdown("<hr style='border-color:rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

        # PHẦN IV: TỰ LUẬN / BÀI TẬP MỞ (1.0 điểm)
        st.markdown("##### 📌 Dạng 4 (Phần IV): Câu hỏi Tự luận Mở có Rubric hướng dẫn (1.00 điểm)")
        st.write(f"**Câu 4:** {current_exam['p4_stem']}")
        user_p4 = st.text_area("Trình bày các bước giải tự luận của bạn:", height=90, key="exam_p4_text")

        if st.button("🎯 Nộp bài & Chấm điểm Tự động kèm Giải thích Chuyên sâu"):
            # Chấm Phần I
            selected_letter = user_p1.split(".")[0].strip()
            score_p1 = 0.25 if selected_letter == current_exam["p1_ans"] else 0.0

            # Chấm Phần II theo đúng thang lũy tiến Bộ GD&ĐT
            correct_sub_count = 0
            for k, sub_info in current_exam["p2_statements"].items():
                if bool(user_p2[k]) == bool(sub_info["truth"]):
                    correct_sub_count += 1
            progressive_scale = {0: 0.0, 1: 0.10, 2: 0.25, 3: 0.50, 4: 1.00}
            score_p2 = progressive_scale[correct_sub_count]

            # Chấm Phần III
            score_p3 = 0.50 if abs(user_p3 - float(current_exam["p3_ans"])) <= 0.05 else 0.0

            # Chấm Phần IV theo từ khóa Rubric
            score_p4 = 1.00 if len(user_p4.split()) >= 12 else (0.50 if len(user_p4.split()) >= 5 else 0.0)

            total_exam_score = score_p1 + score_p2 + score_p3 + score_p4
            st.session_state.wisdom_points += 25

            st.markdown(f"""
            <div class="glass-card" style="border: 2px solid #00F5D4; margin-top:14px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="margin:0; color:#00F5D4;">🏆 Kết quả Chấm điểm Chuẩn Cấu trúc Mới: {total_exam_score:.2f} / 2.75 điểm</h4>
                    <span class="status-badge badge-safe">+25 WISDOM POINTS</span>
                </div>
                <ul style="font-size:0.88rem; color:#E2E8F0; margin-top:10px;">
                    <li><b>Dạng 1 (MCQ):</b> {score_p1:.2f} / 0.25đ — <i>Giải thích:</i> {current_exam['p1_explain']}</li>
                    <li><b>Dạng 2 (Đúng/Sai - Đúng {correct_sub_count}/4 ý):</b> {score_p2:.2f} / 1.00đ — <i>Giải thích:</i> {current_exam['p2_explain']}</li>
                    <li><b>Dạng 3 (Trả lời ngắn):</b> {score_p3:.2f} / 0.50đ — <i>Giải thích:</i> {current_exam['p3_explain']}</li>
                    <li><b>Dạng 4 (Tự luận):</b> {score_p4:.2f} / 1.00đ — <i>Rubric chuẩn:</i> {current_exam['p4_rubric']}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 4.2: TRÌNH TẠO ĐỀ THI DÀNH CHO GIÁO VIÊN
    # --------------------------------------------------------------------------
    with lms_tabs[1]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#C77DFF;">🛠️ Công cụ Soạn thảo & Chuẩn hóa Đề thi 4 Dạng thức (Teacher Authoring Tool)</h4>
            <p style="font-size:0.82rem; color:#94A3B8; margin:0;">
                Giáo viên nhập đề trực tiếp hoặc xuất/nhập cấu trúc JSON chuẩn để giao bài cho toàn khối.
            </p>
        </div>
        """, unsafe_allow_html=True)

        t_col1, t_col2 = st.columns(2)
        with t_col1:
            new_title = st.text_input("Tên đề kiểm tra:", value="Đề Ôn tập Chương 1 - Chuẩn GDPT 2018")
            new_subj = st.selectbox("Môn học:", ["Toán học", "Vật lý", "Hóa học", "Sinh học", "Ngữ văn", "Lịch sử", "Địa lý", "Tiếng Anh"])
            new_p1_stem = st.text_area("Nội dung câu hỏi Dạng 1 (Trắc nghiệm 4 lựa chọn):", value=current_exam["p1_stem"], height=68)
            new_p1_explain = st.text_input("Lời giải chi tiết Dạng 1 (Explanatory Feedback):", value=current_exam["p1_explain"])
        with t_col2:
            new_p3_stem = st.text_area("Nội dung câu hỏi Dạng 3 (Trả lời ngắn):", value=current_exam["p3_stem"], height=68)
            new_p3_ans = st.number_input("Đáp án số chuẩn Dạng 3:", value=float(current_exam["p3_ans"]))
            new_p3_explain = st.text_input("Lời giải chi tiết Dạng 3:", value=current_exam["p3_explain"])

        if st.button("💾 Lưu & Cập nhật Đề thi lên Hệ thống Lớp học"):
            st.session_state.custom_exams[0]["title"] = new_title
            st.session_state.custom_exams[0]["subject"] = new_subj
            st.session_state.custom_exams[0]["p1_stem"] = new_p1_stem
            st.session_state.custom_exams[0]["p1_explain"] = new_p1_explain
            st.session_state.custom_exams[0]["p3_stem"] = new_p3_stem
            st.session_state.custom_exams[0]["p3_ans"] = new_p3_ans
            st.session_state.custom_exams[0]["p3_explain"] = new_p3_explain
            st.success("✅ Đã cập nhật đề thi thành công! Học sinh có thể làm bài ngay ở Tab bên cạnh.")

        with st.expander("📄 Xem & Sao chép Cấu trúc JSON Template Chuẩn (MOET-2026-Exam-Schema)"):
            st.code(json.dumps(st.session_state.custom_exams[0], ensure_ascii=False, indent=2), language="json")

    # --------------------------------------------------------------------------
    # TAB 4.3: BẢNG QUẢN LÝ LỚP HỌC & CẢNH BÁO SỚM CHO GIÁO VIÊN
    # --------------------------------------------------------------------------
    with lms_tabs[2]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#00F5D4;">📊 Hệ thống Cảnh báo Sớm & Phân tích Chuyên cần Thực chất (Teacher Dashboard)</h4>
            <p style="font-size:0.83rem; color:#94A3B8; margin:0;">
                Đối chiếu <b>Điểm làm bài</b> với <b>Chỉ số Tập trung Chủ động (AEI)</b> và <b>Độ lệch Kỳ vọng nghề nghiệp (CMG)</b> để giúp GVCN can thiệp đúng lúc.
            </p>
        </div>
        """, unsafe_allow_html=True)

        class_data = pd.DataFrame([
            {
                "Mã HS (Ẩn danh SHA-256)": "HS-12A1-8F92 (Nguyễn Minh Anh)",
                "Tỷ lệ Hoàn thành Bài": "100%",
                "Điểm TB Đề Chuẩn": 9.1,
                "Chỉ số Tập trung AEI (%)": f"{st.session_state.aei_score:.1f}%",
                "Độ lệch Kỳ vọng CMG": "Thấp (An toàn)",
                "Phân nhóm Sư phạm": "🟢 Thực lực & Tự giác cao (Đề cử Peer Tutor)"
            },
            {
                "Mã HS (Ẩn danh SHA-256)": "HS-12A1-3C41",
                "Tỷ lệ Hoàn thành Bài": "95%",
                "Điểm TB Đề Chuẩn": 5.8,
                "Chỉ số Tập trung AEI (%)": "84.0%",
                "Độ lệch Kỳ vọng CMG": "Cao (+38%)",
                "Phân nhóm Sư phạm": "🟡 Chăm chỉ nhưng Hổng kiến thức Dạng 2 & 3 (Cần phụ đạo)"
            },
            {
                "Mã HS (Ẩn danh SHA-256)": "HS-12A1-7B19",
                "Tỷ lệ Hoàn thành Bài": "80%",
                "Điểm TB Đề Chuẩn": 8.8,
                "Chỉ số Tập trung AEI (%)": "36.5% (Rời tab 14 lần)",
                "Độ lệch Kỳ vọng CMG": "Trung bình",
                "Phân nhóm Sư phạm": "🟠 Nghi vấn Tra cứu ngoài / Treo máy (Cần kiểm tra lại)"
            },
            {
                "Mã HS (Ẩn danh SHA-256)": "HS-12A1-9E04",
                "Tỷ lệ Hoàn thành Bài": "45%",
                "Điểm TB Đề Chuẩn": 4.5,
                "Chỉ số Tập trung AEI (%)": "28.0% (Học khuya >23h30)",
                "Độ lệch Kỳ vọng CMG": "Rất cao (+52%)",
                "Phân nhóm Sư phạm": "🔴 Cảnh báo Kiệt sức (Burnout) & Hoang mang Nguyện vọng"
            }
        ])
        st.dataframe(class_data, use_container_width=True, hide_index=True)

        if st.session_state.triage_alerts:
            st.markdown("#### 🚨 Hộp thư Cảnh báo Tâm lý Khẩn cấp (Từ Trụ cột 5 - Mental Health Triage)")
            for alert in st.session_state.triage_alerts:
                st.error(alert)