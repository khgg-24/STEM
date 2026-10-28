# 🚀 ED-ODYSSEY NEXUS
**Hệ sinh thái Hỗ trợ Học tập Đa môn, Cộng đồng Đồng đẳng, Quản lý Dạy học (LMS) & Định hướng Tuyển sinh Đa cấp học (Lớp 6–12)**

## 1. Cấu trúc Thư mục Dự án (Repository Architecture)
```text
ed-odyssey-nexus/
├── app.py                      # Điểm khởi chạy chính & Điều hướng 5 Phân hệ
├── config.py                   # Cấu hình giao diện CSS Glassmorphism & Session State
├── requirements.txt            # Danh sách thư viện Python
├── README.md                   # Tài liệu hướng dẫn cài đặt & triển khai
└── modules/
    ├── __init__.py
    ├── learning_hub.py         # Mô-đun 1: Công cụ Học tập Đa môn (KHTN, KHXH, Tiếng Anh) & Bảo tàng Sai lầm
    ├── career_navigator.py     # Mô-đun 2: Định hướng Đa chiều & Dự báo Tuyển sinh (THCS thi vào 10 & THPT thi ĐH)
    ├── community_qa.py         # Mô-đun 3: Chợ Hỏi-Đáp Bài tập, Điểm Trí tuệ (WP) & Phòng học Odyssey Squads
    ├── teacher_lms.py          # Mô-đun 4: Phân hệ Giáo viên & Trình tạo/chấm Đề thi chuẩn 4 dạng Bộ GD&ĐT
    └── telemetry_sensor.py     # Mô-đun 5: Cảm biến JS Telemetry (FSI/AEI chống treo máy) & Sơ cứu Tâm lý