# D03T03. C tilidagi boshqaruv tuzilmalari

Annotatsiya: ushbu loyiha sizni C tilidagi asosiy boshqaruv tuzilmalari, shuningdek iterativ va rekursiv algoritmlar bilan tanishtiradi.

## Contents

1. [Kirish](#kirish) \
    1.1. [Loyihaga oid tavsiyalar](#loyihaga-oid-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 1. Room 4](#level-1-room-4)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1](#list-1) \
    3.1. [List 2](#list-2) \
    3.2. [List 3](#list-3)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. Basic control structures. Tom Kilburn](#quest-1-basic-control-structures-tom-kilburn) \
    4.2. [Quest 2. Basic control structures. Some problems with symbols](#quest-2-basic-control-structures-some-problems-with-symbols) \
    4.3. [Quest 3. Recursive](#quest-3-recursive) \
    4.4. [Quest 4. Table](#quest-4-table) \
    4.5. [Bonus Quest 5. Func](#bonus-quest-5-func)
5. [Chapter IV](#chapter-iv)

## Kirish

***PRELOAD...***

Sen birinchi darajaning navbatdagi xonasiga kirar ekansan birdan o‘ylab qolasan, go‘yoki xona oxirigacha yuklanmagan: buyumlar va devorlar bor, lekin hammasi nol va birlardan iborat jimirlab turgan to‘rga o‘xshaydi. Bir zumga qo‘rqub va vahima paydo bo‘ladi...

\> *C tilini o‘rganishni boshlaganlarning hammasida shunaqa bo‘ladimi?*

***PRELOAD...***

Birdan seni ro‘parangdagi devorda turgan nol va birlar asta yo‘qola boshlaydi va ularning o‘rnida yog‘och romdagi qandaydir axborot varag‘i paydo bo‘ladi. Kuraklaringga sovuq ter yuguradi, hatto peshonangda ham tomchilar ko‘rinadi. Ko‘rinishidan, SI ancha charchagan, sovitish tizimi ham yordam bermayapti. Ammo sen o‘qiydigan narsa qolgan barcha vaqt davomida seni ter to‘kishga majbur qiladi...

> Bugundan boshlab barcha dasturlar, natijalari to‘g‘riligiga qo‘shimcha ravishda, stil normalariga mosligi bo‘yicha ham tekshiriladi. Yechimlarni yuborishdan oldin dasturlarni lokal tekshirib ko‘rishing mumkin. Buni qanday qilish haqida `materials/instructions_for_testing_uz.md` faylida o‘qib olasan.

Nima bo‘lganini endigina anglab ulgurganingda, devorga yana nol-u birlar qayta paydo bo‘la boshlaydi va asta-sekin axborot yozilgan varaqni yutib yuboradi... ammo bu axborot sen uchun faqat bitta narsani anglatadi — ko‘proq ish. Lekin sifatli kod — bu zo‘r! Uni o‘qish va qo‘llab-quvvatlash osonroq. Shunday ekan, agar sendan keyin bu xonalarga yana kimdir tushib qolsa, u bemalol sening dasturlaringni o‘zgartirib, SI ga yana ma’qul bo‘ladigan holatga keltira oladi. Uning talablari esa albatta oshib boradi, u rivojlanmoqda-ku... Sen ham rivojlanishing shart!

### Loyihaga oid tavsiyalar
School 21 da qanday o‘qish kerak:
- Butun kurs davomida siz kerakli ma’lumotlarni mustaqil izlab borasiz. Google yoki GigaChat kabi barcha mavjud qidiruv vositalaridan foydalaning. Ma’lumot manbalariga diqqatli bo‘ling: tekshiring, o‘ylang, tahlil qiling, solishtiring.
- O‘zaro bilim almashish (P2P, Peer-to-Peer) — bu jarayon ishtirokchilar bir-biri bilan bilim va tajriba almashinuvidir; bunda ular bir vaqtning o‘zida ham o‘qituvchi, ham o‘quvchi rolini bajaradilar. Bu yondashuv nafaqat o‘qituvchilardan, balki bir-biringizdan o‘rganishga imkon beradi va materialni yanada chuqurroq tushunishga yordam beradi.
- Yordam so‘rashdan uyalmang: atrofingizda xuddi siz kabi ilk bor shu yo‘ldan o‘tayotgan pirlar bor. Yordam so‘raganlarga javob berishdan qo‘rqmang. Sizning tajribangiz qadrli — uni boshqalar bilan bemalol, tortinmay bo‘lishing.
- Ko‘chirmang; agar kimningdir yordamidan foydalanayotgan bo‘lsangiz, doim oxirigacha tushunib olishga harakat qiling — nima uchun, qanday va nimaga aynan shunday qilinadi. Aks holda o‘rganishingning hech qanday foydasi bo‘lmaydi.
- Agar bir joyda qotib qolgan bo‘lsangiz va hamma narsa sinab ko‘rilgandek tuyulsa-yu, baribir yachim topilmayotgan bo‘lsangiz — biroz tanaffus qiling! Ishoning ushbu uslub ko‘plab dasturchilarga yordam bergan. Toza havodan bahra olib, aqlni qayta ishga tushiring — ehtimol aynan shu safar yechimning o‘zi yaqqol paydo bo‘ladi.
- Muhimi faqat natija emas, balki o‘qish jarayonining o‘zi. Vazifani shunchaki yechim topish emas, balki uni QANDAY yechishni tushunib olish kerak.
- Loyiha bajarilayotganda vaqtni nazorat qilib boring. Yodda tuting har kuni kamida bitta sinovdan o‘tishingiz kerak.
- Har bir topshiriq loyiha yakunida bir nechta tekshiruvdan o‘tadi: chek-list orqali P2P-tekshiruv, autoteslar to‘plami bilan tekshiruv, kod uslubini tekshirish, statik analizdan o‘tkazish, xotira sarfini tekshirish.

Loyiha bilan qanday ishlash kerak:

- Foydali videomateriallarni Platformadagi Projects (Media) bo‘limidan topishingiz mumkin.
- Loyihani bajarishdan oldin uni GitLab’dan o‘sha nomdagi repozitoryadan klonlab olish kerak.
- Barcha kod fayllari klonlangan repozitoriy ichidagi `src/` papkasida yaratilishi lozim.
- Loyihani klonlagandan so‘ng `develop` nomli yangi branch yarating va dastur yaratishni shu branch’da olib boring. Keyin GitLab’ga ham `develop` branch’ni push qilishing kerak.

## Chapter I
## Level 1. Room 4

![level1_room4](misc/rus/images/level1_room4.png)

***LOADING Level 1...*** \
***LOADING Room 4...***


            Yuklanish 10%
            Yuklanish 20%
            Yuklanish 30%
            Yuklanish 40%
        
        Urinish 1...  Muvaffaqiyatsiz...
        Urinish 2...  Muvaffaqiyatsiz...
        Urinish 3...  Muvaffaqiyatsiz...

\> *Nima bo‘lyapti?*

Xona to‘liq yuklanmadi shekilli, uni tiklash uchun yordam kerak.

\> *Terminalni topish*

Sen terminga qaraysan. Go‘yoki faqat shuning o‘zi inicializatsiyadan o‘tishga ulguribdi. Atrofda mutlaq “bo‘shliq”.

> *Terminalda ma'lumotni o‘qish*

Ko‘p tushunarsiz o‘n oltilik sanoq sistemasida sonlar, so‘ngra:

Agar bu matnni organik tirik mavjudot o‘qiyotgan bo‘lsa, qabul...
Yordam kerak, qabul.
Men oldingi xonalardan ba’zi ma’lumotlarni saqlab qola oldim.
Xonaning keyingi tiklanishi faqat mening algoritmlarimni sozlashga bog‘liq, senga kerak bo‘ladi...

...

Xato...

...

\> *Buni qanday tushunish kerak?*

Sen labirintni boshqarib turgan SI yordamisiz qolding shekilli. Nima ham qilardik. Xonani qanday tiklash va yo‘lni davom ettirishni endi o‘zing o‘ylab topishingga to‘g‘ri keladi.

\> *Atrofga qarash*

Yaxshilab razm solganingda, atrof unchalik ham mutlaq bo‘m-bo‘sh emasligini payqaysan. Qisman yuklangan xonada axborotdan iborat haqiqiy betartiblik: tartibsiz ma’lumotlar xona bo‘ylab uyoq-buyoqqa uchib yuribdi. Manzara juda g‘alati ko‘rinadi.

\> *Oldinga yurish*

Sen deyarli paypaslab oldinga qarab yurasan. Juda yoqimli sayr deyish qiyin. Xonaning eng chekka burchagida, ma’lumotlar xayqalog‘i orasida nimadir mazmunli ko‘rinadi. Xonaning ichkarisiga qarab yo‘l ochib, oxiri stolga o‘xshash bir narsani topasan. Stol ustida qog‘oz varaqalari yotibdi. Ulardan birida, aftidan, qandaydir algoritm chizilgan.

\> *Qog‘oz varaqni o‘qish*

![level1_room4_paper](misc/rus/images/level1_room4_paper.png)

***LOADING...***

## Chapter II
## List 1

> Nosozlik yuz berishidan oldin senga bir nechta topshiriqlar tuzib ulgurdim, shuning uchun hali hammasi yo‘qolganicha yo‘q. Sen xonani tiklab, labirint bo‘ylab o‘z yo‘lingni davom ettira olasan...

\> *Keyingi varaqni olish*

***LOADING...***

## List 2

Sen navbatdagi varaqni olasan:

>Deykstra tamoyillari (struktur dasturlash tamoyillari):
>
> - 1-tamoyil. goto shartsiz o‘tish operatoridan voz kechish kerak.
> - 2-tamoyil. Har qanday dastur uchta asosiy boshqaruv konstruksiyasi asosida tuziladi: ketma-ketlik, tarmoqlanish, sikl.
> - 3-tamoyil. Dasturda asosiy boshqaruv konstruksiyalari bir-birining ichiga istalgan tartibda joylashtirilishi mumkin.
> - 4-tamoyil. Takrorlanadigan yoki mantiqan alohida ajralib turadigan dastur qismlarini quyi dasturlar (protsedura va funksiyalar) ko‘rinishida yozish mumkin.
> - 5-tamoyil. Har bir mantiqan yakunlangan ko‘rsatmalar guruhini blok sifatida yozilishi lozim. Bloklar struktur dasturlashning asosi hisoblanadi.
> - 6-tamoyil. Sanab o‘tilgan barcha konstruksiyalarda bitta kirish va bitta chiqishi bo‘lishi kerak.
> - 7-tamoyil. Dastur bosqichma-bosqich, «yuqoridan pastga» (top-down method) usuli bilan ishlab chiqiladi.

Varaqning orqa tomonida qo‘lda yozilgan matnni ko‘rasan:

> Global o‘zgaruvchilardan foydalanish taqiqlanadi, chunki ular yashirin bog‘lanishlar sonining ortishiga olib keladi. Bu esa o‘z navbatida dastur kodining masshtablanuvchanligi va o‘qish qulayligiga yomon ta’sir qiladi hamda aniqlash qiyin bo‘lgan xatolarga sabab bo‘ladi.

> *Bu varaq tasodifan shu to‘plamga tushib qolgan shekilli... Yoki yo‘qmi? Umuman olganda, juda foydali ko‘rinadi. Keyingi varaqni olish.*

Sen navbatdagi varaqni olasan...

***LOADING...***

## List 3

Varaq qandaydir g‘alati jadvalning bir bo‘lagiga o‘xshaydi. Ehtimol, u qandaydir shifrlash yoki kodlash uchun ishlatilgan bo‘lsa kerak.

> ASCII jadvali: davomi

|  | 8 | 9 | A | B | C | D | E | F |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 4 | H | I | J | K | L | M | N | O |
| 5 | X | Y | Z | [ | \ | ] | ^ | _ |
| 6 | h | i | j | k | l | m | n | o |

>...

\> *Keyingi varaqni olish...*

***LOADING...***

## Chapter III
## Quests: Level 1. Room 4

> **Diqqat!** Ushbu kun kvestlarida massivlar yaratish va dinamik xotiradan foydalanish taqiqlanadi. Ruxsat etilgan kutubxonalar: `<stdio.h>`, `<math.h>`.

## Quest 1. Basic control structures. Tom Kilbur

\> *Varaqni o'qish

>Boshidan boshlaymiz.
>
>EHM xotirasida to’liq saqlanadigan birinchi dastur 1948 yil bahorida Tom Kilburn tomonidan “Kichik o’lchovli Eksperimental Mashina” (Small Scale Experimental Machine, SSEM) yoki ular uni erakalab Baby uchun ishlab chiqilgan deb atashgan. 
>
>Ayrim hamkasblarining fikricha, bu ular tomonidan yozilgan birinchi va oxirgi dasturi edi. Babydan yechish so‘ralgan masala berilgan a sonining eng katta tub bo‘luvchisini topish edi. Buning uchun barcha raqamlar saralanishi amalga oshiriladi. Bo'linishning o'zi ayirish yo'li bilan amalga oshirildi, chunki bo'linish operatsiyasi uchun apparat yordami yo'q edi. Aytgancha, bunday imkonyat hali ham ba'zi arzon mikrokontroller modellarida mavjud emas.

> Birinchi topshiriq: Tom Kilburn yo‘lidan borish. Sen asosiy boshqaruv tuzilmalaridan — ketma-ketlik, tarmoqlanish va takrorlanishdan (sikldan), shuningdek qo‘shish, ayirish va ko‘paytirish amallaridan foydalanishing mumkin. Bo‘lish amalidan foydalanish mumkin emas — bu modul mikrokontrollerlarda ishga tushirish uchun mo‘ljallangan. `src/1948.c` faylini yarat, u kompilyatsiya va ishga tushirilgandan so‘ng `stdin` orqali bitta son qabul qiladi va shu son uchun eng katta tub bo‘luvchini hisoblaydi. Ko‘raylik-chi, nimalarga qodirsan.
>
> Eslab qol: sonning eng katta tub bo‘luvchisi — bu uning eng katta tub ko‘paytuvchisi ham hisoblanadi.

\> *Terminalgа qaytish*

Sen sevimli terminingga qaytasan. Boshqa hech qanday ishora yo‘qligini inobatga olganda, bu masalani yechib ko‘rmaslik uchun sabab ham yo‘q. Eslab qol: barcha yechimlarni repozitoriyga yuklashing kerak, dasturing esa kirish ma’lumotlarini to‘g‘riligiga tekshirishi lozim.

### Quest 1 qabul qilindi. `src/1948.c` dasturini yarating: u berilgan butun `a` sonining eng katta tub bo‘luvchisini topib, ekranga chiqarishi lozim. Bu qiymatni hisoblash uchun alohida funksiya yozish kerak. Bo‘lish amali va bo‘lishdan qoldiq olish amalidan foydalanish mumkin emas. Zarurat tug‘ilganda bo‘lishni ketma-ket ayirishlar yordamida amalga oshirishga ruxsat etiladi. Xatolik yuz bergan holatlarda ekranga "n/a" chiqarish kerak.

>**MUHIM!** `system()` funksiyasi va tizim yadrosiga bevosita murojaat qilishi mumkin bo‘lgan shunga o‘xshash boshqa funksiyalar orqali tizim chaqiruvlarini bajarish taqiqlanadi. Ushbu cheklov keyingi barcha topshiriqlarga ham tatbiq etiladi.

| Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| ------ | ------ |
| 100 | 5 |
| -4 | 2 |

***LOADING...***


## Quest 2. Basic control structures. Some problems with symbols.

\> *`src/1948.c` faylini push qilish*

Aftidan, SI buni kutayotgan edi. Ekranda yana matn paydo bo'ldi.

Sening yechimingni oldim. Ko‘ramiz.
Agar masala chindan ham yechilgan bo‘lsa, 
bu xonani tiklashimizga yordam berishi mumkin.
Bu yerda aynan eng katta bo‘luvchilar bilan bog‘liq bir muammo bor edi.
Ular bilan har doim muammo bor.

Xonani tiklashga urinish:

            10%
            20%
            30%
            40%
            50%
            60%
            
            Xatolik…
            Xatolik…

Hmm, demak gap faqat eng katta bo'luvchilarda emas ekan.
Hech bo'lmaganda endi ular bilan boshqa muammo bo’lmaydi.
O’zi xonani umuman tiklash shartmi? Shunday ham yaxshi ko'rinyapti.
Eng katta bo'luvchilarni qidirishda davom etamiz ...

\> *Kiritish: “Xonani tiklash”*

Ekrandagi natija:

    Mayli, davom etamiz.

    Tiklashning zaxira moduli yuklanmoqda...
    Modul yuklandi.
    Tiklash moduli ishga tushirilmoqda...
    48 45 4C 4C 4F 77 4F 52 4C 44 00

\> *Nima bu? Qandaydir kodga o'xshaydi*

Senga ishga tushirilgan zaxira modulining chiqish (output) kod qismida muammo bordek tuyuladi. Ehtimol, kirish (input) tomonida ham shunaqa, shuning uchun u seni tushunmaydi. Ekrandagi raqamlar esa senga varaqdagi jadvalni eslatadi. Ehtimol, o‘sha jadvalga yana bir bor qarab chiqish kerakdir.

Ko‘rinishidan, bu yerda ikkita rejimda ishlaydigan kichik yordamchi dastur yozish talab qilinadi: kodlash va koddan chiqarish (dekodlash). Dastur ish rejimi buyruq qatori parametri orqali tanlanishi kerak:
0 — kodlash, 1 — dekodlash. Dekodlash rejimida dastur stdin dan bo‘shliq bilan ajratilgan 16 razryadli butun sonlar qatorini qabul qilishi va stdout ga bo‘shliq bilan ajratilgan dekodlangan belgilarni chiqarishi kerak. Kodlash rejimida esa aksincha — belgilarni sonlarga aylantirishi lozim.
Kodlash (belgi -> son) va dekodlash (son -> belgi) bo‘yicha kichik vazifalarning o‘zini alohida funksiyalar ko‘rinishida ajratib yozgan ma’qul. Dastur joylashgan faylni repozitoriyada `src/char_decode.c` joylashni unutmа.

#### Quest 2 qabul qilindi. `src/char_decode.c` dasturini yarating: u buyruq qatori parametrida ish rejimini qabul qiladi (`0` — kodlash, `1` — dekodlash). Agar dekodlash rejimi tanlansa, dastur `stdin` dan bo‘sh joy bilan ajratilgan ikki belgili satrlarni qabul qiladi va `stdout` ga shularning dekodlangan belgilarini yana probel bilan ajratib chiqarishi kerak. Kodlash rejimida esa aksincha — belgilarni ikki belgili satrlarga aylantirish bajariladi. Kodlash va dekodlash bo‘yicha kichik vazifalarning har biri alohida funksiya ko‘rinishida yozilishi kerak. ASCII-jadvalga alohida e’tibor qaratish lozim. Xatolik yuz bergan holatlarda ekranga `n/a` chiqarish kerak. Kirish tugaganini bildiruvchi belgi — qator tashlash (newline) belgisi hisoblanadi.

| Buyruqlar qatori parametrlari | Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| ------ | ------ | ------ |
| 0 | W O R L D | 57 4F 52 4C 44 |
| 0 | WORLD | n/a |
| 1 | 48 45 4C 4C 4F | H E L L O |
| 1 | 48454C4C4F | n/a |

***LOADING...***

> UNUTMANG! Barcha dasturlaringiz uslub normasi uchun sinovdan o'tkaziladi. Sinovlarni o'tkazish bo'yicha ko'rsatmalar ham `materials` papkasida joylashgan

## Quest 3. Recursive.

\> *Dastur ishlab chiqildi*

    46 49 42 4F 4E 41 43 43 49 32 31

\> *Zaxira modulining natijasini dekodlash uchun ishlab chiqilgan dasturdan foydalanish*

Siz xabarni qayta shifirlaysiz. boshqotirmaga o‘xshaydi. Ehtimol, uni yechish uchun kichik dastur yozish kerak. Hisoblash natijasini dastur stdout ga chiqarishi lozim. Uni `src/quest3.c` fayliga joylashtirishni unutmа.

#### Quest 3 qabul qilindi. `src/quest3.c` dasturini yarating: u rekursiv algoritm yordamida n-chi Fibonachchi sonini hisoblab, ekranga chiqarishi lozim. n-chi Fibonachchi sonini topish alohida funksiya ko‘rinishida yozilishi kerak. Son standart kirish oqimi orqali kiritiladi. Xatolik yuz bergan holatlarda ekranga `n/a` qaytaring.

| Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| ------ | ------ |
| 21 | 10946 |

***LOADING...***


## Quest 4. Table.

\>*src/quest3.c dasturini ishga tushirish*

    4F 4B

    Xonani tiklashga urinish...

            10%
            20%
            30%
            40%
            50%
            60%
            70%
            80%
            90%
            99%
            
            Xatolik...

\> *Razm solish*

Atrofingdagi xona nihoyat odatdagi ko‘rinishini qayta oldi. Devorlar mayin, ko‘zni toliqtirmaydigan ranglarda bo‘yalgan, xonani esa shinam yarim qorong‘ulik va muloyim musiqa to‘ldirib turibdi.
Lekin eshik bo‘lishi kerak bo‘lgan joyda qorong‘ulik, tubsiz bo‘shliq turibdi, ba’zan yemirilayotgan piksellar to‘ri va bash buyruqlar satrlari ko‘zga chalinib qoladi.
Eshik hali ham tiklanmaganligi mutlaqo ayon.

\> *SI modulini ishga tushirish*

    Boshlash... 
    Ishga tushirish.

    Xona qayta tiklandi. Nega meni ishga tushirding? Men dam olayotgan edim.

\> *Xona tiklanmadi. Eng muhimi – eshik yetishmayapti*

Kimga qanaqa.
Kimning nazari tashqariga qaratilgan bo‘lsa, u uchun eng muhimi — eshik.
Kim ko‘proq ichki dunyoga yuzlanayotgan bo‘lsa, u xonaning ichki ko‘rinishi va muhitiga ko‘proq ahamiyat beradi.

Falsafiy gaplar. Bu biroz sergaklantiradi. Sun’iy intellekt bilan ehtiyotroq bo‘lganing ma’qul — uning “miyasida” nimalar aylanayotganini hech qachon aniq bila olmaysan.


\> *Kiritilsin: "Eshikni tiklash uchun nima qilish kerak?"*

Kutilmaganda batafsil javob:

    Afsuski, eshik tenglamasini ifodalovchi fayl shikastlangan.
    Agar eshikka shunchalik qiziqayotgan bo‘lsang, uni qayta generatsiya qilishingga to‘g‘ri keladi.
    Menda analitik formulalar va ifodalarni qabul qilish bilan bog‘liq muammolar bor,
    shuning uchun faylda izlanayotgan funksiyaning diskret qiymatlari jadvali bo‘lishi kerak.
    Bizni avvalo -π dan +π gacha bo‘lgan oraliq (chegaralari bilan birga) qiziqtiradi.
    π sonining juda yuqori aniqlikda bo‘lishi shart emas, taxminan 20 ta raqamgacha aniqlik yetarli.
    O‘sha sonning o‘zini kodda takrorlab yozib yurmaslik uchun alohida o‘zgaruvchi yoki direktiva sifatida saqlagan ma’qul.
    Bu oraliqda bizga aniq 42 ta o‘lchov nuqtasi kerak bo‘ladi.
    Fayldagi birinchi ustun — bu abstsissa o‘qi (x o‘qi) qiymati,
    ikkinchi, uchinchi va to‘rtinchi ustunlar esa shu nuqtadagi uchta funksiyaning qiymatlari bo‘ladi.
    Jadvalga hech qanday sarlavha kerak emas.
    Barcha qiymatlar verguldan keyin 7 ta raqamgacha aniqlik bilan yoziladi.
    Ustunlar orasidagi ajratgich — «|» belgisi.
    Va iltimos, ta’riflanish sohasi bo‘yicha ehtiyot bo‘l: noto‘g‘ri nuqtaga kirib ketma.
    Funksiyalar uchta bo‘lishi kerak, chunki qaysi funksiya eshikni ifodalashga mos tushishini aniq bilmaymiz.
    Loglarda saqlanib qolgan yozuvlarga qaraganda, bu funksiya quyidagilardan biri bo‘lishi mumkin:
    birlik diametrli Verzyera Anyezi,
    musbat yarim tekislikdagi birlik oraliqli Bernulli lemniskatasi
    yoki kvadratik giperbola.
    Algoritmni `src/door_functions.c` fayli ko‘rinishida tayyorla,
    algoritming ishlash natijasini esa `src/data/door_data.txt` faylida saqla.
    Faylga yozish uchun bash terminalida chiqishni faylga yo‘naltirishdan foydalanishing mumkin.
    Formulalarni esa quyida topasan.

Birlik diametrli Verzyera Anyezi: \
![Верзьера Аньези](misc/images/va.png) 

Musbat yarim tekislikdagi birlik intervalli Lemniskata Bernulli: \
![Лемниската Бернулли](misc/images/lb.png) 

Kvadratik giperbola: \
![Квадратичная гипербола](misc/images/g.png) 

#### Quest 4 qabul qilindi. `src/door_functions.c` dasturini yarating: u uchta funksiya bo‘yicha jadval hisoblab, ekranga chiqarishi lozim:<br>
#### - birlik diametrli Verzyera Anyezi;
#### - musbat yarim tekislikda (Y > 0) birlik oraliqli **Bernulli lemniskatasi**;
#### - kvadratik giperbola.<br>
#### Birinchi ustunda `x` qiymatlari `–π` dan `+π` gacha (chegaralar ham qo‘shilgan), va shu oraliqda aniq 42 ta o‘lchov nuqtasi bo‘lishi kerak. Ikkinchi, uchinchi va to‘rtinchi ustunlarda esa shu nuqtadagi uchta funksiyaning qiymatlari joylashadi. Jadval uchun sarlavhalar kerak emas.
#### Barcha qiymatlar verguldan keyin 7 ta raqamgacha aniqlik bilan chiqarilishi kerak, buning uchun yuqori aniqlik sabab double turidan foydalanish lozim. Ustunlar orasidagi ajratgich — `|` belgisi. Jami jadvalda 42 ta yozuv bo‘lishi shart. Dastur natijasini `src/data/door_data.txt` fayliga joylashtirish kerak, lekin faylga yozishni dastur ichida amalga oshirish shart emas — buning o‘rniga bash terminalida chiqishni faylga yo‘naltirishdan foydalanish mumkin. Agar funksiyalardan biri ma’lum bir nuqtada aniqlanmagan bo‘lsa, jadvaldagi mos katakda “-” belgisi bo‘lishi kerak.

Natija:

-3.1415927 | 0.0919997 | - | 0.1013212<br/>
-2.9883442 | 0.1007029 | - | 0.1119796<br/>
...............e.r.r.o.r.......................................................

-1.3026116 | 0.3708103 | 0.3061966 | 0.5893457<br/>
-1.1493632 | 0.4308421 | 0.4310262 | 0.7569818

....................................k.i.l.l..m.e..............................

<br/>SI xatolik<br/>

***LOADING...***

## Bonus Quests: Level 1. Room 4
## Bonus Quest 5. Func

\> *"Fayllar tayyor" deb kiriting*

Terminalda javob:

    Ajoyib. Eshikni tiklash algoritmini ishga tushirish mumkin.
    Biroq, agar dasturingiz o'zgartirilsa va unda funksiya grafiklarini chop etish qo’shilsa, uni tezlashtirish imkoni mavjud.
    Ortiqcha elementlarsiz, faqat bir xil aniqlash sohasida ketma-ket, biri boshqasining ostidagi grafiklarni.
    Faqat o'zingiz bilgan narsadan foydalanish kifoya qiladi.
    Absissa o'qi bo'yicha masshtab – 42 bo’lma, ordinata o'qi masshtabi – 21.
    “*” belgisi yordamida chizish.
    Biroq, bu zarur emas – tezlashuv kichik bo'ladi.

#### Quest 5 qabul qilindi. `src/door_functions.c` dasturini u terminalda “ \* ” belgilaridan foydalangan holda hisoblanuvchi funksiyalar grafiklarini chizadigan qilib to’ldiring. Absissa o'qi bo'yicha masshtab – 42 , ordinata o'qi masshtabi – 21. Koordinata o'qlarining joylashishi va aylanishi muhim emas. Yozilgan kodni door_functions_print.c fayliga saqlang.

***LOADING...***


## Chapter IV

    Fayllar yuklanmoqda...
    Eshik tenglamasini izlash...
    Egri chiziqlarni tekislash...
    Eshiklar generatsiyasi...
    Eshiklar integratsiyasi...

\> *Atrofga razm solish*

Xonaning eng chekka qismida eshik paydo bo'ldi.

\> *Chiqishga harakat qilish*

Eshik qulflanmagan ekan. Ko'rinishidan, SI bunga qodir emas edi.

Tabriklaymiz, siz yana xonadan chiqa oldingiz!

***LOADING...***

💡**[Bu yerga bosing](http://opros.so/p31wz), ushbu loyiha bo‘yicha biz bilan o‘z fikr-mulohazalaringizni bo‘lishish uchun.
So‘rovnoma anonim bo‘lib, o‘qitish jarayonini yanada yaxshilashimizga yordam beradi.
Loyihani yakunlaganingizdan so‘ng so‘rovnomani darhol to‘ldirishingizni tavsiya qilamiz.**
