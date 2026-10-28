import streamlit as st
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components
from datetime import datetime


def render_telemetry_and_triage():
    """Hiển thị Cảm biến Telemetry FSI/AEI chống treo máy, Adaptive Nudge 3 cấp & Chatbot Sơ cứu Tâm lý."""
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div>
                <h3 style="margin:0; color:#00F5D4;">⏱️ Trụ cột 5: Cảm biến Nhận thức Chủ động (FSI/AEI) & Sơ cứu Tâm lý Học đường</h3>
                <p style="font-size:0.85rem; color:#94A3B8; margin:4px 0 0 0;">
                    Kết hợp cảm biến rời tab <code>visibilitychange</code> với <b>Bộ phát hiện treo máy (Heartbeat Idle Detector)</b>, <b>Adaptive Nudge 3 cấp</b> và Chatbot phân luồng căng thẳng (PSS-10 / DASS-21).
                </p>
            </div>
            <span class="status-badge badge-safe">ACTIVE TELEMETRY + TRIAGE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    t_tabs = st.tabs([
        "📡 Buồng lái Pomodoro & Cảm biến Chống Treo máy (FSI & AEI)",
        "🩺 Chatbot Sơ cứu & Phân luồng Tâm lý Học đường (Mental Health Triage)"
    ])

    # --------------------------------------------------------------------------
    # TAB 5.1: CẢM BIẾN TELEMETRY FSI / AEI CHỐNG TREO MÁY & ADAPTIVE NUDGE
    # --------------------------------------------------------------------------
    with t_tabs[0]:
        telemetry_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
            <style>
                * { box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }
                body { margin: 0; padding: 0; background: transparent; color: #F8FAFC; }
                .hud-wrapper {
                    display: grid; grid-template-columns: 1fr 1.45fr; gap: 18px;
                    background: rgba(17, 25, 40, 0.82); border: 1px solid rgba(0, 245, 212, 0.3);
                    border-radius: 16px; padding: 18px;
                }
                .pomo-box {
                    display: flex; flex-direction: column; align-items: center; justify-content: center;
                    border-right: 1px solid rgba(255, 255, 255, 0.08); padding-right: 12px;
                }
                .time-display { font-size: 2.0rem; font-weight: 800; color: #00F5D4; }
                .btn-group { display: flex; gap: 8px; margin-top: 10px; }
                .hud-btn {
                    padding: 7px 14px; border-radius: 10px; border: 1px solid rgba(0, 245, 212, 0.4);
                    background: rgba(0, 245, 212, 0.15); color: #00F5D4; font-weight: 700; cursor: pointer;
                }
                .stat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 10px 0; }
                .stat-card {
                    background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08);
                    border-radius: 10px; padding: 10px;
                }
                .stat-title { font-size: 0.68rem; color: #94A3B8; text-transform: uppercase; font-weight: 600; }
                .stat-num { font-size: 1.15rem; font-weight: 800; margin-top: 4px; color: #00F5D4; }
                .nudge-bar {
                    border-radius: 10px; padding: 10px 14px; font-size: 0.82rem; font-weight: 600;
                    background: rgba(16, 185, 129, 0.14); border: 1px solid rgba(52, 211, 153, 0.4); color: #34D399;
                }
            </style>
        </head>
        <body>
            <div class="hud-wrapper">
                <div class="pomo-box">
                    <div style="font-size:0.75rem; color:#94A3B8; font-weight:700;">CHU KỲ POMODORO</div>
                    <div id="pomoTime" class="time-display">25:00</div>
                    <div id="pomoStatus" style="font-size:0.72rem; color:#34D399;">SẴN SÀNG TẬP TRUNG</div>
                    <div class="btn-group">
                        <button class="hud-btn" onclick="togglePomo()" id="startBtn">▶ Bắt đầu</button>
                        <button class="hud-btn" onclick="resetPomo()">↺ Đặt lại</button>
                    </div>
                </div>
                <div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <b style="font-size:0.84rem;">📡 Cảm biến Rời Tab & Phát hiện Treo máy (Active Heartbeat)</b>
                        <span id="stateBadge" style="font-size:0.72rem; padding:3px 10px; border-radius:99px; background:rgba(16,185,129,0.2); color:#34D399; font-weight:700;">
                            ● TƯƠNG TÁC CHỦ ĐỘNG
                        </span>
                    </div>
                    <div class="stat-grid">
                        <div class="stat-card">
                            <div class="stat-title">TG Rời Tab</div>
                            <div id="offSec" class="stat-num">0.0 s</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-title">Số lần Chuyển Tab</div>
                            <div id="swCount" class="stat-num">0 lần</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-title">TG Nhàn rỗi (Idle)</div>
                            <div id="idleSec" class="stat-num">0 s</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-title">Chỉ số AEI Thực</div>
                            <div id="liveAei" class="stat-num">100.0%</div>
                        </div>
                    </div>
                    <div id="nudgeBox" class="nudge-bar">
                        ✅ Cảm biến đang ghi nhận thao tác chuột/bàn phím và trạng thái tab theo từng mili-giây.
                    </div>
                </div>
            </div>
            <script>
                let rem = 1500, timer = null, running = false;
                let hiddenStart = null, totalOffMs = 0, switches = 0, idleSeconds = 0;

                function togglePomo() {
                    const btn = document.getElementById('startBtn');
                    if (!running) {
                        running = true; btn.innerText = "⏸ Tạm dừng";
                        document.getElementById('pomoStatus').innerText = "ĐANG HỌC SÂU (DEEP WORK)";
                        timer = setInterval(() => {
                            if (rem > 0) {
                                rem--;
                                const m = Math.floor(rem / 60).toString().padStart(2, '0');
                                const s = (rem % 60).toString().padStart(2, '0');
                                document.getElementById('pomoTime').innerText = m + ":" + s;
                            }
                        }, 1000);
                    } else {
                        running = false; btn.innerText = "▶ Tiếp tục";
                        clearInterval(timer);
                    }
                }
                function resetPomo() {
                    clearInterval(timer); running = false; rem = 1500;
                    document.getElementById('pomoTime').innerText = "25:00";
                    document.getElementById('startBtn').innerText = "▶ Bắt đầu";
                }

                // Reset bộ đếm treo máy khi học sinh di chuột hoặc gõ phím
                ['mousemove', 'keydown', 'click', 'scroll'].forEach(evt => {
                    window.addEventListener(evt, () => { idleSeconds = 0; });
                });

                setInterval(() => {
                    if (!document.hidden) { idleSeconds++; }
                    recalcMetrics();
                }, 1000);

                document.addEventListener('visibilitychange', () => {
                    const badge = document.getElementById('stateBadge');
                    if (document.hidden) {
                        hiddenStart = performance.now();
                        switches++;
                        document.getElementById('swCount').innerText = switches + " lần";
                        badge.innerText = "⚠️ ĐÃ RỜI TAB HỌC";
                        badge.style.color = "#F87171";
                    } else {
                        if (hiddenStart !== null) {
                            totalOffMs += (performance.now() - hiddenStart);
                            hiddenStart = null;
                        }
                        badge.innerText = "● TƯƠNG TÁC CHỦ ĐỘNG";
                        badge.style.color = "#34D399";
                        recalcMetrics();
                    }
                });

                function recalcMetrics() {
                    const offS = totalOffMs / 1000.0;
                    const fPresence = Math.exp(-0.04 * offS - 0.03 * switches);
                    const fActive = Math.max(0.0, 1.0 - Math.max(0, idleSeconds - 15) / 120.0);
                    const aei = 100.0 * fPresence * fActive;

                    document.getElementById('offSec').innerText = offS.toFixed(1) + " s";
                    document.getElementById('idleSec').innerText = idleSeconds + " s";
                    document.getElementById('liveAei').innerText = aei.toFixed(1) + "%";
                }
            </script>
        </body>
        </html>
        """
        components.html(telemetry_html, height=205)

        # BẢNG GIẢ LẬP KIỂM CHỨNG CÔNG THỨC TOÁN HỌC AEI DÀNH CHO GIÁM KHẢO
        st.markdown("#### 🎛️ Bảng Kiểm chứng Toán học Chỉ số Tập trung Chủ động (AEI) & Adaptive Nudge")
        sim_c1, sim_c2 = st.columns([1.2, 1.0], gap="large")

        with sim_c1:
            t_off = st.slider("1. Thời gian rời tab học tập t_off (giây):", 0.0, 60.0, float(st.session_state.offscreen_sec), 1.0)
            n_sw = st.slider("2. Số lần chuyển tab liên tục N_switch (lần):", 0, 15, 1, 1)
            t_idle = st.slider("3. Thời gian treo máy không thao tác t_idle (giây):", 0.0, 300.0, float(st.session_state.idle_sec), 10.0)
            deep_solving_mode = st.checkbox("📝 Đang bật chế độ 'Giải toán nháp trên giấy (Deep Solving)' — Nới ngưỡng Idle lên 420s", value=False)

            max_idle_allowed = 420.0 if deep_solving_mode else 180.0
            f_presence = float(np.exp(-0.04 * t_off - 0.025 * n_sw))
            f_active = float(np.clip((max_idle_allowed - min(t_idle, max_idle_allowed)) / max_idle_allowed, 0.0, 1.0) ** 0.6)
            check_ratio = st.session_state.checkin_passed / max(1, st.session_state.checkin_total)
            f_verify = 0.6 + 0.4 * check_ratio

            fsi_pure = 100.0 * float(np.exp(-0.04 * t_off))
            aei_val = float(np.clip(100.0 * f_presence * f_active * f_verify, 0.0, 100.0))

            st.session_state.offscreen_sec = t_off
            st.session_state.idle_sec = t_idle
            st.session_state.fsi_score = fsi_pure
            st.session_state.aei_score = aei_val

            st.markdown(f"""
            <div class="glass-card" style="padding:16px;">
                <div style="display:flex; justify-content:space-between;">
                    <span>Chỉ số FSI Thụ động cũ: <b>{fsi_pure:.1f}%</b></span>
                    <span style="color:#00F5D4;">Chỉ số AEI Chống treo máy mới: <b>{aei_val:.1f}%</b></span>
                </div>
                <div class="progress-track" style="height:12px; margin-top:10px;">
                    <div class="progress-fill" style="width:{aei_val:.1f}%; background:linear-gradient(90deg, #00F5D4, #00BBF9);"></div>
                </div>
                <div style="font-size:0.78rem; color:#94A3B8; margin-top:6px;">
                    Thành phần: Hiện diện = <code>{f_presence:.2f}</code> × Chống treo máy = <code>{f_active:.2f}</code> × Xác thực hiểu bài = <code>{f_verify:.2f}</code>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with sim_c2:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=aei_val,
                number={"suffix": "%", "font": {"size": 36, "color": "#00F5D4"}},
                title={"text": "<b>ACTIVE ENGAGEMENT INDEX (AEI)</b>", "font": {"size": 13, "color": "#CBD5E1"}},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#00F5D4"},
                    "steps": [
                        {"range": [0, 30], "color": "rgba(239, 68, 68, 0.28)"},
                        {"range": [30, 60], "color": "rgba(245, 158, 11, 0.25)"},
                        {"range": [60, 100], "color": "rgba(16, 185, 129, 0.22)"}
                    ]
                }
            ))
            fig_gauge.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(17, 25, 40, 0.65)",
                height=260,
                margin=dict(l=20, r=20, t=40, b=15)
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        # HIỂN THỊ 3 CẤP ĐỘ ADAPTIVE NUDGE
        if aei_val >= 60.0 and t_off <= 10.0:
            st.success("✨ CẤP 0 (FLOW STATE): Sự tập trung chủ động đạt mức tối ưu. Hệ thống giữ im lặng bảo vệ mạch tư duy.")
        elif aei_val >= 60.0 and t_off > 10.0:
            st.info("🔔 CẤP 1 (MICRO-NUDGE): Bạn vừa rời màn hình hơn 10 giây. Hãy quay lại hoàn thành nốt mục tiêu đang dang dở nhé!")
        elif 30.0 <= aei_val < 60.0:
            st.warning("🤝 CẤP 2 (ODYSSEY SQUADS NUDGE): Nhịp độ tương tác giảm xuống dưới 60%. Nhóm bạn học trong Squad đang gửi tín hiệu khích lệ bạn!")
        else:
            st.markdown(f"""
            <div class="cognitive-modal">
                <h4 style="margin:0; color:#FFFFFF;">🧘‍♂️ CẤP 3 — COGNITIVE RESET (AEI = {aei_val:.1f}% < 30%): Gợi ý Bài tập Thở 4-7-8 Xả cơ 3 Phút</h4>
                <p style="font-size:0.88rem; color:#FECACA; margin:8px 0;">
                    Hệ thống phát hiện dấu hiệu quá tải nhận thức hoặc treo máy kéo dài. Đừng ép bản thân học tiếp ngay lúc này — hãy thực hiện 3 nhịp thở:
                    <b>Hít vào 4 giây ➔ Giữ hơi 7 giây ➔ Thở ra chậm 8 giây</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 5.2: CHATBOT SƠ CỨU & PHÂN LUỒNG TÂM LÝ HỌC ĐƯỜNG (MENTAL HEALTH TRIAGE)
    # --------------------------------------------------------------------------
    with t_tabs[1]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#00F5D4;">🩺 Sàng lọc Nhanh & Sơ cứu Tâm lý Học đường (Rule-Based Non-Clinical Triage)</h4>
            <p style="font-size:0.83rem; color:#94A3B8; margin:0;">
                <b>Nguyên tắc Đạo đức Nghiên cứu (Phụ lục 5):</b> Hệ thống tuyệt đối <u>không tự chẩn đoán bệnh lý tâm thần</u> và không dùng AI sinh văn bản tự do. Sàng lọc dựa trên 4 chỉ báo chuẩn hóa từ thang đo <b>PSS-10 / DASS-21</b> để điều hướng nghỉ ngơi hoặc kết nối Cố vấn Tâm lý.
            </p>
        </div>
        """, unsafe_allow_html=True)

        q1 = st.slider("1. Trong 7 ngày qua, bạn có cảm thấy quá tải vì khối lượng bài vở và áp lực điểm số không? (0: Không bao giờ - 3: Hầu như mọi lúc)", 0, 3, 1)
        q2 = st.slider("2. Bạn có gặp tình trạng khó ngủ, trằn trọc hoặc mệt mỏi rã rời ngay cả khi mới thức dậy? (0 - 3)", 0, 3, 1)
        q3 = st.slider("3. Bạn có cảm thấy hoang mang, cô đơn hoặc sợ làm gia đình thất vọng về kỳ thi sắp tới? (0 - 3)", 0, 3, 1)
        q4 = st.slider("4. Bạn có cảm thấy khó lấy lại bình tĩnh khi nghĩ đến kết quả học tập hiện tại? (0 - 3)", 0, 3, 0)

        triage_total = q1 + q2 + q3 + q4

        if st.button("🔍 Phân tích Mức độ Căng thẳng & Nhận Hướng dẫn Sơ cứu Tâm lý"):
            if triage_total <= 4:
                st.success(f"🟢 MỨC XANH (Điểm sàng lọc: {triage_total}/12 — Căng thẳng Học tập Bình thường): Tâm lý của bạn đang ở ngưỡng cân bằng. Hãy duy trì chu kỳ học Pomodoro 25 phút nghỉ 5 phút nhé!")
            elif triage_total <= 8:
                st.warning(f"🟡 MỨC VÀNG (Điểm sàng lọc: {triage_total}/12 — Quá tải Nhận thức Trung bình): Bạn đang có dấu hiệu mệt mỏi tinh thần. Hệ thống khuyến nghị bạn tạm dừng làm đề khó tối nay, thực hiện bài tập thở 4-7-8 và trò chuyện cùng bạn bè trong Odyssey Squads.")
            else:
                alert_msg = f"[{datetime.now().strftime('%H:%M - %d/%m/%Y')}] Cảnh báo Bảo mật Mức Đỏ: Học sinh mã ẩn danh HS-12A1-8F92 có điểm sàng lọc căng thẳng {triage_total}/12. Đề nghị Chuyên viên Tư vấn Tâm lý Học đường hỗ trợ riêng tư."
                st.session_state.triage_alerts.append(alert_msg)
                st.markdown(f"""
                <div class="cognitive-modal">
                    <h4 style="margin:0; color:#FFFFFF;">🚨 MỨC ĐỎ (Điểm sàng lọc: {triage_total}/12 — Nguy cơ Căng thẳng Cao cần Hỗ trợ)</h4>
                    <p style="font-size:0.9rem; color:#FECACA; margin:8px 0;">
                        Bạn không hề đơn độc! Điểm số không bao giờ quan trọng bằng sức khỏe và sự bình an của bạn.
                        Hệ thống đã gửi một <b>Tín hiệu Hỗ trợ Bảo mật</b> tới Chuyên viên Tâm lý Học đường của trường.
                    </p>
                    <div style="background:rgba(0,0,0,0.4); padding:12px; border-radius:10px; font-size:0.88rem; color:#00F5D4;">
                        📞 <b>Đường dây nóng Hỗ trợ Tâm lý Học đường & Bảo vệ Trẻ em Quốc gia (Miễn phí 24/7):</b> <b>111</b>
                    </div>
                </div>
                """, unsafe_allow_html=True)