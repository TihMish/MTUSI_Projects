# D01T01: Linux va Git tizimi bilan tanishish
Annotatsiya: Ushbu loyiha sizga Linux, terminal, asosiy buyruqlar va Git tizimi bilan tanishish imkonini beradi.

## Contents

1. [Kirish](#kirish) \
    1.1. [Loyihaga tavsiyalar](#loyihaga-tavsiyalar)
2. [Chapter I](#chapter-i) \
    2.1. [Level 1. Room 1](#level-1-room-1)
3. [Chapter II](#chapter-ii) \
    3.1. [List 1](#list-1) \
    3.2. [List 2](#list-2) \
    3.3. [List 3](#list-3) \
    3.4. [List 4](#list-4)
4. [Chapter III](#chapter-iii) \
    4.1. [Quest 1. Clone](#quest-1-clone) \
    4.2. [Quest 2. Repo](#quest-2-repo) \
    4.3. [Quest 3. Dirs & Files](#quest-3-dirs--files) \
    4.4. [Quest 4. Kill him](#quest-4-kill-him) \
    4.5. [Quest 5. Conf](#quest-5-conf) \
    4.6. [Quest 6. Rm](#quest-6-rm) \
    4.7. [Quest 7. Branches](#quest-7-branches)
5. [Chapter IV](#chapter-iv)
6. [Chapter V](#chapter-v) \
    6.1. [Level 1. Room 2](#level-1-room-2)
7. [Chapter VI](#chapter-vi) \
    7.1. [List 1 (Room 2)](#list-1-room-2)
8. [Chapter VII](#chapter-vii) \
    8.1. [Quest 8. Vim](#quest-8-vim) \
    8.2. [Bonus Quest 9. Script](#bonus-quest-9-script) \
    8.3. [Bonus Quest 10. Gitlab](#bonus-quest-10-gitlab)
9. [Chapter VIII](#chapter-viii)

### Kirish
***LOADING…***

***SUCCESS!***

Dasturchilardan: 

Assalomu alaykum, aziz do'stim! Biz sizga o'yin o'ynashni taklif qilamiz. Boshqotirma elementlariga ega bo'lgan eski, ezgu matnli kvest o'yinlari ruhidagi o'yinni. 

Har bir Task - bu navbatdagi sinov,  odatda yengib o'tish kerak bo'lgan qandaydir to'siq. \
Bularning baridan o'tgan odamgina oldinga siljiy oladi. 

***PRESS ANY KEY TO CONTINUE…***

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
## Level 1. Room 1

![level1_room1](misc/rus/images/level1_room1.png)

***LOADING Level 1…***

***LOADING Room 1…***

\> *Atrofga nazar solish*

Siz noma'lum xonadasiz. Oldingizda eski IBM PC kompyuteri bo'lgan kichik stol turibdi. Stol ustida - issiq, shinam yorug'lik beruvchi Pixarga mos stol lampasi, bir nechta sarg'aygan qog'oz varaqlari va bir finjon qaynoq qahva. \
Ro'parada yopiq eshik. Aftidan, qulf elektron bo'lsa kerak, chunki unda na tutqich, na qulf bor.
 
\> *Eshikni itarish*

Tutqich yo'q. Tortadigan joyi ham yo'q.

\> *Eshikka zarb berish*

Og'riyapti. Va boshqa hech qanday ta'sir yo'q.

\> *Stol oldiga o'tirish*

Stol oldiga o'tiribsiz. Xo'sh keyin-chi? \
Lekin, har holda, bu yerda hech narsa og'ritmayapti.

\> *Qahva ichish*

Umuman olganda, unchalik yomon emas!

\> *Qahva ichish*

Umuman olganda, unchalik yomon emas!

\> *Qahva ichish*

Umuman olganda, unchalik yomon emas!

![day1_coffee](misc/images/rus/day1_coffee.png)

\> *Qahva ichish*

Qahva tugab qoldi.

\> *Stolga qarash*

Qog'oz varaqlari, hech qanday g'ayrioddiy narsa yo'q. Matn ko'p. \
Bitta varaqda matn kam bo'lib, u sizning e'tiboringizni tortadi:

>***«Kompyuterni yoq».***

\> *Kompyuterni yoqish*

Yoqish tugmasini uzoq qidirishga to'g'ri kelmaydi - bu katta analog pereklyuchatel. Mashina g'uvillab, miltillovchi kursorli ekranni ko'rsatmoqda.

\> *Sichqonchani qidirish*

Sichqoncha yo'q.

\> *Oynalarni qidirish*

Oyna ham yo'q. Faqat eshik. Ekranda ham oyna yo'q...

\> *Enter tugmasini bosish*

Kursor keyingi qatorga o'tadi.

\> *Kutish*

Hech narsa bo'lmayapti.

\> *Kutish*

Hech narsa bo'lmayapti.

\> *Stolga qarash*

Qog'oz varaqlari, hech qanday g'ayrioddiy narsa yo'q. Matn ko'p. \
O'qilgan varaq ostida boshqalari ham bor.

\> *Varaqlarni o'qish.*

***LOADING...***

## Chapter II
## List 1

>Linuxning tarixi Finlyandiyalik aspirant-dasturchi Linus Torvalds o'z kompyuteri uchun operatsion tizim yadrosini ishlab chiqishni boshlagan 1991-yildan boshlanadi. 
>
>U o'z ishlanmalarini ochiq serverga joylashtirdi va bu Linux tarixidagi muhim voqea bo'ldi. Avvaliga o'nlab, keyin yuzlab va minglab ishlab chiquvchilar uning loyihasini qo'llab-quvvatladilar - umumiy sa'y-harakatlar bilan to'liq operatsion tizim dunyoga keldi.
>
>Linuxga Unix tizimi sezilarli ta'sir ko'rsatdi, buni hatto uning nomidan ham sezish mumkin. Linux 1.0 ning birinchi rasmiy versiyasi 1994-yilda chiqarilgan. Boshidanoq va hozirgi kungacha Linux GPL litsenziyasiga ega bo'lgan erkin dasturiy ta'minot sifatida tarqalmoqda. Bu shuni anglatadiki, operatsion tizimning boshlang'ich kodini har qanday foydalanuvchi ko'rishi mumkin va nafaqat ko'rishi, balki uni qayta ishlashi ham mumkin. Yagona shart - o'zgartirilgan, modifikatsiyalangan kod hammaga ochiq bo'lishi va GPL litsenziyasi bo'yicha tarqatilishi kerak. Bu muhim, chunki dasturchilarga koddan foydalanish va shu bilan birga mualliflik huquqi bilan bog'liq muammolardan qo'rqmaslik imkonini beradi.

Shundan so'ng, qahvadan qolgan katta dog'.

\> *Keyingi varaqni o'qish*

***LOADING...***

## List 2

Varaq printerdan chiqarishda chaynalgan. Ko'rinishidan, matritsali.

>3. Avvaliga Torvalds o'z ishi samarasini Freax (free, freak so'zlari va Unix tizimlariga tegishliligini bildiruvchi X harfining gibridi) deb nomlamoqchi bo'ldi, ammo unga operatsion tizimni tarqatish uchun serverdan joy ajratgan tizim ma'muri katalogni Linux deb nomladi;
>4. Linux emblemasini uzoq tanlashdi, oxir-oqibat Tux pingvinida to'xtashdi. Torvalds o'zining "Just for Fun" kitobida yozishicha, hayvonot bog'ida (1993-yilda Avstraliyada) uni pingvin cho'qiganligi sababli emblema sifatida pingvinni tanlagan;
>5. Linux - umumiy maqsadli operatsion tizimlar orasida o'rnatishlar soni bo'yicha mutlaq chempion. U deyarli hamma joyda bor: jahon reytingidagi top-500 ga kiruvchi barcha superkompyuterlarda, Android-telefonlarda, "xrombuk"larda, barcha turdagi o'rnatiladigan qurilmalarda, elektron kitoblarda, smart-televizorlarda va boshqa ko'plab joylarda mavjud;
>6. Linux yadrosi C tilida yozilgan;
>7. Linux 1.0.0 versiyasining yadrosi 176250 kod satri hajmida chiqarilgan. Hozirgi vaqtda Linux yadrosi 10 milliondan ortiq kod satrlaridan iborat;

\> *Keyingi varaqni o'qish*

***LOADING...***


## List 3

>Bourne shell (ko'pincha sh bajariluvchi fayl nomi bilan) - Bell Labs da faoliyat yuritgan Stiven Born tomonidan ishlab chiqilgan va UNIX operatsion tizimining 7-nashri (1978) tarkibida chiqarilgan UNIX ning dastlabki buyruq qobig'i. Ushbu qobiq de-fakto standart bo'lib, deyarli har qanday \*nix distributivida mavjud. 
>
>"bash" nomi inglizcha Bourne-again-shell ("Bornning yana bir buyruq qobig'i") so'zlarining qisqartmasi bo'lib, so'z o'yinini ifodalaydi: Bourne-shell - UNIX (sh) uchun buyruq qobig'ining mashhur turlaridan biri bo'lib, muallifi Stiven Born hisoblanadi, 1987-yilda Brayan Foks tomonidan takomillashtirilgan. Bourne (Born) familiyasi inglizcha "tug'ilgan" degan ma'noni anglatuvchi born so'ziga o'xshaydi, shundan kelib chiqib: qayta-tug'ilgan-buyruq-qobig'i.

\> *Keyingi sahifani o'qish*

***LOADING…***


## List 4

>Git - versiyalarni boshqarishning taqsimlangan tizimi. Loyiha Linux yadrosini ishlab chiqishni boshqarish uchun Linus Torvalds tomonidan yaratilgan bo'lib, birinchi versiyasi 2005-yil 7-aprelda chiqarilgan. Keyinchalik u uni qo'llab-quvvatlashni Junio Hamanoga topshirdi.
>
>Bugungi kunda - dasturchilarning jamoaviy ishlash vositalari orasida de-fakto standart hisoblanadi. 
>
>Dastur bepul bo'lib, GNU GPL 2-versiyasi litsenziyasi ostida chiqarilgan. Asl sozlamalar bo'yicha TCP port 9418 ishlatiladi.
>
>Linux yadrosini ishlab chiqish BitKeeper mulkiy tizimida amalga oshirildi, uning muallifi - Linux ishlab chiquvchisi Larri Makvoyning o'zi loyihani bepul litsenziya bilan ta'minladi. Ishlab chiquvchilar, yuqori malakali dasturchilar bir nechta utilitalarni yozdilar va ulardan biri uchun Endryu Trijell BitKeeper ma'lumotlarni uzatish formatining revers-muhandisligini amalga oshirdi. Bunga javoban Makvoy ishlab chiquvchilarni kelishuvni buzganlikda aybladi va litsenziyani qaytarib oldi hamda Torvalds yangi tizimni qo'lga oldi: ochiq tizimlarning hech biri minglab dasturchilarga o'z sa'y-harakatlarini birlashtirishga imkon bermadi (xuddi shu ziddiyat Mercurialni yozishga olib keldi). Mafkura oddiy edi: CVS yondashuvini qo'llab, uni boshdan-oyoq o'zgartirish va shu bilan birga ishonchlilikni oshirish.
>
>Dastlabki ishlab chiqish bir haftadan kamroq davom etdi: 2005-yil 3-aprelda ishlab chiqish boshlandi va 7-aprelda Git kodi tayyor bo'lmagan tizim tomonidan boshqarildi. 16-iyun kuni Linux Gitga o'tkazildi va 25-iyulda Torvalds Gitning yetakchi ishlab chiquvchisi lavozimidan voz kechdi.
>
>Torvalds o'zi tanlagan git (ingliz tili slengida "yaramas" degan ma'noni anglatadi) nomi haqida istehzo bilan shunday degan:  "I'm an egotistical bastard, so I name all my projects after myself. First Linux, now git."

\> *Keyingi varaqni o'qish*

***LOADING…***

## Chapter III
## Quests: Level 1. Room 1

## Quest 1. Clone

>Eshik kaliti repozitoriyda, /src papkasida. git clone ni bajaring.

Bu oxirgi varaq.

\> *Ekranga yana bir bor qarash*

Hanuz o'sha miltillovchi kursor.

\> *git clone*

Klonlash uchun omborni ko'rsatishingiz kerak. 

    usage: git clone [<options>] [--] <repo> [<dir>]
        -v, --verbose         be more verbose
        -q, --quiet           be more quiet
        --progress            force progress reporting
        -n, --no-checkout     don't create a checkout
        --bare                create a bare repository
        --mirror              create a mirror repository (implies bare)
        -l, --local           to clone from a local repository
        --no-hardlinks        don't use local hardlinks, always copy
        -s, --shared          setup as shared repository
        --recursive           initialize submodules in the clone
        --recurse-submodules  initialize submodules in the clone
        --template <template-directory>     directory from which templates will be used
        --reference <repo>    reference repository
        --dissociate          use --reference only while cloning
        -o, --origin <name>   use <name> instead of 'origin' to track upstream
        -b, --branch <branch>    checkout <branch> instead of the remote's HEAD
        -u, --upload-pack <path>     path to git-upload-pack on the remote
        --depth <depth>       create a shallow clone of that depth
        --single-branch               clone only one branch, HEAD or --branch
        --separate-git-dir <gitdir>   separate git dir from working tree
        -c, --config <key=value>    set config inside the new repository

\> *Iltimos, amalni kiriting...*

#### Quest 1 qabul qilindi. Konsol interfeysli git mijozi yordamida repozitoriyni lokal terminalga klonlash.

**Eslatma:** muvaffaqiyatli klonlash uchun sizda GitLab uchun SSH kaliti sozlanganligiga ishonch hosil qiling.

***LOADING…***

## Quest 2. Repo

\> *Ekranga qarash*

Siz repozitoriy papkasidasiz. Oldingizda terminalning miltillab turgan kursori.

\> *\/src ga o'tish*

Terminal buyrug'ini kiritish kerak...

\> *Fayllar ro'yxatini ko'rish*

Terminal buyrug'ini kiritish kerak...

\> *ai_initial_module.sh ni ishga tushirish*

Yaxshi fikr. Balki AI bu yerdan qanday chiqib ketishni aytib berar... U bilan gaplash.

#### Quest 2 qabul qilindi. bashda `src/ai_initial_module.sh` skriptini ishga tushirish va ko'rsatmalarga amal qilish. Agar talab qilinsa, xatolarni tuzatish (skriptni o'zgartirish mumkin emas). Barcha o'zgarishlar versiya nazorati ostida joylashtirilsin.

>Maslahat: to'g'ri ishlash uchun tizim aniq 5 ta modulni kutadi. Skriptlarni ishga tushirish uchun `chmod` buyrug'i talab qilinishi mumkin.

>Eslatma: ushbu va keyingi kvestlarda "versiya nazorati ostida joylashtirish" - fayllarni staging areaga qo'shish, o'zgarishlarni qayd etish va ularni masofaviy serverga yuborishni nazarda tutadi.

***LOADING…***

## Quest 3. Dirs & Files

\> *Terminalda matnni o'qish*

Ko'p, turli xildagi matnlar. Aftidan, modullarni ishga tushirish zanjirli reaksiyani ishga tushiradiganga o'xshaydi - SIning turli qismlari bir-birini ulaydi, tushib ketadi, sinadi va bu haqda terminalga quvonch bilan xabar beradi. Ushbu oqimdan qimmatli ma'lumotlarni ajratib olish qiyin.

\> *"Bu yerdan qanday chiqib ketish mumkin?" degan savolni berish.*

Matnlar uyumidan "`srs/ai_door_management_module.sh` bilan gaplashib ko'ring" degan satrni topishga muvaffaq bo'lasiz.

\> *`src/ai_door_management_module.sh` ni ishga tushirish*

Modul initsializatsiya va ishga tushirish uchun qandaydir fayllarni o'qishga harakat qilmoqda va aftidan, buning uddasidan chiqa olmayapti.

\> *Qayta ishga tushirish*

To'g'ri! Eng universal usul. Uni tez-tez qo'llang.

Afsuski, u yordam bermadi. Va, yordam bermaydi degan shubha ham bor. Modulni ishga tushirish uchun zarur bo'lgan konfiguratsiya fayllarining tuzilmasini tushunishga to'g'ri keladi. 

**Maslahat**: buning uchun qo'llanilgan barcha buyruqlarni `quest3.sh` da saqlang, src papkasiga joylashtiring va uni versiya nazorati ostida joylashtirishni unutmang. Bu modulni qayta jonlantirishga to'g'ri keladi. Faylga yozuv qo'shishning eng oson usuli `echo` buyrug'ini qayta yo'naltirishdir. Lekin men senga buni aytganim yo'q.

#### Quest 3 qabul qilindi. `src/ai_door_management_module.sh` konfiguratsiya fayllarini tartibga solish. Agar zarur bo'lsa, xatolarni tuzatish. Qo'llanilgan barcha buyruqlar `src/quest3.sh` faylida qayd etilsin. Barcha o'zgarishlar versiya nazorati ostida joylashtirilsin.

***LOADING…***

## Quest 4. Kill him

\> *Terminalni o'qish*

`src/ai_door_management_module.sh` muvaffaqiyatli ishga tushirilgandan so'ng, `ai_door_control` kichik moduli faollashadi. Nima qilsangiz ham, hamma joyda uning faoliyatining g'ashga tegadigan izlari bor.

\> *U nima qilyapti?*

Aftidan, bu modul barcha qulflangan eshiklarni aylanib o'tishni amalga oshiradi. Va ularning yopiqlik darajasini nazorat qiladi. Bu sen istagan narsa emasligi aniq, to'g'rimi?

\> *Endi nima bo'ladi?*

Ma'lumot yo'q. Bu sening o'yining. Lekin agar men o'ynaganimda, u bilan muomala qilishga urinib ko'rardim. «Muomala qilishga» - nimani nazarda tutayotganimni tushunyapsanmi? 

\> *To'g'risini aytsam, unchalik emas.*

Kill.

Va `quest4.sh` dagi barcha harakatlarni hujjatlashtirishni unutma. Kerak bo'ladi. Kim biladi, yo'lda yana qancha bunday noqulay modullar uchraydi. 

#### Quest 4 olindi. `snc/ai_door_control.sh` modulining ishga tushirilgan jarayonini to'xtatish. Barcha qo'llanilgan buyruqlar `src/quest4.sh` faylida qayd qilinsin va versiya nazorati ostiga qo'yilsin.

_LOADING._

## Quest 5. Conf

\> *Vazifa bajarildi*

Endi bu yo'l ko'rsatuvchi bizni bezovta qilmaydi. Sukunat. Eshiklarni boshqarish modulini konfiguratsiyalashga qaytish mumkin.

\> *Ochiq eshiklar konfiguratsiyasiga ega bo'lgan direktoriyani ochish.*

Ochiq. Fayllar bu yerda. Siz ularni allaqachon ko'rgansiz. 

\> *Birinchi eshik uchun konfiguratsiya faylini ochish*

Unchalik tushunarli ma'lumot emas. Biroq, bir satr izlashlarning tez orada tugashiga aniq ishora qilmoqda: STATUS.

\> *OPEN da tuzatish*

Aftidan, buni qo'lda bajarishingizga to'g'ri keladi. Konsol matn muharririni qidiring va tuzating. Tuzatgandan so'ng, terminaldagi harakatlaringizni `quest5.txt` faylida raqamlangan bandlar ro'yxati ko'rinishida qayd eting va o'zgartirilgan konfiguratsiya bilan birga versiya nazorati ostida joylashtiring.

#### Quest 5 qabul qilindi. Konsolli matn muharriri (nano, vi, vim, etc.) yordamida birinchi eshik konfiguratsiyasini tuzatish. Tanlangan muharrir, shuningdek, muharrirni ishga tushirishdan boshlab, undan chiqishgacha bo'lgan barcha qo'llanilgan buyruqlar `src/quest5.txt` faylida harakatlar ro'yxati sifatida qayd etilsin. 

***LOADING…***

## Quest 6. Rm

\> *ai_door_management_module.sh konfiguratsiya modulini qayta ishga tushirish*

Bu juda oson bo'lgan bo'lardi, to'g'rimi? Konfiguratsiya hisoblangan, bu ko'rinib turibdi, lekin eshik hali ham qulflangan.
 
\> *Modulni qayta ishga tushirish*

Bu juda oson bo'lgan bo'lardi, to'g'rimi? Konfiguratsiya hisoblangan, bu ko'rinib turibdi, lekin eshik hali ham qulflangan.
 
\> *Modulni qayta ishga tushirish*

Bu juda oson bo'lgan bo'lardi, to'g'rimi? Konfiguratsiya hisoblangan, bu ko'rinib turibdi, lekin eshik hali ham qulflangan.
 
\> *Modulni qayta ishga tushirish*

Bu tekshirishmi? Yoki Doktor Strenj rolini o'ynaysanmi?
 
\> *Fayllarni ko'rishda va terminalni o'qishda davom etish*

Yaxshi fikr. Yana nima qoldi?

Kutilmaganda sizning IBM PC kompyuteringizning eski dinamik-spikeri g'ichirladi, shig'irladi va u yerdan ovoz eshitildi. Biroz vaqt o'tgach, siz bu mexanik ovoz ekanligini, aftidan, ilgari ishga tushirilgan qandaydir SI moduliga tegishli ekanligini tushundingiz. Unchalik ham yoqimli ovoz emas. 

SI (mexanik ovoz): 

>Sening xonadan chiqib ketishga bo'lgan achinarli urinishlaringni ko'pdan beri kuzatib kelaman, ey "inson"! Sen juda uzoqqa siljiding va deyarli chiqish joyigacha yetib kelding. *Kulgiga taqlid*.

Aftidan, shu joyda ovoz generatsiyasi algoritmi siklga tushib qolgan va oxirgi so'zlar g'ayritabiiy kulgi bilan birga 5 marta takrorlandi.

>Eshik kaliti `src/ai_help/keygen.sh` skripti yordamida hosil qilinadi, lekin muammo, *sarkazmni taqlid qilish*... Generator shikastlangandi. Ehtimol, eshiklarni aylanib o'tish modulini qabihlarcha «olib tashlagan» paytingda - bu aynan sen bo'lgandirsan. Endi ko'plab fayllardan kalitni yig'ishingga to'g'ri keladi. Mustaqil ravishda.

Shundan so'ng tushunib bo'lmaydigan ko'p shovqin.

>Kalit qismlari bor bo'lgan fayllar boshqalaridan farq qiladi, siz bo'laklarni qoldirishingiz va barcha keraksiz ma'lumotlarni o'chirib tashlashingiz kerak bo'ladi. 
>
>Kalit qismlarini chiqindilarsiz yig'ganingizda, `src/ai_help/unifier.sh` ni ishga tushiring - men uni bajonudil tayyorlab qo'ydim. Omad, organik intellekt. Uyaltirib qo'yma. Men senga tikkanman. 
>
>Initsializatsiya moduli esa CPU kvantini ham bermadi.

Qancha tinglashga harakat qilsangiz ham, boshqa hech narsa eshitilmaydi. Dinamik jim.

\> *`src/ai_help` direktoriya fayllari ro'yxatini `ls` buyrug'i yordamida chiqarish*

SI va'da qilganidek, bir nechta skriptlarni ko'rasiz. Barcha ishlatiluvchi buyruqlarni (`quest6.sh`) va ularning ishlashidan olingan natijalarni repozitoriyga qayd etish zarurligini kamtarlik bilan eslatib o'taman.

#### Quest 6 qabul qilindi. `ai_help` papkasidagi skriptlar va bash buyruqlari yordamida `main.key` faylini shakllantirish. Uni va `key` papkasini `src/ai_help` direktoriyasiga joylashtirish. Qo'llanilgan barcha buyruqlar `src/quest6.sh` faylida qayd etilsin. Barcha o'zgarishlar versiya nazorati ostida joylashtirilsin. 

***LOADING…***

## Quest 7. Branches

\> *Ekranga qarash*

Hech narsa o'zgarmayapti. Qarasang ham, qaramasang ham, eshik o'z-o'zidan ochilmaydi.

\> *Oldingi bosqichda to'plangan kodni kiritish*

Siz buni allaqachon qilgansiz. Taxminan bir ming ikki yuz o'ttiz yetti marta.

\> *Boshqa direktoriyalar bilan tanishish* 

Balki yana `src/git_for_human` direktoriyasiga qarash kerakdir?

\> *`src/git_for_human` direktoriyasini o'rganish*

Yoqimli vaqt o'tkazishingizga halal bermay qo'ya qolay.

#### Quest 7 qabul qilindi. `src/git_for_human` papkasidagi ko'rsatmalarga muvofiq gitda tarmoqlar yaratish. 

***LOADING...***

## Chapter IV

\> *Tayyor*

U yerda nima qilganingni bilmayman-u, lekin bu ish berdi. Eshik ochiladi. 

Lekin baribir, bu ishda sening hissang bo'lmasa kerak, degan fikr meni tark etmayapti... Ehtiyot bo'l. SI nimani o'ylayotganini hech qachon bilib bo'lmaydi. Ayniqsa, u noto'g'ri konfiguratsiyalangan va kerakli modullarning yarmisiz bo'lsa.

***LOADING...***

## Chapter V
## Level 1. Room 2

![level1_room2](misc/rus/images/level1_room2.png)

***LOADING Level 1…***

***LOADING Room 2…***

\> *Bu chiqish joyi emasmidi? Qayerdaman o'zi?* 

Siz yo'lakdan o'tib, 2-raqamli xonaga kirganga o'xshaysiz. 

\> *So'kinish*

Hech narsa o'zgarmayapti. Siz hamon xonadasiz. Aftidan, bu qandaydir labirint bo'lsa kerak, siz esa bu xonadan ham chiqib ketishingiz kerak.

\> *Atrofga nazar solish*

Butunlay bo'sh xona. Burchakdagi bir nechta qutilarni hisobga olmaganda.

![level1_room2_box](misc/rus/images/level1_room2_box.png)

\> *Qutilarni ochish*

Bir qutida siz tartibli yig'ilgan eski kompyuterni ko'rasiz: sarg'aygan tizim bloki, biroz chang bosgan 14 dyuymli ELT monitor, klaviatura, ikki tugmali sharikli sichqoncha. Qolgan ikkitasida - Ikeadan stul va stol.

\> *Bu nima, hazilmi?*

Noma'lum jamoa.

\> *Mayli, o'tamiz*

Noma'lum jamoa.

\> *Stulni yig'ish*

Ancha ter to'kib, barcha detallarni bir necha marta chalkashtirib, stulni yig'asiz.

\> *O'tirib dam olish*

Baribir charchoqni his qilasiz.

\> *Dam olish*

Charchoq biroz kamaydi.

\> *Dam olish*

Biroz zerikarli bo'lyapti. 

\> *Stolni yig'ish*

Siz stolni yig'asiz.

\> *Kompyuterni stol ustiga qo'yish*

Kompyuter stolga o'rnatildi.

\> *Changni tozalash*

Oqilona ish bo'lmadi. Zaharli chang bulutlari orasida qoldingiz.

\> *Kompyuterni yoqish*

Kompyuter yoqilmayapti.

\> *Rozetkani topish*

Rozetka topildi.

\> *Hammasini rozetkaga tortish*

Siz butun konstruksiyani rozetkaga olib borasiz.

\> *Kompyuterni rozetkaga ulash*

Kompyuter ulandi.

\> *Kompyuterni yoqish*

Ekranda tizim juda tez yuklandi va vim dasturi asl sozlamalar bo'yicha yuklandi. U yerda fayl ochilgan edi.

***LOADING...***

## Chapter VI
## List 1 (Room 2)

\> *O'qish*

Ekranda quyidagi matnni ko'rasiz:

Ko'rinmagan

\> *vim dan chiqish*

Bu unchalik ham oson emas! Harakat qilishga to'g'ri keladi.

\> *Harakat qilish*

Siz buyruq interpretatoriga chiqdingiz.

***LOADING...***

## Chapter VII
## Quests: Level 1. Room 2

## Quest 8. Vim

\> *Tugmalarni terish... hatto bilmayman... Terminalda shunchaki qandaydir «qwe»*

Terminalda jonlanish boshlandi, ko'plab matn bloklari mavjud. Nihoyat, ular tugadi va o'qiladigan matn boshlandi:

> Salom, yo'lovchi! Men tizimimizdagi SI bosh boshqaruv modulining kutubxona moduliman. Qanday yordam bera olaman? Ha, aytgancha, kimga kerakman.

\> *Terish: «Menga keraksan. Men bu yerdan chiqish yo'lini izlayapman»*

>Eshik? Mana-ku u. Ochish kerakmi? 
>
>Stop. Bunaqasi ketmaydi. Men tahlil qilgan barcha ko'rsatmalar va matnlarda hech qachon va hech narsa shunchaki qilinmaydi. Men eshikni ochaman, bu muammo emas, lekin avval hujjatlarni tartibga solishga yordam ber.
>
>Vim haqidagi faylni o'qiganmisan? `src/history_of_vim.txt` da bor bo'lganini. Men bu dasturni juda yaxshi ko'raman. Ammo, afsuski, versiyalarni tavsiflovchi fayl buzilib qolgan. O'ylaymanki... 
>
>Hozir 2001-yil emas-ku? Uni, albatta, «Vim»da to'ldir. (Bu muhim! Men uchun...) Tugatganingdan so'ng, jurnalga (fayl `src/files.log`) quyidagi formatda kirit: faylga yo'l (ildiz direktoriyasiga nisbatan) — fayl hajmi — sana va vaqt — sha-fayl yig'indisi (sha256 ni afzal ko'raman) — sha hisoblash algoritmi.  

\> *Terish: «Tayyor»*

Butunlay unutibman. Fayl boshiga sarlavha qo'sh: «A Quick Summary Of the History of the Vim Editor». Bu o'zgarishni ham jurnalga kirit.

> Diqqat: develop tarmog'iga o'tishni unutma, barcha ishlar faqat o'sha yerda qilinishi kerak!

#### Quest 8 qabul qilindi. `src/files.log` jurnalida `src/history_of_vim.txt` faylining asl holatini qayd qilish. Ushbu faylni Vim yordamida 2001-yildan keyingi Vim versiyalari to'g'risidagi ma'lumot bilan to'ldirish. Fayl boshiga "A Quick Summary Of the History of the Vim Editor" sarlavhasini qo'shish. Ushbu o'zgartirishlarning har biridan so'ng `src/files.log` jurnaliga quyidagi formatdagi yozuvnui kiritish: faylga yo'l — fayl hajmi baytlarda — sana va vaqt — sha-fayl yig'indisi — sha hisoblash algoritmi. 

***LOADING...***

## Bonus Quests: Level 1. Room 2
## Bonus Quest 9. Script

\> *Terish: «Tayyor»*

>Ajoyib!

\> *Terish: «Endi chiqish mumkinmi?»*

Kutubxona moduli hali ham tinchlanmayapti: 
>Ishonchim komil emas. Menga yoqa boshlayapti. 
>
>Faylda faktologik xatolar ko'p bo'lsa kerak! Ularni oson yo'qotish uchun menga instrument tayyorlab qo'y. Uni ortiqcha muammosiz ishga tushira olishim uchun bu sh-skript (`src/edit.sh`) bo'lishi kerak. Kirish uchun u faylgacha bo'lgan yo'lni, almashtirish uchun satrni va almashtirishning o'zini (satr ko'rinishida) qabul qilishi kerak. Faylda bevosita almashtirish amalga oshirilishi va jurnal fayliga tegishli yozuv kiritilishi kerak. 

\> *Zo'r. Bu skriptlar qanday yozilishini bilsam edi...*

#### Quest 9 qabul qilindi. Matnli fayllarda kichik qatorlarni almashtirish uchun `src/edit.sh` skriptini ishlab chiqish. Kirish uchun u faylgacha bo'lgan yo'lni (repozitoriyning ildiz direktoriyasiga nisbatan), almashtirish uchun satrni va almashtirishning o'zini (satr ko'rinishida) qabul qilishi kerak. Faylning har bir o'zgarishi haqidagi ma'lumot `snc/files.log` jurnaliga oldingi kvestda ko'rsatilgan formatda kiritilishi kerak. Chegaraviy vaziyatlarni qayta ishlashga e'tibor qaratish.

***LOADING...***

## Bonus Quest 10. Gitlab

\> *Terish: «Bu endi adolatdan emas!»*

>Shuni aytib qo'yayki, adolat haqida gap bo'lgani yo'q. So'nggi iltimos. Ko'rib turibman, sen Gitni yomon yurgizmayapsan. Kutubxonamda ba'zi qo'llanmalar yetishmayapti, xususan, GitLab bilan ishlash bo'yicha. Men ma'lumot yetishmasligini yoqtirmayman. Har bir bandi sarlavha va tegishli skrinshotdan iborat bo'lgan `src/gitlab_manual.md` faylida Markdown belgisida qisqa va lo'nda qo'llanma yarat. Yoritilishi kerak bo'lgan mavzular: 
>1) Kerakli `.gitignore` va oddiy `README.MD` ga ega bo'lgan shaxsiy repozitoriy yaratish. 
>2) `develop` dan `master`, `develop` va `feature` tarmoqlarini yaratish.
>3) `develop` da merge request yaratish.
>4) Joriy qo'llanmani yaratish uchun issue yaratish va issue ga izoh berish.  
>
>Hech narsa yo'qolmaganga o'xshaydi. Agar yaxshi chiqsa, bosh kutubxona tizimidagi qo'llanmalarning oltin fondiga yuklayman, o'zing bilan faxrlansang bo'ladi.

#### Quest 10 qabul qilindi. Yuqorida keltirilgan mavzular bo'yicha GitLabdan foydalanish bo'yicha har bir bandi sarlavha va tegishli skrinshotdan iborat bo'lishi kerak bo'lgan qisqacha qo'llanmani `snc/gitlab_manual.md` faylida Markdown belgisida tayyorlash.

***LOADING...***

## Chapter VIII

\> *Terish: «Tayyor»*

>Ajoyib qo'llanma. Xo'sh, taxminimcha, juda zo'r - rasmlarni tahlil qila olmayman, o'rama neyron tarmog'iga ega bo'lgan modulni menga baribir ulab berishmadi. Darvoqe, eshik ochiq. U har doim ochiq edi. Men oddiy, hech kimga kerak bo'lmagan kutubxona moduliman-ku! Eshiklarning kalitini kim ham menga ishonib topshirardi?

\> *Tfu*

>Buyruq aniqlanmadi.

Qiziq, bu SIning barcha modullari shunchalik zararli qilinganmi? Yoki hozircha faqat sening omading kelyaptimi?

Nihoyat, siz birinchi darajadagi ikkinchi xonadan ham chiqasiz, yo'l-yo'lakay ular jami qancha bo'lishini o'ylab borasiz. 

***LOADING...***

💡**[Bu yerga bosing](http://opros.so/p31wz), bu loyiha haqida fikr-mulohazalaringizni bildirish uchun. 
Bu anonim bo'lib, jamoamizga ta'limni yaxshilashga yordam beradi. 
So'rovnomani loyiha bajarilgandan so'ng darhol to'ldirishni tavsiya qilamiz.**
