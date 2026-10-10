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

## 7-dars · 4-oktyabr — FastAPI: endpointlar

### `FastAPI` va `FastAPI()`
- **`FastAPI`** — qolip (kutubxonadan tayyor keladi)
- **`FastAPI()`** — qolipdan bitta ilova yasash 🍪 → `app = FastAPI()`

### `@app.get("/tasks")` qismlari
| Qism | Ma'nosi |
|---|---|
| `@` | yorliq belgisi 🏷️ |
| `app` | ilova nomi |
| `.get` | GET metodi |
| `"/tasks"` | yo'l (path) |

### Endpoint
Ilovadagi bitta "manzil": **metod + yo'l + javob beruvchi funksiya**. Masalan: `GET /tasks → tasks()`.
Restoranda — menyudagi bitta taom 🍽️

### Nega FastAPI'da funksiya nomi ixtiyoriy?
- `http.server` funksiyani **ismi bo'yicha** qidirardi — shuning uchun `do_GET` nomi shart edi
- FastAPI esa **yorlig'i bo'yicha** topadi — nom muhim emas (lekin ma'noli bo'lsin)

### Nechta ilova kerak?
3 ta endpoint uchun **1 ta ilova** yetarli — bitta restoran, menyuda ko'p taom.

### Python → JSON
| Python | JSON | Belgisi |
|---|---|---|
| `list` | massiv | `[ ]` |
| `dict` | obyekt | `{ }` |

React uchun qulay: massivni darhol `.map()` qilib `<li>` larga aylantirish mumkin.

### 404 va 500
- Mavjud bo'lmagan yo'l (`/salom`) → **404** `{"detail":"Not Found"}` — FastAPI o'zi qaytaradi (mijoz xatosi)
- Kodda xato (masalan, `1/0`) → **500** (server xatosi)

### `/docs`
FastAPI avtomatik yaratadigan sahifa: barcha endpointlarni brauzerda ko'rib, sinab ko'rish mumkin.

## 8-dars · 5-oktyabr — Yo'l parametrlari va 404

### Git: tekshirish va tuzatish
| Buyruq | Nima qiladi |
|---|---|
| `git status` | **qaysi** fayllar o'zgarganini ko'rsatadi |
| `git diff` | fayl **ichida** nima o'zgarganini ko'rsatadi (qizil `-` eski, yashil `+` yangi) |
| `git restore fayl` | faylni oxirgi commitdagi holatiga qaytaradi |

Bugun `git diff` tasodifan buzilgan qatorni topdi (`http.server` → `http.servr`), `git restore` uni tuzatdi.
**Qoida:** commitga faqat ataylab qilingan o'zgarishlar tushishi kerak.

### Yo'l parametri `{task_id}`
```python
@app.get("/tasks/{task_id}")
def task(task_id: int):
    if task_id < 0 or task_id >= len(vazifalar):
        raise HTTPException(status_code=404, detail="Vazifa topilmadi")
    return {"vazifa": vazifalar[task_id]}
```
- `{task_id}` — yo'ldagi bo'sh joy: raqamni **mijoz** yozadi (`/tasks/1` → `task_id = 1`)
- Shuning uchun **bitta** endpoint hamma vazifalarga xizmat qiladi
- `vazifalar[task_id]` — ro'yxatdan o'sha raqamdagi elementni oladi

### Type hint `: int`
- URL — matn: `/tasks/0` dan `"0"` (str) keladi, ro'yxatga esa `0` (int) kerak
- `: int` yozilmasa → `vazifa
- lar["0"]` → **500** (`TypeError`)
- `: int` yozilsa → FastAPI matnni songa aylantiradi; `/tasks/abc` → **422** (yaroqsiz ma'lumot)

### 404 va `HTTPException`
- `: int` faqat **turni** tekshiradi, **mavjudlikni** emas: `/tasks/99` → `IndexError` → **500**
- Mavjud bo'lmagan narsa — mijoz xatosi → **404** bo'lishi kerak
- `raise HTTPException(...)` funksiyani shu yerda to'xtatadi va mijozga to'g'ri status qaytaradi
- `task_id < 0` ham tekshiriladi: manfiy son ro'yxatni oxiridan sanaydi (`vazifalar[-1]` — oxirgisi)

### Endpoint funksiyasi nima qiladi?
**Qabul qiladi → tekshiradi → topib qaytaradi.**

## 9-dars · 6–8-oktyabr — POST, Pydantic va RAM

### Yangi vazifa qayerda keladi?
Konvertning ichida — **body**da: `{"nomi": "Referat yozish"}`.
Yo'l esa faqat **qaysi to'plam** ekanini ko'rsatadi: `POST /tasks`.

### Anketa — Pydantic modeli
```python
class VazifaYarat(BaseModel):
    nomi: str
```
- `BaseModel` dan **meros** oladi
- Body qanday ko'rinishda bo'lishi kerakligini aytadi: qaysi maydon (`nomi`) va qaysi turda (`str`)
- Mos kelmasa (masalan, `nomi` o'rniga `ism`) — **422** "Field required"

### POST endpoint va 201
```python
@app.post("/tasks", status_code=201)
def vazifa_qosh(vazifa: VazifaYarat):
    vazifalar.append(vazifa.nomi)
    return {"id": len(vazifalar) - 1, "nomi": vazifa.nomi}
```
- **201** — yangi narsa yaratildi; u **yorliqda** yoziladi (`raise` — faqat xatolar uchun)
- `curl -X POST` — mijoz tomoni (qaysi metod bilan so'rayapti), `status_code=201` — server tomoni (qaysi kod bilan javob beradi)

### ID ni kim beradi? 🧾
| | Kim beradi | Misol |
|---|---|---|
| `GET /tasks/7` | **mijoz** — URL'ga o'zi yozadi | "menga 7-sini ber" |
| `POST /tasks` | **server** — yangi raqam beradi | javob: `{"id": 7, ...}` |

Bank navbati kabi: chipta raqamini apparat beradi (POST), keyin o'sha raqamni o'zing ko'rsatasan (GET).

### `len(vazifalar) - 1` nega `append` dan keyin?
Javob qilinayotgan ishning tartibiga bog'liq: `append` dan keyin ro'yxatning haqiqiy uzunligi kelib chiqadi, yangi element esa oxirgi indeksda turadi (`len - 1`). Agar `append` dan oldin sanalsa — `- 1` kerak emas.

### Nega server qayta ishga tushganda vazifalar yo'qoldi?
Server ma'lumotlarni kompyuterning **RAM**ida saqlab turadi. Server to'xtab, qayta yonganda RAM ham yangilanadi — hamma ma'lumot o'chib ketadi.
Shuning uchun ma'lumotni **SQL**, ya'ni **ma'lumotlar bazasi**da (diskda) saqlash kerak.
- RAM — sinf doskasi 🧑‍🏫 (tez, lekin o'chiriladi)
- Disk / baza — daftar 📓 (yozilgani qoladi)
