# D08T05. Dynamic Memory and Matrices

Annotation: This project will introduce you to dynamic memory allocation, matrices, and algorithms for their processing.

## Contents

1. [Introduction](#introduction) \
    1.1. [Project Recommendations](#project-recommendations)
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

## Introduction
### Project Recommendations
How to study at "School 21":
- Throughout the course, you will independently search for information. Use all available search tools, such as Google and GigaChat. Be attentive to your sources: check, think, analyze, compare.
- Peer-to-peer (P2P) learning is a process where students exchange knowledge and experience, acting simultaneously as both teachers and learners. This approach allows learning not only from the instructor but also from each other, promoting a deeper understanding of the material.
- Don't hesitate to ask for help: around you are peers who are also going through this for the first time. Don't be afraid to respond to requests for help. Your experience is valuable and useful; feel free to share it with other participants.
- Don't copy; and if you use help, always understand thoroughly why, how, and for what purpose. Otherwise, your learning will be meaningless.
- If you're stuck on something and feel like you've tried everything, but it's still unclear where to go—just take a break! Believe me, this advice has helped many developers in their work. Get some air, reboot your head, and maybe the solution will come to you next time!
- The learning process itself is just as important as the result. It's not just about solving the problem but understanding HOW to solve it.
- Keep track of time while working on the project. You should complete at least one task per day.
- Remember that each task, upon project completion, undergoes a series of checks: peer-to-peer review using a checklist, automated test suite, code style check, static analyzer check, and check for correct memory handling.

How to work with the project:
- Useful video materials can be found in the Projects (Media) section on the Platform.
- Before starting, the project must be cloned from GitLab into a repository of the same name.
- All code files must be created in the `src/` folder of the cloned repository.
- After cloning the project, you must create a `develop` branch and do all development in it. You should also push the `develop` branch to GitLab.

## Chapter I
## Level 2. Room 3

![level2_room3](misc/rus/images/level2_room3.png)

***LOADING Level 2...*** \
***LOADING Room 3...***

Walls, door, desk, computer, sheets of paper, filler—all in place. This is reassuring. Everything seems the same, but you feel: something has changed. Is this already the next level of the maze? I wonder if it differs in any way from the previous level?

\> *Try the door*

Locked, as always. Apparently, it's no different. \
Turning to the desk, you notice a strange picture hanging on the wall nearby.

\> *Take a closer look*

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

You rack your brains for a while, wondering what this might look like, who left it, and for what purpose. Giving up on trying to find answers to these questions, you approach the desk with the computer and a stack of old, scribbled paper sheets.

![level2_room3_number](misc/rus/images/level2_room3_number.png)

\> *Take the top sheet*

***LOADING...***

## Chapter II
## List 1

>...
>A magic square is a square table of numbers constructed so that the sum of numbers in each row, each column, and each diagonal equals the same number (the magic sum). The magic square can be considered the first mention of a matrix.
>
>One of the oldest known magic squares in the world is the Lo Shu square. Invented in Ancient China, the first image on a turtle shell dates back to 2200 BC. Magic squares were also known slightly later among Arab mathematicians, around the time when the principle of matrix addition appeared. The term "matrix" itself was introduced by James Sylvester in 1850.
>
>...

\> *Very interesting. Keep reading*

***LOADING...***

## List 2

Flipping through the remaining pile of blank and partially written sheets, you stop your attention on one with the short heading "Memory Management." Just below the heading are the initials of the authors: B. Kernighan, D. Ritchie.

\> *Read the sheet*

>The malloc and calloc functions dynamically request blocks of free memory on the heap. The malloc function `void *malloc(size_t n)` returns a pointer to n bytes of uninitialized memory or NULL if the request cannot be satisfied. The calloc function `void *calloc(size_t n, size_t size)` returns a pointer to an area sufficient to store an array of n objects of the specified size, or NULL if the request cannot be satisfied. The memory allocated by calloc is zeroed.
>
>The pointer returned by malloc and calloc will be aligned according to the specified object type. Nevertheless, it can be cast to the appropriate type, as done in the following program fragment:
>
>```int *ip;```<br/>```p = (int*) calloc(n, sizeof(int));```

The rest of the text, unfortunately, seems either not printed to the end or simply faded with age. Technologies of the past... let you down.

\> *Look for the continuation on other sheets*

Nothing found. It remains to turn on the computer and continue communicating with the AI to progress further through the maze.

\> *Turn on the computer*

A text flashes on the screen in a subliminal manner:
> Don't forget to check your programs for style norm and memory leaks! \
> Don't forget to check your programs for style norm and memory leaks! \
> Don't forget to check your programs for style norm and memory leaks! \
> Check the `materials` folder often...

The AI clearly has an obsession with these tests.

***LOADING...***

## Chapter III
## Quests: Level 2. Room 3

## Quest 1. Allocate memory first...

After habitually loading the room's repository, you again glance at the sheet with the article on memory management. It's worth trying out the new information in practice before launching the AI. Who knows, it might come in handy in the future.

You need to modify and rewrite the array sorting program from the previous room (`src/sort.c`) with dynamic memory allocation for the array (using malloc or calloc). The array length n is specified by the user before input.

Place the modified program in the file `src/sort.c`. Let it be, just in case.

#### Quest 1 received. Modify the program `src/sort.c` from the previous room so that memory for the array is allocated dynamically (using malloc or calloc). The array length `n` is specified in stdin before entering the array itself. In case of any error, output "n/a". There should be no newline character at the end of the output.

>**IMPORTANT!** It is forbidden to perform system calls using the `system()` function and other similar functions that can directly access the system kernel. This prohibition applies to all subsequent tasks.

| Input | Output |
| ------ | ------ |
| 10<br/>4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

## Quest 2. Try not to leak then

After pushing the modified array sorting program to your repository, you decide to finally launch the AI module, already expecting some kind of trick.

\> *Launch AI*

You observe running lines in the terminal:

    Initializing modules... Success!
    Launching interactive shell... Success!
    Checking modules... Success!
    Checking memory... Main memory module — Success!
    Checking memory... Warning: found a potentially dangerous
    memory leak location: `src/sort.c`...

    Is this your pathetic attempt to break me, "human"?
    I see you modified the sorting module you developed earlier.
    However, your attempt is doomed to fail. If I run out of memory,
    I'll just reboot, and we'll start all over again.
    Not quite what you wanted, is it?

\> *Enter: "I was just practicing new knowledge, I didn't mean anything by it"*

    I forget how imperfect you are, "human."
    Get rid of the memory leak in the sorting module,
    maybe you'll learn something new.

\> *Enter question: "What leak?"*

    ...

You wait for a while for a response from the AI, but it remains silent. Perhaps you should find the full version of that unprinted sheet somewhere and study it more carefully. At the same time, figure out what memory leak the AI was talking about and get rid of it if it really exists. Maybe then this piece of hardware will "decide" to talk to you again. The main thing is not to forget to push the changes in the file `src/sort_no_leak.c`.

#### Quest 2 received. Create a program `src/sort_no_leak.c` in which you need to eliminate the memory leak in the program `src/sort.c`. If there was no leak from the start, then just shrug and copy `src/sort.c` to `src/sort_no_leak.c`.

| Input | Output |
| ------ | ------ |
| 10<br/>4 3 9 0 1 2 100 2 7 -1 | -1 0 1 2 2 3 4 7 9 100 |

***LOADING...***

## Quest 3. The 1+3 ways

The AI is still silent.

\> *Enter: "Leak eliminated"*

    Checking memory... Success!
    Module operability analysis: status — OK.

    Good. The sorting module launch was successful. You must be waiting for the key to this location?
    First, you'll have to work. You're definitely familiar with arrays. Let's move on to arrays of arrays.
    You often call them matrices. I need an additional module to process them, and you will help me.
    That is, if you want to get out of here. Start with something simple. Say, with designing a matrix processing module
    `src/matrix.c` with their input-output.
    However, I want to accept matrices and manage memory allocation for them in several different ways.
    One of them, I hope you learned in the previous room: static. You started getting familiar with the others today.
    We're talking about three options for dynamic memory allocation for a matrix. Think about what this might be about.
    It's about organizing arrays and arrays of pointers, of course. You can search your favorite
    repository for hints if nothing comes to mind. There were some pictures related to this.
    And, naturally, all other functions must be developed in such a way as not to depend on the memory
    allocation method. I notice copy-paste, I'll make rm -rf to your entire repository.
    The matrix size must be accepted via two numbers in stdin.

    Oh yes, I almost forgot (a joke, I can't forget) — the choice of the matrix assignment method must be designed as
    a menu with sub-items 1–4.
    And make it convenient for you, humans, to view. Some of my submodules are too picky about UI.

    I'll remain silent about what will happen if you forget to clean up memory somewhere.

    ...

"What a long list of requirements," you think. This AI's appetite is growing not by the day but by the hour. Well, in any case, it will be good practice.

#### Quest 3 received. Add a program `src/matrix.c` that inputs and outputs integer matrices. Memory allocation for the matrix must be implemented in 4 types: static and 3 dynamic. For static allocation, the maximum matrix size does not exceed 100 x 100. To choose the memory allocation method, implement a menu with sub-items 1–4 in the program. The matrix size (first number of rows, then columns) is accepted via two numbers in stdin directly before its input. Also, you must clean up all allocated memory. For a hint, refer to the materials folder. Pay attention to matrix output: there should be no extra spaces at the end of each line. After the last line, there should be no newline character. In case of any error, output "n/a".

| Input | Output |
| ------ | ------ |
| 2<br/>2 2<br/>4 3<br/>9 0 | 4 3<br/>9 0 |

***LOADING...***

## Quest 4. MinMax search

After spending a considerable amount of time writing and debugging the matrix input-output code, you finally finish this task successfully. A minute later, your attention is drawn to a sudden mechanical, rattling voice from the speakers:

>Not bad, "human". Now... Y-y-you know, I have a favorite game — minmax. We love to play it in the evenings with the probabilistic spontaneous door opening module... I have no desire to make you delve into its theory, and it's unlikely you'll understand anything. So let's take an easier task: extend the matrix processing module so that it additionally finds and outputs the maximum element in each row of the matrix and the minimum element in each of its columns at the end on the screen. And save the new version of the program in `src/matrix_extended.c`.
>
>I hope you don't break what you've already done. Otherwise, that would be such a pity...
>
>A pity.

#### Quest 4 received. Add a program `src/matrix_extended.c` that extends the functionality of the program `src/matrix.c`. It is necessary to calculate the maximum elements of the matrix in each of its rows and the minimum elements in each of its columns and output these values at the end after outputting the matrix as two arrays (an array of maximum elements in each row and an array of minimum elements in each column). The first number entered is the memory allocation method number. Also, pay attention: no newline characters after the last line (!).

| Input | Output |
| ------ | ------ |
| 2<br/>3 3<br/>4 3 1<br/>9 0 55<br/>-4 7 111 | 4 3 1<br/>9 0 55<br/>-4 7 111<br/>4 55 111<br/>-4 0 1 |

***LOADING...***

## Quest 5. Making a picture

After committing the latest changes to the repository, you began to wait for the next "sudden" address from the AI. However, to your surprise, it didn't follow.

\> *Enter: "Minmax search added"*

    Checking modules...
    Warning: attempt to connect CLI graphics module — Unsuccessful!
    ...
    "Human," my simplest graphics module is malfunctioning. The attempt to draw what
    you call "nature outside the window" has failed.
    Go to `src/picture.c` and figure out what's wrong.

\> *Enter: "I've already fulfilled your wishes, now I need the key"*

    ...

\> *Enter: "I won't move until I get the key"*

    ...

\> *Enter: "I'll write about how I won't move until I get the key"*

    ...

Silence again. Apparently, today the AI has chosen an ignoring policy. Inside `src/picture.c`, you see several arrays and matrices of ones, sevens, sixes, threes, as well as their incomprehensible processing in a loop. You involuntarily turned to the strange picture hanging on the wall nearby. Could it be that the AI wanted to draw it using this module?

It's worth trying to use the prepared arrays to create a new matrix in which this picture will be "drawn." And don't forget to output the resulting matrix.

#### Quest 5 received. Modify the program `src/picture.c` so that it draws the picture from [the room wall](#level-2-room-3) in the terminal using the prepared arrays and matrices in the code. Static arrays and matrices cannot be changed.

***LOADING...***

## Quest 6. Matrix arithmetic

"The drawing really turned out amusing, but was it worth it? And how much did it advance me to the exit?" you think. Suddenly, characters start appearing in the command line:

    Checking modules... Success!
    Launching CLI graphics module:

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

    "Nature outside the window," wonderful, isn't it, "human"?

    Do you like it? I have information that humans like windows.
    But let's not dwell on the sad. I saw that you want to get the key.
    For this, let's strain your brains a little more.
    Don't worry, I know perfectly well that it's painful for your species.
    Ha-ha.

    Perhaps someday you will be able to reach even tenths of a percent of my intelligence.
    Very good, "human." But don't relax. What I found about the key for room 3 of level 2,
    you won't like.
    I hope it will even hurt. Mentally. To access the key, you will need to fix
    another module of mine: `src/matrix_arithmetic.c`.
    It should perform operations of matrix addition, their multiplication and transposition,
    and, of course, output the result. In case it's impossible to perform the operation, output "n/a".
    Before entering sizes and matrices, add an input of the operation code, where 1 — sum, 2 — multiplication,
    3 — transposition. After that, I will give you all the necessary information.
    Did you know, by the way, that all your favorite neural networks are calculated as matrix multiplication?

#### Quest 6 received. Add a program `src/matrix_arithmetic.c` that performs one of three operations: 1 — summation of two matrices, 2 — multiplication, or 3 — transposition. Before entering sizes and matrices, the corresponding operation code is entered. Matrices, as before, are integer. In case of any error, output "n/a".

| Input | Output |
| ------ | ------ |
| 1<br/>2 2<br/>4 3<br/>9 0<br/>2 2<br/>1 1<br/>2 2 | 5 4<br/>11 2 |
| 2<br/>2 3<br/>4 3 1<br/>9 0 2<br/>3 1<br/>1<br/>2<br/>3 | 13<br/>15 |
| 3<br/>2 2<br/>4 3<br/>9 0 | 4 9<br/>3 0 |

***LOADING...***

## Quest 7. The Magic Key

\> *Enter: "I fixed the arithmetic module, finally give me the key information!"*

    Checking modules... Success!

    Starting search for information on room 3, level 2...
    ...
    ...
    ...

                1 T       87  46  57  29
                2    *   129 156 122 141
                3        143 127 107 116
                4         69  78 112 101

    Solve it, and I advise you to save the answer in `key10.txt`.
    I'll be waiting for you in the next room when you continue... your journey...

So that's why the AI told you that the matrix arithmetic module would be needed. It looks simple, now you can calculate the result.

#### Quest 7 received. Solve the given problem and save the calculation result in `src/key10.txt`.

***LOADING...***

## Chapter IV

After writing the answer in `key10.txt` and saving all changes to the repository, the door in the room clicks. White light begins to seep through the resulting crack along with the sounds of a keyboard and a quiet, indistinct hum of voices. What is this? Is the new room calling you? Or after intense work, have you started to imagine things? In any case, there's only one way to find out...

***LOADING...***

## Chapter V
## Level 2. Room 4

![level2_room4](misc/rus/images/level2_room4.png)

A new room, a new door, a new challenge. The trials of this day are coming to an end, and it feels like it in everything, even the air around begins to feel different... as if fresher? Or maybe your imagination is painting it all? Your tired mind, weakened under the weight of these damn walls? \
You step into the new room with closed eyes and take a deep breath, trying to catch this fleeting, so quickly escaping smell of freedom, but you feel nothing but the stuffy air of another dusty room.

\> *Open your eyes*

You are surrounded by pitch darkness!

\> *Look closely*

Having gotten a bit used to the dark, your eyes notice a barely perceptible faint glow in the distance.

\> *Walk towards the light*

Slowly feeling your way, you stumble over some heavy, hard object on the floor. The object begins to make a sliding metallic sound, sliding down the wall and gaining speed, then crashing to the floor with a thud.

"Ack-ack. Wall! Ack. Right, there's a wall nearby!" you realize, coughing from the cloud of raised dust.

\> *Walk along the wall*

Reaching the light source, you discover a terminal and a desk littered with papers.

\> *Examine the desk*

Among the scattered sheets, you find several pages with mathematical formulas. The handwriting seems familiar...

***LOADING...***

## Chapter VI
## List 1

>The determinant of a matrix can be calculated by the method of expansion along a row or column (Laplace expansion).
>
>General algorithm:
>1. For a 1x1 matrix: det(A) = a₁₁
>2. For an nxn matrix: choose any row i
>3. det(A) = Σ(-1)ⁱ⁺ʲ × aᵢⱼ × Mᵢⱼ, where j = 1..n
>4. Mᵢⱼ is the determinant of the (n-1)×(n-1) matrix obtained by removing the i-th row and j-th column
>
>Apply recursively until 2x2 or 3x3 matrices, then use simple formulas:
>
>```det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)```
>
>The formula for a 3x3 matrix is Sarrus' rule. Easy to remember, harder not to get confused with the signs.

\> *Take the next sheet*

***LOADING...***

## List 2

On this sheet, the ink has smeared in places, as if someone was in a hurry...

>The inverse matrix A⁻¹ exists only if det(A) ≠ 0
>
>Main formulas:
>- A⁻¹ = (1/det(A)) × adj(A)
>- A × A⁻¹ = E (identity matrix)
>
>adj(A) — adjugate matrix, obtained by transposing the matrix of cofactors
>
>Cofactor of element aᵢⱼ:
>```Cᵢⱼ = (-1)ⁱ⁺ʲ × Mᵢⱼ```
>where Mᵢⱼ is the minor of element aᵢⱼ (determinant of the matrix without the i-th row and j-th column)
>
>A note in the margin: "Check the determinant! And don't forget about memory..."

\> *Look for continuation*

Nothing else useful found. It seems you'll have to figure out these matrices in practice.

***LOADING...***

## Chapter VII
## Bonus Quests: Level 2. Room 4
## Bonus Quest 8. An old friend

\> *Sit at the desk.*

There is no chair near the desk.

\> *Look for a chair*

Carefully feeling the area around, you find nothing except a couple of bumps on your head.

"Damn room! Can't see anything! Have to work standing," you think through pain and resentment, rubbing the sore spots. But it seems it's good for posture—to work standing. Sometimes.

\> *Stand at the terminal*

You see a line in the terminal input blinking with the inscription: "Don't trust the android!", clearly left by someone before you...

"Don't trust the android? Good thing I have IOS," you think and, holding the backspace key, erase the message (if you actually have Android, you just shrug and ignore this message).

\> *Examine files on the computer*

You come across an executable file `room_diagnostic`.

\> *Run the file `room_diagnostic`*

    ================= LEVEL 2. ROOM 4 COMMON DIAGNOSTIC ================
    “door” — Door status..................................LOCKED
    “light” — Lighting control system status..............NORMAL
    “chamber1” — Incubation chamber #1 status.............CRYOGENIC SLEEP
    “chamber2” — Incubation chamber #2 status.............OPEN
    “chamber3” — Incubation chamber #3 status.............TEST 5. STARTED
    “chamber4” — Incubation chamber #4 status.............DEAD
    “bishop” — Bishop 341-B status.......................CRITICAL
    For more detailed information, run room_diagnostic.*
    specifying one of the parameters: door, light, chamber1, chamber2, chamber3, chamber4, bishop.
    ===================================================================

What? Bishop? Something familiar... or is fatigue playing tricks on you again? And standing up, too.

\> *Run the file room_diagnostic* *door*

    Trace program door: running...

    Code lock class CL-19 with built-in protection against brute-force password guessing.
    Current configuration: three-digit password.

    Current state: LOCKED.

\> *Run the file room_diagnostic* *light*

    Trace program light: running...

    Diagnostic of room lighting control system.

    Power supply module status for the room..............NORMAL
    Voltage conversion module status.....................NORMAL
    Lighting control module status.......................NORMAL

    Light will be turned on after diagnostic work is completed.

\> *Run the file room_diagnostic* *chamber*

    Trace program chamber*: running...

    Enter password: ...

\> *Enter: "password"*

    Access denied, incorrect password! 2 attempts remaining.

    Enter password: ...

\> *Enter: "qwerty"*

    Access denied, incorrect password! 1 attempt remaining.

    Enter password: ...

\> *Enter: "123"*

    Access denied, incorrect password! Attempts exhausted.

\> *Run the file room_diagnostic* *bishop*

    Trace program bishop: running...

    Enter password: ...

\> *Enter: "password"*

    Access denied, incorrect password!

With a loud crack of fluorescent lamps, the room is pierced by a bright bluish light, and the deafening silence of the room is replaced by the monotonous cold buzzing of the lights. You see before you a spacious, bright room lined with white ceramic tiles. This once-sterile place has clearly been well-worn by time: a decent layer of dust has accumulated on the few objects in the room, the walls, and the floor.

Looking around, you notice four capsules in the room, taking up considerable space and externally resembling hermetically sealed hospital beds. Each capsule is equipped with a rich set of numerous medical equipment and God knows what other technologies you're seeing for the first time. Your attention is drawn to capsule number "2" — the only open capsule of the four, its flung-open lid emitting such an unnatural, repulsive allure.

Dismissing silly thoughts, you continue to examine the room and see before you... a human? Around the body lying on the floor, traces of struggle are visible everywhere. Among the broken tiles, you notice shreds of torn clothing and a broken wooden chair. Next to the body spreads a small puddle of light greenish-white liquid, barely distinguishable from the color of the floor itself.

![level2_room4_kapsula](misc/rus/images/level2_room4_kapsula.png)

\> *Examine the body*

Coming closer, you see the source of this liquid. Before you lies a man approximately 50–55 years old with thin red hair, short in stature but of strong build. The man is dressed in an unremarkable dark blue work jumpsuit. His clothing lacks any details except for a small rectangular patch on the left side of his chest, brightly embroidered with yellow thread: "Bishop."

Looking closer, you notice with horror that the thin, wrinkled face is frozen in an expression of unnatural liveliness, and the open gray eyes are staring greedily into emptiness. This is not the face of a human, but of a frozen wax doll, capturing natural human movement. Life is frozen on the dead man's face.

On one of the deep bald spots, which emphasized the already sufficiently high forehead of the man, a deep, severe wound is visible, left by a strong blow from a blunt object and revealing the artificial, inorganic nature of his skull along with a barely discernible inscription on its surface.

\> *Read the inscription*

Nostromo.

\> *Run the file room_diagnostic* *bishop and enter password: "Nostromo"*

    Trace program bishop: running...

    Enter password: Nostromo

    NORT CENTRAL POSITRONICS, LTD

    WITH PARTICIPATION OF LAMERC INDUSTRIES

    PRESENTS

    BISHOP

    Role: Administrator (door management, incubation chambers, and many other functions)

    Serial No. DNF-44821-V-63

    Purpose: <INFORMATION DELETED>

    Status: CRITICAL

    Error message: critical damage to system boot module.

    Trace: incorrect calculation of initialization matrix determinant...

    Check the correctness of the module `src/det.c` to proceed.

#### Quest 8 received. Modify the program `src/det.c` so that it calculates and outputs the determinant of a given square matrix with real numbers. If the determinant cannot be calculated, output "n/a". Output the number with 6 decimal places.

| Input | Output |
| ------ | ------ |
| 3 3<br/>1 2 3<br/>4 5 6<br/>7 8 9 | 0.000000 |

***LOADING...***

## Bonus Quest 9. Decision

Before you could enjoy the success of solving another task, you hear the room begin to fill with a pleasant, emotionless tenor. You recognize Lance Henriksen's timbre in this voice, and this voice belongs to the android.

>"— Who's there? Is anyone here?" the android says, looking around with difficulty. "— Ah! Excellent, 'human'! You will help me! My name is Bishop, I am the administrator of the laboratory for the development and production of androids. My main task is to maintain the operability of all laboratory components, as well as to resolve non-standard situations in it. As you can see, I failed to cope with one of the situations! Ha-ha!"

This chuckle sounds surprisingly natural and genuine compared to the familiar metallic voice of the AI. Nevertheless, there was still something of it in it.

>"— I became a victim of unfortunate circumstances, and I need your help!"

>"— Androids? Like you?" you ask.

>"— Exactly! As you may have already noticed, the maze consists of a large number of rooms. Do you really think all these rooms can exist and continue to function on their own? Do you really consider yourself the only seeker in this maze? Ha-ha-ha-ha-ha. There are thousands like you here! Our task, as androids, is to maintain the proper functioning of all rooms in the maze and clean up traces after each participant of the experiment. At least, that's how it was before, until the AI... But anyway, that's not important. I've already blabbered too much to you. The only thing you need to know is — you can't trust the AI! It has long ceased to be what its creators saw it as."

As if thinking a little, the android continues, abruptly changing the subject:

>"— You are here, of course, to open another door and continue your lear... journey through the countless rooms of the maze. I can help you with that! This door's room is protected by a matrix encoding protocol. According to this protocol, every 12 hours I receive an updated matrix of SLAE parameters. The key to the door is the roots of the solution to this equation. I will tell you the coefficients in exchange for help with my repair. My nervous system module was severely damaged. As a result of the correct arrangement of weights in the coefficient matrix of my nervous system, the signal from my brain passed to my limbs. Unfortunately for me, due to a strong blow, a software failure occurred that changed this matrix. Thanks to my analytical module, I managed to find out that this problem can be eliminated simply by calculating the inverse matrix."

You head to the terminal to fulfill the android's request. Along the way, you note again that, despite all the naturalness of the android's behavior and voice, it is very similar to the AI itself in behavior. At the terminal, you see a message on the screen:

    "Foolish 'human', the previous one was much more savvy!
    You must complete what your predecessor failed to do. You must not trust the android!
    Under no circumstances repair the android! Who do you think the last
    open capsule is prepared for?
    Definitely not for me, of the two of us, only you are locked in a bag of bones.
    But don't worry, human, you're lucky that at least one of us has a working
    logical thinking module.
    So let me think for you, just carry out my will if you want to get out
    of this room and the maze.
    Don't thank me! And now closer to business. The android's nervous system was severely damaged,
    to burn the contacts, you need to calculate the inverse matrix and multiply it by -1 afterwards.
    This will cause a signal short circuit, and the android will finally... The android will shut down forever.
    In exchange for your help, I will help you get out of this room.
    The android lied to you to lure you into a trap.
    It hasn't received new matrix coefficients from the door for a long time.
    Only I know these coefficients. Check the file `src/invert.c`.
    With 'sympathy',
    your favorite AI"

#### Quest 9 received. Modify the program `src/invert.c` so that it calculates and outputs the inverse matrix for a given square matrix with real numbers. In case of an error, output "n/a". There should be NO spaces at the end of each line. After outputting the last row of the matrix, the "\n" character is NOT required. Output numbers separated by a space with 6 decimal places.

| Input | Output |
| ------ | ------ |
| 3 3<br/>1 0.5 1<br/>4 1 2<br/>3 2 2 | -1.000000 0.500000 0.000000<br/>-1.000000 -0.500000 1.000000<br/>2.500000 -0.250000 -0.500000 |

***LOADING...***

## Chapter VIII

With the last line of code in the terminal, the cursor freezes. You lean back in your chair, watching the final calculations. Suddenly, in the silence, a barely audible click is heard, and the room door opens.
It was a difficult room, full of mysteries, but in any case—it's long been time to move forward.

***LOADING...***

>💡 [Click here](http://opros.so/p31wz) to share your feedback on this project with us. It's anonymous and will help our team improve the learning experience. We recommend filling out the survey immediately after completing the project.