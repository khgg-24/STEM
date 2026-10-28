import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


UNIVERSITY_DATABASE = [
    {
        "school": "ĐH Bách Khoa Hà Nội (HUST)",
        "major": "Khoa học Máy tính & AI (IT1)",
        "group": "STEM - Công nghệ",
        "region": "Miền Bắc",
        "tuition_level": "Trung bình",
        "holland_vec": np.array([9.2, 9.6, 4.5, 4.0, 6.8, 7.8]),
        "vec_3d": np.array([9.4, 4.5, 7.2]),
        "cutoffs_thpt": [28.25, 28.40, 28.60],
        "cutoff_dgnl": 86.5,
        "key_subject": "Toán",
        "color": "#00F5D4"
    },
    {
        "school": "ĐH Y Hà Nội (HMU)",
        "major": "Y khoa Đa khoa",
        "group": "Y Sinh - Sức khỏe",
        "region": "Miền Bắc",
        "tuition_level": "Trung bình",
        "holland_vec": np.array([8.0, 9.5, 4.0, 8.8, 5.5, 8.2]),
        "vec_3d": np.array([8.9, 7.5, 6.8]),
        "cutoffs_thpt": [27.73, 28.15, 28.27],
        "cutoff_dgnl": 85.0,
        "key_subject": "Sinh",
        "color": "#00BBF9"
    },
    {
        "school": "ĐH Ngoại thương (FTU)",
        "major": "Kinh tế Đối ngoại & Thương mại Quốc tế",
        "group": "Kinh tế - Quản trị",
        "region": "Toàn quốc",
        "tuition_level": "Trung bình",
        "holland_vec": np.array([4.5, 7.2, 6.5, 8.0, 9.5, 8.5]),
        "vec_3d": np.array([6.5, 7.8, 9.4]),
        "cutoffs_thpt": [28.10, 28.30, 28.50],
        "cutoff_dgnl": 84.0,
        "key_subject": "Anh",
        "color": "#FEE440"
    },
    {
        "school": "ĐH Sư phạm Hà Nội (HNUE)",
        "major": "Sư phạm Toán / Ngữ văn (Miễn học phí NĐ 116)",
        "group": "Giáo dục - Sư phạm",
        "region": "Miền Bắc",
        "tuition_level": "Thấp / Miễn học phí",
        "holland_vec": np.array([5.5, 8.2, 7.5, 9.6, 7.0, 8.0]),
        "vec_3d": np.array([7.2, 9.1, 7.6]),
        "cutoffs_thpt": [26.50, 27.10, 27.40],
        "cutoff_dgnl": 78.0,
        "key_subject": "Văn",
        "color": "#34D399"
    },
    {
        "school": "ĐH Khoa học Tự nhiên - ĐHQG TP.HCM",
        "major": "Kỹ thuật Phần mềm & Khoa học Dữ liệu",
        "group": "STEM - Công nghệ",
        "region": "Miền Nam",
        "tuition_level": "Trung bình",
        "holland_vec": np.array([9.0, 9.2, 4.8, 4.5, 6.5, 7.5]),
        "vec_3d": np.array([9.0, 4.8, 7.0]),
        "cutoffs_thpt": [26.80, 27.20, 27.50],
        "cutoff_dgnl": 81.5,
        "key_subject": "Toán",
        "color": "#9B5DE5"
    },
    {
        "school": "ĐH Bách Khoa - ĐH Đà Nẵng (DUT)",
        "major": "Kỹ thuật Điều khiển & Tự động hóa",
        "group": "STEM - Công nghệ",
        "region": "Miền Trung",
        "tuition_level": "Thấp / Miễn học phí",
        "holland_vec": np.array([9.2, 8.5, 4.2, 4.5, 6.0, 7.2]),
        "vec_3d": np.array([8.8, 4.4, 6.6]),
        "cutoffs_thpt": [25.20, 25.65, 25.90],
        "cutoff_dgnl": 74.0,
        "key_subject": "Lý",
        "color": "#F15BB5"
    },
    {
        "school": "Học viện Công nghệ Bưu chính Viễn thông (PTIT)",
        "major": "Truyền thông Đa phương tiện & Thiết kế Số",
        "group": "Nghệ thuật - Truyền thông",
        "region": "Toàn quốc",
        "tuition_level": "Trung bình",
        "holland_vec": np.array([5.5, 6.5, 9.5, 8.2, 8.0, 6.2]),
        "vec_3d": np.array([6.0, 9.2, 7.2]),
        "cutoffs_thpt": [26.10, 26.40, 26.55],
        "cutoff_dgnl": 76.0,
        "key_subject": "Anh",
        "color": "#FB5607"
    }
]


HIGH_SCHOOL_GRADE10_DB = [
    {"school": "THPT Chuyên Hà Nội - Amsterdam (Hệ Chuyên)", "cutoff_3yr": [41.5, 42.0, 42.25], "scale": 50.0, "type": "THPT Chuyên"},
    {"school": "THPT Chu Văn An / THPT Kim Liên (Tốp 1 Công lập)", "cutoff_3yr": [41.75, 42.25, 42.50], "scale": 50.0, "type": "Công lập Tốp đầu"},
    {"school": "THPT Yên Hòa / THPT Phan Đình Phùng", "cutoff_3yr": [41.0, 41.5, 41.75], "scale": 50.0, "type": "Công lập Tốp đầu"},
    {"school": "THPT Công lập Khu vực Ngoại thành / Huyện", "cutoff_3yr": [32.0, 33.5, 34.0], "scale": 50.0, "type": "Công lập Địa phương"}
]


def render_career_navigator():
    """Hiển thị hệ thống Định hướng Đa chiều & Dự báo Tuyển sinh Đa phương thức (Lớp 6 - 12)."""
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div>
                <h3 style="margin:0; color:#00F5D4;">🧭 Trụ cột 2: Mô hình Định hướng Đa chiều & Dự báo Tuyển sinh Toàn quốc</h3>
                <p style="font-size:0.85rem; color:#94A3B8; margin:4px 0 0 0;">
                    Kết hợp <b>Ma trận Tương thích 4 Tầng (Fit Score)</b> và <b>Xác suất Trúng tuyển Đa phương thức (Hope Score %)</b> hỗ trợ từ THCS (Lớp 6–9 thi vào 10) đến THPT (Lớp 10–12).
                </p>
            </div>
            <span class="status-badge badge-safe">MULTI-CRITERIA ENGINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. CHỌN CẤP HỌC PHÂN LUỒNG
    pathway_mode = st.radio(
        "🎯 Chọn Cấp học & Lộ trình Định hướng:",
        [
            "🎓 Lộ trình THPT (Lớp 10, 11, 12) — Chọn Tổ hợp môn & Tuyển sinh Đại học Toàn quốc",
            "🎒 Lộ trình THCS (Lớp 6, 7, 8, 9) — Phát hiện Môn thế mạnh & Dự báo Thi vào Lớp 10 THPT"
        ],
        horizontal=True
    )

    # 2. NHẬP HỒ SƠ ĐA CHIỀU (HOLLAND + HỌC LỰC + ƯỚC MƠ + ĐIỀU KIỆN)
    in_col1, in_col2, in_col3 = st.columns([1.05, 1.05, 1.0], gap="medium")

    with in_col1:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#00F5D4;">🧬 Tầng 1: Trắc nghiệm Holland 6D</h4>
            <p style="font-size:0.78rem; color:#94A3B8; margin:0;">Mức độ yêu thích hoạt động (0 - 10):</p>
        </div>
        """, unsafe_allow_html=True)
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            R = st.slider("🛠️ R (Kỹ thuật)", 0.0, 10.0, 8.5, 0.5)
            A = st.slider("🎨 A (Sáng tạo)", 0.0, 10.0, 6.0, 0.5)
            E = st.slider("🚀 E (Quản trị)", 0.0, 10.0, 7.0, 0.5)
        with c_r2:
            I = st.slider("🔬 I (Nghiên cứu)", 0.0, 10.0, 9.0, 0.5)
            S = st.slider("🤝 S (Xã hội)", 0.0, 10.0, 6.5, 0.5)
            C = st.slider("📐 C (Quy trình)", 0.0, 10.0, 7.5, 0.5)

    with in_col2:
        st.markdown("""
        <div class="glass-card neon-card-purple">
            <h4 style="margin:0 0 6px 0; color:#C77DFF;">📚 Tầng 2: Điểm Học thuật & Tổ hợp</h4>
            <p style="font-size:0.78rem; color:#94A3B8; margin:0;">Nhập điểm trung bình các môn (Thang 10):</p>
        </div>
        """, unsafe_allow_html=True)
        s_c1, s_c2 = st.columns(2)
        with s_c1:
            s_toan = st.number_input("📐 Toán học", 0.0, 10.0, 9.2, 0.2)
            s_ly = st.number_input("⚡ Vật lý", 0.0, 10.0, 8.8, 0.2)
            s_hoa = st.number_input("🧪 Hóa học", 0.0, 10.0, 8.4, 0.2)
        with s_c2:
            s_sinh = st.number_input("🧬 Sinh học", 0.0, 10.0, 7.8, 0.2)
            s_van = st.number_input("✒️ Ngữ văn", 0.0, 10.0, 7.5, 0.2)
            s_anh = st.number_input("🌐 Tiếng Anh", 0.0, 10.0, 8.8, 0.2)

    with in_col3:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0 0 6px 0; color:#FEE440;">🌟 Tầng 3 & 4: Ước mơ & Phương thức</h4>
            <p style="font-size:0.78rem; color:#94A3B8; margin:0;">Nguyện vọng cá nhân & Điểm ĐGNL/IELTS:</p>
        </div>
        """, unsafe_allow_html=True)
        dream_group = st.selectbox(
            "Ước mơ / Lĩnh vực khao khát nhất:",
            ["STEM - Công nghệ", "Y Sinh - Sức khỏe", "Kinh tế - Quản trị", "Giáo dục - Sư phạm", "Nghệ thuật - Truyền thông"]
        )
        pref_region = st.selectbox("Khu vực ưu tiên theo học:", ["Tất cả các miền", "Miền Bắc", "Miền Trung", "Miền Nam"])
        need_low_tuition = st.checkbox("Ưu tiên trường Học phí thấp / Miễn học phí (NĐ 116)", value=False)
        dgnl_score = st.slider("Điểm Đánh giá năng lực quy đổi (Thang 100):", 40.0, 100.0, 84.0, 1.0)

    # 3. XỬ LÝ PHÂN LUỒNG THCS (LỚP 6 - 9 THI VÀO 10)
    subject_map = {"Toán": s_toan, "Lý": s_ly, "Hóa": s_hoa, "Sinh": s_sinh, "Văn": s_van, "Anh": s_anh}
    all_scores = np.array(list(subject_map.values()))
    mean_score = float(np.mean(all_scores))
    std_score = float(np.std(all_scores)) + 0.25

    if "THCS" in pathway_mode:
        st.markdown("### 🎒 Kết quả Chẩn đoán Năng lực THCS & Dự báo Kỳ thi vào Lớp 10 THPT")
        # Tính điểm xét tuyển vào 10: (Toán + Văn)*2 + Anh (Thang 50)
        score_into_10 = (s_toan + s_van) * 2.0 + s_anh
        best_subj = max(subject_map, key=subject_map.get)

        thcs_c1, thcs_c2 = st.columns(2, gap="large")
        with thcs_c1:
            st.markdown(f"""
            <div class="glass-card">
                <div class="metric-label">Tổng điểm Dự kiến Thi vào Lớp 10 ((Toán+Văn)×2 + Anh)</div>
                <div class="metric-value">{score_into_10:.2f} / 50.0 điểm</div>
                <p style="font-size:0.86rem; color:#CBD5E1; margin-top:8px;">
                    🌟 <b>Môn học Thế mạnh Vượt trội (Z-Score cao nhất):</b> Môn <b>{best_subj}</b> ({subject_map[best_subj]:.1f} điểm).<br>
                    💡 <b>Định hướng Lớp Chuyên đề xuất:</b> Khuyến nghị bồi dưỡng thi vào <b>Lớp 10 Chuyên {best_subj}</b> hoặc Tổ hợp KHTN chất lượng cao.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with thcs_c2:
            rows_10 = []
            for hs in HIGH_SCHOOL_GRADE10_DB:
                c_mean = float(np.mean(hs["cutoff_3yr"]))
                c_std = float(np.std(hs["cutoff_3yr"])) + 0.35
                prob_10 = 100.0 / (1.0 + np.exp(-1.1 * (score_into_10 - c_mean) / c_std))
                rows_10.append({
                    "Trường THPT Mục tiêu": hs["school"],
                    "Loại hình": hs["type"],
                    "Điểm chuẩn TB 3 năm": round(c_mean, 2),
                    "Xác suất Đỗ (Hope Score %)": round(prob_10, 1)
                })
            st.dataframe(pd.DataFrame(rows_10), use_container_width=True, hide_index=True)

    # 4. TÍNH TOÁN MA TRẬN ĐA BIẾN (HOLISTIC FIT SCORE) & HOPE SCORE ĐA PHƯƠNG THỨC
    student_holland = np.array([R, I, A, S, E, C])
    X_stu = (R + I + np.mean([s_toan, s_ly, s_hoa, s_sinh])) / 3.0
    Y_stu = (A + S + s_van) / 3.0
    Z_stu = (E + C + s_anh) / 3.0
    V_stu_3d = np.array([X_stu, Y_stu, Z_stu])

    evaluated_majors = []
    for uni in UNIVERSITY_DATABASE:
        # 1. Sim_Holland (6 chiều chuẩn hóa)
        h_vec = uni["holland_vec"]
        sim_holland = 100.0 * float(np.dot(student_holland, h_vec) / (np.linalg.norm(student_holland) * np.linalg.norm(h_vec) + 1e-6))

        # 2. Score_Academic (Điểm tổ hợp 3 môn chủ lực quy về thang 100)
        top3_scores = sorted(all_scores, reverse=True)[:3]
        sum_3_subjects = float(np.sum(top3_scores))
        score_academic = (sum_3_subjects / 30.0) * 100.0

        # 3. Subject_Strengths (Z-score môn chủ lực của ngành)
        key_s = subject_map.get(uni["key_subject"], mean_score)
        z_val = (key_s - mean_score) / std_score
        subj_strength = 100.0 / (1.0 + np.exp(-1.5 * z_val))

        # 4. User_Aspiration (Khớp ước mơ + học phí + vùng miền)
        asp_base = 100.0 if uni["group"] == dream_group else 68.0
        tuition_factor = 1.0 if (not need_low_tuition or "Thấp" in uni["tuition_level"]) else 0.72
        region_factor = 1.0 if (pref_region == "Tất cả các miền" or uni["region"] in [pref_region, "Toàn quốc"]) else 0.75
        user_aspiration = asp_base * (0.6 * tuition_factor + 0.4 * region_factor)

        # Tổng hợp Fit Score Đa biến
        fit_score = 0.35 * sim_holland + 0.25 * score_academic + 0.20 * subj_strength + 0.20 * user_aspiration

        # Tính Hope Score Đa phương thức (THPT + ĐGNL có tính độ lệch chuẩn sigma 3 năm)
        c_list = uni["cutoffs_thpt"]
        c_hat = 0.5 * c_list[2] + 0.3 * c_list[1] + 0.2 * c_list[0]
        sigma_c = float(np.sqrt(np.mean([(c - np.mean(c_list))**2 for c in c_list]) + 0.35**2))
        trend_delta = 0.35 * (c_list[2] - c_list[1])

        p_thpt = 1.0 / (1.0 + np.exp(-1.25 * (sum_3_subjects - (c_hat + trend_delta)) / sigma_c))
        p_dgnl = 1.0 / (1.0 + np.exp(-0.22 * (dgnl_score - uni["cutoff_dgnl"])))

        # Hợp nhất xác suất 2 phương thức
        hope_multi = 100.0 * (1.0 - (1.0 - 0.85 * p_thpt) * (1.0 - 0.70 * p_dgnl))
        hope_multi = float(np.clip(hope_multi, 1.0, 99.5))

        # Phân loại 4 Ô Chiến lược
        if fit_score >= 78.0 and hope_multi >= 60.0:
            quadrant = "🟢 Gold Match (Tối ưu)"
        elif fit_score >= 78.0 and hope_multi < 60.0:
            quadrant = "🟣 Dream Target (Thử thách)"
        elif fit_score < 78.0 and hope_multi >= 60.0:
            quadrant = "🔵 Safety Net (An toàn)"
        else:
            quadrant = "🔴 Risk Zone (Mạo hiểm)"

        evaluated_majors.append({
            "school": uni["school"],
            "major": uni["major"],
            "group": uni["group"],
            "region": uni["region"],
            "fit_score": round(fit_score, 2),
            "hope_score": round(hope_multi, 2),
            "cutoff_hat": round(c_hat, 2),
            "sigma": round(sigma_c, 2),
            "quadrant": quadrant,
            "vec_3d": uni["vec_3d"],
            "color": uni["color"]
        })

    evaluated_majors = sorted(evaluated_majors, key=lambda x: (x["fit_score"] * 0.55 + x["hope_score"] * 0.45), reverse=True)

    # 5. TRỰC QUAN HÓA: MA TRẬN NGUYỆN VỌNG 2D & KHÔNG GIAN VECTOR 3D
    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
    vis_col1, vis_col2 = st.columns(2, gap="large")

    with vis_col1:
        st.markdown("""
        <div class="glass-card" style="margin-bottom:10px;">
            <h4 style="margin:0; color:#00F5D4;">🎯 Ma trận Quyết định Nguyện vọng 2D (Fit Score vs Hope Score)</h4>
            <p style="font-size:0.8rem; color:#94A3B8; margin:4px 0 0 0;">
                Trục X: Xác suất đỗ Đa phương thức (%) | Trục Y: Độ tương thích Đa biến (%).
            </p>
        </div>
        """, unsafe_allow_html=True)

        fig_2d = go.Figure()
        for m in evaluated_majors:
            fig_2d.add_trace(go.Scatter(
                x=[m["hope_score"]],
                y=[m["fit_score"]],
                mode="markers+text",
                marker=dict(size=16, color=m["color"], line=dict(width=2, color="#FFFFFF")),
                text=[m["school"].split("(")[0].strip()],
                textposition="top center",
                name=f"{m['school']} ({m['quadrant']})",
                hovertemplate=(
                    f"<b>{m['school']}</b><br>Ngành: {m['major']}<br>"
                    f"Fit Score: <b>{m['fit_score']}%</b> | Hope Score: <b>{m['hope_score']}%</b><br>"
                    f"Phân vùng: {m['quadrant']}<extra></extra>"
                )
            ))

        fig_2d.add_vline(x=60, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        fig_2d.add_hline(y=78, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        fig_2d.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(17, 25, 40, 0.65)",
            height=430,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(title="Xác suất Trúng tuyển Đa phương thức - Hope Score (%)", range=[0, 105]),
            yaxis=dict(title="Độ tương thích Đa biến - Holistic Fit Score (%)", range=[45, 102]),
            showlegend=False
        )
        st.plotly_chart(fig_2d, use_container_width=True)

    with vis_col2:
        st.markdown("""
        <div class="glass-card" style="margin-bottom:10px;">
            <h4 style="margin:0; color:#00BBF9;">🌌 Không gian Vector Định hướng 3D (Xoay 360°)</h4>
            <p style="font-size:0.8rem; color:#94A3B8; margin:4px 0 0 0;">
                💎 <b>Kim Cương Đỏ:</b> Tọa độ Học sinh | ★ <b>Điểm Đa Sắc:</b> Các Trường Đại học mục tiêu.
            </p>
        </div>
        """, unsafe_allow_html=True)

        fig_3d = go.Figure()
        fig_3d.add_trace(go.Scatter3d(
            x=[0, X_stu], y=[0, Y_stu], z=[0, Z_stu],
            mode="lines", line=dict(color="#FF0055", width=6), showlegend=False
        ))
        fig_3d.add_trace(go.Scatter3d(
            x=[X_stu], y=[Y_stu], z=[Z_stu],
            mode="markers+text",
            marker=dict(size=14, color="#FF0055", symbol="diamond", line=dict(color="#FFFFFF", width=2)),
            text=[f"💎 {st.session_state.student_name}"],
            textposition="top center",
            name="Học sinh"
        ))

        for m in evaluated_majors:
            vx, vy, vz = m["vec_3d"]
            fig_3d.add_trace(go.Scatter3d(
                x=[vx], y=[vy], z=[vz],
                mode="markers+text",
                marker=dict(size=9, color=m["color"], symbol="cross"),
                text=[m["school"].split("(")[0].strip()],
                name=m["school"]
            ))

        fig_3d.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(17, 25, 40, 0.65)",
            height=430,
            margin=dict(l=0, r=0, b=0, t=10),
            showlegend=False,
            scene=dict(
                xaxis_title="X: STEM",
                yaxis_title="Y: Xã hội & Sáng tạo",
                zaxis_title="Z: Quản trị & Ngoại ngữ"
            )
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    # 6. BẢNG XẾP HẠNG CHI TIẾT CÁC TRƯỜNG ĐẠI HỌC TOÀN QUỐC
    st.markdown("#### 📋 Bảng Phân tích Chi tiết Nguyện vọng Đại học Toàn quốc")
    df_uni = pd.DataFrame([
        {
            "Trường Đại học": m["school"],
            "Ngành đào tạo": m["major"],
            "Miền": m["region"],
            "Điểm chuẩn kỳ vọng (μ̂ ± σ)": f"{m['cutoff_hat']} ± {m['sigma']}",
            "Holistic Fit (%)": m["fit_score"],
            "Hope Score Đa phương thức (%)": m["hope_score"],
            "Chiến lược Nguyện vọng": m["quadrant"]
        }
        for m in evaluated_majors
    ])
    st.dataframe(df_uni, use_container_width=True, hide_index=True)