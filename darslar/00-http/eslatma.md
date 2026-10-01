# 00-HTTP Mavzusi boʻyicha Eslatma

## 1. Status kod guruhlari
HTTP status kodlari serverning soʻrovga qaytargan javob turi va holatini bildiradi:
* **2xx (Success):** Soʻrov muvaffaqiyatli qabul qilindi va bajarildi (Masalan: `200 OK`, `201 Created`).
* **4xx (Client Error):** Xato mijoz (brauzer yoki frontend) tomonidan boʻlgan. Soʻrov notoʻgʻri shakllantirilgan yoki resurs topilmagan (Masalan: `400 Bad Request`, `404 Not Found`).
* **5xx (Server Error):** Xato server tomonida boʻlgan. Frontend hamma narsani toʻgʻri yuborgan, lekin server kodi qulagan yoki serverda nosozlik bor (Masalan: `500 Internal Server Error`).

## 2. Muhim 8 ta HTTP Status Kodi
1. **200 OK** – Soʻrov muvaffaqiyatli bajarildi (Maʼlumotlar olindi yoki yangilandi).
2. **201 Created** – Yangi resurs (masalan, yangi foydalanuvchi yoki kitob) muvaffaqiyatli yaratildi.
3. **400 Bad Request** – Soʻrovda sintaktik xato bor (Frotend notoʻgʻri formatda maʼlumot yuborgan).
4. **401 Unauthorized** – Foydalanuvchi tizimdan oʻtmagan (Tizim uni tanimadi).
5. **403 Forbidden** – Foydalanuvchi tizimdan oʻtgan, lekin bu amalni bajarishga huquqi (ruxsati) yoʻq.
6. **404 Not Found** – Soʻralgan URL manzil yoki resurs serverda topilmadi.
7. **405 Method Not Allowed** – Endpoint mavjud, lekin bu metod (masalan, POST oʻrniga GET) u yerda ishlamaydi.
8. **500 Internal Server Error** – Server ichki xatoligi (Server kodida crash yoki bug bor).

## 3. 401 va 403 status kodlarining farqi
* **401 Unauthorized (Men kimman?):** Tizim sizning kimligingizni bilmaydi. Login qilishingiz shart.
* **403 Forbidden (Huquqim bormi?):** Tizim sizni taniydi (login qilgansiz), lekin bu eshikdan kirishga haqingiz yoʻq.

**Jonli misol:**
Siz universitet binosiga keldingiz.
* Agar yoningizda talabalik guvohnomangiz (ID-karta) boʻlmasa va qorovul sizni ichkariga kirgizmasa – bu **401 (Siz kimsiz? Identifikatsiya yoʻq)**.
* Agar guvohnomangizni koʻrsatib ichkariga kirdingiz, lekin rektorning xonasiga ruxsatsiz kirmoqchi boʻlganingizda sizni toʻxtatishsa – bu **403 (Siz talabasiz, tizim sizni tanidi, lekin rektor xonasiga kirishga haqingiz yoʻq)**.

## 4. Nega parolni faqat frontendda tekshirib boʻlmaydi?
Frontend (brauzer yoki mobil ilova) kodi toʻliqligicha foydalanuvchining kompyuterida ishlaydi. Bu shuni anglatadiki, yomon niyatli odam (haker) brauzer sozlamalarini (DevTools) ochib, frontenddagi tekshiruv kodlarini (JavaScript validatsiyalarini) osongina oʻchirib qoʻyishi yoki aylanib oʻtishi mumkin.

Bundan tashqari, xaker brauzersiz ham, toʻgʻridan-toʻgʻri API'ga (masalan, Postman yoki cURL orqali) notoʻgʻri parollarni cheksiz yuborishi mumkin.

### Bu qanday xavfsiz boʻladi?
Haqiqiy validatsiya har doim **backend (server) tomonda** boʻlishi shart:
1. Frontend parolni shunchaki foydalanuvchidan qabul qiladi va xavfsiz kanallar (HTTPS) orqali backendga yuboradi.
2. Backend parolni qabul qilib, maʼlumotlar bazasidagi (Database) maxfiy saqlangan xesh (hash) qilingan parol bilan solishtiradi.
3. Agar parol notoʻgʻri boʻlsa, backend brauzerga yuqoridagi **401 Unauthorized** kodini qaytaradi. Frontend kodini oʻzgartirish hakerga bazaga kirish imkonini bermaydi, chunki yakuniy nazorat backend qoʻlida boʻladi.

