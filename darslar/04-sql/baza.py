import sqlite3
qidir = True
ulanish = sqlite3.connect('mashq.db')
while qidir:
    qidiruv = input("Fanni kiriting: ").strip()
    natija = ulanish.execute("SELECT * FROM ustozlar WHERE fan = ?", (qidiruv,))
    qatorlar = natija.fetchall()
    if qatorlar:
        for raqam, ismi, fan in qatorlar:
            print(f"{raqam} - {ismi} - {fan}")
    else:
        print("Bunday fan bo'yicha ustoz topilmadi")

    sorov = input("Yana qidirishni hohlaysizmi?: ").lower().strip()
    if sorov != "ha":
        qidir = False

ulanish.close()

