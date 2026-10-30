# D10T07. Tuzilmalar va kolbeklar

Annotatsiya: ushbu loyiha sizga C dagi tuzilmalar va birlashmalar, shuningdek, kolbek-funksiyalar va qo'shimcha ravishda funksiya chaqiuvlari, o'zgaruvchilar, argumentlar ro'yxati va dinamik tuzilmalar bilan tanishish imkonini beradi.

## Contents

1. [Kirish](#kirish) \
    1.1. [Loyihaga tavsiyalar](#loyihaga-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 3. Room 3](#level-3-room-3)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1. MCO](#list-1-mco) \
    3.2. [List 2. Instructions](#list-2-instructions)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. The Doors](#quest-1-the-doors) \
    4.2. [Quest 2. Linked List](#quest-2-linked-list) \
    4.3. [Quest 3. Stack for key](#quest-3-stack-for-key)
5. [Chapter IV](#chapter-iv)
6. [Chapter V](#chapter-v) \
    6.1. [Level 3. Room 4](#level-3-room-4)
7. [Chapter VI](#chapter-vi) \
    7.1. [List 1](#list-1) \
    7.2. [List 2](#list-2) \
    7.3. [List 3](#list-3)
8. [Chapter VII](#chapter-vii) \
    8.1. [Quest 4. Print Module](#quest-4-print-module) \
    8.2. [Quest 5. Checking Module](#quest-5-checking-module) \
    8.1. [Bonus Quest 6. BST](#bonus-quest-6-bst) \
    8.2. [Bonus Quest 7. Growing tree](#bonus-quest-7-growing-tree) \
    8.3. [Bonus Quest 8. Three styles of traversing](#bonus-quest-8-three-styles-of-traversing)
9. [Chapter VIII](#chapter-viii)

## Kirish
### Loyihaga tavsiyalar
School 21 da qanday ta'lim olish mumkin:  
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
## Level 3. Room 3

![level3_room3](misc/rus/images/level3_room3.png)

***LOADING Level 3...*** \
***LOADING Room 3...***

\> *Atrofga qarash*

Yana o'sha uchinchi daraja. Stol, kompyuter, chirog'i bor, ammo kitoblarsiz navbatdagi xona. Faqat bu safar bitta eshik bo'lishi kerak bo'lgan joyda ular o'n beshta bo'ldi. Ularning har birida klaviaturali g'alati elektron qulf osilgan. Juda shubhali. Lekin hech bo'lmaganda chiroq bor - u bilan har doim qulayroq.

\> *Birinchi eshikni tortish*

Yopiq.

\> *Ikkinchi eshikni tortish*

Qulflangan.

\> *Uchinchi eshikni tortish*

Bo'lmayapti.

\> *To'rtinchi eshikni tortish*

Yo'q.

\> *i = 5 bo'lganda, i &lt;= 15 -&gt; i-chi eshikni tortish va i ni oshirib borish*

Behudaga sarflangan protsessor vaqti...

\> *Atrofga yana bir nazar tashlash*

Stol ustidagi varaqlar uyumi yonida kimdir qoldirgan gazeta qirqimi yotganini payqaysiz. SI uni qandaydir tarzda qoldirganmi yoki buni sizdan oldingi biror kim tashlab ketganmi? Shunday bo'lsa-da, SI gazetalar o'qiydi, ayniqsa, gazeta qirqimlarini tayyorlaydi, deb taxmin qilish g'alati.

\> *Qirqim bo'ylab ko'z yugurtirish*

***LOADING...***

## Chapter II
## List 1. MCO

Varaq bo'lagi sarg'ayib ketgan va anchadan beri yotganligi ko'rinib turibdi. Buning ustiga nihoyatda pala-partish qirqilgan. 

>Mars Climate Orbiter 1998-yil 11-dekabrda RN "Delta-2"da uchirilgan. Apparat Marsga 9 oydan keyin yetib kelgan. Mars Climate Orbiter 1999-yil 23-sentyabrda tormozlash impulsini berishi va 14 soatlik davr bilan yuqori elliptik orbitaga chiqishi, so'ngra ikki oy ichida Marsning yuqori atmosferasida bir qator aerodinamik manyovrlar yordamida orbitani aylana shakliga keltirishi kerak edi. Hisoblangan vaqtda 193 km balandlikda apparat dvigatellarni tormozlash uchun yoqdi. 5 daqiqadan so'ng MCO Mars ortiga ketdi va undan boshqa hech qanday signal kelmadi. Ma'lumotlar tahlilidan apparat Mars sirtidan hisoblangan 110 km o'rniga 57 km balandlikdan o'tib, atmosferada parchalanib ketgani taxmin qilindi. Bunday katta og'ish missiya dasturiy ta'minotidagi xato tufayli yuzaga keldi: Mars Climate Orbiter dasturiy ta'minotidagi dvigatel tortish buyruqlari "nyuton" kuch o'lchov birligidan foydalangan, bu buyruqlarni yaratgan Yerdagi dasturiy ta'minot esa Britaniya o'lchov birligidan (funt-kuch) foydalangan...

\> *Gazeta qirqimi ostidagi to'plamdan birinchi varaqni olish*

***LOADING...***

## List 2. Instructions

Varaq qandaydir dasturlash kitobidan yirtib olingan sahifaga o'xshaydi... Ehtimol, uni diqqat bilan o'qib chiqish kerakdir.

>Tuzilma - foydalanuvchi tomonidan aniqlangan tur bo'lib, turli xildagi bir nechta qiymatlarni birgalikda saqlash va ko'chirish imkonini beradi. Tuzilmani aniqlash quyidagicha amalga oshiriladi:

    struct [tuzilma nomi] {
    elementni aniqlash;
    elementni aniqlash;
    ...
    elementni aniqlash;
    } [bitta yoki bir nechta o'zgaruvchi];

>Tuzilmalardan foydalanish birgalikda foydalaniladigan ma'lumotlarni birlashtirish imkonini beradi, shuningdek, funksiyalar sarlavhalarini o'zgartirmasdan uzatilayotgan ma'lumotlarni keyinchalik ham o'zgartirish imkoniyatini qoldiradi.

Tuzilma egallagan xotira hajmi uning barcha elementlari egallagan xotira hajmining yig'indisiga teng. Shu munosabat bilan C tilidagi tuzilmalar nol qiymatli abstraksiyalardir. Tuzilma elementlari xotirada qanday tartibda aniqlangan bo'lsa, shunday tartibda joylashadi.

\> *Keyingi varaqni olish*

>Birlashma - turli tipdagi qiymatlarni saqlash uchun xotiradan qayta foydalanish imkonini beruvchi ma'lumotlar turi. Birlashmani aniqlash quyidagicha amalga oshiriladi:

    union [birlashma nomi] {
    elementni aniqlash;
    elementni aniqlash;
    ...
    elementni aniqlash;
    } [bitta yoki bir nechta o'zgaruvchi];

>Birlashma egallaydigan xotira birlashmaning eng katta elementini saqlash uchun zarur bo'lgan xotira sifatida aniqlanadi...

Keyingi matnni o'qib bo'lmaydi.

>Birlashmalar va tuzilmalarning qo'llanish sohalaridan biri nishonli birlashmalardir. Bular bir nechta ruxsat etilgan ma'lumotlar turlaridan birini o'zida saqlashga imkon beradigan va o'zida u yordamida ma'lum bir vaqtda birlashmada aynan qaysi ma'lumotlar turi joylashganligini aniqlash mumkin bo'lgan belgini - butun sonni o'z ichiga olgan tuzilmalar hisoblanadi.

\> *Keyingi varaqni olish*

>Bir bog'lamli ro'yxat - bir turdagi ma'lumotlarni o'z ichiga olgan ketma-ket bog'langan uzellardan iborat ma'lumotlar tuzilmasi. Ro'yxatning har bir elementi keyingi elementga ko'rsatkichga ega, oxirgisi u yerda bo'sh ko'rsatkichni saqlaydi (C da 0/NULL). Ro'yxatlar o'zgaruvchan uzunlikka ega bo'lib, ko'plab ro'yxatlarni osonlik bilan birlashtirish imkonini beradi, ammo ular massivlarga qaraganda ko'proq xotirani egallaydi va ularni aylanib o'tish uchun ko'proq elementar operatsiyalarni talab qiladi.

***LOADING...***

## Chapter III
## Quests: Level 3. Room 3

## Quest 1. The Doors 

\> *Qo'shimcha yo'l-yo'riqlar uchun xonani diqqat bilan ko'zdan kechiring*

Bo'sh.

\> *Qo'shimcha yo'l-yo'riqlarni qidirish uchun stolni diqqat bilan ko'zdan kechiring*

Klaviatura tagida kichkina to'q sariq qog'ozga ko'zingiz tushadi. Bunday qog'ozlar ko'pincha eslatma stikerlari sifatida ishlatiladi. 

\> *Olib o'qing*

Ishonching komilmi? Bu shaxsiy bo'lishi mumkin...

![level3_room3_sticker](misc/rus/images/level3_room3_sticker.png)

\> *Ha. Ilgari bu hech kimni xijolat qilmasdi. Tanlovim ham ko'p emas*

>`src/dmanager_module.c` — eshiklarni boshqarish moduli. \
>Eshiklarni initsializatsiya qilish funksiyasiga tegilmang, xona yadrosining mantig'i buziladi. \
>Hamma eshiklarni ochmang, bundan uzatish protokoli buziladi. \
>Boshqarish uchun eshiklarni o'sish tartibida saralash funksiyasini va "ochiq" eshiklarni yopish funksiyasini ajratib ko'rsating. 
> 
>Eshiklarning tuzilishi: butun sonli id va sonli status (0 — yopiq, 1 — ochiq).

Sizdan ancha oldin kimdir qoldirgan esdalik qog'ozchaga o'xshaydi. Ushbu eshiklarni boshqarish moduliga e'tibor berish kerak, bu yordam berishi mumkin.

#### Quest 1 qabul qilindi. `src/door_struct.h` da eshiklar tuzilmasini yaratish. Tuzilmaning o'zi butun sonli eshik "id"si va butun sonli status (0 — yopiq, 1 — ochiq) dan iborat. `src/dmanager_module.c` dasturini shunday tuzatingki, u ishga tushirilgan eshiklar massivini eshiklar "id"sining o'sishi bo'yicha istalgan algoritm bilan tartiblasin va uni "eshik idsi, eshik statusi" formatida chiqarsin. Bundan tashqari, barcha eshiklar uchun "yopiq" statusini belgilang.
#### Eshiklarni initsializatsiya qilish funksiyasini o'zgartirish mumkin emas. Tuzilmaviy yondashuvga amal qiling. Dastur Makefile yordamida yig'ilishi kerak. Bosqich nomi — `door_struct`. Bajariladigan fayl build papkasidagi repozitoriy ildizida joylashishi va "Quest_1" nomiga ega bo'lishi kerak.  

>**MUHIM!** Tizim yadrosiga to'g'ridan-to'g'ri murojaat qilishi mumkin bo'lgan `system()` funksiyasi va unga o'xshash boshqa funksiyalar yordamida tizim chaqiruvlarini amalga oshirish taqiqlanadi. Ushbu taqiq barcha keyingi vazifalarga ham taalluqlidir.

>**Diqqat:** yechim xotira sizdirilishi va uslubiy me'yor bo'yicha tekshiriladi, ko'rsatmalar esa har doimgidek materialsda berilgan.

*Kutiluvchi natija (eshik "id"si, statusi):*

```
0, 0
1, 0
2, 0
3, 0 
4, 0 
5, 0 
6, 0 
7, 0 
8, 0 
9, 0 
10, 0 
11, 0 
12, 0 
13, 0 
14, 0 
```
***LOADING...***

## Quest 2. Linked List

Shunday qilib, eshiklar ishga tushayotganga o'xshaydi. Lekin qanday qilib chiqish mumkin? Qaysi eshik uchun "ochiq" statusini yozish kerak? Agar hamma eshiklar uchun shunday qilinsa, qaydlarga qaraganda, bu qandaydir falokatga olib kelishi mumkin.

\> *Qog'ozni to'ntarish*

Mana, davomi.

>Kerakli eshik har kuni o'zgaradi. \
>Joriy eshik raqami xonaning ichki modullari bilan polinomial funksiya orqali hisoblanadi. Modulni amalga oshirish manbalari mavjud emas. \
>Revers injiniring orqali ushbu modul massivlar bilan ishlashni bilmasligi aniqlandi. Modul o'z ishida bir bog'lamli ro'yxatni amalga oshirish bilan dinamik ulanadigan kutubxonadan foydalangan. Bu kutubxona modulning ishlashi uchun juda muhim, ammo kutubxona joylashgan binar fayl shikastlangan.

Varaqlardan birida bir bog'lamli ro'yxat haqida nimadir deyilgandi. Bu ro'yxat haqida ko'proq ma'lumot olish va shu bilan birga unga xotira ajratish masalasini ko'rib chiqish kerak.

#### Quest 2 qabul qilindi. Bir bog'lamli eshiklar ro'yxati bilan ishlash funksiyalarini amalga oshirishni o'z ichiga olgan `src/list.c` dasturini ishlab chiqish:
#### 1. `struct node* init(struct door door)` — uzatilgan `struct door` asosida bir bog'lamli ro'yxat tuzilmasini initsializatsiya qilish; 
#### 2. `struct node* add_door(struct node* elem, struct door door)` — uzatilgan `elem` uzelidan keyin bir bog'lamli ro'yxatga yangi `struct door` elementini qo'yish; 
#### 3. `struct node* find_door(int door_id, struct node* root)` — ro'yxatdagi eshikni uning id bo'yicha qidirish;
#### 4. `struct node* remove_door(struct node* elem, struct node* root)` — ro'yxat elementini o'chirish; 
#### 5. `void destroy(struct node* root)` — ro'yxat tuzilmasi egallagan xotirani bo'shatish.<br>

#### Ushbu funksiyalarning e'lonlari va bir bog'lamli ro'yxat tuzilmasi `snc/list.h` fayliga chiqarilsin. `src/list_test.c` da bir bog'lamli ro'yxatning `add_door` va `remove_door` funksiyalarining ishlashini tekshirish uchun modulli testlar yozing. Metod funksiyalari testdan muvaffaqiyatli o'tgan taqdirda SUCCESS va xatolik yuz bergan taqdirda FAIL qaytarishi kerak. Testlar Makefile yordamida to'planishi kerak. Bosqich nomi — `list_test`. Bajariladigan fayl build papkasidagi repozitoriy ildizida joylashishi va "Quest_2" nomiga ega bo'lishi kerak.

>**Diqqat:** ushbu kvest `cppcheck` yordamida sinovdan o'tkaziladi.

***LOADING...***

## Quest 3. Stack for key

Yaxshi, joriy eshik raqamini qidirish moduli ishlashi uchun kerakli kutubxona yozildi. Siz ekranda shiddat bilan to'lib borayotgan algoritmning hisoblash faolligi shkalasini ko'rasiz. Bir necha soniyadan so'ng ekranda sizga kerakli eshikning raqami paydo bo'ladi. Bajarilgan ishdan yengillik va qoniqish hissi bilan eshik tomon yo'l olasiz.

\> *Tutqichni tortish*

Qulflangan... \
Biroq eshikda kichkina ekrancha ochilayotganini payqab qolasiz. Ekranda katta harflar bilan quyidagi yozuv yonib turibdi:

> NO DYNAMIC INT STACK AND/OR STACK OPERATIONS

Siz kompyuter oldiga qaytib, bu nimani anglatishi mumkinligi haqida o'ylaysiz. Afsuski, boshqa hech qayerda yordamchi qaydnomalar yo'q... 

Chuqurroq o'ylab ko'rib, stek ko'pincha ro'yxat ko'rinishida amalga oshiriladigan dinamik ma'lumotlar tuzilmasining bir turi ekanligini eslaysiz. Aftidan, eshikni ochish uchun hali butun sonlarni o'z ichiga olgan dinamik stekni yozish kerak. Stek uchun uning standart interfeysini amalga oshirish lozim: ma'lumotlarni stekka surish (`push`) va undan chiqarish (`pop`) operatsiyalari. Barcha amalga oshirishlarni `src/stack.c` da, funksiyalar va tuzilma e'lonlarini esa `src/stack.h` da saqlashni unutmaslik zarur. Shuningdek, stekning ishlashini va uning funksiyalarini tekshirish uchun `src/stack_test.c` da modul testlarini yozish maqsadga muvofiqdir. Aks holda, stek noto'g'ri ishlasa, kim biladi nimalar sodir bo'ladi...

#### Quest 3 qabul qilindi. Dinamik stek (`init`, `push`, `pop`, `destroy`) bilan ishlash funksiyalarini amalga oshirishni o'z ichiga olgan `snc/stack.c` dasturini ishlab chiqish. Butun sonlarni saqlaydigan dinamik stek funksiyalari va tuzilmasi e'lonlarini `src/stack.h` ga chiqarish.
#### `src/stack_test.c` da `push` va `pop` stek funksiyalarining ishlashini tekshirish uchun modulli testlar yozing. Metodlar funksiyalari testdan muvaffaqiyatli o'tgan taqdirda SUCCESSni va xatolik yuz bergan taqdirda FAILni qaytarishi kerak. Testlar Makefile yordamida to'planishi lozim. Bosqich nomi — `stack_test`. Bajariladigan fayl build papkasidagi repozitoriy ildizida joylashishi va "Quest_3" nomiga ega bo'lishi kerak. 

>**Diqqat**: ushbu kvest `cppcheck` utilitasi yordamida sinovdan o'tkaziladi. Bu topshiriq avtotestlashni nazarda tutmaydi!

***LOADING...***

## Chapter IV

\> *"Quest 3" vazifasini repozitoriyga push qilish* 

Hammasi tuzilmalar bo'yicha bajarilganga o'xshaydi, keyingi topshiriqlarga o'tish mumkin.

\> *Qo'shni eshikka yaqinlashib, tutqichni tortish*

Eshik ochiladi va siz qo'shni xonaga qadam tashlaysiz.

***LOADING...***

## Chapter V
## Level 3. Room 4

![level3_room4](misc/rus/images/level3_room4.png)

***LOADING Level 3...*** \
***LOADING Room 4...***

\> *Atrofga nazar solish*

Siz kitoblarsiz, devorlarida g'alati polotnolar bo'lmagan va faqat bitta eshigi bor bo'lgan yangi xonaga o'tasiz. Agar xonaning o'rtasida o'sib turgan ulkan tirik daraxt bo'lmaganida, hammasi ajoyib va odatdagidek bo'lardi. Nega bu bosqichda hamma xonalar shunchalik g'alati... 

Ish stansiyasiga yaqinroq borib, buyruq terminalida ochiq hisobot turganini ko'rasiz — aftidan, muhandislardan biriniki bo'lsa kerak. Daraxtdan to'kilgan bir juft sarg'aygan barglarni ham.

\> *Hisobotni o'rganish*

    Yaqinda yadro rejimi drayverini ishlab chiqishimga to'g'ri keldi.

    Ko'rinmagan

***LOADING...***

## Chapter VI
## List 1

> UNUTMANG! Barcha dasturlaringiz uslub me'yori va xotira sizib chiqishi bo'yicha sinovdan o'tkaziladi. Testlarni ishga tushirish bo'yicha ko'rsatmalar hali ham materials papkasida joylashgan.

    Validating module...
    System segmentation fault...
    Loading module structure seems to be broken
    Checking available documents:
        1. Linked lists   : unavailable
        2. Queues         : unavailable
        3. Maps           : unavailable
        4. Binary Trees   : available

    Select document to open:
    >1
    LOADING...
    Document unavailable

    Select document to open:
    >2
    LOADING...
    Document unavailable

    Select document to open:
    >3
    LOADING...
    Document unavailable

    Select document to open:
    >4
    LOADING...
    LOAD: SUCCESS
    Do you want to read it now? 
    N/Y

***LOADING...***

## List 2

    Definitions: 
    Ko'rinmagan 

    Bitta element (varaq, uzel) ning tuzilmasi quyidagicha tavsiflanadi:

```
typedef struct 		s_btree 
{
struct s_btree 	*left; 
struct s_btree 	*right;
int 			item; 
} t_btree;
```

    Ko'rinmagan

![Binary_tree](misc/images/binary_tree.png) \
Рис. 1. Binar daraxt

    PRESS PAGE DOWN TO CONTINUE

***LOADING...***

## List 3

    Definitions: 
    Ko'rinmagan

Characteristics:

|   | o'rtacha | eng yomon holatda |
| ------ | ------ | ------ |
| Xotira sarfi | O(n)      | O(n)    |
| Izlash         | O(log n)      | O(n)    |
| Qo'yish       | O(log n)      | O(n) |
| O'chirish       | O(log n)      | O(n) |

    Ko'rinmagan

![Binary_search_tree](misc/images/binary_search_tree.png) \
Рис. 2. Binar qidiruv daraxti

    END OF CURRENT DOCUMENT
    PRESS ANY KEY TO RETURN...

    Validating module...
    System segmentation fault...
    AI documentation module found but not loaded correctly... 
    Hint: Try to sort modules in the right order

***LOADING...***

## Chapter VII
## Quests: Level 3. Room 4

>**Diqqat!** Barcha bajariladigan fayllar, avvalgidek, loyihaning ildiz direktoriyasining build papkasida joylashishi kerak.

## Quest 4. Print Module

Hisobot kutilmaganda uzilib qoladi, va siz xato haqidagi xabarni ko'rasiz. Uni batafsil o'rganib chiqqach, chiqarish moduli shikastlanganini (kim o'ylabdi deysiz!) va uni almashtirish kerakligini tushunib yetasiz.\
Tizim o'z modulini qo'shishni taklif qiladi.

\> *Kompyuterda hujjatlarni qidirish*

Bugun senga omad kulib boqmoqda. Kompyuterda chiqarish va hujjatlashtirish modullari haqida ozroq ma'lumot bor.

![level3_room4_leaf](misc/rus/images/level3_room4_leaf.png)

\> *Hujjatlarni o'qish*

Hujjatlarni yuklab olib, ularni o'rganasiz.

...

Hujjatlarni batafsil o'rganib chiqib, tizimda shunchaki ekranga chiqarish funksiyasi yo'qligini tushunasiz. So'rov modulining signaturasi quyidagicha ko'rinadi:

`void print_log(char (*print) (char), char* message);`

Hujjatlarni o'rganib chiqqandan so'ng, tizimning yadrosi teskari chaqiruv funksiyalari (callbacks) bilan ishlayotganini tushunasiz va ekranga chiqarishni amalga oshirishni tushunishingiz hamda uni modulda chaqirishingiz kerak bo'ladi.

#### Quest 4 qabul qilindi. `src/print_module.c` faylida `print_log` funksiyasini, u parametrlarda unga uzatilgan funksiya yordamida quyidagi turdagi xabarni chiqaradigan qilib to'ldiring: «[LOG] joriy_xabar vaqti». Joriy vaqt SS:DD:SS formatida bo'lishi kerak. Lozim bo'lsa, `src/main_module_entry_point.c` faylini o'zgartiring. Dasturni yig'ish Makefile yordamida amalga oshiriladi. Bosqich nomi — `print_module`, bajariladigan fayl nomi — «Quest_4». 

***LOADING...***

## Quest 5. Checking Module

\> *Repozitoriyga o'zgartirishni push qilish*

    System segmentation fault...
    Loading module structure seems to be broken
    System: Output stream module load... Success
                    LOADING...
                      SUCCESS
        Qolgan joyidan o'qishni davom ettirasizmi?
                        N/Y

Hisobot davomida SI kodida foydalanish uchun bir nechta o'rnatilgan ma'lumotlar tuzilmalari keltirilgan. Har qanday yirik dasturiy ta'minot loyihasida bo'lgani kabi, ushbu umumiy ma'lumotlar tuzilmalari va primitivlar kodda qayta foydalanish uchun taqdim etiladi. Dasturchilar iloji boricha ulardan qayta foydalanishlari kerak. 

Hujjatlarning keyingi bo'limlarida quyidagi umumiy ma'lumotlar tuzilmalarining tavsifi keltirilgan, xususan: bog'langan ro'yxatlar (Linked lists), navbatlar (Queues), xaritalar (Maps), binar daraxtlar (Binary Trees). Har bir bo'limda algoritmning tavsifi, qo'llanish sohasi va murakkabligi ko'rsatilgan ma'lumotlar keltirilgan.

        SELECT DOCUMENT YOU WANT TO READ
                    >...

                    ERROR...
                    
Matn kutilmaganda uziladi va tizim qolgan ma'lumotlarning yaxlitligini tekshirishni boshlaydi.

                UNRECOGNIZED OPERATION...
                FILTER MODULE: MISSED 

Katta xatolar logi orasida tizim bir nechta satrlarni ajratib ko'rsatdi:

    System segmentation fault...
    Loading module structure seems to be broken
    missed or unknown header: stdarg.h
    missed or unknown header: varargs.h
    va_start can't be used
    va_arg can't be used
    va_end can't be used
    use 'man stdarg' to get more information

\> *Bu nima bo'ldi ekan?*

Aftida, so'rayotgan kishingiz...

Hujjatlarga ko'ra, siz quyidagi signatura bilan tavsiflangan SI funksiyasi modulini yozishingiz kerak:

`int* check_available_documentation_module(int (*validate) (char*), int document_count, ...);`

Signaturaga ko'ra, funksiya har bir uzatilgan parametrga qayta chaqirish mexanizmini qo'llashi kerak.

#### Quest 5 qabul qilindi. `src/documentation_module.c` faylida `check_available_documentation_module` funksiyasini u parametrlarda unga uzatilgan har bir hujjatga parametrlarda uzatilgan validatsiya funksiyasini qo'llaydigan qilib to'ldirish kerak. Dastur ishining natijasi butun sonlar massividan iborat bo'lgan hujjatlar mavjudligi massivi bo'lishi kerak (0 — hujjat mavjud emas, 1 — hujjat mavjud). 
#### `src/main_module_entry_point.c` modulining funksionalligini, u olingan massiv yordamida hujjatlarning mavjudligini inson o'qiydigan ko'rinishda amalga oshiradigan qilib kengaytiring (format: [hujjat nomi : (un)available]). Tekshirilayotgan hujjatlar uchun chiqarish maydoni o'lchami modifikatorini 15 birlik qilib o'rnating. Funksiya ixtiyoriy sondagi argumentlarni qabul qilishiga e'tibor bering. Dasturni yig'ish Makefile yordamida amalga oshiriladi. Bosqich nomi — `documentation_module`, bajariladigan fayl nomi — «Quest_5».

***LOADING...***

## Bonus Quests 
## Bonus Quest 6. BST

\> *Nima qilish kerak?*

Ko'rinib turibdiki, tizimning nozik ko'rsatmalariga amal qilish va binar qidiruv daraxti yordamida SI modullarini saralash kerak. Har bir modul 0 dan 10 gacha bo'lgan o'z id soniga ega. Kompyuterda topilgan ma'lumotlardan ma'lumki, hujjatlashtirish moduli 4 identifikatoriga ega. 

Baxtingizga, daraxt elementi (barg) tuzilmasi allaqachon hujjatlarda berilgan.

Birinchi navbatda `src/bst.c` da uzel yaratish funksiyasini yozish kerak (funksiya uzeldagi qiymatni saqlashi va tarmoqlanib chiqqan uzellarning boshlang'ich holatlarini initsializatsiya qilishi kerak). Funksiya signaturasi quyidagicha ko'rinishi kerak:

`t_btree *bstree_create_node(int item)`

Tegishli header faylida `t_btree` turini tavsiflash kerak. Oxirida, uzel yaratish funksiyasini `src/bst_create_test.c` da avval qilganingizdek modulli testlash orqali sinab ko'rish kerak.

#### Quest 6 qabul qilindi. `src/bst.c` dasturini, unda `bstree_create_node` binar qidiruv daraxti uzelini yaratish funksiyasini amalga oshirish. `src/bst.h` da daraxt uzeli turining tavsifi joylashtirilsin. Modulli testlash yordamida `src/bst_create_test.c` da ishlab chiqilgan funksiyani tekshirish (nima yaratilganligi haqidagi chiqarish bilan kamida ikkita kirish qiymati). Dasturni yig'ish Makefile yordamida amalga oshirilishi kerak. Bosqich nomi — `bst_create_test`, bajariladigan fayl nomi — «Quest_6».

***LOADING...***

## Bonus Quest 7. Growing tree

\> *Tayyor*

Endi bitta elementni yaratish funksiyasi tayyor bo'lgach, navbatdagi uzelni qo'yish orqali butun daraxtni yaratishga kirishish mumkin.

Funksiya signaturasi quyidagicha ko'rinishi va `src/bst.c` da joylashishi kerak:

`void bstree_insert(t_btree *root, int item, int (*cmpf) (int, int));`

Signaturadan ko'rinib turibdiki, uzellarning qiymatlarini teskari chaqiruv funksiyasi — `cmpf` yordamida taqqoslash zarur. 

Oxirida funksiyani `src/bst_insert_test.c` da kamida ikkita turli kirish qiymatlari to'plami va daraxt bargi qo'yiladigan chiqish bilan tekshirish kerak.

#### Quest 7 qabul qilindi. `src/bst.c` dasturini `bstree_insert` binar qidiruv daraxti uzelini qo'yish funksiyasini amalga oshirish orqali to'ldirish. Modulli testlash yordamida `src/bst_insert_test.c` da ishlab chiqilgan funksiyani tekshirish (daraxt bargining joylashuvini chiqaradigan kamida ikkita turli xil kirish qiymatlari to'plami). Komparator funksiyasini amalga oshirishni ko'zda tuting. Dasturni yig'ish Makefile yordamida amalga oshiriladi. Bosqich nomi — `bst_insert_test`, bajariladigan fayl nomi — «Quest_7». 

***LOADING...***

## Bonus Quest 8. Three styles of traversing

\> *Ko'rinishidan, endi daraxtni aylanib o'tish qoldi*

Daraxtdan o'tish funksiyalarini yozish kerak. SI hujjatlari modullarini to'g'ri yuklash uchun ularni aynan qanday tartibda joylashtirish kerakligi haqida ma'lumot yo'qligi sababli, daraxt bo'ylab o'tishning (traverse) 3 xil funksiyasini yozishga to'g'ri keladi:
- infix — elementlar o'sish tartibida ko'rsatiladi (chap kichik daraxt -> ildiz -> o'ng kichik daraxt);
- prefix — elementlar qanday tartibda saqlangan bo'lsa, xuddi shu tartibda ko'rsatiladi (ildiz -> chap kichik daraxt -> o'ng kichik daraxt);
- postfix — elementlar kamayish tartibida ko'rsatiladi (chap kichik daraxt -> o'ng kichik daraxt -> ildiz).

Funksiya signaturalari quyidagicha ko'rinishga ega va ularning barchasi `src/bst.c` da amalga oshirilishi kerak:

`void bstree_apply_infix(t_btree *root, void (*applyf) (int));`

`void bstree_apply_prefix(t_btree *root, void (*applyf) (int));`

`void bstree_apply_postfix(t_btree *root, void (*applyf) (int));`

`applyf` — ham teskari chaqiruv funksiyasi bo'lib, unga uzel qiymati uzatilishi kerak. Bunday funksiya, masalan, qiymatlarni ekranga chiqarishi mumkin. 

Testlar uchun oldingi testdan kirish ma'lumotlari to'plamini olib, daraxtlar ekraniga chiqishni `src/bst_traverse_test.c` da uch xil usulda rasmiylashtirish kerak.

#### Quest 8 qabul qilindi. `src/bst.c` dasturini `bstree_apply_infix`, `bstree_apply_prefix`, `bstree_apply_postfix` binar qidiruv daraxtini aylanib o'tish funksiyalarini amalga oshirish orqali to'ldirish.
#### Modulli testlash yordamida `src/bst_traverse_test.c` da yozilgan funksiyalarni tekshirish (oldingi testdan kirish ma'lumotlari to'plamlarini oling va daraxtlar ekraniga chiqishni uch xil usulda rasmiylashtiring). Uzel qiymatini terminalga chop etuvchi funksiya sifatida `applyf` funksiyasini amalga oshirishni tayyorlash. Dasturni yig'ish Makefile yordamida amalga oshiriladi. Bosqich nomi — `bst_traverse_test`, bajariladigan fayl nomi — «Quest_8».

***LOADING...***

## Chapter VIII

\> *Yechimni repozitoriyga push qilish*

Terminalda nihoyat tekshiruv satrlari paydo bo'lmoqda va siz hisobotni o'qishni tugatishga tayyorsiz.

    Validating module... 
    ... 
    Success 
    ...

Modullar to'liq tekshiruvdan o'tishini 15 daqiqa kutganingizdan so'ng, kompyuter qotib qolganini va hech qanday harakatga javob bermayotganini tushunasiz.

\> *Kompyuterda qayta ishga tushirish tugmasini bosish*

Ekran o'chdi va siz yoningizdagi tizim blokidan chiqayotgan yengil tutunni payqaysiz. U qizib ketganga o'xshaydi yoki biror narsa uni qizitib yuborganga o'xshaydi...

Nima bo'lganini tushunolmaysiz, chunki xonadagi eshik portlashga o'xshash gumburlash bilan oshiq-moshig'idan chiqib ketib, uchib borib daraxt tomonga qulab tushadi.

«Xo'sh, chiqish eshigi ochildi, kompyuter buzildi. Hisobotni, afsuski, oxirigacha o'qib bo'lmadi. SI esa yana qayergadir g'oyib bo'ldi. Umid qilamanki, u qaytib kelmaydi. Eshikni usiz ham juda yaxshi tushunsa bo'ladi», — deb o'ylaysiz-da, ostonadan hatlab chiqasiz. 

***LOADING...***

>💡 [Loyiha haqida fikr-mulohazalar bildirish uchun bu yerga bosing](http://opros.so/p31wz). Bu anonim bo'lib, jamoamizga ta'limni yaxshilashga yordam beradi. So'rovnomani loyiha bajarilgandan so'ng darhol to'ldirishni tavsiya qilamiz.