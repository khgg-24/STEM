import streamlit as st


def inject_custom_css():
    """Tiêm hệ thống CSS Glassmorphism & Modern Dark Mode vào ứng dụng."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #070B19;
            color: #E2E8F0;
        }

        .stApp {
            background: radial-gradient(circle at 12% 18%, rgba(0, 245, 212, 0.08) 0%, transparent 35%),
                        radial-gradient(circle at 88% 82%, rgba(155, 93, 229, 0.12) 0%, transparent 40%),
                        #070B19;
        }

        [data-testid="stSidebar"] {
            background: rgba(13, 19, 38, 0.85) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(0, 245, 212, 0.2);
        }

        .glass-card {
            background: rgba(17, 25, 40, 0.68);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.09);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            padding: 20px;
            margin-bottom: 16px;
            transition: all 0.28s cubic-bezier(0.25, 0.8, 0.25, 1);
        }

        .glass-card:hover {
            border: 1px solid rgba(0, 245, 212, 0.42);
            box-shadow: 0 10px 30px -5px rgba(0, 245, 212, 0.14);
            transform: translateY(-2px);
        }

        .neon-card-purple {
            border: 1px solid rgba(155, 93, 229, 0.38);
        }

        .neon-card-purple:hover {
            border: 1px solid rgba(155, 93, 229, 0.78);
            box-shadow: 0 10px 30px -5px rgba(155, 93, 229, 0.22);
        }

        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stTextArea > div > div > textarea,
        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
            background-color: rgba(15, 23, 42, 0.85) !important;
            border: 1px solid rgba(0, 245, 212, 0.25) !important;
            color: #F8FAFC !important;
        }

        .stButton > button {
            border-radius: 12px !important;
            background: linear-gradient(135deg, #00F5D4 0%, #00BBF9 100%) !important;
            color: #060B19 !important;
            font-weight: 700 !important;
            border: none !important;
            padding: 0.55rem 1.2rem !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 4px 14px rgba(0, 245, 212, 0.25) !important;
            width: 100%;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 22px rgba(0, 245, 212, 0.45) !important;
        }

        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }

        .badge-safe {
            background: rgba(16, 185, 129, 0.16);
            color: #34D399;
            border: 1px solid rgba(52, 211, 153, 0.45);
        }

        .badge-warning {
            background: rgba(245, 158, 11, 0.16);
            color: #FBBF24;
            border: 1px solid rgba(251, 191, 36, 0.45);
        }

        .badge-danger {
            background: rgba(239, 68, 68, 0.18);
            color: #F87171;
            border: 1px solid rgba(248, 113, 113, 0.5);
        }

        .metric-label {
            font-size: 0.78rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
            margin-bottom: 4px;
        }

        .metric-value {
            font-size: 1.95rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00F5D4, #00BBF9, #9B5DE5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.2;
        }

        .progress-track {
            width: 100%;
            height: 10px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 999px;
            overflow: hidden;
            margin: 8px 0 4px 0;
        }

        .progress-fill {
            height: 100%;
            border-radius: 999px;
            transition: width 0.5s ease;
        }

        .github-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            padding: 10px 14px;
            border-radius: 12px;
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(0, 245, 212, 0.35);
            color: #F8FAFC !important;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 0.85rem;
            transition: all 0.25s ease;
        }

        .github-btn:hover {
            background: rgba(0, 245, 212, 0.14);
            border-color: #00F5D4;
        }

        .cognitive-modal {
            background: linear-gradient(135deg, rgba(127, 29, 29, 0.45) 0%, rgba(17, 24, 39, 0.92) 100%);
            border: 2px solid #EF4444;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 0 32px rgba(239, 68, 68, 0.3);
            margin-top: 14px;
        }
    </style>
    """, unsafe_allow_html=True)


def init_session_state():
    """Khởi tạo đầy đủ biến trạng thái st.session_state chống lỗi Runtime."""
    defaults = {
        "student_name": "Nguyễn Minh Anh",
        "school_name": "THPT Chuyên Hà Nội - Amsterdam",
        "grade_level": "Lớp 12 (Tuyển sinh Đại học Toàn quốc)",
        "project_code": "KHKT-HN-2026-PM21",
        "wisdom_points": 320,
        "aei_score": 88.5,
        "fsi_score": 92.0,
        "offscreen_sec": 3.0,
        "idle_sec": 12.0,
        "checkin_passed": 4,
        "checkin_total": 4,
        "step_math_unlocked": 1,
        "flashcard_idx": 0,
        "flashcard_flipped": False,
        "qa_posts": [
            {
                "id": "QA-101",
                "author": "Trần Gia Bảo (Lớp 12A1)",
                "subject": "Toán học",
                "grade": "Lớp 12",
                "title": "Làm sao tìm nhanh khoảng cách giữa 2 đường thẳng chéo nhau bằng Oxyz?",
                "content": "Mình hay bị nhầm dấu khi dựng mặt phẳng song song chứa đường thẳng. Có cách nào gắn hệ trục tọa độ nhanh không?",
                "bounty": 30,
                "solved": True,
                "verified_by_teacher": True,
                "answers": [
                    {
                        "responder": "Lê Hoàng Nam (Master Guide)",
                        "text": "Bước 1: Chọn gốc tọa độ tại chân đường vuông góc chung hoặc giao điểm mặt đáy. Bước 2: Dùng tích có hướng [u1, u2] làm vector pháp tuyến, áp dụng công thức d = |[u1, u2].M1M2| / |[u1, u2]| để tránh vẽ thêm hình phụ!",
                        "upvotes": 14,
                        "is_verified": True
                    }
                ]
            },
            {
                "id": "QA-102",
                "author": "Phạm Khánh Linh (Lớp 9A2)",
                "subject": "Hoá học",
                "grade": "Lớp 9 (Ôn thi vào 10)",
                "title": "Bẫy hiệu suất phản ứng este hóa khi đề cho số mol rượu và axit không bằng nhau?",
                "content": "Khi tính hiệu suất H%, mình nên tính theo chất có số mol nhỏ hơn hay tính theo hệ số cân bằng?",
                "bounty": 25,
                "solved": False,
                "verified_by_teacher": False,
                "answers": []
            }
        ],
        "mistake_museum": [
            {
                "subject": "Toán học",
                "topic": "Hàm số & Cực trị",
                "trap": "Đếm nghiệm bội chẵn của f'(x) = 0 thành điểm cực trị.",
                "fix": "Chỉ những nghiệm đơn hoặc nghiệm bội lẻ làm f'(x) đổi dấu mới là điểm cực trị.",
                "contributor": "Nguyễn Minh Anh"
            },
            {
                "subject": "Vật lý",
                "topic": "Dao động cơ học",
                "trap": "Quên đổi đơn vị độ cứng k về N/m và biên độ A về mét khi tính cơ năng W = 0.5*k*A^2.",
                "fix": "Luôn đổi cm -> m (chia 100) trước khi bình phương biên độ A.",
                "contributor": "Vũ Đức Duy"
            },
            {
                "subject": "Tiếng Anh",
                "topic": "Mệnh đề quan hệ rút gọn",
                "trap": "Dùng V-ing thay vì V-ed/P2 khi danh từ phía trước mang nghĩa bị động.",
                "fix": "Kiểm tra chủ thể thực hiện hành động: Chủ động -> V-ing; Bị động -> P2.",
                "contributor": "Đỗ Thảo Nguyên"
            }
        ],
        "custom_exams": [
            {
                "exam_id": "MOET-2026-TOAN12-01",
                "title": "Đề Kiểm tra Định kỳ Chuẩn Cấu trúc GDPT 2018 - Toán 12",
                "subject": "Toán học",
                "grade": "Lớp 12",
                "duration": 45,
                "p1_stem": "Cho hàm số y = f(x) có đạo hàm f'(x) = x(x - 2)^2 với mọi x thuộc R. Số điểm cực trị của hàm số là:",
                "p1_options": {"A": "0", "B": "1", "C": "2", "D": "3"},
                "p1_ans": "B",
                "p1_explain": "Vì f'(x) chỉ đổi dấu khi đi qua nghiệm đơn x = 0 và không đổi dấu qua nghiệm kép x = 2 nên hàm số có đúng 1 cực trị.",
                "p2_stem": "Một vật chuyển động thẳng với vận tốc v(t) = 3t^2 - 6t + 9 (m/s), với t >= 0 (giây).",
                "p2_statements": {
                    "a": {"text": "Vận tốc ban đầu tại t = 0 là 9 m/s.", "truth": True},
                    "b": {"text": "Gia tốc của vật tại t = 2s là 6 m/s^2.", "truth": True},
                    "c": {"text": "Vật đạt vận tốc nhỏ nhất tại thời điểm t = 2s.", "truth": False},
                    "d": {"text": "Quãng đường vật đi được trong 2 giây đầu là 14 mét.", "truth": True}
                },
                "p2_explain": "v(t) = 3(t-1)^2 + 6 >= 6 nên đạt GTNN tại t = 1s (ý c Sai). Các ý a, b, d đều Đúng.",
                "p3_stem": "Trong không gian Oxyz, tính khoảng cách từ điểm M(1; 2; -2) đến mặt phẳng (P): 2x + 2y - z + 5 = 0.",
                "p3_ans": 5.0,
                "p3_explain": "Áp dụng công thức khoảng cách: d = |2(1) + 2(2) - (-2) + 5| / sqrt(4 + 4 + 1) = 15 / 3 = 5.",
                "p4_stem": "Trình bày phương pháp lập bảng biến thiên để tìm giá trị lớn nhất của hàm số trên đoạn [a; b].",
                "p4_rubric": "Bước 1: Tìm tập xác định và tính f'(x) (0.25đ). Bước 2: Tìm nghiệm f'(x)=0 thuộc (a;b) (0.5đ). Bước 3: So sánh f(a), f(b) và f(x_i) để kết luận (0.25đ)."
            }
        ],
        "triage_alerts": []
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val