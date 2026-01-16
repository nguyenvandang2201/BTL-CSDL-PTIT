# 🎬 Hệ Thống Đặt Vé Xem Phim Online

> **Bài tập lớn môn Cơ sở dữ liệu - Học viện Công nghệ Bưu chính Viễn thông (PTIT)**

Hệ thống đặt vé xem phim trực tuyến hoàn chỉnh với đầy đủ tính năng cho người dùng và quản trị viên.

---

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Tính năng](#-tính-năng)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Screenshots](#-screenshots)
- [Tác giả](#-tác-giả)

---

## 🎯 Giới thiệu

Hệ thống đặt vé xem phim online cho phép:
- **Khách hàng**: Xem thông tin phim, chọn suất chiếu, đặt ghế và thanh toán vé
- **Quản trị viên**: Quản lý phim, phòng chiếu, suất chiếu và theo dõi doanh thu

---

## 🛠 Công nghệ sử dụng

### Backend
| Công nghệ | Phiên bản | Mô tả |
|-----------|-----------|-------|
| **Python** | 3.11+ | Ngôn ngữ lập trình |
| **Django** | 5.2.6 | Web Framework |
| **Django REST Framework** | 3.16.1 | REST API Framework |
| **PostgreSQL** | 14+ | Hệ quản trị CSDL |
| **JWT** | - | Xác thực người dùng |

### Frontend
| Công nghệ | Phiên bản | Mô tả |
|-----------|-----------|-------|
| **React** | 18.2.0 | JavaScript Library |
| **React Router** | 6.20.0 | Routing |
| **Axios** | 1.6.2 | HTTP Client |
| **CSS3** | - | Styling |

---

## 💻 Yêu cầu hệ thống

- **Node.js**: 14.0+
- **Python**: 3.11+
- **PostgreSQL**: 14+
- **npm** hoặc **yarn**
- **pip**: Python package manager

---

## 🚀 Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/your-username/BTL_CSDL_PTIT.git
cd BTL_CSDL_PTIT
```

### 2. Cài đặt Backend

```bash
# Di chuyển vào thư mục backend
cd backend

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy script setup tự động (tạo database + admin user)
./setup.sh

# Chạy server
python manage.py runserver
```

**Backend chạy tại:** http://localhost:8000

### 3. Cài đặt Frontend

```bash
# Mở terminal mới, di chuyển vào thư mục frontend
cd frontend

# Cài đặt dependencies
npm install

# Chạy development server
npm start
```

**Frontend chạy tại:** http://localhost:3000

### 4. Seed dữ liệu mẫu (Tùy chọn)

```bash
cd backend
python seed_demo_data.py
```

---

## 📁 Cấu trúc dự án

```
BTL_CSDL_PTIT/
├── backend/                    # Django REST API
│   ├── api/                    # API Application
│   │   ├── models/             # Database Models
│   │   │   ├── user.py         # Model User
│   │   │   ├── movie.py        # Model Movie
│   │   │   ├── auditorium.py   # Model Auditorium
│   │   │   ├── seat.py         # Model Seat
│   │   │   ├── showtime.py     # Model Showtime
│   │   │   ├── booking.py      # Model Booking
│   │   │   ├── ticket.py       # Model Ticket
│   │   │   ├── payment.py      # Model Payment
│   │   │   └── genre.py        # Model Genre
│   │   ├── views/              # API Views
│   │   ├── serializers/        # Data Serializers
│   │   └── permissions/        # Custom Permissions
│   ├── config/                 # Django Configuration
│   ├── services/               # Business Logic
│   ├── schema.sql              # Database Schema
│   └── requirements.txt        # Python Dependencies
│
├── frontend/                   # React Application
│   ├── public/                 # Static Files
│   ├── src/
│   │   ├── components/         # React Components
│   │   │   └── layout/         # Layout Components
│   │   ├── pages/              # Page Components
│   │   │   ├── auth/           # Login, Register
│   │   │   ├── user/           # User Pages
│   │   │   └── admin/          # Admin Pages
│   │   ├── services/           # API Services
│   │   ├── contexts/           # React Contexts
│   │   └── styles/             # CSS Stylesheets
│   └── package.json            # Node Dependencies
│
└── README.md                   # Documentation
```

---

## ✨ Tính năng

### 👤 Người dùng (User)

| Tính năng | Mô tả |
|-----------|-------|
| 🔐 Đăng ký / Đăng nhập | Xác thực JWT an toàn |
| 🎬 Xem danh sách phim | Duyệt phim đang chiếu |
| 🔍 Tìm kiếm phim | Lọc theo tên, thể loại |
| 📋 Chi tiết phim | Xem thông tin, suất chiếu |
| 🪑 Chọn ghế | Giao diện trực quan |
| 💳 Thanh toán | Nhiều phương thức |
| 📜 Lịch sử đặt vé | Xem các vé đã đặt |
| 👤 Quản lý tài khoản | Cập nhật thông tin cá nhân |

### 👨‍💼 Quản trị viên (Admin)

| Tính năng | Mô tả |
|-----------|-------|
| 📊 Dashboard | Thống kê tổng quan |
| 🎬 Quản lý phim | CRUD phim |
| 🏷️ Quản lý thể loại | CRUD thể loại |
| 🏛️ Quản lý phòng chiếu | CRUD phòng chiếu |
| 🕐 Quản lý suất chiếu | Tạo lịch chiếu |
| 📈 Báo cáo doanh thu | Thống kê booking |

---

## 📡 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Authentication Endpoints
| Method | Endpoint | Mô tả |
|--------|----------|-------|
| POST | `/auth/register/` | Đăng ký tài khoản |
| POST | `/auth/login/` | Đăng nhập |
| POST | `/auth/refresh/` | Refresh token |

### Movie Endpoints
| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/movies/` | Danh sách phim |
| GET | `/movies/{id}/` | Chi tiết phim |
| POST | `/movies/` | Tạo phim (Admin) |
| PUT | `/movies/{id}/` | Cập nhật phim (Admin) |
| DELETE | `/movies/{id}/` | Xóa phim (Admin) |

### Booking Endpoints
| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/bookings/` | Danh sách booking |
| POST | `/bookings/` | Tạo booking mới |
| GET | `/bookings/{id}/` | Chi tiết booking |

### Showtime Endpoints
| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/showtimes/` | Danh sách suất chiếu |
| GET | `/showtimes/{id}/` | Chi tiết suất chiếu |
| GET | `/showtimes/{id}/available-seats/` | Ghế trống |

---

## 🗄 Database Schema

### Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    User     │       │    Movie    │       │    Genre    │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │       │ id (PK)     │◄──────│ id (PK)     │
│ username    │       │ title       │       │ name        │
│ email       │       │ duration    │       └─────────────┘
│ password    │       │ rating      │
│ full_name   │       │ release_date│
│ phone       │       │ description │
│ role        │       │ poster_url  │
└──────┬──────┘       └──────┬──────┘
       │                     │
       │                     │
       ▼                     ▼
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   Booking   │       │  Showtime   │◄──────│ Auditorium  │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │◄──────│ id (PK)     │       │ id (PK)     │
│ user_id(FK) │       │ movie_id(FK)│       │ name        │
│ showtime_id │       │ auditorium  │       │ rows_config │
│ status      │       │ start_time  │       └──────┬──────┘
│ total_amount│       │ base_price  │              │
└──────┬──────┘       └─────────────┘              │
       │                                           ▼
       ▼                                   ┌─────────────┐
┌─────────────┐                            │    Seat     │
│   Ticket    │                            ├─────────────┤
├─────────────┤                            │ id (PK)     │
│ id (PK)     │◄───────────────────────────│ auditorium  │
│ booking_id  │                            │ row_label   │
│ seat_id(FK) │                            │ seat_number │
│ price       │                            │ seat_type   │
│ status      │                            └─────────────┘
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Payment   │
├─────────────┤
│ id (PK)     │
│ booking_id  │
│ amount      │
│ provider    │
│ status      │
└─────────────┘
```

### Các bảng chính

| Bảng | Mô tả |
|------|-------|
| `api_user` | Thông tin người dùng |
| `api_movie` | Thông tin phim |
| `api_genre` | Thể loại phim |
| `api_auditorium` | Phòng chiếu |
| `api_seat` | Ghế ngồi |
| `api_showtime` | Suất chiếu |
| `api_booking` | Đơn đặt vé |
| `api_ticket` | Vé |
| `api_payment` | Thanh toán |

---


Đăng nhập phân quyền (Admin/User)
<img width="975" height="577" alt="image" src="https://github.com/user-attachments/assets/715b0b55-1cb5-4a81-b802-609fea89d4ca" />
Giao diện Admin
Thông tin tài khoản
Tính năng đổi mật khẩu
Tính năng quản trị của Admin
Tính năng Quản lý phim
Tính năng Thêm phim mới
Tính năng Quản lý thể loại
Tính năng Thêm thể loại mới
Tính năng Quản lý phòng chiếu 
Tính năng Thêm phòng chiếu
Tính năng Quản lý suất chiếu
Tính năng Thêm suất chiếu
Đăng kí tài khoản Người dùng - User
Giao diện người dùng 
Tính năng Đặt vé ngay
Tính năng Chọn ghế
Tính năng Thanh toán
Tính năng xem lịch sử đặt vé

---

## 🔧 Cấu hình

### Backend (`backend/config/settings.py`)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cinema_btl',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### Frontend (`frontend/src/services/api.js`)
```javascript
const API_URL = 'http://localhost:8000/api'
```

---

## 📝 Ghi chú

- JWT Token tự động refresh khi hết hạn
- Booking hết hạn sau 10 phút nếu chưa thanh toán
- Hỗ trợ 3 loại ghế: Standard, VIP, Couple
- Phân quyền User/Admin được kiểm tra ở cả client và server

---

## 👥 Tác giả

**Sinh viên Học viện PTIT**

---
