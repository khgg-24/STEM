import streamlit as st


def render_community_qa():
    """Hiển thị Chợ Hỏi-Đáp Bài tập, Bảng vinh danh Học giả & Phòng học Odyssey Squads."""
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div>
                <h3 style="margin:0; color:#00F5D4;">🤝 Trụ cột 3: Cộng đồng Hỏi - Đáp Bài tập & Phòng học Odyssey Squads</h3>
                <p style="font-size:0.85rem; color:#94A3B8; margin:4px 0 0 0;">
                    Kết nối học sinh giải bài tập đa môn, tích lũy <b>Điểm Trí tuệ (Wisdom Points)</b> và duy trì kỷ luật tích cực qua <b>Tình bạn giám sát (Odyssey Squads)</b>.
                </p>
            </div>
            <span class="status-badge badge-safe">ZERO-PII PEER HUB</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c_tab1, c_tab2, c_tab3 = st.tabs([
        "💬 Chợ Hỏi - Đáp Bài tập Đa môn (Peer Q&A)",
        "🔥 Phòng học Đồng đẳng (Odyssey Squads Live)",
        "🏆 Bảng vàng Học giả & Quy đổi Điểm Trí tuệ"
    ])

    # --------------------------------------------------------------------------
    # TAB 3.1: CHỢ HỎI - ĐÁP BÀI TẬP ĐA MÔN
    # --------------------------------------------------------------------------
    with c_tab1:
        with st.expander("➕ Đăng câu hỏi bài tập mới nhờ Cộng đồng & Giáo viên hỗ trợ (Treo thưởng WP)"):
            q_subj = st.selectbox("Chọn môn học cần hỏi:", ["Toán học", "Vật lý", "Hóa học", "Sinh học", "Ngữ văn", "Lịch sử", "Địa lý", "Tiếng Anh"])
            q_grade = st.selectbox("Khối lớp:", ["Lớp 6 - 8", "Lớp 9 (Ôn thi vào 10)", "Lớp 10 - 11", "Lớp 12 (Ôn thi ĐH)"])
            q_title = st.text_input("Tiêu đề câu hỏi ngắn gọn:")
            q_body = st.text_area("Nội dung chi tiết bài tập & bước bạn đang bị vướng:")
            q_bounty = st.slider("Mức thưởng Điểm Trí tuệ (WP) cho người giải đúng:", 10, 50, 20, 5)

            if st.button("🚀 Đăng Câu hỏi lên Chợ Hỏi - Đáp"):
                if q_title.strip() and q_body.strip():
                    if st.session_state.wisdom_points >= q_bounty:
                        st.session_state.wisdom_points -= q_bounty
                        new_id = f"QA-{101 + len(st.session_state.qa_posts)}"
                        st.session_state.qa_posts.insert(0, {
                            "id": new_id,
                            "author": f"{st.session_state.student_name} ({q_grade})",
                            "subject": q_subj,
                            "grade": q_grade,
                            "title": q_title.strip(),
                            "content": q_body.strip(),
                            "bounty": q_bounty,
                            "solved": False,
                            "verified_by_teacher": False,
                            "answers": []
                        })
                        st.success(f"Đã đăng câu hỏi {new_id}! Đã trích {q_bounty} WP làm phần thưởng.")
                        st.rerun()
                    else:
                        st.error("Bạn không đủ Điểm Trí tuệ (WP). Hãy giải bài giúp bạn khác hoặc học ở Trụ cột 1 để tích điểm!")
                else:
                    st.warning("Vui lòng nhập tiêu đề và nội dung bài tập.")

        for idx, post in enumerate(st.session_state.qa_posts):
            status_cls = "badge-safe" if post["solved"] else "badge-warning"
            status_txt = "✅ ĐÃ GIẢI QUYẾT" if post["solved"] else f"⏳ ĐANG CẦN GIÚP • THƯỞNG +{post['bounty']} WP"

            st.markdown(f"""
            <div class="glass-card" style="padding:18px; border-left: 4px solid #00F5D4;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                    <span style="font-size:0.8rem; color:#00BBF9; font-weight:700;">
                        [{post['id']}] • {post['subject']} ({post['grade']}) — Đăng bởi: {post['author']}
                    </span>
                    <span class="status-badge {status_cls}">{status_txt}</span>
                </div>
                <h4 style="margin:8px 0 4px 0; color:#F8FAFC;">{post['title']}</h4>
                <p style="font-size:0.88rem; color:#CBD5E1; margin-bottom:10px;">{post['content']}</p>
            </div>
            """, unsafe_allow_html=True)

            for ans in post["answers"]:
                v_badge = " 🏅 [Đã được Giáo viên Xác thực Chuẩn]" if ans.get("is_verified") else ""
                st.markdown(f"""
                <div style="margin: -8px 0 12px 24px; padding:12px 16px; background:rgba(16,185,129,0.1); border-left:3px solid #10B981; border-radius:10px;">
                    <div style="font-size:0.78rem; color:#34D399; font-weight:700;">💡 Lời giải từ: {ans['responder']}{v_badge}</div>
                    <div style="font-size:0.86rem; color:#E2E8F0; margin-top:4px;">{ans['text']}</div>
                </div>
                """, unsafe_allow_html=True)

            with st.expander(f"✍️ Gửi lời giải hướng dẫn cho câu hỏi [{post['id']}] (Nhận +{post['bounty'] + 10} WP)"):
                ans_input = st.text_area(f"Nhập lời giải từng bước cho {post['id']}:", key=f"ans_in_{post['id']}")
                if st.button(f"Gửi Lời giải & Nhận +{post['bounty'] + 10} WP", key=f"btn_ans_{post['id']}"):
                    if ans_input.strip():
                        post["answers"].append({
                            "responder": f"{st.session_state.student_name} (Peer Tutor)",
                            "text": ans_input.strip(),
                            "upvotes": 1,
                            "is_verified": False
                        })
                        post["solved"] = True
                        reward = post["bounty"] + 10
                        st.session_state.wisdom_points += reward
                        st.success(f"🎉 Cảm ơn bạn đã hỗ trợ bạn học! Bạn được cộng +{reward} Wisdom Points!")
                        st.rerun()
                    else:
                        st.warning("Vui lòng viết lời giải chi tiết trước khi gửi.")

    # --------------------------------------------------------------------------
    # TAB 3.2: PHÒNG HỌC ĐỒNG ĐẲNG ODYSSEY SQUADS (ZERO-PII)
    # --------------------------------------------------------------------------
    with c_tab2:
        sq_col1, sq_col2 = st.columns([1.1, 1.0], gap="large")
        with sq_col1:
            st.markdown("""
            <div class="glass-card">
                <h4 style="margin:0 0 6px 0; color:#00F5D4;">🔥 Phòng Tự học Đồng đẳng: Squad #AMS-NEXUS-89</h4>
                <p style="font-size:0.83rem; color:#94A3B8; margin:0;">
                    Bảo mật Zero-PII: Không bật Camera, không thu âm. Các thành viên chỉ đồng bộ <b>Vòng sáng Trạng thái Tập trung</b> và gửi đốm lửa khích lệ.
                </p>
            </div>
            """, unsafe_allow_html=True)

            squad_members = [
                ("💎 " + st.session_state.student_name + " (Bạn)", "🟢 Đang Flow Sâu (AEI: 88.5%)", "Đang giải Toán 12 - Cực trị hàm số"),
                ("🌟 Trần Gia Bảo", "🟢 Đang Flow Sâu (AEI: 91.0%)", "Đang ôn Từ vựng Tiếng Anh SM-2"),
                ("⚡ Lê Hoàng Nam", "🟡 Đang Thảo luận Nhóm (Co-op Mode)", "Đang giải đáp câu hỏi QA-102 trên Chợ Hỏi-Đáp"),
                ("🌸 Nguyễn Phương Thảo", "🔴 Đang Nghỉ thở 4-7-8 (Cognitive Reset)", "Tạm nghỉ tái tạo năng lượng 3 phút")
            ]
            for m_name, m_state, m_task in squad_members:
                st.markdown(f"""
                <div class="glass-card" style="padding:14px 18px; margin-bottom:10px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <b style="color:#F8FAFC;">{m_name}</b>
                        <span style="font-size:0.78rem; color:#00F5D4; font-weight:700;">{m_state}</span>
                    </div>
                    <div style="font-size:0.8rem; color:#94A3B8; margin-top:4px;">📌 Mục tiêu hiện tại: {m_task}</div>
                </div>
                """, unsafe_allow_html=True)

        with sq_col2:
            st.markdown("""
            <div class="glass-card neon-card-purple">
                <h4 style="margin:0 0 8px 0; color:#C77DFF;">🛡️ Cơ chế Đồng thuận Thảo luận (Chống Phạt oan Epic Fail 2)</h4>
                <p style="font-size:0.83rem; color:#CBD5E1;">
                    Khi từ 2 thành viên trở lên bật chế độ <b>Thảo luận Bài tập Nhóm (Zalo/Discord)</b>, thuật toán tự động giảm 70% hệ số phạt rời tab ($\\lambda_1$) để bạn thoải mái trao đổi bài mà không bị trừ điểm tập trung.
                </p>
            </div>
            """, unsafe_allow_html=True)

            coop_toggle = st.toggle("🤝 Bật chế độ 'Đang thảo luận nhóm cùng Squad' (Nới lỏng cảm biến)", value=True)
            if coop_toggle:
                st.info("Đang kích hoạt Hệ số Khoan dung Đồng đẳng (γ = 0.3): Cho phép chuyển tab tra cứu tài liệu nhóm.")

            if st.button("🔥 Gửi 'Đốm lửa Khích lệ' tới toàn bộ thành viên trong Squad (+5 WP)"):
                st.session_state.wisdom_points += 5
                st.toast("🔥 Đã gửi tín hiệu khích lệ đồng đẳng tới 3 người bạn trong phòng học!")

    # --------------------------------------------------------------------------
    # TAB 3.3: BẢNG VÀNG HỌC GIẢ & CHỨNG NHẬN CỘNG ĐIỂM RÈN LUYỆN
    # --------------------------------------------------------------------------
    with c_tab3:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                <div>
                    <div class="metric-label">Tài khoản Điểm Trí tuệ Hiện tại của Bạn</div>
                    <div class="metric-value">{st.session_state.wisdom_points} WP (Wisdom Points)</div>
                </div>
                <span class="status-badge badge-safe">CẤP BẬC: PEER SCHOLAR (HỌC GIẢ ĐỒNG ĐẲNG)</span>
            </div>
            <p style="font-size:0.84rem; color:#94A3B8; margin-top:8px;">
                Điểm WP không quy đổi thành tiền mặt mà được tổng hợp gửi thẳng về <b>Teacher Dashboard</b> để Giáo viên Chủ nhiệm cộng điểm thưởng quá trình và cấp <b>Chứng nhận Cố vấn Học thuật</b> cuối học kỳ.
            </p>
        </div>
        """, unsafe_allow_html=True)

        leaderboard_df = pd.DataFrame([
            {"Hạng": "🥇 Hạng 1", "Học sinh": "Lê Hoàng Nam (12A1)", "Số bài đã giải giúp bạn": 28, "Lỗi đóng góp Bảo tàng Sai lầm": 9, "Tổng điểm WP": 640, "Danh hiệu": "Master Guide"},
            {"Hạng": "🥈 Hạng 2", "Học sinh": f"{st.session_state.student_name} (Bạn)", "Số bài đã giải giúp bạn": 14, "Lỗi đóng góp Bảo tàng Sai lầm": 5, "Tổng điểm WP": st.session_state.wisdom_points, "Danh hiệu": "Peer Scholar"},
            {"Hạng": "🥉 Hạng 3", "Học sinh": "Trần Gia Bảo (12A1)", "Số bài đã giải giúp bạn": 11, "Lỗi đóng góp Bảo tàng Sai lầm": 4, "Tổng điểm WP": 290, "Danh hiệu": "Active Helper"},
            {"Hạng": "Hạng 4", "Học sinh": "Phạm Khánh Linh (9A2)", "Số bài đã giải giúp bạn": 7, "Lỗi đóng góp Bảo tàng Sai lầm": 3, "Tổng điểm WP": 210, "Danh hiệu": "Rising Star"}
        ])
        st.dataframe(leaderboard_df, use_container_width=True, hide_index=True)