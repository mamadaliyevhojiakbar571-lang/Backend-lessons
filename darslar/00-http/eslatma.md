1.Server bu - malumotlar saqlanadigon kampyuter yani javob qaytaradign mijoz esa nima sorashni aytadign brauzer yoki faoydalanuvchi 
2.bu 2 qismda iborat edi hop boshi nima qilishni qoraydi 2 chsi esa osha nimani nima qish kerailni aytadu masln birinchisiga    ochirishni olamz  va ikinxhiaiga kitobni
3 get - oqish post-yanig yartish , put/putch - ozgartish , delete ochirish 
4. GET /books 
   GET /books/1
   POST /books
   PUT /books/1
   DELETE /books/1
  2- qadam 
5. 1.Sttus kodida 2 bian bosjlamgnlar muvafaqiyatli ishlayapti degan manoni beradi 4 bilan boshlanganlar hato bizda ekanlgigini 5 bilan boshlanganlar esa serverda muammo ekanligni bildradi
6. 2. 200- muvafaqiyatli ishlayapti, 201- POST yangi foydalanuvchi muvafaqiyarli yaratildi , 204-bajarildi lekn qaytariadgn narsa yoq, 400 - sorvda hatolik yani bizni soraovda 401-foydalanuchchi royhatdan otmagan 403-Foydalanuvchi tizimdan oʻtgan, lekin bu amalni bajarishga huquqi  yoʻq, 404-bunday narsa yoq yani serverda toplmadi 500 serverda hatilk 
7. 3. 401 bilan 403 ni farqi shundaki misol tariqasida bitta saytni olaylik biz unda yanig foydalnuvchimiz tabiyki bizda login bolmaydi royhatdan otish kerak boladi va 401 biz royhatdan otmagan bolsak sen royhatdan otmagasn deb bildradi hop royhtdan otgandan keyin biz oddiy foydlanuchi bolamiz lekin biz admin panellga kirmoqchimiz 403 esa oshani oldini oladi yani sen foydaluvxhisna lekin kira olmaysan yani amal baajrilmaydi yoki saytdan nimadr ochirmoqchi blsak bomaydi 
8. 4. Frontenda parlni tekshirb bolmaslkdan sabab chunki curl orqali terminlda serverga sorav yuborish mumkin forntenda esa tugmalar boladi lekin uni aylanib otish mumkin    
      ya       