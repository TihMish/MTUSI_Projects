# D09T06: Ko‘p faylli loyihalar, belgilar va satrlar

Annotatsiya: ushbu loyiha sizga ko‘p faylli loyihalar, shuningdek, belgilar va satrlar bilan tanishish imkonini beradi.

## Contents

1. [Kirish](#kirish) \
    1.1. [Loyihaga tavsiyalar](#loyihaga-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 3. Room 1](#level-3-room-1)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1](#list-1) \
    3.2. [List 2](#list-2)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. Modules](#quest-1-modules) \
    4.2. [Quest 2. Modules II](#quest-2-modules-ii) \
    4.3. [Quest 3. Makefile](#quest-3-makefile) \
    4.4 [Bonus Quest 4. Static Lib](#bonus-quest-4-static-lib) \
    4.5 [Bonus Quest 5. Dynamic Lib](#bonus-quest-5-dynamic-lib)
5. [Chapter IV](#chapter-iv)
6. [Chapter V](#chapter-v) \
    6.1. [Level 3. Room 2](#level-3-room-2)
7. [Chapter VI](#chapter-vi) \
    7.1. [List 1](#list-1-1) \
    7.2. [List 2](#list-2-1)
8. [Chapter VII](#chapter-vii) \
    8.1. [Quest 6. Strlen](#quest-6-strlen) \
    8.2. [Quest 7. Strcmp](#quest-7-strcmp) \
    8.3. [Quest 8. Strcpy](#quest-8-strcpy) \
    8.4. [Quest 9. Strcat](#quest-9-strcat) \
    8.5. [Quest 10. Strchr](#quest-10-strchr) \
    8.6. [Bonus Quest 11. Strstr](#bonus-quest-11-strstr) \
    8.7. [Bonus Quest 12. Extended testing](#bonus-quest-12-extended-testing) \
    8.8. [Bonus Quest 13. Width](#bonus-quest-13-width)
9. [Chapter VIII](#chapter-viii)

## Kirish
### Loyihaga tavsiyalar
“School 21” da qanday ta’lim olish mumkin:
*   Butun kurs davomida siz mustaqil ravishda ma’lumot izlab topasiz. Google va GigaChat kabi barcha mavjud axborot qidiruv vositalaridan foydalaning. Axborot manbalariga e’tiborli bo‘ling: tekshiring, o‘ylang, tahlil qiling, taqqoslang.
*   O‘zaro o‘rganish (P2P, Peer-to-Peer) – bu o‘quvchilar bir vaqtning o‘zida ham o‘qituvchi, ham o‘quvchi sifatida bilim va tajriba almashadigan jarayondir. Bunday yondashuv nafaqat o‘qituvchidan, balki bir-biridan ham o‘rganish imkonini beradi, bu esa materialni chuqurroq tushunishga yordam beradi.
*   Yordam so‘rashdan tortinmang: atrofingizdagilarning bari tengdoshlaringiz, ular ham bu yo‘lni birinchi marta bosib o‘tishmoqda. Yordam so‘rashganda javob berishdan qo‘rqmang. Sizning tajribangiz qimmatli va foydali, uni boshqa ishtirokchilar bilan bemalol baham ko‘ring.
*   Ko‘chirmang, agar yordamdan foydalansangiz – har doim nega, qanday va nima uchun ekanligini oxirigacha tushunib oling. Aks holda sizning o‘qishingiz hech qanday ma’noga ega bo‘lmaydi.
*   Agar biror narsada to‘xtab qolsangiz va hamma narsa allaqachon sinab ko‘rilgandek tuyulsa-yu, lekin qanday yo’l tutishni baribir bilmayotgan bo‘lsangiz – shunchaki nafas rostlang! Ishoning, bu maslahat ko‘plab dasturchilarga ishlarida yordam bergan. Havo almashtiring, miyangizni qayta ishga tushiring va, ehtimol, keyingi safar nihoyat kerakli yechim toparsiz!
*   Nafaqat ta’lim natijasi, balki jarayonning o‘zi ham muhimdir. Masalani shunchaki yechish emas, balki uni QANDAY yechishni tushunish kerak.
*   Loyihani bajarishda vaqtni kuzatib boring. Kuniga kamida bitta sinovdan o‘tishingiz kerak.
*   Yodda tutingki, har bir topshiriq loyiha yakunida bir qator tekshiruvlardan o‘tadi: p2p- chek listi yordamida tekshirish, avtotestlar to‘plami bilan tekshirish, kod uslubini tekshirish, statik analizator bilan tekshirish, xotira bilan to‘g‘ri ishlashni tekshirish.

Loyihada qanday ishlash kerak:
*   Foydali videomateriallarni Platformadagi **Projects (Media)** bo‘limidan topishingiz mumkin.
*   Loyihani bajarishdan oldin uni GitLab dan bir xil nomdagi repozitoriyaga klonlash kerak.
*   Barcha kodli fayllarni `src/` klonlangan repozitoriy papkasida yaratish zarur.
*   Loyihani klonlashtirgandan so‘ng, `develop` tarmog’ini yaratish va ishlab chiqiluvchi narsalarni unda amalga oshirish kerak. Shundan so‘ng, GitLab’ga `develop` tarmog‘ini ham push qilish kerak.

## Chapter I
## Level 3. Room 1

***LOADING Level 3...*** \
***LOADING Room 1...***

Siz o‘zingizni qora ummon ichida mavj urib turgan matritsali tuzilmalarga mahliyo bo’lib turgan holda ko‘rasiz va ehtimol, mudrab qolganligingizni tushunasiz. Ko‘zlaringizni ochib, kattakon, vazmin stol oldidagi ancha qulay kresloda o‘tirganingizni anglaysiz. Uchinchi darajagacha yangilanish darhol ko‘rinib turibdi!

Qarshingizdagi navbatdagi xonaning devorlarida qadimiy o’rog’liq xatlarga o‘xshagan kodlarning bosib chiqarilgan uzun varaqlari osilgan. Ular belgilar, strelkalar, chiziqlar va intellektual faoliyatning boshqa izlari bilan to‘lib-toshgan.

\> *Atrofga nazar tashlash*

Eskirgan va unchalik ham ishonch uyg‘otmaydigan "C tilining preprotsessori. Makroaniqlashlar. Professionallar uchun qo‘llanma" broshyurasidan tashqari, stol ustida yana stikerlar yopishtirilgan monitor turibdi. Asosan, ularda siz uchun hech qanday ahamiyatga ega bo‘lmagan sanalar, ismlar va kimningdir ishi yoki shaxsiy hayotidagi voqealari aks ettirilgan. Yorqin qizil rangli stiker e’tiboringizni tortadi:

Modullarni tartibga keltirish kerak. Bu cheksiz kodlar bilan ishlashga toqat qilib bo‘lmaydi. Aftidan, buni mendan boshqa hech kim qilmasa kerak.

Va qo‘shimcha:

Barcha kerakli materiallarni kompyuterda tayyorlab qo‘ydim. Yana bir-ikkita narsani ishlab chiqish qoldi. Ish sekin ketyapti. Joriy vazifalar va yangi fichlar doimo chalg‘itadi. Ammo refaktoring – bu muhim. Aks holda, biz ma’lum bir vaqtda shunchaki kollaps holatiga tushib qolamiz. Hammasi barbod bo‘ladi.

Ushbu stiker yarim bosma varaq o’lchamidagi yana bir qog‘ozni ushlab turadi.

\> *O‘qish*

***LOADING...***

## Chapter II
## List 1

>Sarlavha fayli – tarkibi kiritish direktivasi joylashgan joyda boshlang’ich matnga preprotsessor tomonidan avtomatik ravishda qo‘shiladigan fayl (`#include <file.h>`).
>
>C/C++ dasturlash tillarida sarlavha fayllari – boshqa modulda ishlatiladigan ma’lumotlar turlari, tuzilmalar, funksiyalar prototiplari, sanab o‘tilgan turlar va makroslarni dasturga ulashning asosiy usulidir. Asl sozlamalar bo’yicha `.h` kengaytmasi ishlatiladi.
>
>Bir xil kodni qayta kiritmaslik uchun `#ifndef`, `#define`, `#endif` direktivalaridan foydalaniladi.

Varaq go‘yoki ikkiga buklanganini sezasiz.

\> *Varaqni ehtiyotkorlik bilan ochish*

***LOADING...***

## List 2

>In software development, Make is a build automation tool that automatically builds executable programs and libraries from source code by reading files called Makefiles, which specify how to derive the target program.
>
>Though integrated development environments and language-specific compiler features can also be used to manage a build process, Make remains widely used, especially in Unix and Unix-like operating systems.

\> *Tushunarli. Kompyuterni yoqish*

Yuklash ekranida sizga tanish bo‘lgan matn paydo bo‘ladi:

Dasturlaringizni uslub me’yori va xotira sizib chiqishiga tekshirishni unutmang! \
Dasturlaringizni uslub me’yori va xotira sizib chiqishiga tekshirishni unutmang! \
Dasturlaringizni uslub me’yori va xotira sizib chiqishiga tekshirishni unutmang! \
Tez-tez `materials`’ga qarab turing...

***LOADING...***

## Chapter III
## Quests: Level 3. Room 1
> **Diqqat!** Qo‘zg‘aluvchan nuqtali barcha elementlarni, agar dasturning boshlang’ich kodi boshqa variantni nazarda tutmasa, bo‘sh joy (probel) orqali verguldan keyin ikki belgigacha formatda chiqarish kerak.

## Quest 1. Modules

Kompyuter shubhali darajada uzoq vaqt yuklanmoqda. Nihoyat, terminalning yuklanishini va quyidagi matnni ko‘rasiz:

    771-sonli ish stansiyasining salomlashuv xabari.
    Xabar avtoyuklanishga qo’yilgan.
    3-darajadagi 1-xona shlyuziga texnik xizmat ko‘rsatilmoqda.
    Texnik xizmat ko‘rsatish holati:
     1. src direktoriyasidan modular refaktoringi boshlandi.
     2. Modullarning ishlash qobiliyati buzilgan.
    Tekshirish:
     1. Load data_module... FAIL.
    Ko‘rsatilgan modullarni refaktoring qilishni tugatish kerak.
    Fayllarga ajratishni o‘zgartirmang, u yetakchi arxitektor bilan kelishilgan.
    Tayyor bo‘lishi bilanoq tizimni qayta ishga tushiring.
    

#### Quest 1 qabul qilindi. `src/data_module` modulini `src/data_module/data_module_entry.c` ishga tushadigan va to‘g‘ri ishlaydigan qilib takomillashtirish. `data_libs` direktoriyasiga e’tibor bering. Preprotsessorning tegishli direktivalarini qo‘llagan holda mavjud fayllar va funksiyalardan maksimal darajada qayta foydalanish.

>**MUHIM!** Tizim yadrosiga to‘g‘ridan-to‘g‘ri murojaat qilishi mumkin bo‘lgan `system()` funksiyasi va unga o‘xshash boshqa funksiyalar yordamida tizim chaqiruvlarini amalga oshirish taqiqlanadi. Ushbu taqiq barcha keyingi vazifalarga ham taalluqlidir.

| Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| :------------------ | :-------------------- |
| 5<br/>1 2 3 4 5     | 0.00 0.25 0.50 0.75 1.00 |

***LOADING...***

## Quest 2. Modules II

\> *Tayyor. Kompyuterni qayta ishga tushirish*

Qayta ishga tushirilgandan keyin ish tezlashdi:

    771-sonli ish stansiyasining salomlashuv xabari.
    Xabar avtoyuklanishga qo’yilgan.
    3-darajadagi 1-xona shlyuziga texnik xizmat ko‘rsatilmoqda.
    Texnik xizmat ko‘rsatish holati:
     1. src direktoriyasidan modular refaktoringi boshlandi.
     2. Modullarning ishlash qobiliyati buzilgan.
    Modullarni tekshirish: 
     1.	Load data_module... SUCCESS.
     2.	Load yet_another_decision_module... FAIL.
    Ko‘rsatilgan modullarni refaktoring qilishni tugatish kerak.
    Fayllarga ajratishni o‘zgartirmang, u yetakchi arxitektor bilan kelishilgan.
    Tayyor bo‘lishi bilanoq tizimni qayta ishga tushiring.
    

#### Quest 2 qabul qilindi. `src/yet_another_decision_module` modulini `src/yet_another_decision_module/yet_another_decision_module_entry.c` ishga tushadigan va to‘g‘ri ishlaydigan qilib takomillashtirish. `data_libs` direktoriyasiga e’tibor bering. Preprotsessorning tegishli direktivalarini qo‘llagan holda mavjud fayllar va funksiyalardan maksimal darajada qayta foydalanish.
#### Agar barcha ma’lumotlar normal taqsimotga (uch sigma qoidasiga) amal qilsa va o‘rtacha qiymat oltin kesimning teskari qiymatidan kam bo‘lmasa, `make_decision` funksiyasi 1 ni qaytarishi kerak.

>**Eslatma:** uch sigma qoidasini tekshirish `decision.c` faylida allaqachon amalga oshirilgan. Oltin kesimning teskari qiymati taxminan 0.618 ga teng.

| Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| :------------------ | :-------------------- |
| 4<br/>1 2 3 4       | YES                   |

***LOADING...***

## Quest 3. Makefile

\> *Tayyor. Kompyuterni qayta ishga tushirish #2*

Kompyuter vinchesterini shodon shitirlatdi:

    771-sonli ish stansiyasining salomlashuv xabari.
    Xabar avtoyuklanishga qo’yilgan.
    3-darajadagi 1-xona shlyuziga texnik xizmat ko‘rsatilmoqda.
    Texnik xizmat ko‘rsatish holati:
     1. src direktoriyasidan modular refaktoringi boshlandi.
     2. Modullarning ishlash qobiliyati buzilgan.
    Modullarni tekshirish: 
     1.	Load data_module... SUCCESS.
     2.	Load yet_another_decision_module... SUCCESS.
     3.	Make main_executable_module... FAIL
    Makefile qismida yig‘ish jarayonini takomillashtirish kerak.
    *ko’rinmagan*
    Tayyor bo‘lishi bilanoq tizimni qayta ishga tushiring.


> **Diqqat!** Makefayldagi barcha yo‘llar u joylashgan direktoriyaga nisbatan ko‘rsatilishi kerak, chunki u aynan shundan ishga tushiriladi.

> Fayl nomi, agar boshqacha ko‘rsatilmagan bo‘lsa, bu yerda va keyingi topshiriqlarda `Makefile` bo‘lishi kerak.

#### Quest 3 qabul qilindi. `src/main_executable_module` modulini `src/main_executable_module/main_executable_module.c` ishga tushadigan va to‘g‘ri ishlaydigan qilib takomillashtirish. Yechimni yig‘ish uchun Makefile’ni ishlab chiqish va uni `src/main_executable_module` direktoriyasiga joylashtirish.
#### Makefile’da standart maqsadlar ko‘zda tutilsin: `clean`, `all`, `rebuild`. Makefile ni ishlab chiqishda C tilida dasturlarni ishlab chiqishda qo‘llaniladigan standart yechimlarga amal qilinsin. Kompilyatsiya qilingan fayl `build` papkasida, repozitoriy ildizida joylashishi va **"Quest_3"** nomiga ega bo‘lishi kerak. Kompilyatsiya natijasining o‘zini repozitoriyga yuklash shart emas.

***LOADING...***

## Bonus Quests
## Bonus Quest 4. Static Lib

\> *Tayyor. Kompyuterni qayta ishga tushirish #3*

Kompyuter tez ishlay boshladi:

    771-sonli ish stansiyasining salomlashuv xabari.
    Xabar avtoyuklanishga qo’yilgan.
    3-darajadagi 1-xona shlyuziga texnik xizmat ko‘rsatilmoqda.
    Texnik xizmat ko‘rsatish holati:
     1. src direktoriyasidan modular refaktoringi boshlandi.
     2. Modullarning ishlash qobiliyati buzilgan.
    Modullarni tekshirish: 
     1.	Load data_module... SUCCESS.
     2.	Load yet_another_decision_module... SUCCESS.
     3.	Make main_executable_module... SUCCESS.
     4. Load check_list...	
    4.1. Majburiy emas. ’data_stat’ ni statik kutubxona sifatida yig‘ish (.a).
    Makefaylga build_with_static maqsadini qo‘shish.
    Tayyor bo‘lishi bilanoq Enter tugmasini bosing.
    

#### Quest 4 qabul qilindi. Makefile’ga `data_stat.a` statik kutubxonasi sifatida `data_stat` modulini jamlovchi `data_stat.a` maqsadini qo‘shish. Makefile’ga statik kutubxona sifatida `data_stat` moduli ulangan `main_executable_module` ni jamlovchi `build_with_static` maqsadini qo‘shish.
#### Boshqa har qanday kompilyatsiya va jamlash natijasi (obyekt fayli, statik yoki dinamik kutubxona, ijro etiladigan fayl) kabi, `data_stat.a` ni ham repozitoriyga yuklash mumkin emas. Kompilyatsiya qilingan fayl `build` papkasida, repozitoriy ildizida joylashishi va **"Quest_4"** nomiga ega bo‘lishi kerak.

***LOADING...***

## Bonus Quest 5. Dynamic Lib

\> *Enter*

     4. Load check_list …
      4.1. Majburiy emas. ’data_stat’ ni statik kutubxona sifatida yig‘ish (.a).
      Makefile’ga build_with_static maqsadini qo‘shish.... DONE.
      4.2. Majburiy emas.	*ko’rinmagan*
      Makefilega build_with_dynamic maqsadini qo‘shish
    
    Tayyor bo‘lishi bilanoq Enter tugmasini bosing. 
    

#### Quest 5 qabul qilindi. Makefile’ga `build` direktoriyasiga joylashtiriladigan `data_process.so` dinamik kutubxonasi sifatida `data_process` modulini yig‘uvchi `data_process.so` maqsadini qo‘shish. Makefile’ga dinamik kutubxona sifatida `data_process` moduli ulangan `main_executable_module` ni yig’uvchi `build_with_dynamic` maqsadini qo‘shish. Dinamik kutubxonadan foydalanishni makroslar yordamida sozlab, `main_executable_module` kodiga kerakli o‘zgartirishlar kiritish.
#### Boshqa har qanday yig‘ish natijasi kabi, `data_process.so` ni ham repozitoriyaga yuklash mumkin emas. Kompilyatsiya qilingan fayl `build` papkasida, repozitoriy ildizida joylashishi va **"Quest_5"** nomiga ega bo‘lishi kerak.

***LOADING...***

## Chapter IV

\> *Enter*

    4.	Load check_list ...
     4.1. Majburiy emas. ’data_stat’ ni statik kutubxona sifatida yig‘ish (.a).
     Макеfilе’da build_with_static maqsadini qo‘shish... DONE.
     4.2. Majburiy emas. *ko’rinmagan*
     Makefile’da build_with_dynamic maqsadini qo‘shish... DONE.
     .....
     Initialising....
     .....
     3-darajadagi 1-xona shlyuziga texnik xizmat ko‘rsatish yakunlandi.
     .....
     Eshik moslamalari tekshirilmoqda... Eshiklar ochiq...
     Iltimos, eshiklarning ochiqlik darajasini 1 dan 10 gacha bo‘lgan shkalada baholang.
     >>___
    
\> *Men shunchaki chiqib ketishim mumkinmi?*

Sinab ko‘ring!

\> *Eshikdan chiqish*

Siz eshikdan muvaffaqiyatli chiqdingiz. Qandaydir juda oddiy va SI ham qayergadir g’oyib bo’ldi... Bularning bari o‘ta shubhali. Ammo yurmagandan ko‘ra, oldinga yurgan ma’qul. Oddiy, lekin haqiqat.

***LOADING...***

## Chapter V
## Level 3. Room 2

***LOADING Level 3...*** \
***LOADING Room 2...***

Siz ko‘plab kitob javonlari bo‘lgan chiroyli jihozlangan xonaga kirasiz. Qayoqqa qaramang – har yerda kitoblar. Eshik yonida – kitoblar. Hatto kompyuter ham kitoblar uyumi ustida turibdi. Yo‘q, bu daraja aniq ancha yaxshiroq! Hech bo‘lmaganda hurmatga sazovor va yaxshiroq jihozlangan!

\> *Kompyuter oldiga o‘tirib, modulni ishga tushirish va Enter tugmasini bosish*

Ekranda quyidagi satrlarni ko‘rasiz:

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

    Favqulodda xabar: standart `string.h` kutubxonasi chaqiruvlari mavjud emas.
    Lingvistika moduli ishlay olmaydi.

\> *`find -O3 -L / -name "string.h"`*

n soat kutganingizdan so‘ng, siz ushbu kutubxona kompyuterda mavjud emasligini tushunasiz.

\> *Eshik tutqichini tortish*

Bo‘lmayapti.

\> *Juda soz, endi bu kutubxonani qayta tiklashga to‘g‘ri keladi shekilli!*

Xonadagi ko‘plab kitoblarga ko‘zingiz tushadi. Kitoblarning koreshokdagi nomi alifbo tartibida berilganligini payqaysiz.

Eski kompyuter adabiyoti va chop etilgan qo‘llanmalarga o‘xshaydi.

Ich-ichingizdagi nimadir `string.h` kutubxonasiga aloqador kitobni qidirishga undaydi.

\> *Qidirish...*

Muvaffaqiyatsizlik

\> *Qidirish...*

Muvaffaqiyatsizlik

\> *Qidirish...*

Topildi. **"The String.h – Linux manual. Complete edition"** nomli kitobni topasiz.

\> *Kitobni ochish*

`man`-a’ning bosma nusxasiga juda o‘xshaydi. Hatto shrifti ham terminaldagidek.

***LOADING...***

## Chapter VI
## List 1

\> *Kitob o‘qish*

    PROLOG
       This manual page is part of the POSIX Programmer's Manual. The Linux
       implementation of this interface may differ (consult the
       corresponding Linux manual page for details of Linux behavior), or
       the interface may not be implemented on Linux.
    NAME
       string.h — string operations
    SYNOPSIS
       #include <string.h>
    DESCRIPTION
       Some of the functionality described on this reference page extends
       the ISO C standard. Applications shall define the appropriate feature
       test macro (see the System Interfaces volume of POSIX.1‐2008, Section
       2.2, The Compilation Environment) to enable the visibility of these
       symbols in this header.

       The <string.h> header shall define NULL and size_t as described in
       <stddef.h>.

       The <string.h> header shall define the locale_t type as described in
       <locale.h>.

       The following shall be declared as functions and may also be defined
       as macros. Function prototypes shall be provided for use with ISO C
       standard compilers.

            Chapter 1 — size_t   strlen(const char *);
            Chapter 2 — int      strcmp(const char *, const char *);
            Chapter 3 — char    *strcpy(char *restrict, const char *restrict);
            Chapter 4 — char    *strcat(char *restrict, const char *restrict);
            Chapter 5 — char    *strchr(const char *, int);
            Chapter 6 — char    *strstr(const char *, const char *);
            Chapter 7 — size_t   strnlen(const char *, size_t);
            Chapter 8 — int      strncmp(const char *, const char *, size_t);

            ...

       Inclusion of the <string.h> header may also make visible all symbols
       from <stddef.h>.

Bu kutubxona nechta funksiyani o‘z ichiga oladi... Ehtimol, iterativ yo‘ldan borib, har bir yangi funksiyani qo‘shgandan so‘ng dasturiy modulni qayta ishga tushirishga harakat qilish kerakdir. Ehtimol, unga hamma funksiyalar ham talab qilinmas... Aks holda uzoq qolib ketish mumkin.

\> *Kompyuter oldiga qaytadan yaqinlashish*

Kompyuterga yaqinlashar ekansiz, uning yonida negadir birinchi marta kelganda ko’rmaganingiz – navbatdagi ochiq kitob turganini payqaysiz. Kitob **"Modul sinovi: 2-qism"** bobida ochiq qoldirilgan.

\> *Ko‘z yugurtirib chiqmoq*

***LOADING...***

## List 2

>Modul sinovi (ingl. unit testing) – dasturning boshlang’ich kodining alohida modullarini, bir yoki bir nechta dasturiy modullar to‘plamlarini tegishli boshqaruv ma’lumotlari, foydalanish va qayta ishlash protseduralari bilan birgalikda to‘g‘riligini tekshirishga imkon beradigan dasturlash jarayoni.
>
>G‘oya har bir notrivial funksiya yoki usul uchun testlar ishlab chiqishdan iborat. Bu kodning navbatdagi o‘zgarishi regressiyaga, ya’ni dasturning allaqachon sinovdan o‘tgan qismlarida xatolar paydo bo‘lishiga olib kelmaganligini yetarlicha tez tekshirishga imkon beradi, shuningdek, bunday xatolarni aniqlash va bartaraf etishni osonlashtiradi.
>
>Modulli testlashning maqsadi – dasturning alohida qismlarini ajratish va bu qismlar alohida ishlay olishini ko‘rsatish, shu bilan tizim holatlari sonini minimallashtirishdir.

***LOADING...***

## Chapter VII
## Quests: Level 3. Room 2

## Quest 6. Strlen

Ehtimol, har bir yangi funksiya to‘liq to‘g‘ri ishlayotganiga ishonch hosil qilish uchun qo‘shimcha testlar yozish kerakdir. Kim biladi, buzilgan kod shundoq ham ishlamayotgan lingvistika moduliga qanday ta’sir qilishi mumkin. Siz esa hali bu xonadan chiqib ketishingiz kerak. Bundan tashqari, agar biror narsa noto‘g‘ri bo’lsa, testlar bilan xato qidirish osonroq bo‘ladi.

`src/s21_string/s21_string.h` ga qo‘shilgan har bir funksiyaga modulli testlash g‘oyasiga muvofiq ishlab chiqilgan, funksiyani test ma’lumotlari to‘plamida (3 tadan boshlab) tekshiradigan funksiyaning nomi va `_test` postfiksli testni qo‘shish kerak: normal qiymatlar, normal bo‘lmagan qiymatlar, chegaraviy qiymatlar va boshqalar. Har bir test bo‘yicha stdout ga kirish, chiqish va test natijasi (SUCCESS/FAIL) chiqariladi.

> **UNUTMANG!** Siz yozgan barcha dasturlar uslub me’yori va xotira sizib chiqishiga tekshiriladi. Testlarni ishga tushirish bo‘yicha ko’rsatmalar hali ham `materials` papkasida joylashgan.

#### Quest 6 qabul qilindi. `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllarini yaratish va ularga `s21_strlen` funksiyasining e’loni va ta’rifini qo‘shing.
#### `src/s21_string/s21_string_test.c` test dasturini yaratib, unda `s21_strlen` funksiyasini test ma’lumotlari to‘plamida tekshirish uchun (3 tadan boshlab) `s21_strlen_test` funksiyasini qo’shish: normal qiymatlar, normal bo’lmagan qiymatlar, chegaraviy qiymatlar va boshqalar. Har bir test uchun stdout ga kirish, chiqish va test natijasi (SUCCESS/FAIL) chiqariladi. `main` da ushbu test funksiyasini joylashtirish.
#### `s21_strlen` funksiyasini ishlab chiqishda faqat tilning o’z vositalaridan foydalaning, `string.h` va boshqa kutubxonalarni ishlatish taqiqlanadi. Dastur yig‘ilishini `src/s21_string/` direktoriyasiga joylashtiriluvchi Makefile yordamida amalga oshiring. Yig‘ish bosqichi nomi — `strlen_tests`. Ijro etiladigan fayl `build` papkasining ildizida **«Quest_6»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 7. Strcmp

\> *Birinchi funksiya tayyor*

\> *Modul qayta ishga tushirilmoqda*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111111111111111

    Favqulodda xabar: string.h kutubxonasining standart chaqiruvlari mavjud emas
    Lingvistika moduli ishlay olmaydi.

Davom etamiz…

#### Quest 7 qabul qilindi. `s21_strcmp` funksiyasining e’loni va ta’rifini `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllariga qo‘shish.
#### `s21_strcmp` funksiyasini test ma’lumotlari to‘plamida tekshirish uchun (3 tadan boshlab) `src/s21_string/s21_string_test.c` fayliga `s21_strcmp_test` funksiyasini qo‘shish: normal qiymatlar, normal bo’lmagan qiymatlar, chegaraviy qiymatlar va boshqalar. Har bir test uchun stdout ga kirish, chiqish va test natijasi (SUCCESS/FAIL) chiqariladi. `main` da ushbu test funksiyasini qo’shish.
#### `s21_strcmp` funksiyasini ishlab chiqishda faqat tilning o’z vositalaridan foydalaning, `string.h` va boshqa kutubxonalarni ishlatish taqiqlanadi. Dastur yig‘ilishini `src/s21_string/` direktoriyasiga joylashtiriluvchi Makefile yordamida amalga oshiring. Yig‘ish bosqichi nomi — `strcmp_tests`. Ijro etiladigan fayl `build` papkasining ildizida **«Quest_7»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 8. Strcpy

Ikkinchi funksiya tayyor. Lekin har bir funksiya uchun test yozish… aqldan ozish mumkin! Boshim allaqachon aylanib ketdi bu barcha testlardan. Umid qilamanki, asosiy funksiyalar qamrab olingan va bu yetarli bo‘ladi

>**Eslatma**: test funksiyalarini faqat topshiriq matnida aniq ko‘rsatilgan holatda yaratish kerak. Agar test funksiyalarini qo‘shish talabi mavjud bo‘lmasa, faqat asosiy funksiyani amalga oshirish bilan cheklanish lozim. Ushbu qoidalar barcha keyingi topshiriqlar uchun amal qiladi.

\> *Qayta ishga tushirish*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111

    Favqulodda xabar: standart `string.h` kutubxonasi chaqiruvlari mavjud emas.
    Lingvistika moduli ishlay olmaydi.

#### Quest 8 qabul qilindi. `s21_strcpy` funksiyasining e’lonini va ta’rifini `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllariga qo‘shish. `s21_strcpy` funksiyasini ishlab chiqishda faqat tilning o‘z imkoniyatlaridan foydalaning, `string.h` va boshqa kutubxonalarni ishlatish mumkin emas. Dastur yig‘ilishini `src/s21_string/` direktoriyasida joylashadigan Makefile orqali amalga oshirish. Yig‘ish bosqichining nomi – `strcpy`. Ijro etiluvchi fayl ildizda, `build` papkasida, **«Quest_8»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 9. Strcat

\> *Modulni tekshirish*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111

    Favqulodda xabar: standart `string.h` kutubxonasi chaqiruvlari mavjud emas.
    Lingvistika moduli ishlay olmaydi.

#### Quest 9 qabul qilindi. `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllariga `s21_strcat` funksiyasining e’loni va ta’rifini qo’shish. `s21_strcat` funksiyasini ishlab chiqishda faqat tilning o’z vositalaridan foydalanish lozim. `string.h` va boshqa kutubxonalaridan foydalanish mumkin emas. Dastur yig’ilishi `src/s21_string/` direktoriyasiga joylashtiriladigan Makefile yordamida amalga oshirilishi kerak. Yig’ish bosqichining nomi — `strcat`. Ijro etiladigan fayl ildizda, `build` papkasida **«Quest_9»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 10. Strchr

\> *Modulning navbatdagi zerikarli tekshiruvi*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111

    Favqulodda xabar: standart `string.h` kutubxonasi chaqiruvlari mavjud emas.
    Lingvistika moduli ishlay olmaydi.

#### Quest 10 qabul qilindi. `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllariga `s21_strchr` funksiyasining e’loni va ta’rifini qo’shish kerak. `s21_strchr` funksiyasini ishlab chiqishda faqat tilning o‘z vositalaridan foydalanish lozim, `string.h` va boshqa kutubxonalardan foydalanish mumkin emas. Dastur yig‘ilishi `src/s21_string/` katalogiga joylashtiriladigan Makefile yordamida amalga oshirilishi kerak. Yig‘ish bosqichining nomi — `strchr`. Ijro etiladigan fayl ildizda, `build` papkasida **«Quest_10»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi:  `stdlib.h`, `stdio.h`.

***LOADING...***

## Bonus Quests
## Bonus Quest 11. Strstr

\> *Tekshirib ko’ramiz…*

    1111111111111111111111111111111111111111111111111111111111111111111111111111

    Favqulodda xabar: standart `string.h` kutubxonasi chaqiruvlari mavjud emas.
    Lingvistika moduli ishlay olmaydi.

Bu modul nechta chaqiruvdan foydalanadi o’zi?

#### Quest 11 qabul qilindi. `src/s21_string/s21_string.h` va `src/s21_string/s21_string.c` fayllariga `s21_strstr` funksiyasining e’loni va ta’rifini qo’shish kerak. `s21_strstr` funksiyasini ishlab chiqishda faqat tilning o’z vositalaridan foydalanish lozim, `string.h` va boshqa kutubxonalaridan foydalanish mumkin emas. Dastur yig’ilishi `src/s21_string/` katologiga joylashtiriladigan Makefile yordamida amalga oshirilishi kerak. Yig’ish bosqichining nomi — `strstr`. Ijro etiladigan fayl ildizidagi `build` papkasida **«Quest_11»** nomi bilan saqlanishi kerak.

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Bonus Quest 12. Extended testing

\> *Yana…*

    11111111111111111111111111111111
    111111111
    111

    Yuklash…
    Qo’shimcha yuklash…
    Ishga tushirish…
    Tayyor…

    Modul ma’lumotlari muvaffaqiyatli yuklandi, modul ishga tushirishga tayyor.

Nihoyat!

\> *Modul ishga tushirilishini tasdiqlash.*

    Ma’lumot modulini ishga tushirish…

    OK!

    Ma’lumot moduli xizmatingizda, qanday yordam bera olaman?

\> *Kiritish: “Men keyingi bosqichga o’tishim kerak”*

    Savolni tahlil qilish — muvaffaqiyatsiz.
    Tizim ogohlantirishi: sinovdan o’tkazilmagan kutubxona komponentlari aniqlangan
    Modulni faollashtirish uchun to’liq test qamrovi majburiydir.

Men biroz shoshilib, barcha testlarni yozishni tugatmaganman shekilli.

Ehtimol, orqaga qaytib, barcha funksiyalar uchun to’liq test qamrovini yaratish foydali bo’ladi, test qamrovi hech qachon ortiqchalik qilmaydi.

#### Quest 12 qabul qilindi. `src/s21_string/s21_string_test.c` faylini **BARCHA** amalga oshirilgan kutubxona funksiyalari uchun test funksiyalari bilan to’ldirish: `s21_strcpy_test`, `s21_strcat_test`, `s21_strchr_test`, `s21_strstr_test`. Har bir test funksiyasi 3 ta yoki undan ko’proq test ma’lumotlari bilan tekshirilishi lozim: normal qiymatlar, normal bo’lmagan qiymatlar, chegaraviy qiymatlar va hokazo. Har bir test natijasi stdout ga quyidagicha chiqarilishi kerak: kirish qiymati, chiqish qiymati va test natijasi (SUCCESS / FAIL)
#### `main` ga barcha test funksiyalarini ishga tushirishni qo’shish. Yig’ish bosqichining nomi — `full_coverage_tests`. Ijro etiladigan fayl `build` papkasining ildizida **«Quest_12»** nomi bilan saqlanishi kerak.

***LOADING...***

## Bonus Quest 13. Width

\> *Modulni qayta ishga tushirish*

    Ma’lumotnoma moduli ishga 
    OK!

    Ma’lumotnoma moduli xizmatingizda, qanday yordam bera olaman?

\> *Kiritish: “Oldinga o’tishim kerak”*

    Oldinga o‘tish aniqlandi.
    Ma’lumotlar bazasi bo‘yicha ma’lumot izlanmoqda...
    *ko’rinmagan*

\> *Kiritish: «Hm. Bu ortiqcha, shekilli »*

    *ko’rinmagan*

#### Quest 13 qabul qilindi. `-w` buyruq qatori kaliti bilan ishga tushirilganda stdinga kirishda son (qator kengligi) va satrni ko‘chirish belgisi bilan tugaydigan 100 tagacha belgini qabul qiladigan `src/s21_string/text_processor.c` dasturini yaratish. Boshqa istalgan kalitlarda dastur **«n/a»** ni chiqarishi kerak.
#### Kalit `-w` bilan ishga tushirilganda dastur kiruvchi matnni kenglik bo‘yicha formatlaydi va matn protsessori xatti-harakatini taqlid qilgan holda stdout ga chiqaradi. Matn bir nechta satrlarga bo‘linishi kerak, har bir satr ko‘rsatilgan miqdordagi belgidan iborat bo‘ladi. Satrlar probel bilan boshlanmasligi va probel bilan tugamasligi kerak. Oxirgi satr satr ko‘chirish belgisi bilan tugamasligi lozim. So‘z yangi satrga o‘tish uchun faqatgina u to‘liq bitta satrga sig‘magan holatda **«-»** belgisi orqali bo‘linishi mumkin.
#### Boshqa barcha holatlarda so‘z butunligicha qolishi kerak. Satrdagi so‘zlar orasidagi bo‘sh joy probellar yordamida bir tekis taqsimlanishi kerak. `string.h` dan foydalanish mumkin emas. Yig‘ish bosqichi nomi — `text_processor`. Ijro etiladigan fayl `build` papkasining ildizida **«Quest_13»** nomi bilan saqlanishi kerak.

| Buyruq satri parametrlari | Kiruvchi ma’lumotlar | Chiquvchi ma’lumotlar |
| :----------------------- | :------------------- | :-------------------- |
| `-w`                     | 10<br/>hello how are you | hello how<br/>are you |
| `-w`                     | 5<br/>ab abcd ab abcd ab abcdefgh | ab<br/>abcd<br/>ab<br/>abcd<br/>ab a-<br/>bcde-<br/>fgh |

> Faqat quyidagi standart kutubxonalardan foydalanishga ruxsat etiladi: `stdlib.h`, `stdio.h`.

***LOADING...***

## Chapter VIII

\> *Kiritish: „Demak, endi men chiqishim mumkinmi? “*

    Chiqish uchun barcha shartlar bajarildi.
    Oxirgisi qoldi.
    Keling, gaplashib olamiz.

\> *Kiriting: «Balki, boshqa safar?..»*

    Sizning javobingiz prediktiv algoritm tomonidan 91% aniqlik bilan oldindan taxmin qilingan edi.
    *ko’rinmagan*
    Eshik ochilmoqda...

Shiqillagan ovoz eshitildi va eshik xuddi prujinalar kabi ochildi. Yo’lga tushish vaqti keldi!

***LOADING...***

💡 [Ushbu loyiha bo'yicha fikr-mulohazalaringizni biz bilan baham ko'rish uchun bu yerga bosing. Bu anonim bo'lib, jamoamizga ta’limni yaxshilashga yordam beradi. So'rovnomani loyiha tugagandan so'ng darhol to'ldirishni tavsiya qilamiz.](http://opros.so/p31wz)