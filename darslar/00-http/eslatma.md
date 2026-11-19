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

## 10-dars · 9–23-oktyabr — SQL asoslari

### Baza, jadval, ustun va qator
- **Baza** — jadvallar to'plami. Bitta `mashq.db` faylida bir nechta jadval bo'lishi mumkin: `royhat` va `ustozlar` (`.tables` bilan tekshirildi)
- **Jadval** — bitta mavzu bo'yicha ma'lumotlar (masalan, talabalar ro'yxati yoki oylik chiqim). Talabalar bir jadvalda, ustozlar boshqasida
- **Ustun** — ma'lumotlarni guruhlaydi: `ismi`, `yoshi`. Tepadan pastga qarab hammaning yoshini ushlaydi
- **Qator** — bitta narsa (foydalanuvchi, xodim, vazifa) haqidagi barcha ustunlardagi ma'lumot

📓 Baza — daftar, jadval — uning bir sahifasi.

### PRIMARY KEY va NOT NULL
```sql
CREATE TABLE ustozlar (id INTEGER PRIMARY KEY, ismi TEXT NOT NULL, fan TEXT);
```
- **`PRIMARY KEY`** — har bir qatorning **takrorlanmas** raqami. `id` yozilmasa, baza o'zi beradi (Soliha → `1`).
  Band raqam berilsa: `UNIQUE constraint failed: ustozlar.id`
- **`NOT NULL`** — bu ustunni bo'sh qoldirib bo'lmaydi.
  Ismsiz ustoz qo'shilsa: `NOT NULL constraint failed: ustozlar.ismi`

### `.tables` va `DROP TABLE`
- `.tables` — bazadagi jadvallarni ko'rsatadi
- `DROP TABLE` — jadvalning ichidagi qatorlarni ham, **o'zini ham** o'chiradi
- **Nega xavfli:** o'chirilgan jadvalni **qaytarib bo'lmaydi** — savatcha yo'q 🗑️

### Jim xato 🤫
**Jim xato** — xato chiqmaydi, lekin natija noto'g'ri bo'ladi.
- **Qizil xato:** `IMTO` (`INTO` o'rniga) → baza darrov `Parse error` chiqardi 🔴
- **Jim xato, 1-misol:** `ORDER BY yoshi` da `DESC` unutildi → xato yo'q, lekin tartib teskari chiqdi
- **Jim xato, 2-misol:** `ismi == 'Umid' OR 'Asilbek'` — chala shart → xato yo'q, natija noto'g'ri

Xato xabaridagi `near "..."` va `^---` xato **qayerdaligini** ko'rsatadi (`IMTO`, ko'rinmas belgi `�`).
Hech narsa chiqmasa — buyruq umuman **ishga tushmagan**; qizil xato chiqsa — baza o'qidi, lekin **rad etdi**.

### WHERE ning 3 qismi
```sql
WHERE yoshi > 18
```
**USTUN** (`yoshi`) · **BELGI** (`>`) · **QIYMAT** (`18`)

### AND va OR
- `AND` — ikkala shart ham to'g'ri bo'lsa bajariladi
- `OR` — bittasi to'g'ri bo'lsa yetarli

### ORDER BY, DESC, LIMIT
- `ORDER BY` — kichikdan kattaga tartiblaydi
- `DESC` — kattadan kichikka
- `LIMIT` — nechta qator chiqishini belgilaydi
- **Yozilish tartibi:** `WHERE` → `ORDER BY` → `LIMIT`

```sql
SELECT * FROM royhat WHERE yoshi > 18 ORDER BY yoshi DESC LIMIT 2;
```

### Teng qiymatlar tartibiga nega ishonib bo'lmaydi?
Umar, Sanjar va G'ayrat — uchalasi 19 yoshda. `ORDER BY yoshi` da ularning o'zaro tartibini biz **aytmaganmiz**,
shuning uchun baza buni **kafolatlamaydi**: bugun birinchi qo'shilgani chiqdi, ertaga boshqacha chiqishi mumkin.

Yechim — ikkinchi ustun qo'shish: `ORDER BY yoshi, ismi` → yoshi teng bo'lsa, ismi bo'yicha 🔒

## 11-dars · 28 va 30-oktyabr — UPDATE

### UPDATE nima qiladi? INSERT dan farqi nima?
- `UPDATE` — **bor** qatordagi qiymatni o'zgartiradi → qatorlar soni o'zgarmaydi (3 → 3)
- `INSERT` — **yangi** qator qo'shadi → qatorlar soni ortadi (3 → 4)

### Yozilish qoidasi — 3 qism
```sql
UPDATE ustozlar SET fan = 'Kimyo' WHERE id = 3;
```
| Qism | Bazaga nima deydi |
|---|---|
| `UPDATE ustozlar` | qaysi jadval |
| `SET fan = 'Kimyo'` | nimani nimaga o'zgartirish |
| `WHERE id = 3` | qaysi qatorni |

O'zgartirishdan **oldin** ma'lumotga qarash kerak: Soliha allaqachon `Ingliz tili` edi —
uni yana `Ingliz tili` qiladigan `UPDATE` hech narsani o'zgartirmas edi.

### Nega WHERE da `ismi` emas, `id` ishlatish kerak? (Dilnoza tajribasi)
- Jadvalda 2 ta Dilnoza bor edi → `WHERE ismi = 'Dilnoza'` **ikkalasini ham** o'zgartirdi 🪤
- `ismi` takrorlanishi mumkin, `id` esa **takrorlanmaydi** → `WHERE id = ...` doim **bitta** qatorni topadi

### Bir nechta ustunni / bir nechta qatorni qanday o'zgartirasiz?
```sql
-- bir nechta ustun: SET ichida vergul bilan
UPDATE ustozlar SET ismi = 'Zarina', fan = 'Fizika' WHERE id = 3;

-- bir nechta qator: OR yoki IN
UPDATE ustozlar SET fan = 'Tarix' WHERE id = 1 OR id = 2;
UPDATE ustozlar SET fan = 'Tarix' WHERE id IN (1, 2);
```
SQL katta-kichik harfni farqlamaydi (`or` ham ishlaydi), lekin buyruq so'zlari odatda **KATTA** yoziladi —
shunda buyruq qayerda, ma'lumot qayerda ekani darrov ko'rinadi.

### Jim xato (28-oktyabr)
- Soliha'ning fanini o'zgartirganda `'Ingiliz tili'` deb yozildi — **imlo xatosi**
- SQLite **xato chiqarmadi**: u matnning imlosini tekshirmaydi → bazaga noto'g'ri ma'lumot yozildi 🤫
- `SELECT` bilan tekshirib o'zim topdim va yana `UPDATE` bilan tuzatdim

## 12-dars · 2-noyabr — DELETE

### CRUD — backend'dagi 4 ta amal
| Harf | Ma'nosi | SQL |
|---|---|---|
| **C** | Create — yaratish | `INSERT` |
| **R** | Read — o'qish | `SELECT` |
| **U** | Update — o'zgartirish | `UPDATE` |
| **D** | Delete — o'chirish | `DELETE` |

### Yozilishi
```sql
DELETE FROM ustozlar WHERE id = 3;
```
- `SET` kerak emas: `DELETE` bitta ustunni emas, **butun qatorni** o'chiradi — "nimani nimaga" yo'q,
  faqat **qaysi qator** (`WHERE id = ...`)
- `WHERE` da `ismi` ham ishlaydi, lekin Dilnoza tuzog'i 🪤 — `DELETE` da bu yanada og'ir:
  o'zgartirilgan qatorni tuzatsa bo'ladi, o'chirilganini **qaytarib bo'lmaydi** 🗑️

### WHERE siz DELETE ⚠️
```sql
DELETE FROM ustozlar;
```
- **Hamma** qatorlar o'chadi, jadvalning o'zi qoladi (`.tables` da bor, `SELECT` bo'sh)
- SQLite **"Ishonchingiz komilmi?"** deb so'ramaydi — bitta `Enter`, hammasi ketdi

### Avval SELECT, keyin DELETE 🛡️
```sql
SELECT * FROM ustozlar WHERE id = 3;   -- 1) kimni o'chirayotganimni ko'raman
DELETE FROM ustozlar WHERE id = 3;     -- 2) xuddi o'sha WHERE bilan o'chiraman
```
**Nega:** noto'g'ri qatorni o'chirib yubormaslik uchun.

### DELETE va DROP farqi 📚
Jadval — kitob javoni, qatorlar — kitoblar.

| Buyruq | Kitoblar (qatorlar) | Javon (jadval) |
|---|---|---|
| `DELETE FROM ustozlar;` | ketadi | **qoladi** |
| `DROP TABLE ustozlar;` | ketadi | **ketadi** |

### O'chirilgandan keyin yangi id qanday beriladi?
- SQLite: **yangi id = jadvaldagi eng katta id + 1**. Jadval bo'sh edi → Soliha `1` oldi (men `4` deb o'ylagandim)
- PostgreSQL ishlatilgan raqamlarni eslab qoladi → u `4` bergan bo'lardi

### Bitta INSERT bilan bir nechta qator
```sql
INSERT INTO ustozlar (ismi, fan) VALUES ('Dilnoza', 'Matematika'), ('Aziza', 'Fizika');
```
Har bir qator — o'z qavsida, qavslar orasida vergul.

### Bugungi qizil xato 🔴
```sql
UPDATE ustozlar DELETE WHERE id = 3;
```
`Parse error: near "DELETE"` — `UPDATE` ichiga `DELETE` yozdim. `UPDATE ustozlar` dan keyin SQLite doim `SET` kutadi.
`DELETE` — `UPDATE` ning bir qismi emas, **alohida buyruq**: `DELETE FROM jadval WHERE ...`

## 13-dars · 16–18-noyabr — FOREIGN KEY

### FOREIGN KEY nima?
**FOREIGN KEY** (begona kalit) — boshqa jadvalning `PRIMARY KEY` ini saqlaydigan ustun.
Uni jadval eshigi oldidagi **qorovul** deb tasavvur qilsa bo'ladi 💂 Uning ikkita vazifasi bor:

1. **Bog'laydi** — ustun qaysi jadvalga ishora qilishini ko'rsatadi 📎
2. **Tekshiradi** — jadvalga kiritilayotgan ma'lumotni tekshiradi: ota jadvalda yo'q qiymatni kiritmaydi

### Yetim qator 👻
Boshqa jadvalda **mavjud bo'lmagan** qatorga ishora qiladigan qator.

Misol: `bookings` jadvalida `pitch_id = 99`, lekin `pitches` jadvalida 99-maydon **yo'q** — o'yinchi
mavjud bo'lmagan maydonni bron qilib qo'ygan bo'ladi ⚽ Bu katta xato, shuning uchun uni tekshirish kerak — buni FOREIGN KEY qiladi.

### Yozilishi
```sql
CREATE TABLE guruhlar(
    id INTEGER PRIMARY KEY,
    nomi TEXT NOT NULL,
    ustoz_id INTEGER NOT NULL,
    FOREIGN KEY (ustoz_id) REFERENCES ustozlar(id)
);
```
| Qism | Ma'nosi |
|---|---|
| `FOREIGN KEY (ustoz_id)` | **bu yoqdagi** ustun — shu jadvaldan |
| `REFERENCES ustozlar` | **u yoqdagi** jadval |
| `(id)` | u yoqdagi jadvalning ustuni |

Bitta gap bilan: bu yoqdagi `ustoz_id` u yoqdagi `ustozlar` jadvalining `id` siga murojaat qiladi — `ustoz_id → ustozlar.id`.
`FOREIGN KEY` ustunlardan **keyin**, vergul bilan yoziladi.

### Nega `ustoz_id` — `PRIMARY KEY` emas?
Bitta ustoz bir nechta guruhga dars berishi mumkin → `ustoz_id` da bir xil son (masalan, `1`) ikki marta yoziladi.
`PRIMARY KEY` esa **takrorlanmaydi** → `UNIQUE constraint failed`. Shuning uchun `ustoz_id` — oddiy `INTEGER NOT NULL`.

### ⚠️ SQLite'da FOREIGN KEY o'zi ishlamaydi — uni yoqish kerak
```sql
PRAGMA foreign_keys = ON;
```
- Yoqilmasa, jadval FOREIGN KEY yozilgan bo'lsa ham yetim qatorni **qabul qilaveradi** 😈
- `.quit` bilan chiqib ketilsa, keyingi safar **yana yoqish** kerak

Tajribam (`ustozlar` da faqat 1, 2, 3-id lar bor):

| Holat | Natija |
|---|---|
| `ustoz_id = 7`, `PRAGMA` siz | qabul qilindi — yetim qator kirdi 👻 |
| `PRAGMA foreign_keys = ON;` dan keyin `ustoz_id = 8` | `FOREIGN KEY constraint failed` 💂 |

Yoqishdan oldin kirib olgan yetim qator jadvalda qolgan edi — uni o'zim o'chirdim:
```sql
DELETE FROM guruhlar WHERE id = 1;
```

### Loyihada (pitch-booking)
```
owner_id    → users.id
customer_id → users.id
pitch_id    → pitches.id
```
Shu uchta strelka `schema.sql` da uchta FOREIGN KEY bo'ldi.

### Xatolarim
| Xato | To'g'risi |
|---|---|
| `REFERENCES ustozlar(ustozlar_id)` — bunday ustun yo'q, lekin SQLite `CREATE` da xato bermadi | `ustozlar(id)` |
| `)` va `;` ni unutdim → terminal `...>` da kutib qoldi | buyruq oxirida `);` |
| `INSERT INTO guruhlar(nom, ...)` → `has no column named nom` | ustun nomi — `nomi` |
| jadvalni `.schema` bilan ko'rmasdan `DROP` qildim → ustunlarini eslay olmadim | avval `.schema`, keyin `DROP` |
| "FOREIGN KEY bor — demak xato chiqadi" deb o'yladim | SQLite'da avval `PRAGMA foreign_keys = ON;` |
| `phone INTEGER` — boshidagi `0` yo'qoladi | `phone TEXT` |
| commit: "users jadvali**ga** qo'shildi" — bitta qo'shimcha ma'noni o'zgartirdi | "users jadvali qo'shildi" |

## 14-dars · 18–19-noyabr — Python'dan SQLite va SQL injection

### Python'dan bazaga ulanish — 4 qadam
`sqlite3` Python'ning ichida bor — `pip install` shart emas.
```
connect → execute → fetchall → close
```
```python
import sqlite3
ulanish = sqlite3.connect('mashq.db')                  # 1. ulanish
natija = ulanish.execute("SELECT * FROM ustozlar")     # 2. buyruq yuborish
qatorlar = natija.fetchall()                           # 3. javobni olish
for raqam, ismi, fan in qatorlar:
    print(f"{raqam} - {ismi} - {fan}")
ulanish.close()                                        # 4. yopish
```
- `fetchall()` **tuple'lar ro'yxati**ni qaytaradi: `[(1, 'Soliha', 'Ingliz tili'), (2, 'Dilnoza', 'Matematika'), ...]`
- `qatorlar[1][2]` → 2-qatorning 3-ustuni → `'Matematika'` (indeks 0 dan boshlanadi)
- `for raqam, ismi, fan in qatorlar:` — tuple'ni ochish: `qator[0]`, `qator[1]` kabi "sehrli raqamlar" o'rniga nomlar

### SQL injection 😈
Xaker formaga **tirnoqni yopib, OR qo'shadi** va bazaga ruxsatsiz kiradi.
```python
qidiruv = "x' OR '1'='1"
f"SELECT * FROM ustozlar WHERE fan = '{qidiruv}'"
# → SELECT * FROM ustozlar WHERE fan = 'x' OR '1'='1'
```
`'1'='1'` — **doim rost**. `OR` tufayli shart har bir qator uchun rost bo'ladi → **hamma ustoz chiqdi**.
Teshik — **tirnoqning yopilishi**: foydalanuvchi yozgan ma'lumot buyruqqa aylanib qoladi.

JavaScript'dagi `innerHTML` bilan bir xil g'oya — u yerda **XSS** deyiladi. Ikkalasi ham *injection* oilasidan.

### Himoya: `?` — xavfsiz bo'sh joy 🛡️
```python
natija = ulanish.execute("SELECT * FROM ustozlar WHERE fan = ?", (qidiruv,))
```
- `?` ning ichiga nima tushsa ham — **matn** bo'lib qoladi, buyruq emas
- `fan = ?` da **tirnoq yo'q** — xakerga yopadigan narsa qolmaydi
- `?` lar **tartib bilan** to'ldiriladi: `"... fan = ? AND ismi = ?", (qidiruv, ism)`

| Kiritilgan | f-string | `?` |
|---|---|---|
| `Fizika` | `3 - Aziza - Fizika` | `3 - Aziza - Fizika` |
| `x' OR '1'='1` | 😈 hamma ustoz | 🛡️ hech kim (bunday fan yo'q) |

### Vergul nega kerak — `(qidiruv,)`
Vergulsiz tuple bo'lmaydi. `(5)` — shunchaki `5`, `(5,)` — tuple.
Vergulsiz `(qidiruv)` → so'zning o'zi ketadi va **harfma-harf** bo'linadi:
```
Incorrect number of bindings supplied. The current statement uses 1, and there are 10 supplied.
```
`"Matematika"` — 10 ta harf = 10 ta qiymat 😄

### Qidiruv sikli (o'z g'oyam)
`input` + `while` bilan: fan kiritiladi → ustozlar chiqadi → "Yana qidirishni xohlaysizmi?"
- `input()` **doim `str`** qaytaradi — `5` yozilsa ham `'5'` keladi (`type()` bilan tekshirdim: `<class 'str'>`)
- `.strip()` — boshi va oxiridagi probellarni olib tashlaydi (JS'dagi `.trim()`)
- `.lower()` — kichik harfga o'tkazadi (JS'dagi `.toLowerCase()`) → `Ha`, `HA` ham ishlaydi
- `if qatorlar:` — bo'sh ro'yxat **yolg'on** → "topilmadi"

### Xatolarim
| Xato | To'g'risi |
|---|---|
| `import sqlite3` ni yozmadim → `NameError` | fayl boshida `import sqlite3` |
| `close()` tushib qoldi | oxirida `ulanish.close()` |
| `'qidiruv'` — `f` va `{}` siz, jim xato: `qidiruv` degan so'zni qidirdi | `f"... '{qidiruv}'"` (lekin xavfsizi — `?`) |
| `(qidiruv)` — vergulsiz → `10 supplied` | `(qidiruv,)` |
| `str(input(...))` — "input int qaytaradi" deb o'yladim | `input()` o'zi `str` |
| `.strip()` ni boshqa `input` ga qo'ydim → `"  HA "` ishlamadi | ikkalasiga: `.strip().lower()` |
| `AM` — PyCharm bo'sh faylni o'zi add qilgan, kod surati eskirgan | kod tugagach yana `git add baza.py` |

## 15-dars · 19-noyabr — Python'dan INSERT va commit()

### INSERT — `?` bilan
```python
ulanish.execute("INSERT INTO ustozlar(ismi, fan) VALUES (?, ?)", (ism, fan))
```
- 1-juft — **ustun nomlari**, 2-juft — **qiymatlar**. Tartib bir xil: 1-ustunga 1-qiymat
- `id` yozilmaydi — `PRIMARY KEY` o'zi beradi
- Qiymatni o'zim yozsam ham — **doim `?`**: ertaga u `input()` dan keladi

### `commit()` — saqlash 💾
`commit()` saqlash vazifasini bajaradi, `close()` esa yopadi. Shuning uchun `commit()` **`close()` dan oldin** yoziladi.
```
INSERT    → ✏️ qoralama (Python ko'radi, bazada yo'q)
commit()  → 💾 saqlash (Word'dagi Cmd+S)
close()   → 🔒 yopish — saqlanmagan qoralama o'chadi 🗑️
```
Tajribam — `close()` dan **keyin** `commit()`:

| Qayerda | Natija |
|---|---|
| Python ekranida | `5 - Bekzod` — **bor** 👻 |
| 9-qator `commit()` | `Cannot operate on a closed database` |
| `sqlite3 mashq.db` | 5-qator **yo'q** — saqlanmagan |

- `commit()` kerak: `INSERT`, `UPDATE`, `DELETE` — CRUD'ning **C, U, D**
- `SELECT` (**R**) uchun kerak emas — u faqat o'qiydi
- **git commit** ham xuddi shu g'oya: "o'zgarishlarni saqlab qo'y"

### NULL, `""` va 0 — uch xil narsa
| | Ma'nosi | `NOT NULL` |
|---|---|---|
| `NULL` | noma'lum — katakcha **bo'sh turibdi**, hech narsa yo'q 📭 | to'xtatadi 🛑 |
| `""` | **bo'sh matn** — matn bor, uzunligi 0 📦 | o'tkazib yuboradi 🤷 |
| `0` | **raqam** | o'tkazib yuboradi |

Shuning uchun bo'sh kiritishni **Python'da** tekshiraman — bo'sh matn **yolg'on**:
```python
if not ism or not fan:
    print("Xatolik: Ism yoki fan bo'sh bo'lishi mumkin emas!")
```

### Iflos ma'lumot 🧹
Bitta fan bazada har xil yozilsa — `Ingliz tili` va `ingiliz-tili` — `"Ingliz tili"` deb qidirganda ikkinchisi **chiqmaydi**.
Yangi qiymat bazadagi yozilishga mos bo'lishi kerak.

### Ustoz qo'shish formasi (o'z g'oyam)
`qoshish.py`: `while` ichida ism + fan kiritiladi → bo'sh emasligi tekshiriladi → `INSERT` + `commit()` → ro'yxat chiqadi.
`for raqam, ismi, fan_nomi in natija:` — `fan` emas, chunki tepada `fan` o'zgaruvchisi bor, sikl uni **ustidan yozib** yuborardi.

### Xatolarim
| Xato | To'g'risi |
|---|---|
| qiymatlarni SQL matnining ichiga yozdim | `VALUES (?, ?)` + tuple |
| `'ingiliz-tili'` — bazada `Ingliz tili` | bazadagi yozilishga moslash |
| `SELECT ... WHERE fan = ?", ()` — hamma qator kerak edi | `"SELECT * FROM ustozlar"` — `WHERE` yo'q → `?` yo'q → tuple yo'q |
| `close()` dan keyin `commit()` → saqlanmadi | avval `commit()`, keyin `close()` |
| bo'sh Enter → ismsiz "arvoh" ustoz kirdi | `if not ism or not fan:` |
| `""` = 0 deb o'yladim | `""` — bo'sh matn, 0 — raqam |
| "commit CRUD uchun" — lekin R (`SELECT`) ga kerak emas | `commit()` — C, U, D uchun |
