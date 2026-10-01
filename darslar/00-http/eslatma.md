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
