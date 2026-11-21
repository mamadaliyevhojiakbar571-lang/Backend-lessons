import sqlite3
ulanish = sqlite3.connect("mashq.db")
yangi_fan = "Psixologiya"
ustoz_id = 7
kursor = ulanish.execute("UPDATE ustozlar SET fan = ? WHERE id = ?", (yangi_fan, ustoz_id))
ulanish.commit()

if kursor.rowcount == 0:
    print(f"Xatolik: ID={ustoz_id} bo'lgan ustoz bazada topilmadi!")
else:
    print(f"Muvaffaqiyatli! {kursor.rowcount} ta qator yangilandi.")
    natija = ulanish.execute("SELECT * FROM ustozlar").fetchall()
    for raqam, ism, fan in natija:
        print(f"{raqam} - {ism} - {fan}")

ulanish.close()

