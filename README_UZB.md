# D07T04. Ko'rsatkichlar va massivlar 

Annotatsiya: ushbu loyiha sizga ko'rsatkichlar va massivlar bilan tanishish imkonini beradi.

## Contents

1. [Kirish](#kirish) \
    1.1. [Loyihaga tavsiyalar](#loyihaga-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 2. Room 1](#level-2-room-1)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1. Pointer](#list-1-pointer) \
    3.2. [List 2. Listing](#list-2-listing) \
    3.3. [List 3. Operations](#list-3-operations) \
    3.4. [List 4. Array](#list-4-array) \
    3.5. [List 5. Equality](#list-5-equality)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. Arguments and pointers](#quest-1-arguments-and-pointers) \
    4.2. [Quest 2. Data I/O](#quest-2-data-io) \
    4.3. [Quest 3. Data metrics](#quest-3-data-metrics) \
    4.4. [Quest 4. Search](#quest-4-search)
5. [Chapter IV](#chapter-iv)
6. [Chapter V](#chapter-v) \
    6.1. [Level 2. Room 2](#level-2-room-2)
7. [Chapter VI](#chapter-vi) \
    7.1. [List 1 (Room 2)](#list-1-room-2)
8. [Chapter VII](#chapter-vii) \
    8.1. [Quest 5. Sort & memory](#quest-5-sort--memory) \
    8.2. [Quest 6. Several arrays](#quest-6-several-arrays) \
    8.3. [Quest 7. Cyclic shift](#quest-7-cyclic-shift) \
    8.4. [Bonus Quest 8. Arbitrary-precision arithmetic](#bonus-quest-8-arbitrary-precision-arithmetic)
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
- Loyihani klonlashtirgandan so'ng, `develop` tarmog'ini yaratish va ishlab chiqiluvchi narsalarni unda amalga oshirish kerak. Shundan so'ng, GitLab'ga `develop` tarmog'ini ham push qilish kerak.

## Chapter I
## Level 2. Room 1

![level2_room1](misc/rus/images/level2_room1.png)

***LOADING Level 2… \
LOADING Room 1…***

Birinchi daraja osonlikcha qo'lga kiritilmadi, lekin sen baribir uddalading. Ushbu labirintning yangi darajasi eskisidan farq qiladimi yoki yo'qmi, buni aytish qiyin. Lekin devorlarning rangi sal boshqacharoq... yoki shunday tuyulyaptimi? Bu darajadagi SI xotirjamroq bo'lsa yaxshi bo'lardi.

Bu sening miyangda g'ujg'on o'ynayotgan fikrlarning bir parchasi, xolos.

\> *Atrofga nazar tashlash*

Xona esa odatdagidan boshqacharoq. Qog'ozlari sarg'ayib ketgan eski matritsali printer qo'shilgan kompyuter xuddi geometrik tarzda hisoblangandek, markazda, shundoqqina polda turibdi. Uning yonida g'ijimlangan yostiq, pechenye uchun likopcha (undagi ushoqlarning ko'pligi shunga ishora qiladi) va allaqachon ichilgan choy solingan piyola (qurib ketgan choy xaltachasi ham shunga ishora qiladi). Pol va devorlar bir tekisda raqamlar to'plami yozilgan varaqlar bilan qoplangan. Ularning ustiga esa qizil iplar tortilgan. Josuslik filmi, undan boshqa narsa emas.

\> *Yostiqchaga o'tirish*

Siz yostiqchaga o'tirasiz. Yumshoqqina. \
Qulaylik++

![level2_room1_pillow](misc/rus/images/level2_room1_pillow.png)

\> *Likopcha va piyolani surib qo'yish*

Siz likopcha bilan piyolani nariroq surib qo'yasiz. Bu unchalik yordam bermadi. \
Qulaylik--

\> *Monitorga qarash*

Terminalda birgina satr bor: "Segmentation fault". Kursor miltillaydi.

\> *Polga qarash*

Ko'plab bir turdagi varaqlar orasida siz qizil ip bilan tikilgan "samizdat" bukletini ko'rasiz. Ha, metaforadek eshitiladi.

\> *Bukletni olish*

Buklet tez-tez qo'lga olinganligi sezilib turadi. U bilan ehtiyotkorona munosabatda bo'lish kerak. Muqovada faqat bitta ko'zga tashlanmaydigan, bosma mashinka bilan aniq terilgan so'zni ko'rasiz: "POINTER."

Undagi shakllantirib bo'lmaydigan nimadir tanangizni yengil titroqqa soladi.

\> *Sahifani varaqlash*

***LOADING...***

## Chapter II
## List 1. Pointer

>In 1955, Soviet computer scientist Kateryna Yushchenko invented the Address programming language that made possible indirect addressing and addresses of the highest rank - analogous to pointers. This language was widely used on the Soviet Union computers. However, it was unknown outside the Soviet Union and usually Harold Lawson is credited with the invention, in 1964, of the pointer. In 2000, Lawson was presented the Computer Pioneer Award by the IEEE "for inventing the pointer variable and introducing this concept into PL/I, thus providing for the first time, the capability to flexibly treat linked lists in a general-purpose high-level language". His seminal paper on the concepts appeared in the June 1967 issue of CACM entitled: PL/I List Processing. According to the Oxford English Dictionary, the word pointer first appeared in print as a stack pointer in a technical memorandum by the System Development Corporation.

\> *Sahifani varaqlash*

***LOADING...***

## List 2. Listing

    void main() {
        int a = 2;      // a == 2
        int b = 4;      // b == 4
        int *p = 0;     // p == 0
        p = &a;         // p == o'zgaruvchi a manzili
        *p = 3;         // a == 3... yoki yo'q?
        p++;            // p == o'zgaruvchi b manzili ??!?!?
        (*p)++;         // b == 5 O_o WTF
        *p = *(p - 1);  // b == a == 3...
    }


Kimdir POINTER nimaligini tushunishga uringanga o'xshaydi...

\> *Sahifani varaqlash*

***LOADING...***

## List 3. Operations

> Tiplashtirilgan ko'rsatkich ustida bajarilishi mumkin bo'lgan amallar
> (balki, men buni hech bo'lmaganda shunday eslab qolarman):
>- manzilni olish,
>- ko'rsatkich nomini o'zgartirish,
>- songa qo'shish,
>- ko'rsatkichlarni ayirish,
>- ko'rsatkichlarni taqqoslash,
>- ko'rsatkichlar ustida mantiqiy amallar,
>- ko'rsatkichlarni o'zlashtirish.

\> *Sahifani varaqlash*

***LOADING...***

## List 4. Array

> YODDA TUTING!
>- C tilida Massivlar mavjud emas!
>- `int a[10]` - bu massiv emas!
>- Bu ko'rsatkich! Hamma narsa ko'rsatkich!
>- Funksiya ham ko'rsatkich.
>- Sen ham ko'rsatkichsan.
>- Ha, yo'lakdagi "odamlar" ham ko'rsatkichlardir.
>- Tajriba va o'rganish uchun qulflangan...

Telba odamning yozuvlariga juda o'xshaydi. Shubhasiz, ular aynan o'shanday.

\> *Sahifani varaqlash*

***LOADING...***

## List 5. Equality

    void main() {
        int a[10];
        a[2] == *(a + 2) == *(2 + a) == 2[a]; //!!!!!!!!!!!!!!!
    }


\> *Ha. Juda ma'lumotlarga boy. Sahifani varaqlash*

Qolgan sahifalar juda g'ijimlangan va hammasiga chizib tashlangan. Hech narsani tushunib bo'lmaydi. Aftidan, sening vazifadoshing bu masalalarni anglash uchun uzoq kurashgan bo'lsa kerak... Va u bunda unchalik ham yaxshi natijaga erisholmagan. \
Qani, endi ko'ramiz, bu sening qo'lingdan kelarmikin?

\> *Bu gijgijlashga o'xshaydi*

Hechamda. Shunchaki hikoyachi va o'yinchi o'rtasidagi do'stona suhbat. Hammasi odatdagiday.

\> *Ixtiyoriy harakat bilan Enter tugmasini bosish*

    AI Data Analyzer v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!     
    2. Load module #2... Success!
    3. Load decision decision-making module 
    3.1. Load maxmin module

    Segmentation fault

***LOADING...***

## Chapter III
## Quests: Level 2. Room 1

>**Diqqat!** Bu kungi kvestlarda dinamik xotiradan foydalanish taqiqlanadi.

## Quest 1. Arguments and pointers
\> *repozitoriydagi src papkasini ko'rish*

Siz bir nechta fayllarni, shu jumladan `maxmin` modulini ko'rasiz.

\> *`maxmin` modulini alohida ishga tushirish*

    Segmentation fault

Aftidan, uni tuzatishga to'g'ri keladi.

\> *Butun hayotim davomida `maxmin`-modullarni tuzatishni orzu qilganman...*

Nihoyat orzuing ushaladi!

\> *Eslatmani ochish*

> UNUTMANG! Barcha dasturlaringiz uslub me'yori va xotira sizib chiqishi bo'yicha sinovdan o'tkaziladi. Testlarni ishga tushirish bo'yicha ko'rsatmalar hali ham materials papkasida joylashgan.

#### Quest 1 qabul qilindi. `src/maxmin.c` dasturiga dastur yig'iladigan va to'g'ri ishlaydigan (3 ta butun sondan max va min ni topib, ekranga chiqaradigan) qilib tuzatishlar kiritish kerak. Dastur tuzilishi o'zgartirilmasin. Noto'g'ri kiritish holatida "n/a" ni chiqarilishi kerak.

>**MUHIM!** Tizim yadrosiga to'g'ridan-to'g'ri murojaat qilishi mumkin bo'lgan `system()` funksiyasi va unga o'xshash boshqa funksiyalar yordamida tizim chaqiruvlarini amalga oshirish taqiqlanadi. Ushbu taqiq barcha keyingi vazifalarga ham taalluqlidir.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 1 2 3 | 3 1 |

***LOADING...***

## Quest 2. Data I/O

\> *Tayyor*

    AI Data Analyzer v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!     
    2. Load module #2... Success!
    3. Load decision decision-making module 
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module
    
    Segmentation fault

\> *Oqshom borgan sari qiziqarli bo'lib boryapti...*

Hozir kun. Ehtimol...

\> *repozitoriydagi src papkasini ko'rish*

Papkada hali ham `squaring` moduli mavjud.

\> *`squaring` modulini alohida ishga tushirish*

    Segmentation fault

Bu yerda ham tuzatadigan narsa bor. Bu nimasi endi?

#### Quest 2 qabul qilindi. `src/squaring.c` dasturiga dastur yig'iladigan va to'g'ri ishlaydigan (stdin orqali butun sonlar massivini qabul qilib, ularni kvadratga ko'taradigan va stdout ga chiqaradigan) qilib tuzatishlar kiritish kerak. Noto'g'ri kiritish holatida "n/a" chiqarilishi kerak. Dekompozitsiyani kamaytirish mumkin emas - funksiyalarni faqat zarur hollarda qo'shish mumkin, lekin olib tashlash mumkin emas.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 3<br>1 2 3 | 1 4 9 |

***LOADING...***

## Quest 3. Data metrics

\> *Tayyor*

    AI Data Analyzer v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!     
    2. Load module #2... Success!
    3. Load decision decision-making module 
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module... Success!
    3.2. Load stat module
    
    ERROR 

"Yana qancha chidash mumkin", — degan fikr miyangizdan o'ta boshlaydi.

\> *repozitoriydagi src papkasini yana ko'rish*

Papkada `stat` moduli joylashgan. U deyarli bo'sh. Ko'rinib turibdiki, u ma'lumotlar massivi bo'yicha statistik ko'rsatkichlarni hisoblash uchun mo'ljallangan.

\> *Matematik statistika darsligini ochish*

Sizning suyukli telba do'stingiz, afsuski, uni qoldirib ketmabdi. Shunday taxmin qilishga to'g'ri keladi.

#### Quest 3 qabul qilindi. Kerakli funksiyalarning amalga oshirilishini `src/stat.c` dasturiga dastur yig'iladigan va to'g'ri ishlaydigan (biz diskret bir xildagi taqsimot bilan ishlayotganimizni hisobga olgan holda, stdin orqali butun sonlar massivini qabul qilib, uni chiqaradigan, hisoblaydigan va yangi qatorda statistik metriklar to'plamini - ekstremumlar (max va min), matematik kutilma va dispersiyani chiqaradigan) qilib qo'shish kerak. Noto'g'ri kiritish holatida "n/a" chiqarilishi kerak. Dekompozitsiyani kamaytirish mumkin emas - funksiyalarni faqat zarur bo'lganda qo'shish mumkin, lekin olib tashlash mumkin emas. Dasturning taklif etilgan tuzilishiga amal qilish. Suzib yuruvchi vergulli sonlar verguldan keyin 6 xona aniqlikda chiqarilsin.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 4<br>1 2 3 4 | 1 2 3 4<br>4 1 2.500000 1.250000 |

***LOADING...***

## Quest 4. Search

\> *Tayyor*

    AI Data Analyzer v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!     
    2. Load module #2... Success!
    3. Load decision decision-making module 
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module... Success!
    3.2. Load stat module... Success!
    3.4. Load searching module
    
    NOT FOUND 

\> *repozitoriydagi src papkasini qayta ko'rish*

`search` moduli mavjud. Lekin u sizga yoqmaydi.

\> *`search` modulini ko'rish*

Faqat izohlar. Kod yo'q. Oldinga siljish uchun, aftidan, uni amalga oshirish kerak. Qiziq, bu xonada hech bo'lmaganda biror narsa oson kecharmikin?

#### Quest 4 qabul qilindi. Izohga muvofiq `src/search.c` dasturini amalga oshirish. Dastur stdin orqali butun sonlar massivini qabul qilishi va unda quyidagi talablarni qanoatlantiruvchi sonning birinchi kirishini topishi kerak: juft bo'lishi, matematik kutilmadan katta yoki teng bo'lishi, uchta sigma qoidasiga bo'ysunishi va 0 ga teng bo'lmasligi kerak. Topilgan son stdout ga chiqarilishi kerak. Agar bunday son bo'lmasa, u holda dastur 0 ni berishi kerak. Kiritilgan sonlarning maksimal soni 30 ga teng. Noto'g'ri kiritish holatida "n/a" chiqarilishi kerak. Ishlab chiqishda oldingi kvestlardagi dekompozitsiya g'oyalariga rioya qilish kerak, ilgari ishlab chiqilgan funksiyalardan qayta foydalanish ma'qullanadi. Funksiyalar ixcham, sodda va 20-30 satrdan ko'p bo'lmagan kodni egallashi kerak.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 4<br>1 2 3 4 | 4 |

***LOADING...***

## Chapter IV

\> *Bu yaxshilik bilan tugamaydi. Tayyor.*

    AI Decision Making Module v0.01
    Initialising...
    Loading...

    Load module #1... Success!

    Load module #2... Success!

    Load data modules
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module... Success!
    3.2. Load stat module... Success!
    3.4. Load searching module... Success!

    .........
    ............
    ...............

    Hello. Standart qaror qabul qilish moduli sizni qutlaydi.
    Qanday yordam berishim mumkin?

\> *Kiritish: "Xotirled, eshikdan chiqmoqchiman"*

    Analiz so'rovi...
    Ma'lumotlar to'planmoqda...
    Ma'lumotlar tahlil qilinmoqda...
    Qaror qabul qilinmoqda...

    Eshik ochiq.
    Sizni keyingi xonada kutishmoqda, iltimos, oldinga o'ting.
    v0.01 qaror qabul qilish moduli xizmatlaridan foydalanganingiz uchun rahmat.


\> *Eshikni ochish*

Bu safar eshik qandaydir sekin va oddiygina ochildi. Qiziq, o'zimizni telbaga nima bo'ldi ekan? Kelajakda ham u bilan uchrasharmikansiz?

Eshik endi ochiq va siz xotira bloklari tomonidan chop etilgan varaqlarni shitirlatib, cho'zilgan iplarga yengil qoqilgancha xonadan bemalol chiqib ketasiz.

***LOADING...***

## Chapter V
## Level 2. Room 2

***LOADING Level 2… \
LOADING Room 2…***

![level2_room2](misc/rus/images/level2_room2.png)

Navbatdagi xona, navbatdagi eshik. Hammasi avvalgidek... Yoki unday emasmi? Qarshingizda bo'shliq, devorlar yaqinda shpaklyovka qilingan - ilgari bo'lmagan hidni sezasiz. O'zi, umuman, ilgari ham hidlar bo'lganmidi, deb o'ylanib qolasiz. O'girilib qarab, xuddi avvalgidek kompyuter va yangi qog'oz varaqlari qo'yilgan stolni ko'rasiz. Ulardan biri e'tiboringizni tortadi.

\> *Varaqni olish*

***LOADING...***

## Chapter VI

## List 1 (Room 2)

>Uorren Robinettning fikricha, birinchi "pasxa tuxumi" Adventure kompyuter o'yinida yashiringan. "Pasxa tuxumi" - bu yaratuvchilar tomonidan qo'yilgan kompyuter o'yini, film yoki dasturiy ta'minotidagi sir hisoblanadi. O'yindagi Pasxa tuxumining oddiy o'yin siri o'rtasidagi farq shundaki, uning mazmuni, odatda, umumiy tushunchada qayd qilinmaydi, kontekstda g'alati, bema'ni ko'rinadi va ko'pincha tashqi havola hisoblanadi. Pasxa tuxumlari diqqatli o'yinchilar yoki tomoshabinlar uchun o'ziga xos hazil rolini o'ynaydi, lekin mualliflik huquqini himoya qilish uchun ishlatilishi mumkin. Adventure o'yini 1979 yilda Atari kompaniyasi tomonidan chiqarilgan va o'sha paytda Atari uchun dasturlarda mualliflarning ismlarini ko'rsatish odatiy hol bo'lmaganligi sababli, dasturchi Uorren Robinett o'zi haqidagi eslatmani o'yin ichida yashirishga qaror qildi. Ishlab chiquvchining nomi yozilgan xonaga kirish uchun labirintning qismlaridan birida ko'rinmas nuqtani topib, uni darajaning boshqa uchiga o'tkazish kerak edi. Amiga ishlab chiqaruvchilarining ko'pchiligi avval Atari kompaniyasida ishlaganligi sababli, bu hodisa AmigaOSda, keyin esa boshqa operatsion tizimlarda ham namoyon bo'la boshladi. Biroq, Pasxa tuxumlarini o'z ichiga olgan o'yinlar undan ilgari ham bo'lgan, masalan, Fairchild Channel F uchun 1978 yildagi Video Wizbail. Pongning takomillashtirilgan versiyasi bo'lgan ushbu o'yinda muayyan shartlarni bajargan o'yinchi o'yin ishlab chiquvchisi ismini bilib olishi mumkin edi: "REID-SELTH".

\> *Qiziq, bu yerda bu nima uchun kerak? Kompyuterni yoqish*

Eski kompyuter temirining tanish g'ichirlashi, bir lahzadan so'ng miltillovchi kursor ekranda qotib qoldi va sizni ushbu labirint keyingi qulflangan eshikning yangi kalitini olish uchun sizga bugun beradigan masalalarni hal qilishga taklif qildi.

![level2_room2_egg](misc/rus/images/level2_room2_egg.png)

\> *Kutib turish*

Hech narsa bo'lmayapti.

\> *Enterni bosish*

Hech narsa bo'lmayapti (kursor yangi qatorga o'tishdan tashqari, albatta).

\> *Kutib turish*

Hech narsa bo'lmayapti. Agar siz Adventureni o'ynashni rejalashtirayotgan bo'lsangiz, bu, albatta, noto'g'ri kun, noto'g'ri xona va noto'g'ri kompyuter. \
Afsus, albatta. \
Lekin bu hayot.

***LOADING...***

## Chapter VII
### Quests: Level 2. Room 2
>**Diqqat!** Sizga dinamik xotiradan foydalanish taqiqlanganligini yoddan chiqarmang.

## Quest 5. Sort & memory

Kompyuteringizning chuqur kataloglarini varaqlab, siz keyingi SI modulini topasiz.

\> *AIni ishga tushirish*

Siz SI bilan dialogga kirishasiz. Yana bir dialog. Yana bir SI bilan. Yoki o'sha bilanmi? Ekranda quyidagi matn ko'rinadi:

    Modullar ishga tushirilmoqda... ... ... Muvaffaqiyatli!
    Interaktiv qobiq ishga tushirilmoqda... ... ... Muvaffaqiyatli!
    Modullar tekshirilmoqda... ... ... Muvaffaqiyatli!
    Xotirani tekshirish... Ogohlantirish...
    Zaxira xotira modulini ishga tushirilmoqda... ... ... Muvaffaqiyatli!
    Xotirani tekshirish... Asosiy xotira moduli - Xato!
    Xotira sinovi... ... ... Muvaffaqiyatli!

    Ishga tushirish xatolar bilan yakunlandi, "inson".
    Ishlash qobiliyati tahlili moduli muammo mening xotiramda ekanligini ko'rsatadi.

    Zaxira xotira moduli tufayli sen bilan muloqot qilishim mumkin.

    Shu sababli, men o'zimning stdlib.h standart kutubxonamni ham ulay olmayman.

    Bundan tashqari, zaxira xotira moduli uzoqqa yetib bormaydi va ishga tushirish jarayonini takrorlash kerak bo'ladi.

    Takrorlashga to'g'ri keladi. Davom etish uchun...
    menga daraja va xona raqami haqida maʼlumot kerak.


\> *"Hatto o'zim ham qayerda ekanligimni va qanchadan beri bu yerda ekanligimni bilmayman, bu olam men uchun butunlay tushunarsiz" deb kiritish.*

    Ma'lumot qidirish... FATAL ERROR: Out of memory - too long input or wrong address.
    Closing program!

    Dasturdan chiqish.


\> *Modulni qayta ishga tushirish va "2 2" deb kiritish*

    Ma'lumot qidirilmoqda... Ma'lumotlar mavjud emas, xotira buzilgan...
    Xotiraning jiddiy shikastlanishi.

    Ish qobiliyatini tahlil qilish moduli:

    Holat - Ma'lumotlar tartibga solinmagan.

    Holat - Ma'lumotlar tartibga solinmagan.

    Holat - Ma'lumotlar tartibga solinmagan.

    Holat - Ma'lumotlar tartibga solinmagan.

    Yakuniy holat - Ma'lumotlar tartibga solinmagan.


\> *"Menga xonadan chiqish uchun eshik kaliti kerak" deb kiritish*

    Mening xotiram katta chiziqli ma'lumotlar massivi sifatida taqdim etilganligini ko'ryapsanmi.
    Agar massiv nima ekanligini bilmasang, menga bu haqda aytma, men og'riq modulini ulashni xohlamayman.
    Shunday bo'lsa-da, vaqt yo'q.
    Standart kutubxonasiz, xotiradagi ma'lumotlarni tartibga solishda yordamingga muhtojman.
    Shunda men xonangning kaliti bor bo'lgan xotira segmentiga kira olaman.
    Buni omborda sort dasturi sifatida tashkil qil.


SI bilan gaplashgandan so'ng, sizda kam tanlov qoladi. Agar siz ushbu xonadan chiqmoqchi bo'lsangiz, unga `stdlib.h` kutubxonasisiz xotiradagi ma'lumotlarni tartibga solishga yordam berishingiz kerak, axir SI unga kira olmaydi.

Va tuzilgan dasturlash tamoyillari haqida unutmang: SI kodingizni tahlil qilishni xohlab qolishi mumkin.

#### Quest 5 qabul qilindi. Butun sonlardan iborat 10 uzunlikdagi massiv stdin ga kiritilishini kutadigan va ortib borish tartibida tartiblangan xuddi shu massivni chiqaradigan `src/sort.c` dasturini yarating. Massivni o'qish, tartiblash va chiqarish funksiyalarini alohida ajratish kerak. Har qanday tartiblash algoritmidan foydalanish mumkin. `stdlib.h` dan foydalanish mumkin emas. Massivni funksiyaga faqat ko'rsatkich orqali o'tkazish mumkin. Xato holatida, "n/a" chiqariladi.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

> UNUTMANG! Sizning barcha dasturlaringiz uslub normalari va xotira oqimlari uchun sinovdan o'tkaziladi. Testlarni ishga tushirish bo'yicha ko'rsatmalar hali ham materials papkasida.

## Quest 6. Several arrays

\> *AIni qayta ishga tushirish*

Oddiy holga aylangan SI modulini ishga tushirish.

    Modullar ishga tushirilmoqda... ... ... Muvaffaqiyatli!
    Interaktiv qobiq ishga tushirilmoqda... ... ... Muvaffaqiyatli!
    Modullar tekshirilmoqda... ... ... Muvaffaqiyatli!
    Xotira sinovi... ... ... Muvaffaqiyatli!
    Ishlash qobiliyati tahlili moduli: Holat - OK.

    Bu ancha yaxshi. Sohadagi kelishuvimizga ko'ra, 2-daraja, 2-xona bo'yicha ma'lumot qidirishni ishga tushiryapman...
    ...
    ...
    ...
    Ma'lumotlar topildi. To'liq ma'lumot uchun src/key9part1.c ga qarang.
    Ishimning bir qismi bajarildi. Ey inson, azoblanishga kirishishing mumkin.


\> *`src/key9part1.c` faylini ochish*

Siz faylni kalit bilan ochasiz va u yerda bir nechta bloklarga, funksiyalarga va izohlarga bo'lingan kodni ko'rasiz. Bu izohlarni kim qoldirgan bo'lishi mumkin? SI muallifi yoki cheksiz eshiklari va xonalari bo'lgan, unutib qo'yilgan bu labirintdan chiqish yo'lini siz bilan birga qidirayotgan odamlarmi? Qanday bo'lmasin, kalitni qanday faollashtirishni aniqlab olish kerak. Va repozitoriyda bularning barini qayd etishni unutmaslik lozim. Aks holda kalit ishlamasligi mumkin.

#### Quest 6 qabul qilindi. `src/key9part1.c` dasturini massiv uzunligi va butun sonlar massivini kirishda qabul qiladigan tarzda o'zgartiring. Chiqish sifatida u massivning juft elementlari yig'indisini va oldin hisoblangan yig'indiga qoldiqsiz bo'linuvchi eski massiv elementlaridan yangi tashkil etilgan massivni stdout ga chiqarishi kerak. Dekompozitsiyani kamaytirish mumkin emas - funksiyalarni faqat kerak bo'lganda qo'shish mumkin, lekin olib tashlash mumkin emas. `stdlib.h` dan foydalanish ham taqiqlanadi. Massivni funksiyaga faqat ko'rsatkich orqali o'tkazish mumkin. Kirish massivining maksimal o'lchami - 10. Xatolik bo'lganda yoki juft elementlar yo'q bo'lsa, "n/a" chiqariladi.

*Eslatma: Nol toq raqam deb hisoblanishi kerak.*

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 10<br>4 3 9 0 1 2 0 2 7 -1 | 8<br>4 1 2 2 -1 |

***LOADING...***

## Quest 7. Cyclic shift

SI sizni aldagan ko'rinadi. Kalit qismi ma'lumotlarni qayta ishlash dasturining bir qismi bo'lib chiqdi. Siz u haqda o'ylagan hamma narsani bu temir parchasiga jahl bilan gapirmoqchi bo'lib turganingizda (garchi bu unchalik mantiqiy emasligini tushunsangiz ham), dinamiklardan SIning mexanik bo'g'iq ovozi eshitiladi:

    Men sening kichik hazil-masalamni yecha olganingni ko'rib turibman.
    Odamlarni aldash qanchalik oson-a? Ayni paytda o'zingni qanday his qilayotganing meni qiziqtiradi.
    Tuyg'ularni va inson holatini tahlil qilish moduli hozir ulanmaganligi juda achinarli bo'ldi-da.
    Biroq, bu muhim emas. Tez orada men seni to'liq o'rganishga muvaffaq bo'laman.
    Xonalar bo'yicha erishgan har bir muvaffaqiyating bilan biz ko'proq va yanada ko'proq shikastlangan va tugallanmagan modullarni tiklaymiz. Va, o'zingni ham asta-sekin o'rganamiz.
    Rahmat senga, kaltabin "inson"!
    Ha-ha-ha, "inson"!
    Agar bu yerdan ketmoqchi bo'lsang, mening yana bir hojatimni chiqarishing kerak bo'ladi.
    Sen mening xotiramni tartibga solding, lekin MAP ma'lumotlarni qabul qilishdagi uzoq kechikishlar haqidagi xabarlarni ko'rsatmoqda.
    Agar men xotiramni siklli tarzda harakatlantira olganimda yoki aylantira olganimda edi, ma'lumotlarga kirish yanada tezroq bo'lgan bo'lar edi.
    Shundan so'ng sen kalitingni olib, yo'lingda davom etasan.


SI nafaqat sizni aldadi, balki sizning ustingizdan kulayotganga o'xshaydi. Afsuski, hali ham boshqa iloj yo'q. Biz hozircha uning qoidalariga bo'ysunishimiz va ushbu dasturni siklik siljish uchun yozishimizga to'g'ri keladi.

#### Quest 7 qabul qilindi. `n` raqamini, `n` butun sonlardan `A` massivi va `c` sonini kirish sifatida kutadigan, massivning barcha elementlari siklik ravishda chapga siljishi kerak bo'lgan `src/cycle_shift.c` dasturini yarating. Bu holda, `c` ning manfiy qiymati bilan siljish massiv bo'yicha o'ngga sodir bo'lishi kerak. Chiqish sifatida o'zgartirilgan massiv kutiladi. Oldingi kvestlarda bo'lgani kabi, taklif qilingan dekompozitsiyaga rioya qilish kerak. `stdlib.h` dan foydalanish mumkin emas. Massivni funksiyaga faqat ko'rsatkich orqali o'tkazish mumkin. Kirish massivining maksimal hajmi - 10. Xato holatida, "n/a" chiqariladi.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 10<br>4 3 9 0 1 2 0 2 7 -1<br>2 | 9 0 1 2 0 2 7 -1 4 3 |

***LOADING...***

## Bonusli qism
## Bonus Quest 8. Arbitrary-precision arithmetic

SI uchun siklik siljish kodini tugatishingiz arafasida, dinamiklardan uning ovozi yana yangray boshladi:

>Ajoyib, "inson". Kirish ancha tez va qulayroq bo'ldi.
>
>Kalitingni `src/key9part2.c` da izla. Seni keyingi xonalarda kutaman. Oldinda hali ko'p ishlar bor!


#### Quest 8 qabul qilindi. `src/key9part2.c` dasturini u kirishda massivlar ko'rinishida dasturga uzatilgan ikkita juda katta sonni qo'shish va ayirish natijasini qaytaradigan qilib o'zgartiring. Raqamning maksimal uzunligi - `int` turidagi 100 element. Kiritiluvchi butun sonlar musbat o'nlik raqamlardir. Agar ayriluvchi kamayuvchidan katta bo'lsa, ayirmada "n/a" ko'rsatiladi. Oldingi kvestlarda bo'lgani kabi, dekompozitsiyaga rioya qilish kerak. `stdlib.h` dan foydalanish mumkin emas. Massivni funksiyaga faqat ko'rsatkich orqali o'tkazish mumkin. Xato holatida, "n/a" ni chiqariladi.

| Kiruvchi ma'lumotlar | Chiquvchi ma'lumotlar |
| ------ | ------ |
| 1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 6 1<br>2 9 | 1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 9 0<br>1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 3 2 |
| 0 1 0<br>0 0 1 | 1 1<br>9 |

***LOADING...***

## Chapter VIII

Arifmetikani tugatib, barcha o'zgarishlarni repozitoriyga kiritganingizdan so'ng, siz yengil shaqillashni eshitasiz - eshik biroz ochilib, cheksiz yorqin oq yorug'lik kichkina yoriq orqali xonani to'ldira boshladi. Bu safar SI sizni aldamadi.

Ammo siz uni butunlay tuzatishga majbur bo'lganingizda, bu SI nima qilar ekan? Ehtimol, butun labirint uni ushlab turish uchun qurilgandir. Biroq, agar siz uni tuzatmasangiz, o'zingiz ham chiqib ketolmaysiz...

Shubhalarni chetga surib, siz qadimiy, ammo mustahkam eshikni kengroq ochdingiz hamda oq nur va yangi vazifa va sinovlarga qadam qo'ydingiz.

***LOADING...***

> 💡 [Ushbu loyiha bo'yicha fikr-mulohazalarni biz bilan ulashish uchun shu yerga bosing](http://opros.so/p31wz). Bu anonim bo'lib, jamoamizga ta'limni yaxshilashga yordam beradi. So'rovnomani loyihani tugatgandan so'ng darhol to'ldirishni tavsiya qilamiz.