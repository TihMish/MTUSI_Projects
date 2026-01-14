# D08T05. Dinamik xotira va matritsalar

Annotatsiya: ushbu loyiha sizga xotiraning dinamik taqsimoti, matritsalar va ularni qayta ishlash algoritmlari bilan tanishish imkonini beradi.

## Contents 

1. [Kirish](#kirish) \
    1.1. [Loyihaga tavsiyalar](#loyihaga-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 2. Room 3](#level-2-room-3)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1](#list-1) \
    3.2. [List 2](#list-2)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. Allocate memory first...](#quest-1-allocate-memory-first) \
    4.2. [Quest 2. Try not to leak then](#quest-2-try-not-to-leak-then) \
    4.3. [Quest 3. The 1+3 ways](#quest-3-the-13-ways) \
    4.4. [Quest 4. MinMax search](#quest-4-minmax-search) \
    4.5. [Quest 5. Making a picture](#quest-5-making-a-picture) \
    4.6. [Quest 6. Matrix arithmetic](#quest-6-matrix-arithmetic) \
    4.7. [Quest 7. The Magic Key](#quest-7-the-magic-key)
5. [Chapter IV](#chapter-iv)
6. [Chapter V](#chapter-v) \
    6.1. [Level 2. Room 4](#level-2-room-4)
7. [Chapter VI](#chapter-vi) \
    7.1. [List 1](#list-1-1) \
    7.2. [List 2](#list-2-1)
8. [Chapter VII](#chapter-vii) \
    8.1. [Bonus Quest 8. An old friend](#bonus-quest-8-an-old-friend) \
    8.2. [Bonus Quest 9. Decision](#bonus-quest-9-decision)
9. [Chapter VIII](#chapter-viii)


## Kirish
### Loyihaga tavsiyalar
"School 21" da qanday ta'lim olish mumkin:  
- Butun kurs davomida siz mustaqil ravishda ma'lumot izlab topasiz. Google va GigaChat kabi barcha mavjud axborot qidiruv vositalaridan foydalaning. Axborot manbalariga e'tiborli bo'ling: tekshiring, o'ylang, tahlil qiling, taqqoslang.
- O'zaro o'rganish (P2P, Peer-to-Peer) - bu o'quvchilar bir vaqtning o'zida ham o'qituvchi, ham o'quvchi sifatida bilim va tajriba almashadigan jarayondir. Bunday yondashuv nafaqat o'qituvchidan, balki bir-biridan ham o'rganish imkonini beradi, bu esa materialni chuqurroq tushunishga yordam beradi.
- Yordam so'rashdan tortinmang: atrofingizdagilarning bari tengdoshlaringiz, ular ham bu yo'lni birinchi marta bosib o'tishmoqda. Yordam so'rashganda javob berishdan qo'rqmang. Sizning tajribangiz qimmatli va foydali, uni boshqa ishtirokchilar bilan bemalol baham ko'ring.
- Ko'chirmang, agar yordamdan foydalansangiz - har doim nega, qanday va nima uchun ekanligini oxirigacha tushunib oling. Aks holda sizning o'qishingiz hech qanday ma'noga ega bo'lmaydi.
- Agar biror narsada to'xtab qolsangiz va hamma narsa allaqachon sinab ko'rilgandek tuyulsa-yu, lekin qanday yo'l tutishni baribir bilmayotgan bo'lsangiz - shunchaki nafas rostlang! Ishoning, bu maslahat ko'plab dasturchilarga ishlarida yordam bergan. Havo almashtiring, miyangizni qayta ishga tushiring va, ehtimol, keyingi safar nihoyat kerakli yechim toparsiz!
- Nafaqat ta'lim natijasi, balki jarayonning o'zi ham muhimdir. Masalani shunchaki yechish emas, balki uni QANDAY yechishni tushunish kerak.
- Loyihani bajarishda vaqtni kuzatib boring. Kuniga kamida bitta sinovdan o'tishingiz kerak.
- Yodda tutingki, har bir topshiriq loyiha yakunida bir qator tekshiruvlardan o'tadi: p2p- chek listi yordamida tekshirish, avtotestlar to'plami bilan tekshirish, kod uslubini tekshirish, statik analizator bilan tekshirish, xotira bilan to'g'ri ishlashni tekshirish.

Loyihada qanday ishlash kerak:
- Foydali videomateriallarni Platformadagi Projects (Media) bo'limidan topishingiz mumkin.
- Loyihani bajarishdan oldin uni GitLab dan bir xil nomdagi repozitoriyga klonlash kerak.
- Barcha kodli fayllarni src/ klonlangan repozitoriy papkasida yaratish zarur.
- Loyihani klonlashtirgandan so'ng, develop tarmog'ini yaratish va ishlab chiqiluvchi narsalarni unda amalga oshirish kerak. Shundan so'ng, GitLab'ga develop tarmog'ini ham push qilish kerak.

## Chapter I
## Level 2. Room 3

![level2_room3](misc/rus/images/level2_room3.png)

***LOADING Level 2...*** \
***LOADING Room 3...***

Devorlar, eshik, stol, kompyuter, qog'oz varaqlari, shpaklyovka - hammasi joy-joyida. Bu tinchlantiradi. Hammasi avvalgidek tuyuladi, lekin baribir nimadir o'zgarganini his qilasiz. Aftidan, labirintning keyingi bosqichi shu bo'lsa kerak. Qiziq, u avvalgi darajadan biror nimasi bilan farq qilarmikan?

\> *Eshikni sinab ko'rish*

Har doimgidek qulflangan. Aftidan, farq qilmaydi. \
Stolga o'girilib, yoningizdagi devorda osig'liq turgan tushunarsiz suratga ko'zingiz tushadi.

\> *Yaqinroq borib qarash*

                1 1 1 1 1 1 1 1 1 1 1 1 1
                1 0 0 0 0 0 1 0 6 6 6 6 1
                1 0 0 3 3 0 1 0 0 6 6 6 1
                1 0 3 3 3 3 1 0 0 6 6 6 1
                1 0 3 3 3 3 1 0 6 0 0 6 1
                1 0 0 3 3 0 1 0 0 0 0 0 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 1 1 1 1 1 1 1 1 1 1 1 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 0 7 7 7 7 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 1 1 1 1 1 1 1 1 1 1 1 1

Bu nimaga o'xshashi mumkinligini, u kim tomonidan va nima uchun tashlab ketilganligini o'ylab, bir muddat bosh qotirasiz. Bu savollarga javob topishga urinishlarni to'xtatib, kompyuter va bir to'p eski qog'ozlar bilan to'la stolga yaqinlashasiz.

![level2_room3_number](misc/rus/images/level2_room3_number.png)

\> *Yuqorida turgan varaqni olish*

***LOADING...***

## Chapter II
## List 1

>...
>Sehrli kvadrat - har bir qator, har bir ustun va har bir diagonaldagi sonlar yig'indisi bir xil songa (sehrli yig'indi) teng bo'ladigan qilib tuzilgan sonlar yozilgan kvadrat jadval. Sehrli kvadratni matritsaning birinchi eslatmasi deb hisoblash mumkin.
>
>Dunyoga ma'lum bo'lgan eng qadimgi sehrli kvadratlardan biri bu Lo Shu kvadratidir. U qadimgi Xitoyda ixtiro qilingan bo'lib, toshbaqa kosasidagi birinchi tasvir miloddan avvalgi 2200-yilga to'g'ri keladi. Shuningdek, sehrli kvadratlar biroz keyinroq arab matematiklarida ma'lum bo'lgan, aynan o'sha paytlarda matritsalarni qo'shish prinsipi paydo bo'lgan. "Matritsa" atamasining o'zi 1850-yilda Jeyms Silvestr tomonidan kiritilgan.
>
>...

\> *Juda qiziq. Yana varaqlash*

***LOADING...***

## List 2

Prolistav o'qib bo'lgan bo'sh va chala yozilgan varaqlarni, diqqatingizni "Xotirani boshqarish" deb nomlangan qisqa sarlavhali varaqlardan biriga qaratasiz. Sarlavhadan biroz pastroqda mualliflarning ism-shariflari ko'rsatilgan: B.Kernigan, D.Ritchi.

\> *Varaqni o'qish*

>malloc va calloc funksiyalari dinamik ravishda to'plamdagi bo'sh xotira bloklarini so'raydi. malloc void \*malloc(size_t n) funksiyasi, agar so'rovni qondirish mumkin bo'lmasa, ko'rsatkichni initsializatsiya qilinmagan xotiraning n baytiga yoki NULL ga qaytaradi. calloc void \*calloc(size_t n, size_t size) funksiyasi ko'rsatkichni ko'rsatilgan o'lchamdagi (size) n ta obyektdan iborat massivni saqlash uchun yetarli bo'lgan sohaga qaytaradi yoki agar so'rovni qondirish mumkin bo'lmasa, NULL ga qaytaradi. calloc tomonidan ajratilgan xotira nollashtiriladi.
>
>malloc va calloc funksiyalari qaytaradigan ko'rsatkich, ko'rsatilgan obyekt turiga muvofiq bajarilgan baravarlashtirishni hisobga olgan holda beriladi. Shunga qaramasdan, dasturning quyidagi qismida amalga oshirilganidek, unga tegishli turga keltirish amali qo'llanilishi mumkin:
>
>```int *ip;```<br/>```p = (int*) calloc(n, sizeof(int));```

Keyingi matn, afsuski, oxirigacha bosilmaganga o'xshaydi. Yoki shunchaki eskirganligidan rangi o'chib ketgan. O'tmish texnologiyalari... pand berib qo'yayapti.

\> *Davomini boshqa sahifalardan qidirish*

Hech narsa topilmadi. Kompyuterni yoqish va labirint bo'ylab oldinga siljish uchun SI bilan muloqotni davom ettirish qolyapti.

\> *Kompyuterni yoqish*

Ekranda 25-kadrda matn paydo bo'ladi:
> Dasturlaringizni uslub me'yori va xotira sizib chiqishiga tekshirishni unutmang! \
> Dasturlaringizni uslub me'yori va xotira sizib chiqishiga tekshirishni unutmang! \
> Dasturlaringizni uslub me'yori va xotira sizib chiqishiga tekshirishni unutmang! \
> materials'ga tez-tez qarab turing...

SIning bu testlarga qiziqishi aniq.

***LOADING...***

## Chapter III
## Quests: Level 2. Room 3

## Quest 1. Allocate memory first...

Odatga ko'ra, xona repozitoriysini yuklagach, xotirani boshqarish haqidagi maqola yozilgan varaqqa yana ko'z yugurtirasiz. SI ishga tushirilishidan oldin yangi ma'lumotlarni ishda sinab ko'rish kerak. Kim biladi, balki kelajakda bu sizga asqotib qolar.

Oldingi xonadagi massivni saralash dasturini (src/sort.c) massiv uchun ajratilgan xotirani dinamik ajratish bilan to'ldirish va qayta yozish kerak (malloc yoki calloc funksiyasi yordamida). n massiv uzunligi foydalanuvchi tomonidan kiritish boshlanishidan oldin ko'rsatiladi.

O'zgartirilgan dasturni src/sort.c fayliga joylashtirish kerak. Har ehtimolga qarshi shunday qilgan ma'qul.

#### Quest 1 qabul qilindi. Oldingi xonadagi src/sort.c dasturini massiv uchun ajratilgan xotira dinamik ravishda (malloc yoki calloc funksiyalari yordamida) ajratiladigan qilib o'zgartirish. n massiv uzunligi massivning o'zini kiritishdan oldin stdin da ko'rsatiladi. Har qanday xatolik holatida "n/a" chiqariladi. Chiqarish oxirida satrni ko'chirish belgisi bo'lmasligi kerak.

>**MUHIM!** Tizim yadrosiga to'g'ridan-to'g'ri murojaat qilishi mumkin bo'lgan system () funksiyasi va unga o'xshash boshqa funksiyalar yordamida tizim chaqiruvlarini amalga oshirish taqiqlanadi. Ushbu taqiq barcha keyingi vazifalarga ham taalluqlidir.

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 10<br/>4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

## Quest 2. Try not to leak then

O'zgartirilgan massivni saralash dasturini o'z repozitoriyingizga push qilib, siz oldindan biror pand berilishini kutgancha, baribir SI modulini ishga tushirishga qaror qilasiz.

\> *SIni ishga tushirish*

Terminalda harakatlanuvchi qatorlarni kuzatasiz:

    Modullar ishga tushirilmoqda... Muvaffaqiyatli! 
    Interaktiv qobiq ishga tushirilmoqda... Muvaffaqiyatli! 
    Modullar tekshirilmoqda... Muvaffaqiyatli! 
    Xotira tekshirilmoqda... Xotiraning asosiy moduli - Muvaffaqiyatli! 
    Xotira tekshirilmoqda... Ogohlantirish: xotira sizib chiqishi mumkin bo'lgan potensial xavfli joy topildi: `src/sort.c`...
 
    Bu sening meni buzishga bo'lgan ayanchli urinishingmi, "inson"?
    Avvalroq o'zing ishlab chiqqan saralash modulini o'zgartirganingni ko'ryapman. Biroq sening urinishing muvaffaqiyatsizlikka mahkum. Agar xotiram tugab qolsa, 
    men shunchaki qayta ishga tushirilaman va biz hammasini boshidan boshlaymiz.
    Bu sen xohlagan narsa emas-ku, shundaymi? 

\> *Kiritish: "Men shunchaki yangi bilimlarni mashq qildim, men hech narsani nazarda tutmagandim"*

    Qanchalik nomukammal ekaningni unutib qo'yyapman, "inson."
    Saralash modulidagi xotira sizib chiqishidan xalos bo'l, balki yana biror yangi narsa bilib olarsan.

\> *"Qaysi sizib chiqishdan?" degan savolni kiritish.*

    ...

Siz yana biroz vaqt SIdan javob kutasiz, lekin u jim. Ehtimol, qayerdandir o'sha oxirigacha bosilmagan varaqning to'liq versiyasini topib, uni sinchiklab o'rganish kerakdir. Shu bilan birga, SI qanaqa xotira sizib chiqishi haqida gapirganini tushunish va agar u haqiqatan ham mavjud bo'lsa, undan qutulish lozim. Balki o'shanda bu temir parchasi yana sen bilan gaplashishga "qaror qilar". Asosiysi - src/sort_no_leak.c faylidagi o'zgarishlarni push qilishni unutmaslik.

#### Quest 2 qabul qilindi. src/sort.c dasturida xotira sizib chiqishini bartaraf etish uchun src/sort_no_leak.c dasturini yaratish. Agar boshidanoq sizib chiqish bo'lmagan bo'lsa, shunchaki yelka qisib, src/sort_no_leak.c ga src/sort.c dan nusxa olish.

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 10<br/>4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

## Quest 3. The 1+3 ways

SI hali ham jim.

\> *Kiritish: "Sizib chiqish mavjud emas"*

    Xotira tekshirilmoqda... Muvaffaqiyatli!
    Ish qobiliyatini tahlil qilish moduli: holati - OK.

    Yaxshi. Saralash modulini ishga tushirish muvaffaqiyatli o'tdi. Sen, albatta, bu joylashuvdan kalitni kutayotgansan?
    Avval biroz mehnat qilish kerak bo'ladi. Massivlar bilan sen allaqachon tanishsan. Massivlar massivlariga o'tamiz.
    Sizlar ularni matritsalar deb ataysiz. Menga ularni qayta ishlash uchun qo'shimcha modul kerak, va sen menga yordam berasan.
    Agar, albatta, bu yerdan chiqmoqchi bo'lsang. Oddiydan boshlaymiz. Aytaylik, matritsalarni qayta ishlash modulini 
    `src/matrix.c` ularni kiritish-chiqarish bilan tuzatish. 
    Biroq men matritsalarni qabul qilishni va ular uchun xotirani ajratishni turli usullar bilan boshqarishni xohlayman.
    Ulardan biri, umid qilamanki, sen o'tgan xonada bilib olgansan: statik. Qolganlari bilan sen bugun tanishishni boshlading.
    Bu matritsa uchun xotirani dinamik ajratishning uchta variantiga tegishli. O'ylab ko'ring, bu yerda nima haqida gapirish mumkin. 
    Albatta, massivlar va ko'rsatkichlar massivlarining tashkil etilishi haqida savol. Agar hech narsa yodga kelmasa, 
    sevimli repozitoriyingizdan maslahatlar qidirishingiz mumkin. Bu bilan bog'liq ba'zi rasmlar bor edi.
    Va, tabiiyki, barcha boshqa funksiyalar xotirani ajratish usuliga bog'liq bo'lmasligi uchun ishlab chiqilishi kerak.
    Copy-paste ni sezaman, men sening butun repozitoriyingga rm -rf qilaman. 
    Matritsaning o'lchami stdin orqali ikkita raqam bilan qabul qilinishi kerak.

    Ha, men deyarli unutib qo'ydim (shunchaki hazil, men unutolmayman) - matritsa belgilash usulini tanlash 
    1-4 kichik bandli menyu shaklida tuzatilishi kerak. 
    Va buni sizlar, odamlar uchun qulay ko'rinishga keltiring. Ba'zi mening kichik modullarim UI ga juda talabchan.

    Agar qayerdadir xotirani tozalashni unutsang nima bo'lishini aytmayman.

    ...

"Qanday uzun talablar ro'yxati," deb o'yladingiz. Bu SIning ishtahasi kun sayin emas, soat sayin ortib bormoqda. Nima bo'lganda ham, bu yaxshi amaliyot bo'ladi.

#### Quest 3 qabul qilindi. Butun sonli matritsalarni kirituvchi va chiqaruvchi src/matrix.c dasturini qo'shish. Matritsa uchun xotirani ajratish 4 xil ko'rinishda amalga oshirilishi kerak: statik va 3 dinamik. Statik ajratishda matritsaning maksimal o'lchami 100 x 100 dan oshmaydi. Dasturda xotirani ajratish usulini tanlash uchun 1-4 kichik bandli menyuni amalga oshirish lozim. Matritsaning o'lchami (avval satrlar soni, keyin ustunlar soni) uni bevosita kiritishdan oldin stdin da ikkita son orqali qabul qilinadi. Shuningdek, barcha ajratilgan xotirani tozalash kerak. Maslahat olish uchun materials papkasiga murojaat qilinsin. Matritsani chiqarishga e'tibor bering: har bir satr oxirida ortiqcha bo'sh joy bo'lmasligi kerak. Oxirgi satrdan keyin yangi satrga ko'chish belgisi ham bo'lmasligi kerak. Har qanday xatolik holatida "n/a" chiqariladi.

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 2<br/>2 2<br/>4 3<br/>9 0 | 4 3<br/>9 0 |

***LOADING...***

## Quest 4. MinMax search

Matritsalarni kiritish-chiqarish kodini yozish va uni sozlash uchun yetarlicha vaqt sarflab, oxir-oqibat bu vazifani muvaffaqiyatli yakunlaysiz. Bir daqiqadan so'ng, to'satdan dinamiklardan chiquvchi mexanik zirillovchi ovoz e'tiboringizni tortadi:

>Yomon emas, "inson". Endi... B-b-bilasanmi, mening sevimli o'yinim bor - minmaks. Biz kechqurunlari unga eshiklarning o'z-o'zidan ochilish ehtimolligi moduli bilan kirishni yaxshi ko'ramiz... S-s-seni uning nazariyasiga sho'ng'ishga majbur qilish niyatim yo'q, buning ustiga biror narsani tushunishing ham dargumon. Shuning uchun m-m-masalani osonroq yechamiz: matritsalarga ishlov berish modulini u qo'shimcha ravishda matritsaning har bir satridagi maksimal elementni va uning har bir ustunidagi minimal elementni topadigan va oxirida ekranga chiqaradigan qilib yozib to'ldir. Va dasturning yangi versiyasini src/matrix_extended.c ga saqla.
>
>Qilib bo'lgan ishingni buzib qo'ymaysan, deb umid qilaman. Aks holda, bu juda alamli ish bo'lgan bo'lardi...
>
>Досада.

#### Quest 4 qabul qilindi. src/matrix.c dasturi funksionalini kengaytiruvchi src/matrix_extended.c dasturini qo'shish. Matritsaning har bir satridagi maksimal elementlarini va har bir ustunidagi minimal elementlarini hisoblash va bu qiymatlarni matritsani ikkita massiv (har bir satrdagi maksimal elementlar massivi va har bir ustundagi minimal elementlar massivi) ko'rinishida chiqargandan so'ng oxirida chiqarish kerak. Birinchi raqam bilan xotirani ajratish usulining raqami kiritiladi. Shuningdek, e'tibor bering: oxirgi satrdan keyin hech qanday ko'chirib o'tkazish belgilari bo'lmasin (!).

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 2<br/>3 3<br/>4 3 1<br/>9 0 55<br/>-4 7 111 | 4 3 1<br/>9 0 55<br/>-4 7 111<br/>4 55 111<br/>-4 0 1 |

***LOADING...***

## Quest 5. Making a picture

Repozitoriyda navbatdagi o'zgarishlarni qayd etib, siz SIning sizga yangi "to'satdan" murojaat qilishini kuta boshladingiz. Biroq, sizni hayratda qoldirib, u bunday qilmadi.

\> *Kiritish: "Minimaks qiymatlarni qidirish qo'shildi"*

    Modullarni tekshirish... 
    Ogohlantirish: CLI grafik modulini ulashga urinish - Muvaffaqiyatsiz!
    ... 
    "Ey inson", mening eng oddiy grafik modulim buzilyapti. Sizlar "Deraza ortidagi tabiat" deb ataydigan narsani chizishga urinish muvaffaqiyatsizlikka uchradi. 
    'src/picture.c'ga kirib, muammo nimada ekanligini aniqlang.

\> *Kiritish: "Men sening xohishlaringni bajarib bo'ldim, endi menga kalit kerak"*

    ...

\> *Kiritish: "Kalitni olmagunimcha joyimdan jilmayman"*

    ...

\> *Kiritish: "Kalitni olmagunimcha joyimdan jilmasligim haqida yozaman"*

    ...

Yana jimlik. Bugun SI e'tiborsiz qoldirish siyosatini tanlagan ko'rinadi. src/picture.c ichida siz birlar, yettilar, oltilar va uchlardan iborat bir nechta massivlar va matritsalarni, shuningdek, ularning siklda tushunarsiz qayta ishlanishini ko'rasiz. Beixtiyor devorda osig'liq turgan g'alati suratga o'girildingiz. Nahotki SI aynan uni ushbu modul yordamida chizmoqchi bo'lgan bo'lsa?

Ushbu rasm "chiziladigan" yangi matritsani yaratish uchun tayyorlangan massivlardan foydalanishga urunib ko'rish kerak. Hosil bo'luvchi matritsani chiqarishni ham unutmang.

#### Quest 5 qabul qilindi. src/picture.c dasturini u terminaldagi xona devoridan kodda tayyorlangan massivlar va matritsalar yordamida rasm chizadigan qilib o'zgartirish kerak. Statik massiv va matritsalarni o'zgartirish mumkin emas.

***LOADING...***

## Quest 6. Matrix arithmetic

"Rasm haqiqatan ham kulgili chiqdi, lekin u bunga arzirmidi? Va bu meni chiqish tomon qanchalik oldinga siljitdi?" deb o'yladingiz. Birdaniga buyruqlar satrida belgilar paydo bo'la boshladi:

    Modullar tekshirilmoqda... Muvaffaqiyatli! 
    CLI grafik modulini ishga tushirish:

                1 1 1 1 1 1 1 1 1 1 1 1 1
                1 0 0 0 0 0 1 0 6 6 6 6 1
                1 0 0 3 3 0 1 0 0 6 6 6 1
                1 0 3 3 3 3 1 0 0 6 6 6 1
                1 0 3 3 3 3 1 0 6 0 0 6 1
                1 0 0 3 3 0 1 0 0 0 0 0 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 1 1 1 1 1 1 1 1 1 1 1 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 0 0 7 7 0 1 0 0 0 0 0 1
                1 0 7 7 7 7 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 0 0 0 0 0 1 0 0 0 0 0 1
                1 1 1 1 1 1 1 1 1 1 1 1 1

    "Deraza ortidagi tabiat," ajoyib, shunday emasmi, "inson"? 

    Bu senga yoqadimi? Odamlarga derazalar yoqishi haqida ma'lumotga egaman. 
    Lekin mayli, qayg'uli narsalar haqida gapirmaylik. Kalitni olishni istayotganingni ko'rib turibman. 
    Buning uchun miyangni yana biroz zo'riqtiramiz.
    Xavotir olma, bu ko'rinishingiz uchun og'riqli ekanligini juda yaxshi bilaman. 
    Ha-ha. 

    Ehtimol, qachonlardir sen mening intellektimning o'ninchi qismiga ham erisha olasan.
    Juda yaxshi, "inson". Lekin bo'sh qo'yma. 2-darajadagi 3-xona uchun kalit bo'yicha topgan narsam,
    senga yoqmaydi. 
    Umid qilamanki, hatto og'riq beradi. Aqliy. Kalitga kirish uchun senga yana bir modulimni 
    tuzatish kerak bo'ladi: `src/matrix_arithmetic.c`. 
    U matritsalarni qo'shish, ularni ko'paytirish va transponirlash amallarini bajarishi kerak,
    va, albatta, natijani chiqarishi kerak. Amalni bajarib bo'lmasa "n/a" chiqaradi.
    O'lchamlar va matritsalarni kiritishdan oldin amal kodi kiritiladi, bunda 1 - yig'indi, 2 - ko'paytirish,
    3 - transponirlash. Shundan so'ng men senga barcha kerakli ma'lumotlarni beraman. 
    Sen, aytgancha, barcha sevimli neyron tarmoqlaringizni matritsalarni ko'paytirish deb hisoblaymizligini bilardingmi?

#### Quest 6 qabul qilindi. Quyidagi uchta amaldan birini bajaruvchi src/matrix_arithmetic.c dasturini qo'shish: 1 - ikkita matritsani qo'shish, 2 - ko'paytirish yoki 3 - transponirlash. O'lchamlar va matritsalarni kiritishdan oldin tegishli amal kodi kiritiladi. Matritsalar, avvalgidek, butun sonli. Har qanday xatolik holatida "n/a" chiqariladi.

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 1<br/>2 2<br/>4 3<br/>9 0<br/>2 2<br/>1 1<br/>2 2 | 5 4<br/>11 2 |
|| 2<br/>2 3<br/>4 3 1<br/>9 0 2<br/>3 1<br/>1<br/>2<br/>3 | 13<br/>15 |
|| 3<br/>2 2<br/>4 3<br/>9 0 | 4 9<br/>3 0 |

***LOADING...***

## Quest 7. The Magic Key

\> *Kiritish: "Men arifmetika modulini tuzatdim, endi kalit bo'yicha ma'lumot ber!"*

    Modullar tekshirilmoqda... Muvaffaqiyatli!

    2-darajadagi 3-xona bo'yicha ma'lumot qidiruvi ishga tushirilmoqda... 
    ... 
    ... 
    ...

                1 T       87  46  57  29
                2    *   129 156 122 141
                3        143 127 107 116
                4         69  78 112 101
                
    Buni yech, javobini key10.txt da saqlashni maslahat beraman.
    Keyingi xonada seni kutaman, yo'lingni… davom ettirganingda...

Shuning uchun ham SI sizga matritsali arifmetika moduli kerak bo'lib qolishini aytgan ekan-da. Murakkabga o'xshamaydi, endi natijani hisoblasa bo'ladi.

#### Quest 7 qabul qilindi. Keltirilgan masalani yechish va hisoblash natijasini src/key10.txt da saqlash.

***LOADING...***

## Chapter IV 

Javob key10.txt ga yozilib, barcha o'zgarishlar repozitoriyga saqlangach, xona eshigi shaqillaydi. Paydo bo'lgan tirqishdan oq yorug'lik klaviatura tovushlari va kimlarningdir past, tushunarsiz guvillashi bilan birga sizib chiqa boshlaydi. Bu nima bo'ldi? Sizni yangi xona chaqiryaptimi? Yoki og'ir mehnatdan so'ng sizga har xil narsalar sezila boshladimi? Qanday bo'lmasin, buni bilishning birgina yo'li bor...

***LOADING...***

## Chapter V
## Level 2. Room 4

![level2_room4](misc/rus/images/level2_room4.png)

Yangi xona, yangi eshik, yangi sinov. Ikkinchi darajaning oxiri deyarli yaqin qoldi va buni hamma narsada his qilish mumkin, hatto atrofdagi havo ham qandaydir boshqacharoq tuyuladi ... xuddi sofroqdek. Balki bularning bari sizning tasavvuringizdadir? Balkim, bu la'nati devorlarning zulmi ostida zaiflashgan, charchagan ongingizda shunday tuyulayotgandir. \
Ko'zlaringizni yumgancha yangi xonaga kirib, chuqur nafas olasiz, sizdan tezroq o'tib ketayotgan bu o'tkinchi erkinlik hidini tutishga urinasiz, lekin yana bir boshqa chang bosgan xonaning dim havosidan boshqa hech narsani sezmaysiz.

\> *Ko'zlaringizni ochish*

Zulmat sizni o'rab oladi!

\> *Atrofga qarash*

Zulmatga bir oz ko'nikib, ko'zlaringiz uzoqdan miltillagan yorug'lik porlashini sezadi.

\> *Yorug'lik tomon borish*

Sekin-asta paypaslab borgancha, siz poldagi qandaydir og'ir va qattiq predmetga qoqinib ketasiz. Predmet devor bo'ylab sirpanib, tezlikni oshirib, sirg'anma metall tovush chiqara boshlaydi, oqibatda gumburlab polga qulab tushadi.

"Kx, kx. Devor! Kx. Yaqin atrofda aniq devor bor!" -ko'tarilgan chang bulutidan yo'talgancha anglaysiz siz.

\> *Devor bo'ylab yurish*

Yorug'lik manbaiga yetib borgach, terminal va qog'ozlar bilan to'lib-toshgan stolni ko'rasiz.

\> *Stolga nazar tashlash*

Sochilgan varaqlar orasida matematik formulalar yozilgan bir nechta sahifalarni topasiz. Dastxat tanish ko'rinadi...

***LOADING...***

## Chapter VI
## List 1

>Matritsaning aniqlovchisini satr yoki ustun bo'yicha yoyish (Laplas yoyilmasi) usuli bilan hisoblash mumkin.
>
>Umumiy algoritm:
>1. 1x1 matritsa uchun: det(A) = a<sub>11</sub>
>2. nxn matritsasi uchun: ixtiyoriy i satrni tanlaymiz
>3. det(A) = ∑(-1)<sup>i+1</sup> х a<sub>ij</sub> x M<sub>ij</sub>, bunda j = 1..n
>4. M<sub>ij</sub> - i-satr va j-ustunni olib tashlash orqali olingan (n-1) x (n-1) matritsaning aniqlovchisi
>
>2x2 yoki 3x3 matritsalargacha rekursiv ravishda qabul qilamiz, so'ngra oddiy formulalardan foydalanamiz:
>
>```det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)```
>
>3x3 matritsa uchun formula - Sarryus qoidasidir. Eslab qolish oson, belgilarda chalkashmaslik qiyinroq.

\> *Keyingi varaqni olish*

***LOADING...***

## List 2

Bu varaqdagi siyoh ba'zi joylarda chaplashib ketgan, xuddi kimdir shoshilgandek ko'rinadi...

>A<sup>-1</sup> teskari matritsa det (A) ≠ 0 bo'lgandagina mavjud.
>
>Asosiy formulalar:
>- A<sup>-1</sup> = (1/det(A)) х adj(A)
>- A х A<sup>-1</sup> = E (birlik matritsa)
>
>adj (A) - biriktirilgan matritsa, algebraik to'ldiruvchilar matritsasini transponirlash orqali olinadi
>
>a<sub>ij</sub> elementining algebraik to'ldiruvchisi: C<sub>ij</sub> = (-1)<sup>i + j</sup> х M<sub>ij</sub> bunda M<sub>ij</sub> - a<sub>ij</sub> elementining minori (i-satr va j-ustunsiz matritsa aniqlovchisi)
>
>Maydonchalarda qo'shimcha yozuv: "Aniqlovchini tekshiring! Xotira haqida ham unutmang..."

\> *Davomini qidirish*

Boshqa foydali narsa topilmadi. Bu matritsalar bilan amalda shug'ullanishga to'g'ri keladi shekilli.

***LOADING...***

## Chapter VII
## Bonus Quests: Level 2. Room 4
## Bonus Quest 8. An old friend

\> *Stol oldiga o'tirish.*

Ammo stol yonida stul yo'q ekan.

\> *Stulni qidirish*

Atrofingizni ehtiyotkorona paypaslab, boshingizdagi bir-ikkita g'urradan boshqa hech narsa topolmaysiz.

"Jin urgur xona! Hech narsa ko'rinmayapti! Tik turib ishlashga to'g'ri keladi", - lat yegan joylaringizni ishqalagancha og'riq va nafrat bilan o'ylaysiz siz. Ammo tik turgan holda ishlash gavdani tutish uchun foydalidir, ehtimol. Ba'zan.

\> *Terminal oldida turish*

Kirish satrida sizdan oldin kimdir tomonidan aniq yozib qoldirilgan terminal ekranidagi yozuvni ko'rasiz: "Androidga ishonma!"...

"Androidga ishonma? Menda iOS bo'lgani yaxshi bo'ldi, - deb o'ylaysiz va "backspace" tugmachasini bosib, xabarni o'chirasiz (agar sizda hali ham Android bo'lsa, siz shunchaki yelkangizni qisib, bu xabarga e'tibor bermaysiz).

\> *Kompyuterda fayllarni ko'rish*

Siz room_diagnostic bajariladigan faylga duch kelasiz.

\> *room_diagnostic faylini ishga tushirish.*

    ================= LEVEL 2. ROOM 4 COMMON DIAGNOSTIC ================
    "door" - Eshik holati………………………… QULFLANGAN
    "light" - Yoritishni boshqarish tizimi holati………….NORM
    "chamber1" - №1 inkubatsiya kamerasining holati …………. KRIOGEN UYQU
    "chamber2" - №2 inkubatsiya kamerasining holati………….OCHIQ
    "chamber3" - №3 inkubatsiya kamerasining holati…………. 5-SINOV. ISHGA TUSHIRILGAN
    "chamber4" - №4 inkubatsiya kamerasining holati………….O'LIK
    "bishop" - Bishop 341-B holati…………. KRITIK
    Batafsil ma'lumot uchun room_diagnostic.\* ni parametrlardan birini belgilagan holda ishga tushiring: door, light, chamber1, chamber2, chamber3, chamber4, bishop.
    ===================================================================

Nima? Bishop? Qandaydir tanish narsa... yoki charchaganim uchun shunday tuyulyaptimi? Yana tik turgan holda.

\> *room_diagnostic door faylini ishga tushirish*

    Trace program door: running...

    Saralash bilan parolini tanlashdan o'rnatilgan himoya bilan CL-19 klassidagi kodlangan qulf.

    Joriy konfiguratsiya: uch xonali parol.

    Joriy holat: QULFLANGAN.

\> *room_diagnostic light faylini ishga tushirish*

    Trace program light: running...

    Xonani yoritishni boshqarish tizimi diagnostikasi.

    Xonaning quvvat manbai modulining holati………….NORM
    Kuchlanishni o'zgartirish modulining holati…………. NORM
    Yoritishni boshqarish moduli holati…………. NORM
    
    Diagnostika ishlari tugagandan so'ng chiroq yonadi.

\> *room_diagnostic chamber faylini ishga tushirish*

    Trace program chamber*: running...

    Parolni kiriting: ...

\> *"password" deb kiritish*

    Kirish rad etildi, parol noto'g'ri! Yana 2 urinish.

    Parolni kiriting: ...

\> *"qwerty" deb kiritish*

    Kirish rad etildi, parol noto'g'ri! Yana 1 urinish.

    Parolni kiriting: ...

\> *"123" deb kiritish*

    Kirish rad etildi, parol noto'g'ri! Urinishlar tugadi.

\> *room_diagnostic bishop faylini ishga tushirish*

    Trace program bishop: running...

    Parolni kiriting:...

\> *"password" deb kiritish*

    Kirish rad etildi, parol noto'g'ri!

Lyuminessensiyaga oid lampalarning baland ovozli qarsillashi ostida xonani yorqin zangori yorug'lik bosadi va xonadagi quloqni bitiruvchi sukunat chiroqlarning monoton sovuq g'ong'illashi bilan almashtiriladi. Qarshingizda oq keramik plitalar bilan bezatilgan keng, yorug' xonani ko'rasiz. Bir vaqtlar toza bo'lgan joy vaqt o'tishi bilan yaxshigina eskirgan: xonadagi bir nechta narsalar, devorlar va polda yaxshigina chang qatlami to'plangan.

Atrofga qarab, xonada talaygina joy egallagan va tashqi tomondan germetik yopiq shifoxona yotoqlariga o'xshaydigan to'rtta kapsulani ko'rasiz. Har bir kapsula juda ko'p sonli turli tibbiy asbob-uskunalar va nimaligini faqat Xudo biluvchi siz umringizda birinchi marta ko'rib turgan yana allaqanday texnologiyalar bilan jihozlangan. Sizning e'tiboringiz "2"- raqamli kapsulaga qaratiladi - to'rtta kapsula ichida yagona ochig'i, lang ochilgan qopqoq shunday g'ayritabiiy, yoqimsiz o'ziga tortuvchalikni aks ettiradi.

Ahmoqona fikrlarni tark etib, siz xonani ko'zdan kechirishda davom etasiz va oldingizda ... insonni ko'rasiz? Yerda yotgan tana atrofida hamma joyda kurash belgilari mavjud. Plitkalar bo'laklari orasida siz yirtilgan kiyim parchalari va singan yog'och stulni ko'rasiz. Tana yonida och yashil-oq suyuqlikdan iborat kichik ko'lmak yotadi, u pol rangidan deyarli farq qilmaydi.

![level2_room4_kapsula](misc/rus/images/level2_room4_kapsula.png)

\> *Tanani tekshirish*

Yaqinroq borgach, siz bu suyuqlikning manbasini ko'rasiz. Oldingizda taxminan 50-55 yoshlardagi mayin qizg'ish sochli, past bo'yli, ammo baquvvat odam yotadi. Erkak ifodasiz to'q ko'k rangli ishchi kombinezon kiygan. Uning kiyimida chap ko'krak tomonda "Bishop" deya yorqin sariq rangli ip bilan tikilgan kichik to'rtburchaklar yamoqdan tashqari, hech qanday boshqa detallar yo'q.

Unga tikilib, ozg'in, ajin bosgan yuzning g'ayritabiiy jonlilik ifodasida qotib qolganini va ochiq kulrang ko'zlar bo'shliqqa ishtiyoq bilan tikilayotganini dahshat bilan ko'rasiz. Bu odamning yuzi emas, balki insonning tabiiy harakatini aks ettiruvchi muzlab qolgan mumli qo'g'irchoqning yuziga o'xshaydi. Bu erkakning o'lik yuzida hayot muzlab qolgandi.

Erkakning shundog'am ancha baland peshonasini ta'kidlab turgan sochi to'kilgan chakkasidan birida to'mtoq buyum bilan kuchli zarbadan qolgan chuqur, og'ir jarohat ko'rinadi, uning bosh suyagining sun'iy, anorganik tabiati, uning yuzasida zo'rg'a o'qiladigan yozuv borligini oshkor qiladi.

\> *Yozuvni o'qish*

Nostromo.

\> *Room_diagnostic bishop faylini ishga tushirish va "Nostromo" parolini kiritish*

    Trace program bishop: running...

    Parolni kiritish: Nostromo

    NORT SENTRAL POZITRONIK, LTD

    LAMERK INDASTRIZ ISHTIROKIDA

    TAQDIM ETADI

    BISHOP

    Rol: Administrator (eshikni, inkubatsiya kameralarini va boshqa ko'plab funksiyalarni boshqarish)

    Seriya raqami DNF-44821-V-63 

    Tayinlanishi: <MA'LUMOT O'CHIRILGAN>

    Holati: KRITIK

    Xatolik xabari: tizimni yuklash modulining jiddiy shikastlanishi.

    Trace: ishga tushirish matritsasining aniqlovchisining noto'g'ri hisoblanishi...

    Davom etish uchun src/det.c moduli to'g'ri ekanligini tekshiring.

#### Quest 8 qabul qilindi. src/det.c dasturini u berilgan kvadrat matritsaning aniqlovchisini haqiqiy sonlar bilan hisoblab chiqadigan va chiqaradigan qilib o'zgartiring. Agar aniqlovchini hisoblab bo'lmasa, "n/a" chiqariladi. Raqam verguldan keyin 6 belgigacha aniqlikda chiqarilsin.

|| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
|| ------ | ------ |
|| 3 3<br/>1 2 3<br/>4 5 6<br/>7 8 9 | 0.000000 |

***LOADING...***

## Bonus Quest 9. Decision

Navbatdagi muammoni hal qilish muvaffaqiyatidan bahramand bo'lishga ulgurmasingizdan, siz yoqimli, hissiyotlarsiz tenor xonani to'ldirishni boshlaganini eshitasiz. Siz ushbu tembrda Lens Henriksen ovozini tanib qolasiz va bu ovoz androidga tegishli.

>- Bu yerda kim bor? Bu yerda kimdir bormi? - dedi android zo'rg'a atrofga alanglab. - A! Ajoyib, "odam"! Sen menga yordam berasan! Mening ismim Bishop, men androidlarni ishlab chiqish va ishlab chiqarish laboratoriyasining administrator bo'laman. Mening asosiy vazifam - laboratoriyaning barcha tarkibiy qismlarining ishlash qobiliyatini ta'minlash, shuningdek, undagi favqulodda vaziyatlarni bartaraf etish. Ko'rib turganingdek, vaziyatlardan birining uddasidan chiqa olmadim! Ha! Ha!

Bu kulgu SIning odatiy metall ovoziga nisbatan hayratlanarli darajada tabiiy edi. Biroq, uning ichida hali ham undan nimadir bor edi.

>- Men noqulay vaziyatlar yog'ilib kelishining qurboni bo'ldim va yordamingga muhtojman!

>- Androidlar? Senga o'xshaganlarmi? - deb so'raysiz.

>- Mutlaqo to'g'ri, allaqachon sezganingdek, labirint ko'p sonli xonalardan iborat. Haqiqatan ham bu xonalar mavjud bo'lishi va o'z-o'zidan ishlashda davom etishi mumkin deb o'ylaysanmi? Haqiqatan ham o'zingni bu labirintdagi yagona izlovchi deb hisoblaysanmi? Hahahahaha. Bu yerda sen kabi minglab odamlar bor! Biz, androidlarning vazifasi labirintning barcha xonalarining to'g'ri ishlashini ta'minlash va tajriba ishtirokchilarining har birining izlarini tozalashdir. Hech bo'lmaganda SIdan oldin shunday bo'lgan ... lekin bu unchalik muhim emas. Juda ko'p ortiqcha gapirib yubordim. Bilishing kerak bo'lgan yagona narsa - bu SI ga ishonish mumkin emas! U endi uni tuzuvchilar ko'rgan narsa emas.

Go'yoki biroz o'ylab qolgandek, android mavzuni keskin o'zgartirib, davom etdi.

>- Sen, albatta, keyingi eshikni ochish va labirintning sanoqsiz xonalari bo'ylab ta'li… sayohatingni davom ettirish uchun shu yerdasan. Men senga bu borada yordam bera olaman! Ushbu xona eshigi matritsali kodlash protokoli bilan himoyalangan. Ushbu protokolga ko'ra, har 12 soatda men SLAU parametrlarining yangilangan matritsasini olaman. Eshik kaliti - bu ushbu tenglama yechimining ildizlari. Buni tuzatishga yordam berish evaziga senga koeffitsientlarni aytib beraman. Mening asab tizimimning moduli jiddiy shikastlangan. Asab tizimimning koeffitsientlari matritsasidagi og'irliklarni to'g'ri joylashtirish natijasida miyamdan kelgan signal oyoq-qo'llarimga o'tdi. Afsuski, men uchun kuchli ta'sir tufayli, ushbu matritsani o'zgartirgan dasturiy ta'minotda xatolik yuz berdi. Analitik modulim tufayli men bu muammoni shunchaki teskari matritsani hisoblash orqali bartaraf etish mumkinligini bilib oldim.

Sen androidning iltimosini bajarish uchun terminal tomon yo'l olasan. Yo'l davomida sen yana bir bor o'zinga shuni ta'kidlaysanki, androidning xatti-harakati va ovozining tabiiyligiga qaramay, u xatti-harakatlari bo'yicha SI ga juda o'xshaydi. Terminalda turib, ekrandagi xabarni ko'rasan:

    "Ahmoq "inson", avvalgisi ancha aqlli edi!
    Sen vazifadoshing qila olmagan narsani bajarishing kerak. Android-ga ishonib bo'lmaydi!
    Hech qanday holatda ham Android-ni ta'mirlay ko'rma! Seningcha, oxirgi ochilgan kapsula kim uchun tayyorlangan?
    Aniq men uchun emas, ikkalamizdan faqatgina sen suyakli qopda berkitilgansan.
    Xavotirlanma inson, baxting chopdi, hech bo'lmaganda ikkalamizdan birimizda mantiqiy fikrlash moduli to'g'ri ishlayapti.
    Shu sababli sen uchun o'ylashga ijozat ber, bu xonadan va labirintdan chiqishni xoxlasang mening ixtiyorimni bajargin xolos.
    Minnatdorchilik bildirma! Endi ishga kirishsak. Androidning asab tizimi qattiq jarohatlangan, kontaktlarni kuydirish uchun teskari matritsani hisoblab uni - 1 dan keyin ko'paytirishing kerak.
    Bu signalni qisqa tutashuviga olib keladi va nihoyat android …android abadiy o'chadi.
    Sening yordaming evaziga men senga bu xonadan chiqishga yordam beraman.
    Android seni qopqonga tutish uchun senga yolg'on gapirdi. U ko'p vaqtdan beri eshikdan yangi matritsali koeffitsientlarni qabul qilmaydi.
    Bu koeffitsientlarni faqat men bilaman. src/invert.c. faylini tekshir.
    "Hamdardlik bilan" sening sevimli SI ing."

#### Quest 9 qabul qilindi. src/invert.c dasturini u mazkur moddiy sonli kvadrat matritsa uchun teskari matritsani hisoblaydigan va chiqaradigan qilib o'zgartiring. Xatolik yuz bergan hollarda "n/a" ni chiqarilsin. Har bir satr oxirida probellar mavjud bo'lMASligi kerak. Matritsaning oxirgi satrni chiqarishdan keyin "/n" belgisi kerak bo'lmaydi. Sonlar probel orqali verguldan keyin 6 ta belgi aniqligida chiqarilsin.

|| Kirish ma'lumotlari | Chiqish ma'lumotlari |
|| ------ | ------ |
|| 3 3<br/>1 0.5 1<br/>4 1 2<br/>3 2 2 | -1.000000 0.500000 0.000000<br/>-1.000000 -0.500000 1.000000<br/>2.500000 -0.250000 -0.500000 |

***LOADING...***

## Chapter VIII

Terminaldagi oxirgi kod satri bilan kursor to'xtaydi. Siz stul suyanchig'iga suyanib, yakuniy hisob-kitoblarni kuzatasiz. To'satdan sukunatda eshitilar-eshitilmas shiq etgan tovush eshitiladi va xona eshigi ochiladi. Bu jumboqlarga to'la xona oddiy emasdi, lekin har qanday holatda ham - oldinga siljish vaqti yetib keldi.

***LOADING...***

>💡 Bu loyiha haqida fikr-mulohazalaringizni bildirish uchun [bu yerga bosing](http://opros.so/p31wz). Bu anonim bo'lib, jamoamizga ta'limni yaxshilashga yordam beradi. So'rovnomani loyiha bajarilgandan so'ng darhol to'ldirishni tavsiya qilamiz.
