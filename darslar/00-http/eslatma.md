# 0-bosqich: HTTP asoslari

## 1-dars · 29-sentyabr

### Server va mijoz
**Server** — ma'lumotlar saqlanadigan va so'rovlarga javob qaytaradigan kompyuter.
**Mijoz** — serverga so'rov yuboradigan dastur: brauzer, mobil ilova yoki `curl`. Foydalanuvchi (inson) esa mijoz orqali ishlaydi.

### So'rovning yuragi: metod + yo'l
So'rovning asosi ikki qismdan iborat:
1. **Metod** — nima qilish kerakligini bildiradi
2. **Yo'l (path)** — amal nima ustida bajarilishini ko'rsatadi

Masalan, kitobni o'chirish uchun metod — `DELETE`, yo'l — `/books/1`:
`DELETE /books/1`

### 4 ta metod
| Metod | Ma'nosi |
|---|---|
| `GET` | o'qish |
| `POST` | yangi yaratish |
| `PUT` / `PATCH` | o'zgartirish |
| `DELETE` | o'chirish |

### CRUD: /books
```
GET    /books
GET    /books/1
POST   /books
PUT    /books/1
DELETE /books/1
```

## 2-dars · 1-oktyabr

### Status kod guruhlari
Kodning birinchi raqami guruhni bildiradi:
- **2xx** — so'rov muvaffaqiyatli bajarildi
- **4xx** — xato mijoz tomonida, ya'ni so'rovni to'g'rilash kerak
- **5xx** — xato server tomonida

### 8 ta asosiy kod
| Kod | Ma'nosi |
|---|---|
| `200` | so'rov muvaffaqiyatli bajarildi |
| `201` | yangi resurs yaratildi (odatda `POST` dan keyin) |
| `204` | bajarildi, lekin qaytaradigan narsa yo'q |
| `400` | so'rov noto'g'ri tuzilgan (masalan, majburiy maydon bo'sh) |
| `401` | foydalanuvchi tizimga kirmagan (login qilinmagan), server uni tanimaydi |
| `403` | foydalanuvchi tizimga kirgan, lekin bu amalni bajarishga huquqi yo'q |
| `404` | so'ralgan resurs yoki yo'l serverda topilmadi |
| `500` | server ichida xatolik yuz berdi |

### 401 va 403 farqi
Bitta saytni misol qilib olaylik. Biz unga endi kirdik va hali login qilmaganmiz.

- **401 — "Sen kimsan?"** Login qilmagan bo'lsak, server bizni tanimaydi va himoyalangan sahifani ochmaydi.
- **403 — "Seni taniyman, lekin mumkin emas."** Login qilganimizdan keyin biz oddiy foydalanuvchimiz. Admin panelga kirmoqchi yoki saytdan biror narsani o'chirmoqchi bo'lsak, server bizni taniydi, lekin ruxsat bermaydi.

### Nega parolni faqat frontendda tekshirib bo'lmaydi?
Frontenddagi tekshiruv va tugmalarni aylanib o'tish mumkin: masalan, `curl` orqali terminaldan serverga to'g'ridan-to'g'ri so'rov yuborsa bo'ladi. Shuning uchun haqiqiy tekshiruv har doim **serverda** bo'lishi kerak.

> Frontend — qulaylik, backend — xavfsizlik.

## 3-dars · 1-oktyabr

### Header va body
So'rovni konvertdagi xatga o'xshatish mumkin:
- **Header** — konvert ustidagi, ya'ni tashqi ma'lumot. Masalan, so'rov qayerga jo'natilayotgani shu yerda yoziladi.
- **Body** — konvert ichidagi asosiy ma'lumot.

### Content-Type
```
Content-Type: application/json; charset=utf-8
```
- `application/json` — body'ning formati
- `charset=utf-8` — harflar qanday yozilgani

### curl flaglari
| Flag | Vazifasi |
|---|---|
| `-X` | metodni tanlaydi (masalan, `-X POST`) |
| `-H` | header qo'shadi |
| `-d` | body'da yuboriladigan ma'lumot |

### Nega yaratilgan post 404 berdi?
`POST /posts` dan keyin server `201` va `id: 101` qaytardi, lekin `GET /posts/101` — `404`.
Sababi: bu mashq uchun qilingan server bo'lib, postni **ma'lumotlar bazasiga saqlamadi**, shuning uchun keyin uni topa olmadi.


## 4-dars · 2-oktyabr — Birinchi server

### So'rov yuborish va qabul qilish nega kerak?
Universitet guruhi misolida: starosta vazifani **serverga** yuboradi (`POST`), talabalar esa uni **serverdan** oladi (`GET`).
Server **o'rtada** turadi — shuning uchun bir odam qo'shgan narsani boshqalar ham ko'radi.

### `localhost` va port
- **`localhost`** — o'zimizning kompyuterimiz
- **`8000`** — port, ya'ni kirish eshigi

### `python3 -m http.server`
Papkani saytga aylantiradi, lekin ichidagi **hamma narsani** ochib beradi.
qan
### Nega terminal "qotib qoladi"?
Sababi — `serve_forever()`: server to'xtamasdan so'rov kutib turadi. To'xtatish — **Ctrl+C**.

### Server javobining 4 qismi
| Qism | Python'da |
|---|---|
| 1. Status | `self.send_response(200)` |
| 2. Header — body qanday formatda va qaysi yozuvda | `self.send_header("Content-Type", "text/plain; charset=utf-8")` |
| 3. Headerlar tugashi (bo'sh qator) | `self.end_headers()` |
| 4. Body | `self.wfile.write("...".encode())` |

### `do_GET` ni kim chaqiradi?
Python'ning o'zi (`HTTPServer`) — **GET so'rov kelganda**.

### Meros
Koddagi meros — `BaseHTTPRequestHandler`. U javobning 4 qismini noldan yozmasdan, **otadan meros** olish uchun kerak.

### `.encode()`
Harflarni baytlarga aylantirish uchun kerak.

### Oxirgi qator nega chekinishsiz?
Class — bu qolip, oxirgi qator esa o'sha qolipni **ishlatadi**. Shuning uchun u class'dan tashqarida, ya'ni chekinishsiz turadi.

### `text/plain` va `text/html`
Body bir xil — masalan, `<h1>Salom</h1>`:
- **`text/html`** — brauzer teglarni **chizadi**, katta sarlavha ko'rinadi (JavaScript'dagi `innerHTML` kabi)
- **`text/plain`** — teglar **matn** bo'lib ko'rinadi (`textContent` kabi)

### Server uchun brauzer va curl
Server uchun **farq yo'q** — ikkalasidan ham bir xil HTTP matni keladi.
Xulosa: server mijozga ko'r-ko'rona ishonmaydi, hamma narsani **o'zi** tekshiradi.

### Traceback'ni o'qish
Pastdan o'qi → o'z faylingni top → `^^^^` ga qara.

### Bugungi 2 ta xato
- **`NameError`** — "bunday **nom**ni tanimayman"
- **`AttributeError`** — "bu narsada bunday **xususiyat/funksiya** yo'q"

## 5-dars · 2-oktyabr (kechqurun) — Routing va funksiya

### Muammo
Birinchi server hamma yo'lga (`/tasks`, `/users`, mavjud bo'lmagan manzil) **bir xil javob** va **200** qaytarardi — yo'llarni ajrata olmasdi.

### Routing
"Qaysi yo'l kelsa — qaysi kod ishlasin" degan qoida. So'ralgan yo'l `self.path` da turadi (meros orqali keladi, import shart emas):
```python
if self.path == '/users':     ...
elif self.path == '/tasks':   ...
else:                         ... # 404
```

### `javob_ber` funksiyasi (DRY — o'zingni takrorlama)
Har bir `if`/`else` ichidagi `self.javob_ber()` faqat **status** va **body**ni oladi. Qolgan qolip (header, bo'sh qator) bir xil bo'lgani uchun funksiya ichida turadi va avtomatik chiqadi.
```python
def javob_ber(self, status, matn):
    self.send_response(status)
    self.send_header('Content-Type', 'text/plain; charset=utf-8')
    self.end_headers()
    self.wfile.write(matn.encode())
```
`do_GET` 12 qatordan **3 qatorga** qisqardi.

### Yodda tutish
- **400** — so'rov noto'g'ri tuzilgan, **404** — bunday narsa yo'q
- 🔒 404 xabarida ortiqcha ma'lumot (masalan, foydalanuvchilar ro'yxati) bermaslik kerak
- Kod o'zgarsa — eski serverni **Ctrl+C** bilan to'xtatib, qayta ishga tushirish kerak (aks holda port band)

## 6-dars · 3-oktyabr — FastAPI'ga birinchi qadam

### Takrorlash: ikki muhim tushuncha
- **`do_GET` ni server chaqiradi — har safar GET so'rov kelganda.** Server 2 soat ishlab, 5 ta so'rov kelsa — `do_GET` 5 marta chaqiriladi.
- **Brauzer ham, curl ham — mijoz.** Ikkalasi ham so'rov yuboradi va javob oladi. Farqi: brauzer javobni chiroyli chizadi, curl xom ko'rsatadi. Server uchun farq yo'q — shuning uchun server o'zi tekshirishi kerak (ruxsat bo'lmasa — **403**).

### O'rnatish
```bash
cd darslar/03-fastapi
python3 -m venv .venv
source .venv/bin/activate          # avval qutiga kirish!
pip install "fastapi[standard]"    # qo'shtirnoq shart (zsh)
```

### Birinchi endpoint
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def qaytar():
    return {"habar": "Hello World"}
```
Ishga tushirish: `fastapi dev main.py` → `curl -v http://localhost:8000/` → **200** va `content-type: application/json`.

### `server3.py` va FastAPI
| | `server3.py` | FastAPI |
|---|---|---|
| Routing | `if self.path == "/..."` | `@app.get("/...")` |
| Javob | `self.javob_ber(200, ...)` | `return ...` |
| Format | `text/plain` | JSON — avtomatik |
| Status va header | o'zim yozardim | FastAPI o'zi qo'shadi |
