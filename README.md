# Cinema Booking System

> **Bài tập lớn môn Cơ sở Dữ liệu - Học viện Công nghệ Bưu chính Viễn thông (PTIT)**

Hệ thống đặt vé xem phim trực tuyến được xây dựng với Django REST Framework và PostgreSQL, tập trung vào thiết kế cơ sở dữ liệu và xử lý nghiệp vụ bằng SQL.

---

## Mục lục

- [Tổng quan](#-tổng-quan)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Thiết kế kiến trúc dữ liệu](#-thiết-kế-kiến-trúc-dữ-liệu)
- [Xử lý nghiệp vụ bằng SQL](#-xử-lý-nghiệp-vụ-business-logic-bằng-sql)
- [Tối ưu hiệu năng](#-tối-ưu-hiệu-năng)
- [Cài đặt và chạy](#-cài-đặt-và-chạy)
- [API Endpoints](#-api-endpoints)

---

## Tổng quan

### Chức năng chính

| Module | Mô tả |
|--------|-------|
| **Quản lý phim** | CRUD phim, thể loại, poster, thời lượng |
| **Quản lý phòng chiếu** | Phòng chiếu, ghế ngồi (Standard/VIP/Couple) |
| **Quản lý suất chiếu** | Lịch chiếu, giá vé cơ bản, trạng thái |
| **Đặt vé** | Chọn ghế, giữ chỗ tạm thời, thanh toán |
| **Check-in** | Quét QR code, xác nhận vé tại rạp |
| **Xác thực** | JWT Authentication, phân quyền User/Admin |

### Quy trình đặt vé

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Chọn phim  │ -> │ Chọn suất   │ -> │  Chọn ghế   │ -> │  Đặt vé     │
│  & thể loại │    │  chiếu      │    │  (realtime) │    │  (pending)  │
└─────────────┘    └─────────────┘    └─────────────┘    └──────┬──────┘
                                                                │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│  Check-in   │ <- │  Vé điện tử │ <- │ Thanh toán  │ <─────────┘
│  tại rạp    │    │  (QR Code)  │    │ (10 phút)   │
└─────────────┘    └─────────────┘    └─────────────┘
```

---

## Công nghệ sử dụng

| Layer | Technology |
|-------|------------|
| **Backend Framework** | Django 5.2.6 |
| **REST API** | Django REST Framework 3.16.1 |
| **Database** | PostgreSQL 15+ |
| **Authentication** | JWT (Simple JWT 5.5.1) |
| **Filtering** | django-filter 25.2 |
| **Database Adapter** | psycopg 3.2.10 |

---

## Thiết kế kiến trúc dữ liệu

### Entity Relationship Diagram (ERD)

```
                              ┌──────────────────┐
                              │     api_user     │
                              ├──────────────────┤
                              │ PK id (UUID)     │
                              │    username      │
                              │    email         │
                              │    password      │
                              │    full_name     │
                              │    phone         │
                              │    role          │
                              │    date_of_birth │
                              └────────┬─────────┘
                                       │
                                       │ 1:N
                                       ▼
┌────────────────┐           ┌──────────────────┐           ┌────────────────┐
│   api_movie    │           │   api_booking    │           │  api_payment   │
├────────────────┤           ├──────────────────┤           ├────────────────┤
│ PK id (UUID)   │           │ PK id (UUID)     │◄──────────│ PK id (UUID)   │
│    title       │           │ FK user_id       │   1:1     │ FK booking_id  │
│    duration_min│           │ FK showtime_id   │           │    amount      │
│    rating      │           │    status        │           │    provider    │
│    release_date│           │    total_amount  │           │    status      │
│    description │           │    expires_at    │           │    paid_at     │
│    poster_url  │           │    created_at    │           │    external_id │
└───────┬────────┘           └────────┬─────────┘           └────────────────┘
        │                             │
        │ M:N                         │ 1:N
        ▼                             ▼
┌────────────────┐           ┌──────────────────┐
│ api_moviegenre │           │   api_ticket     │
├────────────────┤           ├──────────────────┤
│ PK id          │           │ PK id (UUID)     │
│ FK movie_id    │           │ FK booking_id    │
│ FK genre_id    │           │ FK showtime_id   │
└───────┬────────┘           │ FK seat_id       │
        │                    │    price         │
        ▼                    │    qr_code       │
┌────────────────┐           │    status        │
│   api_genre    │           │    booked_at     │
├────────────────┤           └────────┬─────────┘
│ PK id (UUID)   │                    │
│    name        │                    │
└────────────────┘                    │
                                      │
┌────────────────┐           ┌────────┴─────────┐           ┌────────────────┐
│ api_auditorium │◄──────────│  api_showtime    │           │    api_seat    │
├────────────────┤    N:1    ├──────────────────┤    N:1    ├────────────────┤
│ PK id (UUID)   │           │ PK id (UUID)     │──────────►│ PK id (UUID)   │
│    name        │           │ FK movie_id      │           │ FK auditorium_id│
│ standard_row_  │           │ FK auditorium_id │           │    row_label   │
│    count       │           │    start_time    │           │    seat_number │
│ vip_row_count  │           │    end_time      │           │    seat_type   │
│ couple_row_    │           │    base_price    │           └────────────────┘
│    count       │           │    status        │
│ seats_per_row  │           └──────────────────┘
└────────────────┘
```

### Chi tiết các bảng

#### 1. `api_user` - Người dùng
```sql
CREATE TABLE "api_user" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "username" varchar(150) NOT NULL UNIQUE,
    "email" varchar(254) NOT NULL UNIQUE,
    "password" varchar(128) NOT NULL,
    "full_name" varchar(100) NULL,
    "phone" varchar(20) NULL,
    "role" varchar(12) NOT NULL DEFAULT 'user' 
        CHECK ("role" IN ('user', 'admin')),
    "date_of_birth" date NULL,
    "is_active" boolean NOT NULL DEFAULT TRUE,
    "created_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

#### 2. `api_movie` - Phim
```sql
CREATE TABLE "api_movie" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "title" varchar(200) NOT NULL,
    "duration_min" integer NOT NULL CHECK ("duration_min" >= 0),
    "rating" varchar(10) NULL,  -- P, C13, C16, C18
    "release_date" date NULL,
    "description" text NOT NULL DEFAULT '',
    "poster_url" text NOT NULL DEFAULT ''
);
```

#### 3. `api_auditorium` - Phòng chiếu
```sql
CREATE TABLE "api_auditorium" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" varchar(60) NOT NULL UNIQUE,
    "standard_row_count" integer NOT NULL CHECK ("standard_row_count" >= 0),
    "vip_row_count" integer NOT NULL CHECK ("vip_row_count" >= 0),
    "couple_row_count" integer NOT NULL CHECK ("couple_row_count" >= 0),
    "seats_per_row" integer NOT NULL CHECK ("seats_per_row" >= 0),
    "created_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

#### 4. `api_seat` - Ghế ngồi
```sql
CREATE TABLE "api_seat" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "auditorium_id" uuid NOT NULL REFERENCES "api_auditorium" ("id"),
    "row_label" varchar(5) NOT NULL,        -- A, B, C, ...
    "seat_number" integer NOT NULL,          -- 1, 2, 3, ...
    "seat_type" varchar(10) NOT NULL DEFAULT 'standard' 
        CHECK ("seat_type" IN ('standard', 'vip', 'couple')),
    UNIQUE ("auditorium_id", "row_label", "seat_number")
);
```

#### 5. `api_showtime` - Suất chiếu
```sql
CREATE TABLE "api_showtime" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "movie_id" uuid NOT NULL REFERENCES "api_movie" ("id"),
    "auditorium_id" uuid NOT NULL REFERENCES "api_auditorium" ("id"),
    "start_time" timestamp with time zone NOT NULL,
    "end_time" timestamp with time zone NOT NULL,
    "base_price" numeric(12, 2) NOT NULL DEFAULT 0,
    "status" varchar(20) NOT NULL DEFAULT 'scheduled',
    UNIQUE ("auditorium_id", "start_time")
);
```

#### 6. `api_booking` - Đơn đặt vé
```sql
CREATE TABLE "api_booking" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "user_id" uuid NOT NULL REFERENCES "api_user" ("id"),
    "showtime_id" uuid NOT NULL REFERENCES "api_showtime" ("id"),
    "status" varchar(20) NOT NULL DEFAULT 'pending' 
        CHECK ("status" IN ('pending', 'reserved', 'paid', 'canceled')),
    "total_amount" numeric(12, 2) NOT NULL DEFAULT 0,
    "payment_method" varchar(30) NULL,
    "created_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expires_at" timestamp with time zone NULL  -- Hết hạn thanh toán
);
```

#### 7. `api_ticket` - Vé
```sql
CREATE TABLE "api_ticket" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "booking_id" uuid NOT NULL REFERENCES "api_booking" ("id"),
    "showtime_id" uuid NOT NULL REFERENCES "api_showtime" ("id"),
    "seat_id" uuid NOT NULL REFERENCES "api_seat" ("id"),
    "price" numeric(12, 2) NOT NULL,
    "qr_code" varchar(64) NULL,
    "status" varchar(20) NOT NULL DEFAULT 'reserved' 
        CHECK ("status" IN ('reserved', 'paid', 'checked_in', 'canceled', 'refunded')),
    "booked_at" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE ("showtime_id", "seat_id")  -- Mỗi ghế chỉ bán 1 lần/suất chiếu
);
```

#### 8. `api_payment` - Thanh toán
```sql
CREATE TABLE "api_payment" (
    "id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "booking_id" uuid NOT NULL UNIQUE REFERENCES "api_booking" ("id"),
    "amount" numeric(12, 2) NOT NULL,
    "provider" varchar(40) NOT NULL DEFAULT 'credit_card' 
        CHECK ("provider" IN ('credit_card', 'cash', 'e_wallet', 'bank_transfer')),
    "external_id" varchar(80) NULL,  -- Transaction ID từ payment gateway
    "status" varchar(20) NOT NULL DEFAULT 'pending' 
        CHECK ("status" IN ('pending', 'completed', 'failed', 'refunded')),
    "paid_at" timestamp with time zone NULL,
    "created_at" timestamp with time zone NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Mối quan hệ giữa các bảng

| Quan hệ | Mô tả |
|---------|-------|
| `User` → `Booking` | 1:N - Một user có nhiều booking |
| `Booking` → `Ticket` | 1:N - Một booking có nhiều ticket (nhiều ghế) |
| `Booking` → `Payment` | 1:1 - Mỗi booking có một payment |
| `Showtime` → `Ticket` | 1:N - Một suất chiếu có nhiều vé |
| `Showtime` → `Movie` | N:1 - Nhiều suất chiếu cho một phim |
| `Showtime` → `Auditorium` | N:1 - Nhiều suất chiếu trong một phòng |
| `Auditorium` → `Seat` | 1:N - Một phòng có nhiều ghế |
| `Movie` → `Genre` | M:N - Phim có nhiều thể loại (qua `MovieGenre`) |

---

## Xử lý nghiệp vụ (Business Logic) bằng SQL

### 1. Trigger: Tự động cập nhật `updated_at`

```sql
-- Function để update timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN 
    NEW.updated_at = CURRENT_TIMESTAMP; 
    RETURN NEW; 
END;
$$ LANGUAGE plpgsql;

-- Trigger cho bảng auditorium
CREATE TRIGGER trigger_auditorium_updated_at 
    BEFORE UPDATE ON api_auditorium 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Trigger cho bảng user
CREATE TRIGGER trigger_user_updated_at 
    BEFORE UPDATE ON api_user 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 2. Trigger: Tự động set thời hạn thanh toán (10 phút)

```sql
CREATE OR REPLACE FUNCTION set_booking_expiry()
RETURNS TRIGGER AS $$
BEGIN 
    IF NEW.expires_at IS NULL THEN 
        NEW.expires_at = NEW.created_at + INTERVAL '10 minutes'; 
    END IF; 
    RETURN NEW; 
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_booking_expiry 
    BEFORE INSERT ON api_booking 
    FOR EACH ROW EXECUTE FUNCTION set_booking_expiry();
```

**Giải thích:** Khi user đặt vé, họ có 10 phút để hoàn tất thanh toán. Sau thời gian này, booking sẽ tự động bị hủy và ghế được trả lại.

### 3. Function: Lấy danh sách ghế trống với giá đã tính

```sql
CREATE OR REPLACE FUNCTION get_available_seats(p_showtime_id UUID)
RETURNS TABLE (
    seat_id UUID, 
    row_label VARCHAR(5), 
    seat_number INTEGER, 
    seat_type VARCHAR(10), 
    calculated_price NUMERIC(12,2)
) AS $$
DECLARE 
    v_base_price NUMERIC(12,2);
BEGIN
    -- Lấy giá cơ bản từ suất chiếu
    SELECT base_price INTO v_base_price 
    FROM api_showtime WHERE id = p_showtime_id;
    
    RETURN QUERY
    SELECT 
        s.id, 
        s.row_label, 
        s.seat_number, 
        s.seat_type,
        -- Tính giá theo loại ghế
        v_base_price * CASE s.seat_type 
            WHEN 'standard' THEN 1.0   -- Ghế thường: x1.0
            WHEN 'vip' THEN 1.5        -- Ghế VIP: x1.5
            WHEN 'couple' THEN 2.0     -- Ghế đôi: x2.0
        END AS calculated_price
    FROM api_seat s
    WHERE s.auditorium_id = (
        SELECT auditorium_id FROM api_showtime WHERE id = p_showtime_id
    )
    -- Loại bỏ ghế đã được đặt
    AND NOT EXISTS (
        SELECT 1 FROM api_ticket t 
        WHERE t.seat_id = s.id 
        AND t.showtime_id = p_showtime_id 
        AND t.status IN ('reserved', 'paid', 'checked_in')
    )
    ORDER BY s.row_label, s.seat_number;
END;
$$ LANGUAGE plpgsql;
```

**Sử dụng:**
```sql
SELECT * FROM get_available_seats('showtime-uuid-here');
```

### 4. View: Phim kèm thể loại

```sql
CREATE OR REPLACE VIEW v_movie_with_genres AS
SELECT 
    m.id, 
    m.title, 
    m.duration_min, 
    m.rating, 
    m.release_date,
    m.description,
    m.poster_url,
    STRING_AGG(g.name, ', ' ORDER BY g.name) as genres
FROM api_movie m 
LEFT JOIN api_moviegenre mg ON m.id = mg.movie_id 
LEFT JOIN api_genre g ON mg.genre_id = g.id
GROUP BY m.id, m.title, m.duration_min, m.rating, 
         m.release_date, m.description, m.poster_url;
```

**Kết quả:**
| id | title | duration_min | rating | genres |
|----|-------|--------------|--------|--------|
| ... | Avengers: Endgame | 181 | C13 | Action, Sci-Fi |
| ... | The Notebook | 123 | C16 | Drama, Romance |

### 5. Hệ thống tính giá vé động

```python
# Python Model - Seat pricing multiplier
class Seat(models.Model):
    PRICE_MULTIPLIER = {
        'standard': 1.0,  # 100% giá gốc
        'vip': 1.5,       # 150% giá gốc  
        'couple': 3.0,    # 300% giá gốc (2 người)
    }
```

```python
# Tự động tính giá khi tạo ticket
class Ticket(models.Model):
    def save(self, *args, **kwargs):
        if not self.price or self.price == 0:
            base_price = self.showtime.base_price
            multiplier = Seat.PRICE_MULTIPLIER.get(self.seat.seat_type, 1.0)
            self.price = base_price * Decimal(str(multiplier))
        super().save(*args, **kwargs)
```

### 6. Kiểm tra và tự động hủy booking hết hạn

```python
class Booking(models.Model):
    def is_expired(self):
        """Check booking đã hết hạn thanh toán chưa"""
        if self.status != "pending":
            return False
        return timezone.now() > self.expires_at

    def auto_cancel_if_expired(self):
        """Tự động hủy nếu hết hạn"""
        if self.is_expired() and self.status == "pending":
            self.status = "canceled"
            self.save()
            # Hủy tất cả tickets của booking này
            self.tickets.update(status="canceled")
            return True
        return False

    @classmethod
    def cleanup_expired_bookings(cls):
        """Cleanup tất cả booking hết hạn - chạy định kỳ"""
        now = timezone.now()
        expired_bookings = cls.objects.filter(
            status="pending", 
            expires_at__lt=now
        )
        
        for booking in expired_bookings:
            booking.status = "canceled"
            booking.save()
            booking.tickets.update(status="canceled")
```

### 7. Kiểm tra ghế khả dụng (Prevent Double Booking)

```python
# Trong BookingCreateSerializer
def validate(self, data):
    showtime = data["showtime"]
    seat_ids = data["seat_ids"]
    
    # Kiểm tra ghế đã được đặt chưa (với transaction lock)
    existing_tickets = Ticket.objects.filter(
        showtime=showtime,
        seat__in=seats,
        status__in=["reserved", "paid", "checked_in"],
    )
    
    if existing_tickets.exists():
        booked_seats = existing_tickets.values_list(
            "seat__row_label", "seat__seat_number"
        )
        seat_labels = [f"{row}{num}" for row, num in booked_seats]
        raise serializers.ValidationError(
            f"Ghế đã được đặt: {', '.join(seat_labels)}"
        )
```

### 8. Constraint: Đảm bảo một ghế chỉ bán một lần mỗi suất chiếu

```sql
-- Unique constraint level database
ALTER TABLE "api_ticket" ADD CONSTRAINT 
    "api_ticket_showtime_id_seat_id_c45a7e90_uniq" 
    UNIQUE ("showtime_id", "seat_id");
```

---

## Tối ưu hiệu năng

### 1. Indexing Strategy

#### Primary Indexes (Tự động với Primary Key)
```sql
-- UUID Primary Keys cho tất cả bảng chính
"id" uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4()
```

#### Secondary Indexes (Query Optimization)

```sql
-- Index cho tìm kiếm suất chiếu theo phim
CREATE INDEX "api_showtim_movie_i_043b6b_idx" 
    ON "api_showtime" ("movie_id");

-- Composite index cho tìm kiếm suất chiếu theo phòng + thời gian
CREATE INDEX "api_showtim_auditor_3717c2_idx" 
    ON "api_showtime" ("auditorium_id", "start_time");

-- Index cho tìm kiếm booking theo user
CREATE INDEX "api_booking_user_id_cfdf50_idx" 
    ON "api_booking" ("user_id");

-- Index cho tìm kiếm booking theo showtime
CREATE INDEX "api_booking_showtim_c4c32e_idx" 
    ON "api_booking" ("showtime_id");

-- Index cho cleanup expired bookings (cron job)
CREATE INDEX "api_booking_expires_651e73_idx" 
    ON "api_booking" ("expires_at");

-- Index cho tìm kiếm ticket theo showtime
CREATE INDEX "api_ticket_showtim_31e4c3_idx" 
    ON "api_ticket" ("showtime_id");

-- Index cho payment lookup
CREATE INDEX "api_payment_booking_a0e9be_idx" 
    ON "api_payment" ("booking_id");
```

#### Pattern-based Indexes (Text Search)
```sql
-- Index cho tìm kiếm auditorium theo tên
CREATE INDEX "api_auditorium_name_af3b8bc3_like" 
    ON "api_auditorium" ("name" varchar_pattern_ops);

-- Index cho tìm kiếm user theo username
CREATE INDEX "api_user_username_cf4e88d2_like" 
    ON "api_user" ("username" varchar_pattern_ops);

-- Index cho tìm kiếm user theo email
CREATE INDEX "api_user_email_9ef5afa6_like" 
    ON "api_user" ("email" varchar_pattern_ops);
```

### 2. Query Optimization với Django ORM

#### Select Related (Giảm N+1 Query)
```python
# Bad: N+1 queries
bookings = Booking.objects.all()
for b in bookings:
    print(b.showtime.movie.title)  # Mỗi lần loop = 2 query

# Good: 1 query với JOIN
bookings = Booking.objects.select_related(
    'showtime__movie',
    'showtime__auditorium'
)
```

#### Prefetch Related (Cho quan hệ Many-to-Many/Reverse FK)
```python
# Prefetch tickets của booking
bookings = Booking.objects.prefetch_related(
    'tickets__seat'
)
```

#### Kết hợp cả hai
```python
# BookingViewSet.get_queryset()
def get_queryset(self):
    return (
        Booking.objects.filter(user=self.request.user)
        .select_related(
            "showtime__movie",      # FK -> FK
            "showtime__auditorium"  # FK -> FK
        )
        .prefetch_related(
            "tickets__seat"         # Reverse FK -> FK
        )
    )
```

### 3. Database-level Constraints

```sql
-- Check constraints để validate data tại DB level
CHECK ("duration_min" >= 0)
CHECK ("standard_row_count" >= 0)
CHECK ("role" IN ('user', 'admin'))
CHECK ("seat_type" IN ('standard', 'vip', 'couple'))
CHECK ("status" IN ('pending', 'reserved', 'paid', 'canceled'))
```

### 4. UUID vs Auto-increment ID

| Aspect | UUID | Auto-increment |
|--------|------|----------------|
| **Uniqueness** | Globally unique | Unique per table |
| **Security** | Khó đoán | Dễ đoán (enumeration attack) |
| **Distributed** | Có thể generate ở client | Phải query DB |
| **Storage** | 16 bytes | 4-8 bytes |
| **Index Performance** | Chậm hơn một chút | Nhanh hơn |

**Lý do chọn UUID:** Bảo mật tốt hơn cho booking/payment IDs, tránh enumeration attacks.

### 5. Connection Pooling (Production)

```python
# settings.py - Django Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'CONN_MAX_AGE': 60,  # Connection pooling
        'OPTIONS': {
            'connect_timeout': 10,
        }
    }
}
```

### 6. Caching Strategy (Đề xuất)

```python
# Cache danh sách ghế trống (Redis)
from django.core.cache import cache

def get_available_seats_cached(showtime_id):
    cache_key = f"seats_available_{showtime_id}"
    
    # Try cache first
    cached = cache.get(cache_key)
    if cached:
        return cached
    
    # Query DB
    result = get_available_seats(showtime_id)
    
    # Cache 30 seconds (short TTL vì data thay đổi nhanh)
    cache.set(cache_key, result, timeout=30)
    
    return result
```

### 7. Phân tích Query Performance

```sql
-- Sử dụng EXPLAIN ANALYZE
EXPLAIN ANALYZE 
SELECT * FROM api_ticket t
JOIN api_seat s ON t.seat_id = s.id
WHERE t.showtime_id = 'uuid-here'
AND t.status IN ('reserved', 'paid');

-- Kết quả mong đợi: Index Scan thay vì Seq Scan
```

---

## Cài đặt và chạy

### Yêu cầu

- Python 3.10+
- PostgreSQL 15+
- pip

### Bước 1: Clone repository

```bash
git clone https://github.com/nguyenvandang2201/BTL-CSDL-PTIT.git
cd BTL-CSDL-PTIT/backend
```

### Bước 2: Tạo virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình database

Tạo file `.env`:
```env
DB_NAME=cinema_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key
DEBUG=True
```

### Bước 5: Tạo database và chạy schema

```bash
# Tạo database trong PostgreSQL
psql -U postgres -c "CREATE DATABASE cinema_db;"

# Chạy schema SQL
psql -U postgres -d cinema_db -f schema.sql
```

### Bước 6: Chạy migrations (nếu cần)

```bash
python manage.py migrate
```

### Bước 7: Tạo superuser

```bash
python manage.py createsuperuser
```

### Bước 8: Chạy server

```bash
python manage.py runserver
```

Server chạy tại: `http://127.0.0.1:8000/`

---

## API Endpoints

### Authentication

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| POST | `/api/auth/register/` | Đăng ký tài khoản |
| POST | `/api/auth/login/` | Đăng nhập (JWT) |
| POST | `/api/auth/token/refresh/` | Refresh token |

### Movies

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/api/movies/` | Danh sách phim |
| GET | `/api/movies/{id}/` | Chi tiết phim |
| GET | `/api/movies/{id}/showtimes/` | Suất chiếu của phim |

### Showtimes

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/api/showtimes/` | Danh sách suất chiếu |
| GET | `/api/showtimes/{id}/` | Chi tiết suất chiếu |
| GET | `/api/showtimes/{id}/seats/` | Sơ đồ ghế + trạng thái |

### Bookings

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/api/bookings/` | Booking của user |
| POST | `/api/bookings/` | Tạo booking mới |
| GET | `/api/bookings/{id}/` | Chi tiết booking |
| POST | `/api/bookings/{id}/cancel/` | Hủy booking |
| GET | `/api/bookings/history/` | Lịch sử đặt vé |
| GET | `/api/bookings/upcoming/` | Vé sắp tới |

### Payments

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| POST | `/api/payments/` | Thanh toán booking |
| GET | `/api/payments/{id}/` | Chi tiết thanh toán |
| POST | `/api/payments/{id}/refund/` | Hoàn tiền |
| GET | `/api/payments/{id}/receipt/` | Xuất hóa đơn |
| GET | `/api/payments/history/` | Lịch sử thanh toán |

### Tickets

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/api/tickets/` | Vé của user |
| GET | `/api/tickets/{id}/` | Chi tiết vé |
| POST | `/api/tickets/{id}/check_in/` | Check-in tại rạp |

---

## Tác giả

- **Sinh viên:** [Nguyễn Văn Đăng]
- **Mã sinh viên:** [B23DCCN119]
- **Lớp:** [D23CQCN07-B]
- **Môn học:** Cơ sở Dữ liệu

---