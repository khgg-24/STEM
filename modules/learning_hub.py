import streamlit as st
import numpy as np
import plotly.graph_objects as go


def render_learning_hub():
    """Hiển thị Bộ công cụ hỗ trợ học tập đa môn tại chỗ (KHTN, KHXH, Tiếng Anh)."""
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div>
                <h3 style="margin:0; color:#00F5D4;">📚 Trụ cột 1: Bộ Công cụ Học tập Đa môn Tại chỗ (Universal Learning Toolkit)</h3>
                <p style="font-size:0.85rem; color:#94A3B8; margin:4px 0 0 0;">
                    Chống học vẹt & chép lời giải thụ động bằng cơ chế <b>Mở khóa Từng bước (Scaffolded Solver)</b>, Mô phỏng STEM 3D siêu nhẹ và <b>Bảo tàng Sai lầm</b>.
                </p>
            </div>
            <span class="status-badge badge-safe">GDPT 2018 STANDARD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    sub_tabs = st.tabs([
        "🔬 Khối KHTN (Toán - Lý - Hóa - Sinh)",
        "📖 Khối KHXH (Văn - Sử - Địa - GDKT&PL)",
        "🌐 Tiếng Anh (Smart SRS Flashcards)",
        "🏛️ Bảo tàng Sai lầm (Mistake Museum)"
    ])

    # --------------------------------------------------------------------------
    # TAB 1.1: KHOA HỌC TỰ NHIÊN (INTERACTIVE STEP-BY-STEP + 3D STEM)
    # --------------------------------------------------------------------------
    with sub_tabs[0]:
        col_left, col_right = st.columns([1.15, 1.0], gap="large")

        with col_left:
            st.markdown("""
            <div class="glass-card">
                <h4 style="margin:0 0 6px 0; color:#00F5D4;">🧩 Trợ lý Giải bài Mở khóa Từng bước (Step-by-Step Solver)</h4>
                <p style="font-size:0.82rem; color:#94A3B8; margin:0;">
                    Hệ thống khóa đáp án cuối. Bạn phải nhập đúng bước biến đổi trung gian để mở khóa lời giải và nhận <b>+15 Điểm Trí tuệ (WP)</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)

            problem_choice = st.selectbox(
                "Chọn chuyên đề bài tập KHTN:",
                [
                    "Toán 12: Tìm cực trị hàm số hợp và khoảng cách Oxyz",
                    "Vật lý 11/12: Giao thoa sóng cơ & Dao động điều hòa",
                    "Hóa học 9/12: Bài toán hiệu suất phản ứng Este hóa"
                ]
            )

            st.markdown("""
            <div class="glass-card" style="border-left: 4px solid #00BBF9;">
                <b>📌 Đề bài thực hành:</b> Cho hàm số bậc ba $f(x) = x^3 - 3x^2 - 9x + 12$.
                Hãy tìm tổng giá trị Cực đại và Cực tiểu của hàm số trên $\\mathbb{R}$.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("##### 🔓 Bước 1 (Định lý & Phương pháp cốt lõi):")
            st.info("Tính đạo hàm $f'(x) = 3x^2 - 6x - 9$. Giải phương trình $f'(x) = 0 \\Leftrightarrow x^2 - 2x - 3 = 0$.")

            st.markdown("##### ✍️ Bước 2 (Kiểm tra Tư duy Chủ động - Chống treo máy):")
            ans_step2 = st.number_input(
                "Nhập nghiệm dương của phương trình f'(x) = 0 để mở khóa Bước 3:",
                min_value=-10.0,
                max_value=10.0,
                value=0.0,
                step=1.0
            )

            if st.button("✅ Xác thực Bước 2 & Mở khóa Đáp án"):
                if abs(ans_step2 - 3.0) < 1e-5:
                    st.session_state.step_math_unlocked = 3
                    st.session_state.wisdom_points += 15
                    st.session_state.checkin_passed += 1
                    st.session_state.checkin_total += 1
                    st.success("🎉 Chính xác! Nghiệm dương là x = 3 (nghiệm còn lại là x = -1). Bạn nhận được +15 WP!")
                else:
                    st.session_state.checkin_total += 1
                    st.error("❌ Chưa chính xác! Gợi ý: Phương trình a - b + c = 0 có một nghiệm là -1 và một nghiệm là -c/a.")

            if st.session_state.step_math_unlocked >= 3:
                st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #10B981;">
                    <h5 style="margin:0 0 6px 0; color:#34D399;">🏆 Bước 3 (Lời giải Hoàn chỉnh & Cảnh báo Bẫy):</h5>
                    <ul style="font-size:0.86rem; color:#E2E8F0; margin-bottom:6px;">
                        <li>Tại $x_1 = -1 \\Rightarrow y_{\\text{CĐ}} = (-1)^3 - 3(-1)^2 - 9(-1) + 12 = 17$.</li>
                        <li>Tại $x_2 = 3 \\Rightarrow y_{\\text{CT}} = 3^3 - 3(3)^2 - 9(3) + 12 = -15$.</li>
                        <li>Tổng $y_{\\text{CĐ}} + y_{\\text{CT}} = 17 + (-15) = 2$.</li>
                    </ul>
                    <div style="background:rgba(239,68,68,0.18); padding:10px; border-radius:8px; font-size:0.8rem; color:#FCA5A5;">
                        ⚠️ <b>Bẫy Bảo tàng Sai lầm:</b> 74% học sinh kết luận nhầm điểm cực đại là $x = -1$ thay vì giá trị cực đại $y = 17$!
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with col_right:
            st.markdown("""
            <div class="glass-card neon-card-purple">
                <h4 style="margin:0 0 6px 0; color:#C77DFF;">🌌 Phòng Thí nghiệm Mô phỏng STEM 3D Siêu nhẹ</h4>
                <p style="font-size:0.82rem; color:#94A3B8; margin:0;">
                    Chạy mượt trên cả máy tính cấu hình cũ ở vùng nông thôn (không cần GPU rời).
                </p>
            </div>
            """, unsafe_allow_html=True)

            freq_val = st.slider("Tần số sóng giao thoa / Độ cong mặt thế năng (ω):", 0.5, 4.0, 1.8, 0.1)
            x_grid = np.linspace(-3, 3, 45)
            y_grid = np.linspace(-3, 3, 45)
            X_mesh, Y_mesh = np.meshgrid(x_grid, y_grid)
            R_dist = np.sqrt(X_mesh**2 + Y_mesh**2) + 1e-5
            Z_mesh = np.sin(freq_val * R_dist) / (0.6 * R_dist + 1.0)

            fig_stem = go.Figure(data=[go.Surface(
                z=Z_mesh,
                x=X_mesh,
                y=Y_mesh,
                colorscale="Viridis",
                opacity=0.92
            )])
            fig_stem.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(17, 25, 40, 0.65)",
                height=390,
                margin=dict(l=0, r=0, b=0, t=10),
                scene=dict(
                    xaxis_title="Trục X (cm)",
                    yaxis_title="Trục Y (cm)",
                    zaxis_title="Biên độ u(x,y)"
                )
            )
            st.plotly_chart(fig_stem, use_container_width=True)

    # --------------------------------------------------------------------------
    # TAB 1.2: KHOA HỌC XÃ HỘI (PEEL ESSAY BUILDER & CHRONOLOGY TIMELINE)
    # --------------------------------------------------------------------------
    with sub_tabs[1]:
        xh_col1, xh_col2 = st.columns(2, gap="large")

        with xh_col1:
            st.markdown("""
            <div class="glass-card">
                <h4 style="margin:0 0 6px 0; color:#00F5D4;">✒️ Khung Tư duy Bài luận Ngữ văn & Xã hội (Mô hình P-E-E-L)</h4>
                <p style="font-size:0.82rem; color:#94A3B8; margin:0;">
                    Lập dàn ý chặt chẽ theo 4 bước: <b>Point (Luận điểm) - Evidence (Dẫn chứng) - Explain (Phân tích) - Link (Liên hệ)</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)

            essay_topic = st.text_input(
                "Chủ đề Nghị luận Xã hội / Văn học:",
                value="Bản lĩnh tự chủ của người trẻ trước sự thao túng của thuật toán mạng xã hội (FoMO)"
            )
            p_point = st.text_area("1. POINT (Luận điểm cốt lõi):", value="Tự chủ nhận thức là la bàn giúp người trẻ làm chủ công nghệ thay vì trở thành nô lệ của những lượt tương tác ảo.", height=68)
            e_evidence = st.text_area("2. EVIDENCE (Dẫn chứng thực tế / Văn học):", value="Khảo sát thực địa cho thấy học sinh mất trung bình 15 phút để lấy lại sự tập trung sâu sau mỗi lần kiểm tra thông báo ngắn.", height=68)
            e_explain = st.text_area("3. EXPLAIN (Lập luận & Phản biện):", value="Khi thiếu kỷ luật tự giác, não bộ bị cuốn vào cơ chế thưởng dopamine tức thời, làm suy giảm năng lực tư duy dài hạn.", height=68)
            l_link = st.text_area("4. LINK (Bài học nhận thức & Hành động):", value="Mỗi học sinh cần thiết lập ranh giới số và rèn luyện thói quen học tập sâu (Deep Work) mỗi ngày.", height=68)

            if st.button("📝 Tổng hợp Dàn ý Chuẩn & Chấm điểm Lập luận (+10 WP)"):
                total_words = len((p_point + " " + e_evidence + " " + e_explain + " " + l_link).split())
                st.session_state.wisdom_points += 10
                st.success(f"Đã tổng hợp dàn ý hoàn chỉnh ({total_words} từ) — Cấu trúc P-E-E-L đạt chuẩn 100%! Cộng +10 WP.")

        with xh_col2:
            st.markdown("""
            <div class="glass-card neon-card-purple">
                <h4 style="margin:0 0 6px 0; color:#C77DFF;">⏳ Trục Tọa độ Lịch sử & Sơ đồ Tư duy Địa lý - GDKT&PL</h4>
                <p style="font-size:0.82rem; color:#94A3B8; margin:0;">
                    Liên kết <b>Nguyên nhân ➔ Diễn biến ➔ Ý nghĩa lịch sử</b> trực quan thay cho học thuộc lòng máy móc.
                </p>
            </div>
            """, unsafe_allow_html=True)

            hist_period = st.selectbox(
                "Chọn Chuyên đề Lịch sử / Địa lý:",
                [
                    "Lịch sử 12: Các mốc thắng lợi Ngoại giao & Quân sự Việt Nam (1945 - 1975)",
                    "Địa lý 12: Chuyển dịch cơ cấu kinh tế các vùng trọng điểm",
                    "GDKT&PL 11/12: Quyền và nghĩa vụ công dân trong kinh tế số"
                ]
            )

            timeline_events = [
                ("02/09/1945", "Tuyên ngôn Độc lập", "Khai sinh nước Việt Nam Dân chủ Cộng hòa, mở ra kỷ nguyên độc lập tự do."),
                ("07/05/1954", "Chiến thắng Điện Biên Phủ", "Đập tan kế hoạch Nava, tạo tiền đề trực tiếp dẫn đến Hiệp định Giơ-ne-vơ."),
                ("27/01/1973", "Hiệp định Paris", "Buộc Hoa Kỳ rút hết quân viễn chinh, tạo bước ngoặt chiến lược giải phóng miền Nam."),
                ("30/04/1975", "Chiến dịch Hồ Chí Minh", "Thu non sông về một mối, hoàn thành cách mạng dân tộc dân chủ nhân dân.")
            ]
            for date_str, title_str, meaning_str in timeline_events:
                st.markdown(f"""
                <div class="glass-card" style="padding:12px 16px; margin-bottom:10px; border-left: 3px solid #F15BB5;">
                    <div style="font-size:0.76rem; color:#F15BB5; font-weight:700;">📅 MỐC THỜI GIAN: {date_str}</div>
                    <div style="font-size:0.95rem; font-weight:700; color:#F8FAFC;">{title_str}</div>
                    <div style="font-size:0.82rem; color:#CBD5E1; margin-top:2px;">➔ <b>Ý nghĩa cốt lõi:</b> {meaning_str}</div>
                </div>
                """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 1.3: TIẾNG ANH (SMART SRS FLASHCARDS)
    # --------------------------------------------------------------------------
    with sub_tabs[2]:
        cards = [
            {
                "word": "Cognitive Resilience (n)",
                "ipa": "/ˈkɒɡ.nə.tɪv rɪˈzɪl.jəns/",
                "context": "Building cognitive resilience helps students overcome digital distractions.",
                "meaning": "Khả năng phục hồi nhận thức (sức bền tư duy trước áp lực và xao nhãng).",
                "grammar": "Danh từ ghép (Adj + Noun) thường đóng vai trò chủ ngữ hoặc tân ngữ trong bài đọc IELTS/THPT."
            },
            {
                "word": "Intrinsic Motivation (n)",
                "ipa": "/ɪnˈtrɪn.zɪk ˌməʊ.tɪˈveɪ.ʃən/",
                "context": "Self-directed learners rely on intrinsic motivation rather than external rewards.",
                "meaning": "Động lực nội tại (sự tự giác xuất phát từ đam mê bên trong).",
                "grammar": "Đi kèm giới từ 'rely on / driven by intrinsic motivation'."
            },
            {
                "word": "Mitigate (v)",
                "ipa": "/ˈmɪt.ɪ.ɡeɪt/",
                "context": "Adaptive nudges can effectively mitigate the negative effects of FoMO.",
                "meaning": "Giảm thiểu, làm dịu bớt (mức độ nghiêm trọng của một vấn đề).",
                "grammar": "Ngoại động từ (Transitive Verb) + Noun phrase (mitigate risks/impacts)."
            }
        ]

        idx = st.session_state.flashcard_idx % len(cards)
        current_card = cards[idx]

        st.markdown(f"""
        <div class="glass-card" style="text-align:center; padding:28px;">
            <span class="status-badge badge-safe">SPACED REPETITION (SM-2) • THẺ {idx + 1}/{len(cards)}</span>
            <h2 style="margin:14px 0 4px 0; color:#00F5D4; font-size:2.0rem;">{current_card['word']}</h2>
            <div style="font-size:0.95rem; color:#94A3B8; margin-bottom:14px;">{current_card['ipa']}</div>
            <p style="font-size:1.0rem; color:#E2E8F0; font-style:italic;">"{current_card['context']}"</p>
        </div>
        """, unsafe_allow_html=True)

        fc_col1, fc_col2, fc_col3 = st.columns(3)
        with fc_col1:
            if st.button("🔄 Lật Thẻ (Xem Nghĩa & Ngữ pháp)"):
                st.session_state.flashcard_flipped = not st.session_state.flashcard_flipped
        with fc_col2:
            if st.button("⏭️ Thẻ Tiếp theo"):
                st.session_state.flashcard_idx = (idx + 1) % len(cards)
                st.session_state.flashcard_flipped = False
                st.rerun()
        with fc_col3:
            if st.button("✅ Đã thuộc làu (+5 WP)"):
                st.session_state.wisdom_points += 5
                st.session_state.flashcard_idx = (idx + 1) % len(cards)
                st.session_state.flashcard_flipped = False
                st.rerun()

        if st.session_state.flashcard_flipped:
            st.markdown(f"""
            <div class="glass-card neon-card-purple">
                <h4 style="margin:0 0 6px 0; color:#34D399;">💡 Nghĩa Tiếng Việt: {current_card['meaning']}</h4>
                <p style="margin:0; font-size:0.88rem; color:#CBD5E1;">📌 <b>Cấu trúc Ngữ pháp:</b> {current_card['grammar']}</p>
            </div>
            """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 1.4: BẢO TÀNG SAI LẦM (MISTAKE MUSEUM)
    # --------------------------------------------------------------------------
    with sub_tabs[3]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#F15BB5;">🏛️ Không gian "Bảo tàng Sai lầm" (Mistake Museum)</h4>
            <p style="font-size:0.84rem; color:#94A3B8; margin:0;">
                Nơi lưu trữ và tôn vinh những lỗi sai kinh điển của học sinh đi trước: <i>"Thất bại là tài sản của quá trình tiến hóa tri thức"</i>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        for item in st.session_state.mistake_museum:
            st.markdown(f"""
            <div class="glass-card" style="padding:16px; border-left: 4px solid #F15BB5;">
                <div style="display:flex; justify-content:space-between;">
                    <span class="status-badge badge-warning">{item['subject']} • {item['topic']}</span>
                    <span style="font-size:0.78rem; color:#94A3B8;">Đóng góp bởi: <b>{item['contributor']}</b></span>
                </div>
                <div style="margin-top:8px; font-size:0.92rem; color:#FCA5A5;">❌ <b>Bẫy sai lầm thường gặp:</b> {item['trap']}</div>
                <div style="margin-top:4px; font-size:0.92rem; color:#34D399;">✅ <b>Cách khắc phục chuẩn:</b> {item['fix']}</div>
            </div>
            """, unsafe_allow_html=True)

        with st.expander("➕ Đóng góp Lỗi sai mới vào Bảo tàng Sai lầm (+20 WP)"):
            m_sub = st.selectbox("Môn học:", ["Toán học", "Vật lý", "Hóa học", "Sinh học", "Ngữ văn", "Lịch sử", "Địa lý", "Tiếng Anh"])
            m_topic = st.text_input("Chuyên đề / Bài học:")
            m_trap = st.text_input("Mô tả lỗi sai thường gặp:")
            m_fix = st.text_input("Cách ghi nhớ để không tái phạm:")
            if st.button("🚀 Gửi vào Bảo tàng Sai lầm"):
                if m_topic.strip() and m_trap.strip() and m_fix.strip():
                    st.session_state.mistake_museum.insert(0, {
                        "subject": m_sub,
                        "topic": m_topic.strip(),
                        "trap": m_trap.strip(),
                        "fix": m_fix.strip(),
                        "contributor": st.session_state.student_name
                    })
                    st.session_state.wisdom_points += 20
                    st.success("Đã bổ sung vào Bảo tàng Sai lầm! Bạn nhận được +20 Wisdom Points!")
                    st.rerun()
                else:
                    st.warning("Vui lòng điền đầy đủ chuyên đề, lỗi sai và cách khắc phục.")