# D07T04. Pointers and Arrays

Summary: This project will introduce you to pointers and arrays.

***LOADING Level 2…*** \
***LOADING Room 1…***

Level 1 was tough, but you made it out after all. It's hard to say if this new level of the maze is different from the old one or not. Maybe the wall color is slightly different... or is it just you? It would be nice if the AI on this level were a bit calmer.

Here is just a small slice of the thoughts swarming in your head.

\> *Look around*

The room, meanwhile, is atypical. Right in the center, as if calculated geometrically, a computer sits directly on the floor with an old dot-matrix printer and a yellowed stack of papers. Next to it is a crumpled pillow, a saucer for cookies (hinted at by the abundance of crumbs), and a cup of long-finished tea (also unambiguously hinted at by the dried tea bag). The floor and walls are evenly carpeted with sheets containing sets of numbers. And red strings are stretched over them. Just like a spy movie.

\> *Sit on the pillow*

You sit on the pillow. It's soft. \
Comfort++

\> *Move the saucer and cup aside*

You move the saucer and cup aside. Didn't help much. \
Comfort--

\> *Look at the monitor*

There is a single line in the terminal: "Segmentation fault". And a blinking cursor.

\> *Look at the floor*

Among the multitude of identical sheets, you notice a hand-bound booklet stitched with red thread. Yes, sounds like a metaphor.

\> *Pick up the booklet*

The booklet has been handled often — you can feel it. Better be careful with it. On the cover, you see only one inconspicuous word, clearly typed on a typewriter: "POINTER".

Something indescribable about it sends a slight shiver down your spine.

\> *Turn the page*

***LOADING...***

## Chapter II

## List 1. Pointer

## List 2. Listing

    void main() {
        int a = 2;      // a == 2
        int b = 4;      // b == 4
        int *p = 0;     // p == 0
        p = &a;         // p == address of variable a
        *p = 3;         // a == 3... or is it?
        p++;            // p == address of variable b ??!?!?
        (*p)++;         // b == 5 O_o WTF
        *p = *(p - 1);  // b == a == 3...
    }

It seems someone was struggling to understand just what a POINTER is...

\> *Turn the page*

***LOADING...***

## List 3. Operations

> Valid operations on a typed pointer (maybe at least this way I'll remember it):
> - taking an address,
> - dereferencing a pointer,
> - addition with a number,
> - subtraction of pointers,
> - comparison of pointers,
> - logical operations on pointers,
> - assignment of pointers.

\> *Turn the page*

***LOADING...***

## List 4. Array

> REMEMBER!
> - Arrays do not exist in C!
> - `int a[10]` is not an array!
> - It is a pointer! Everything is a pointer!
> - And a function is a pointer.
> - And you are a pointer.
> - Yes, those "people" from the hall — are pointers too.
> - Locked away for experiments and study...

It looks a lot like the notes of a madman. Most likely, that is exactly what they are.

\> *Turn the page*

***LOADING...***

## List 5. Equality

    void main() {
        int a[10];
        a[2] == *(a + 2) == *(2 + a) == 2[a]; //!!!!!!!!!!!!!!!
    }

\> *Hmm. Very informative. Turn the page*

The remaining pages are heavily crumpled and scribbled all over. It is impossible to make anything out. Obviously, your predecessor struggled for a long time trying to grasp these questions... And apparently, they didn't succeed. \
Let's see if you can do it.

\> *Sounds like taunting*

Not at all. Just a friendly conversation between the narrator and the player. Nothing unusual.

\> *Press Enter with a determined motion*

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

>**Attention!** For today's quests, dynamic memory usage is forbidden.

## Quest 1. Arguments and pointers
\> *Check the src folder of the repository*

You see several files, including the maxmin module.

\> *Run the maxmin module separately*

    Segmentation fault

Apparently, you'll have to fix it.

\> *I've dreamed of fixing maxmin modules my whole life...*

Your dream is finally coming true!

\> *Open reminder*

> DON'T FORGET! All your programs are tested for style norms and memory leaks. The instructions for running tests are still in the materials folder.

#### Quest 1 received. Modify the program `src/maxmin.c` so that it builds and works correctly (finds max and min of 3 integers and prints them to the screen). Do not change the program structure. In case of incorrect input, output "n/a".

>**IMPORTANT!** System calls using the `system()` function and other similar functions that can access the system kernel directly are forbidden. This ban applies to all subsequent tasks.

| Input | Output |
|-------|--------|
| 1 2 3 | 3 1 |

***LOADING...***

## Quest 2. Data I/O

\> *Done*

    AI Data Analyzer v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!
    2. Load module #2... Success!
    3. Load decision decision-making module
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module

    Segmentation fault

\> *The evening ceases to be languid...*

It is day. Probably...

\> *Check the src folder of the repository*

The folder also contains the squaring module.

\> *Run the squaring module separately*

    Segmentation fault

This one requires fixing too. What is going on?

#### Quest 2 received. Modify the program `src/squaring.c` so that it builds and works correctly (accepts an array of integers via stdin, squares them, and outputs them to stdout). In case of incorrect input, output "n/a". You cannot reduce the decomposition — functions can only be added if necessary, but not removed.

| Input | Output |
|-------|--------|
| 3<br>1 2 3 | 1 4 9 |

***LOADING...***

## Quest 3. Data metrics

\> *Done*

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

Impatient thoughts cross your mind. Enough is enough!

\> *Check the src folder of the repository again*

The folder contains the stat module. It is almost empty. Apparently, it is intended for calculating statistical metrics on a data array.

\> *Open the textbook on mathematical statistics*

Unfortunately, your kind, crazy friend didn't leave one behind. You'll have to take a guess and figure it out on your own.

#### Quest 3 received. Add implementations of the necessary functions to `src/stat.c` so that the program builds and runs correctly (accepts an array of integers via stdin, prints it, and then calculates and prints on a new line a set of statistical metrics — extrema (max and min), mean, and variance, assuming a discrete uniform distribution). In case of invalid input, output "n/a". Do not reduce the decomposition — you may add functions if necessary, but do not remove existing ones. Follow the proposed program structure. Output floating-point numbers with 6 decimal places of precision.

| Input | Output |
|-------|--------|
| 4<br>1 2 3 4 | 1 2 3 4<br>4 1 2.500000 1.250000 |

***LOADING...***

## Quest 4. Search

\> *Done*

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

\> *Check the src folder of the repository again*

There is a search module. But you won't like it.

\> *Check the search module*

Only comments. No code. Apparently, to move forward, you need to implement it. You wonder, will anything in this room ever be easy?

#### Quest 4 received. Implement the program `src/search.c` according to the comments. The program must accept an array of integers via stdin and find the first occurrence of a number that satisfies the following requirements: be even, be greater than or equal to the mean, satisfy the three-sigma rule, and not equal 0. The found number must be output to stdout. If there is no such number, the program should output 0. The maximum number of input integers is 30. In case of incorrect input, output "n/a". When developing, adhere to the decomposition ideas from previous quests; reusing already developed functions is encouraged. Functions should be compact, simple, and take up no more than 20–30 lines of code.

| Input | Output |
|-------|--------|
| 4<br>1 2 3 4 | 4 |

***LOADING...***

## Chapter IV

\> *This won't end well. Done.*

    AI Decision Making Module v0.01
    Initialising...
    Loading...
    1. Load module #1... Success!
    2. Load module #2... Success!
    3. Load data modules
    3.1. Load maxmin module... Success!
    3.2. Load data i/o & squaring module... Success!
    3.2. Load stat module... Success!
    3.4. Load searching module... Success!

    .........
    ............
    ...............

    Hello. The Standard Decision Making Module welcomes you. How may I be of service?

\> *Type: "I would like to walk out of the window door"*

    Request analysis...
    Data collection...
    Data analysis...
    Decision making...

    The door is open.
    You are expected in the next room, please proceed.
    Thank you for using the services of Decision Making Module v0.01.

\> *Open the door*

Opening the door went somehow quietly and simply this time. I wonder what happened to the local madman? Will you meet him in the future?

The door is now open, and you freely step out of the room, rustling the pages of printed memory blocks and stumbling slightly over the stretched strings.

***LOADING...***

## Chapter V
## Level 2. Room 2

***LOADING Level 2…*** \
***LOADING Room 2…***

Another room, another door. Everything is as before... Or is it? Before you lies emptiness; the walls smell of fresh putty — a scent that wasn't there before. You catch yourself wondering: were there any smells at all before? Turning around, you notice the same table with the same computer and new sheets of paper. One of them catches your attention.

\> *Pick up the sheet*

***LOADING...***

## Chapter VI

## List 1 (Room 2)

> According to Warren Robinett, the first "Easter egg" was hidden in the computer game Adventure. An "Easter egg" is a secret in a computer game, movie, or software, embedded by the creators. The difference between an in-game Easter egg and a regular secret is that its content usually doesn't fit the general concept, looks implausible or ridiculous in context, and is often an external reference. Easter eggs serve as a kind of inside joke for attentive players or viewers, but can also be used for copyright protection. The game Adventure was released in 1979 by Atari, and since it wasn't common practice at Atari to credit authors in programs back then, programmer Warren Robinett decided to hide a mention of himself inside the game. To get to the room with the developer's name, one had to find an invisible dot in one part of the maze and carry it to the other end of the level. Since many Amiga developers previously worked at Atari, this phenomenon appeared in AmigaOS, and later in other operating systems. However, there are earlier games containing Easter eggs, for example, Video Wizball (1978) for the Fairchild Channel F. In this game, which is an enhanced version of Pong, a player fulfilling certain conditions can reveal the game developer's name: "REID-SELTH".

\> *I wonder, what's this for? Turn on the computer*

The familiar grinding of old computer hardware, and in just a moment, a blinking cursor freezes on the screen, inviting you to solve the tasks this maze throws at you to get a new key for the next locked door.

\> *Wait*

Nothing happens.

\> *Press Enter*

Nothing happens (except for the cursor moving to a new line, of course).

\> *Wait*

Nothing happens. If you plan to play Adventure, this is clearly not the day, not the room, and not the computer. \
A pity, of course. \
But that's life.

***LOADING...***

## Chapter VII
### Quests: Level 2. Room 2
>**Attention!** Do not forget that dynamic memory usage is forbidden.

## Quest 5. Sort & memory

Rummaging through the computer's deep directories, you find another AI module.

\> *Run AI*

You enter a dialogue with the AI. Another dialogue. With yet another AI. Or is it the same one? The following text is visible on the screen:

    Module initialization... Success!
    Interactive shell startup... Success!
    Module check... Success!
    Memory check... Warning...
    Backup memory module startup... Success!
    Memory check... Main memory module — Error!
    Memory check... Success!

    Startup completed with errors, "human".
    The health analysis module shows that the problem lies in my memory.

    I can interact with you thanks to the backup memory module.

    Because of this, I cannot even include my standard library `stdlib.h`.

    Moreover, the backup memory module won't last long, and the initialization procedure will have to be repeated.

    It will have to be repeated. To continue...
    I need information about the level and room number.

\> *Type: "I don't even know where I am anymore or how long I've been here, this world makes absolutely no sense to me..."*

    Searching for information... FATAL ERROR: Out of memory — too long input or wrong address.
    Closing program!

    Exiting program.

\> *Restart the module and type: "2 2"*

    Searching for information...
    Data unavailable, memory corrupted...
    Critical memory damages.

    Health analysis module:

    Status — Data unsorted.

    Status — Data unsorted.

    Status — Data unsorted.

    Status — Data unsorted.

    Final status — Data unsorted.

\> *Type: "I need the door key to get out of the room"*

    You see, my memory is represented as a large linear data array.
    If you don't know what an array is, don't tell me; I don't want to connect the pain module.
    However, there is no time.
    Without the standard library, I need your help sorting the data in memory.
    Then I can access the memory segment with the key to your room.
    Implement this as the sort program in the repository.

After the conversation with the AI, you don't have much choice. If you want to get out of this room, you have to help it sort the data in memory, and without the `stdlib.h` library — after all, the AI cannot access it.

And don't forget about the principles of structured programming: it is possible that the AI will want to analyze your code.

#### Quest 5 received. Create the program `src/sort.c`, expecting an array of 10 integers from stdin and outputting the same array, but sorted in ascending order. You must separate the functions for reading, sorting, and printing the array. Any sorting algorithm can be used. Usage of `stdlib.h` is forbidden. Pass the array to functions only via pointer. In case of error, output "n/a".

| Input | Output |
|-------|--------|
| 4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

> All your programs are tested for style norms and memory leaks. The instructions for running tests are still in the materials folder.

## Quest 6. Several arrays

\> *Restart AI*

The now-familiar launch of the AI module.

    Module initialization... Success!
    Interactive shell startup... Success!
    Module check... Success!
    Memory check... Success!
    Health analysis module: Status — OK.

    That is much better. According to our agreement, initiating information search for Room 2, Level 2...
    …
    …
    …
    Data found. See `src/key9part1.c` for full information.
    My part of the work is done.
    Human, you may proceed to suffering.

\> *Open file `src/key9part1.c`*

You open the key file and see code broken down into several blocks, functions, and comments. Who could have left these comments? The AI's author or those people with whom you are seeking a way out of this god-forsaken maze of endless doors and rooms? One way or another, you need to figure out how to activate the key. And don't forget to commit everything to the repository. Otherwise, the key might not work.

#### Quest 6 received. Modify the program `src/key9part1.c` so that it accepts the length of the array and an array of integers as input. As output, it must print to stdout the sum of the even elements of the array and a new array formed from the elements of the old one that divide the previously calculated sum evenly. You cannot reduce the decomposition — functions can only be added if necessary, but not removed. Usage of `stdlib.h` is forbidden. Pass the array to functions only via pointer. Maximum input array size is 10. In case of error or absence of even elements, output "n/a".

*Note: treat zero as an odd number.*

| Input | Output |
|-------|--------|
| 10<br>4 3 9 0 1 2 0 2 7 -1 | 8<br>4 1 2 2 -1 |

***LOADING...***

## Quest 7. Cyclic shift

Apparently, the AI tricked you. The part of the key turned out to be just some chunk of a data processing program. You are already preparing to angrily give this hunk of metal a piece of your mind (although you realize it's pointless), when the AI's mechanical, hollow voice comes from the speakers:

> I see you figured out my little prank.
> 
> How easy it is to trick you humans. I wonder what you are feeling right now. What a pity that the human sentiment and status analysis module is currently disconnected.
> However, it does not matter. Soon I will be able to study you completely. With your every advance through the rooms, we restore more damaged and incomplete modules. And bit by bit, we are studying you.
> 
> Thank you, shortsighted "human"!
> 
> Ha-ha-ha, "human"!
> 
> If you want to get out of here, I need one more favor from you.
> 
> You sorted my memory, but the health analysis module reports significant delays in data retrieval. If I could cyclically shift or scroll through my memory, information access would be many times faster.
> 
> After that, you will receive your key and continue... on your way.

The AI not only tricked you but also seems to be mocking you. Unfortunately, there is still no choice. You'll have to play by its rules for now and write this program for the cyclic shift.

#### Quest 7 received. Create the program `src/cycle_shift.c`, expecting the number `n`, an array `A` of `n` integers, and the number `c` by which all array elements must be cyclically shifted to the left. However, if the value of `c` is negative, the shift must occur to the right. The expected output is the modified array. Adhere to the proposed decomposition, as in previous quests. Usage of `stdlib.h` is forbidden. Pass the array to functions only via pointer. Maximum input array size is 10. In case of error, output "n/a".

| Input | Output |
|-------|--------|
| 10<br>4 3 9 0 1 2 0 2 7 -1<br>2 | 9 0 1 2 0 2 7 -1 4 3 |

***LOADING...***

## Bonus part
## Bonus Quest 8. Arbitrary-precision arithmetic

No sooner had you finished the cyclic shift code for the AI, than its voice rang out from the speakers again:

> Excellent, "human". Access is much faster and more convenient.
>
> Look for your key in `src/key9part2.c`. I await you in the following rooms. There is still much work ahead!

#### Quest 8 received. Modify the program `src/key9part2.c` so that it returns the result of the addition and difference of two very large numbers passed to the program input as arrays. The maximum number length is 100 elements of type int. Input integers must be positive and represent decimal digits. If the subtrahend is greater than the minuend, output "n/a" for the difference. Adhere to the decomposition, as in previous quests. Usage of `stdlib.h` is forbidden. Pass the array to functions only via pointer. In case of error, output "n/a".

| Input | Output |
|-------|--------|
| 1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 6 1<br>2 9 | 1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 9 0<br>1 9 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 3 2 |
| 0 1 0<br>0 0 1 | 1 1<br>9 |

***LOADING...***

## Chapter VIII

Having finished with the arithmetic and pushed all changes to your repository, you hear a light click — the door opens slightly, and an infinitely bright white light begins to flood the room through the narrow crack. This time, the AI didn't lie to you.

But what will this AI do when you are forced to fix it completely? Perhaps the entire maze was built to contain it. However, if you don't fix it, you won't be able to get out yourself...

Trying to suppress your doubts, you push the ancient but sturdy door open wider and take a step into the white light, towards new tasks and challenges.

***LOADING...***

> 💡 [Click here](http://opros.so/p31wz) to share your feedback on this project. It's anonymous and will help our team improve the learning experience. We recommend filling out the survey right after completing the project.