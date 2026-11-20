import sqlite3

ulanish = sqlite3.connect("mashq.db")
davom_etish = True

while davom_etish:
    ism = input("Ustoz ismini kiriting: ").strip()
    fan = input("Fan nomini kiriting: ").strip()

    if not ism or not fan:
        print("Xatolik: Ism yoki fan bo'sh bo'lishi mumkin emas!")
    else:
        ulanish.execute("INSERT INTO ustozlar(ismi, fan) VALUES (?, ?)", (ism, fan))
        ulanish.commit()
        print("Muvaffaqiyatli qo'shildi!")

        natija = ulanish.execute("SELECT * FROM ustozlar").fetchall()
        print("\n--- Yangilangan ro'yxat ---")

        for raqam, ismi, fan_nomi in natija:
            print(f"{raqam} - {ismi} - {fan_nomi}")

    sorov = input("\nYana ustoz qo'shasizmi? (ha/yo'q): ").strip().lower()
    if sorov != "ha":
        davom_etish = False

ulanish.close()
