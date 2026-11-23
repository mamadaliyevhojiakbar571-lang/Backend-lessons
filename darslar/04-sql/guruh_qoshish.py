import sqlite3
ulanish = sqlite3.connect("mashq.db")
ulanish.execute("PRAGMA foreign_keys = ON")
guruh_nomi = "A guruh"
ustoz_id = 70
try:
    ulanish.execute("INSERT INTO guruhlar(nomi, ustoz_id) VALUES (?, ?)", (guruh_nomi, ustoz_id))
    ulanish.commit()
    print(" Muvaffaqiyatli qo'shildi")
except sqlite3.IntegrityError:
    print(f"ID si {ustoz_id} bo'lgan ustoz bazada yo'q")

ulanish.close()

