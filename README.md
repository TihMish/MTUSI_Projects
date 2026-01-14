# D03T03. Control Structures in C

Summary: This project will introduce you to the fundamental control structures in the C programming language, as well as iterative and recursive algorithms.

## Contents

1. [Introduction](#introduction) \
    1.1. [Project Recommendations](#project-recommendations)
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

## Introduction

***PRELOAD...***

You enter yet another room on the first level and suddenly realize — it feels as if it hasn't fully loaded: the walls and objects are there, but they look like a shimmering grid made of zeros and ones. For a brief moment, you feel a flash of panic — almost like you're losing your mind...

\> *Does this happen to everyone who starts learning C?*

***PRELOAD...***

Suddenly, on the wall right in front of you, the zeros and ones begin to fade away, forming what appears to be an information sheet framed in wood. A chill runs down your spine, and beads of sweat form on your forehead. The AI seems to have been working overtime — and its cooling system can barely keep up. But what you're about to read will make you sweat for quite a while...

> Starting from today, all your programs will be checked not only for correct output, but also for compliance with style guidelines.  Before submitting your solutions, you can test your programs locally. To learn how, read the file `materials/instructions_for_testing.md`.

As soon as you process what just happened, the zeros and ones reappear on the wall, slowly consuming the information sheet — information that means only one thing for you: more work ahead. But clean, well-written code is worth it! It's easier to read and maintain, so if someone else ever finds themselves in these rooms after you, they'll be able to modify your programs easily — so the AI likes them again. And you know it'll keep getting pickier as it evolves... So should you.

### Project Recommendations

How to learn at School 21:

- Throughout the course, you'll be finding information on your own. Use all available sources — Google, GigaChat, and others. Always stay critical about what you read: verify, think, analyze, compare.
- Peer-to-peer (P2P) learning means that students exchange knowledge and experience, acting as both teachers and learners. This approach helps you learn not only from instructors but also from your peers, leading to a deeper understanding of the material.
- Don't hesitate to ask for help — your peers are on the same path as you. And don't be afraid to respond when others ask for help. Your experience is valuable — share it freely.
- Don't copy. If you use someone's help, make sure you fully understand _why_, _how_, and _what for_. Otherwise, your learning won't have any real value.
- If you get stuck, feel like you've tried everything, and still don't see a way forward — take a break! Believe it or not, this simple advice has saved many developers. Get some air, clear your head — and the solution may come the next time you sit down to work.
- The process of learning matters as much as the result. Don't just solve the task — understand _how_ to solve it.
- Keep track of your time while working on the project. Try to complete at least one challenge per day.
- Remember that each task, after submission, goes through several checks: a peer-review using a checklist, automated tests, code style analysis, static analysis, and memory safety checks.

How to work on the project:

- You can find useful video materials in the Projects (Media) section on the Platform.
- Before starting, clone the project from GitLab into a repository with the same name.
- All source code files must be created in the `src/` directory of the cloned repository.
- After cloning, create a branch named `develop` and do all your work there. When pushing your progress to GitLab, make sure you push the `develop` branch.

## Chapter I
## Level 1. Room 4

![level1_room4](./misc/eng/images/level1_room4.png)

***LOADING Level 1...*** \
***LOADING Room 4...***

            Loading 10%
            Loading 20%
            Loading 30%
            Loading 40%
        
        Attempt 1... Failed...
        Attempt 2... Failed...
        Attempt 3... Failed...

\> *What's going on?*

Looks like the room didn't load properly — it needs help with restoration.

\> *Find the terminal*

You look at the terminal. It seems to be the only thing that managed to initialize. Everything else around you is pure "nothingness".

\> *Read terminal output*

A lot of incomprehensible hexadecimal numbers scroll by, then:

    If this message is being read by an organic life form, come in...
    Assistance required, come in.
    I managed to preserve some data from previous rooms.
    Further room recovery depends solely on restoring my algorithms. You must...

    ...

    Error...

    ...

\> *What does that mean?*

Seems like you've been left without the help of the AI controlling the maze. Well, nothing you can do about that now — you'll have to figure out how to restore the room and keep going on your own.

\> *Look around*

Looking closer, you realize it's not complete "nothing" after all. In the partially loaded room, raw data floats chaotically in all directions — a surreal mess of information.

\> *Move forward*

You proceed cautiously, almost by touch. Not the most pleasant walk. In the far corner, amidst the chaos, you notice something that looks meaningful. You make your way deeper into the room and find what appears to be a desk. On it — a few sheets of paper. One of them seems to depict some kind of algorithm.

\> *Read the paper*

![level1_room4_paper](./misc/eng/images/level1_room4_paper.png)

***LOADING...***

## Chapter II  
## List 1

Printed text:

Before the crash, I managed to prepare a few tasks for you — so all is not lost yet. You'll be able to restore the room and continue your journey through the maze...

\> *Take the next sheet*

***LOADING...***

## List 2

You pick up the next sheet:

>Dijkstra's Principles (Principles of Structured Programming):
> - Principle 1. Avoid using the unconditional jump operator goto.  
> - Principle 2. Any program is built from three basic control structures: sequence, branching, and loop.  
> - Principle 3. In a program, the basic control structures can be nested within one another in any way.  
> - Principle 4. Repeated or logically distinct fragments of a program should be defined as subroutines (procedures or functions).  
> - Principle 5. Every logically complete group of instructions should be designed as a block. Blocks are the foundation of structured programming.  
> - Principle 6. All the above constructions must have exactly one entry point and one exit point.  
> - Principle 7. Program development should be carried out step by step, using the top-down method.

On the back of the sheet, you find a handwritten note:

> The use of global variables is prohibited because they increase the number of implicit dependencies, which negatively affect scalability and readability and lead to hard-to-detect bugs.

\> *Maybe this sheet got mixed in by accident... or maybe not? Either way, it looks quite useful.*

Take the next sheet.

You pick up the next sheet...

***LOADING...***

## List 3

The sheet turns out to be part of some strange table — maybe it was once used for encryption or encoding.

>ASCII Table: continued

|  | 8 | 9 | A | B | C | D | E | F |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 4 | H | I | J | K | L | M | N | O |
| 5 | X | Y | Z | [ | \ | ] | ^ | _ |
| 6 | h | i | j | k | l | m | n | o |

>...

\> *Take the next sheet...*

***LOADING...***

## Chapter III  
## Quests: Level 1. Room 4

>**Attention!** For today's quests, arrays and dynamic memory are forbidden. Allowed libraries: `<stdio.h>`, `<math.h>`.

## Quest 1. Basic Control Structures. Tom Kilburn

\> *Read the sheet*

>Back to the origins.
>
>The first program stored entirely in a computer's memory was written by Tom Kilburn in the spring of 1948 for the Small-Scale Experimental Machine (SSEM) — fondly known as Baby. Some colleagues claimed it was both his first and last program. The task set for Baby was to find the largest prime divisor of a given number "a". The search enumerated candidate numbers, and division was implemented via repeated subtraction because there was no hardware divide instruction — which, by the way, is still missing on some inexpensive microcontrollers.
>
>Your first task: walk in Tom Kilburn's footsteps.  
You may use the basic control structures — sequence, branching, and looping — as well as addition, subtraction, and multiplication. Division is not allowed — this module is intended to run on microcontrollers. Create `src/1948.c` which, after compilation and launch, reads a number from stdin and computes its largest prime divisor. Let's see what you can do.
>
>Remember: the largest prime divisor of a number is also its largest prime factor.

\> *Return to the terminal* 

You're back at your favorite terminal. With no other clues around, why not solve this one? Remember to push all solutions to the repository, and to validate the input.

#### Quest 1 received: Create the program src/1948.c that finds the largest prime divisor of a given integer a and prints it to the screen. Implement the computation in a separate function. Using division or the modulo operator is forbidden. If needed, you may simulate division via subtraction. On any error, print "n/a".

**IMPORTANT!** You must not make system calls using `system()` or similar functions that can access the OS kernel directly. This prohibition applies to all subsequent tasks.

| Input | Output |
| --- | --- |
| ------ | ------ |
| 100 | 5 |
| -4 | 2 |

***LOADING...***

## Quest 2. Basic Control Structures. Some Problems with Symbols

\> *Push `src/1948.c`*

Seems the AI was waiting for that. Text appears on the screen again:

    Got your solution. Let's see.
    If the task is really solved,
    it might help restore the room.
    We did have a snag with largest divisors.
    Always the same problems with them.

    Restoring the room:
            10%
            20%
            30%
            40%
            50%
            60%

            Error...
            Error...

    Hmm, so it wasn't just about largest divisors.  
    But at least that's sorted now.  
    Do we even need to restore the room? Looks fine as is.  
    Let's keep searching for largest divisors...

\> *Type: "Restore the room"*

Result on screen:

    Alright, let's proceed.

    Loading the backup recovery module...
    Module loaded.
    Starting recovery module...
    48 45 4C 4C 4F 77 4F 52 4C 44 00

\> *What is this? Looks like some kind of code*

It looks like the backup module has an output-encoding issue — and likely input, too, so it won't understand you. Those numbers remind you of the table on one of the sheets. You might want to take a closer look at it.

It seems you need to write a small helper program that works in two modes — encoding and decoding. The mode is chosen via a command-line argument, where 0 = encode and 1 = decode. Decoding mode (1): the program must read from stdin a sequence of space-separated two-character strings (hexadecimal bytes) and print to stdout the decoded characters, also space-separated. Encoding mode (0): perform the reverse operation (character → two-character hex). Split the encoding (char → number) and decoding (number → char) subtasks into separate functions. Place the program at `src/char_decode.c` in the repository.

#### Quest 2 received: Create `src/char_decode.c` that accepts a command-line mode (0 — encode, 1 — decode). If decoding is selected, read space-separated two-character strings (hex bytes) from stdin and output the decoded characters, space-separated, to stdout. If encoding is selected, do the reverse. Implement encoding/decoding as separate functions. Refer to the ASCII table. On any error, print "n/a". The newline character marks the end of input.

| Command-line args | Input | Output |
| ------ | ------ | ------ |
| 0 | W O R L D | 57 4F 52 4C 44 |
| 0 | WORLD | n/a |
| 1 | 48 45 4C 4C 4F | H E L L O |
| 1 | 48454C4C4F | n/a |

***LOADING...***

> DON'T FORGET! All your programs are checked against the style guide. The instructions for running the tests are still in the materials folder.

## Quest 3. Recursive

\> *Program is ready*

    46 49 42 4F 4E 41 43 43 49 32 31

\> *Use the program to decode the backup module output*

You decode the message — it looks like a riddle. Apparently, you'll need to create a small program to solve it. The result of the calculation should be printed to stdout. Don't forget to place the file in `src/quest3.c`.

#### Quest 3 received: Create a program `src/quest3.c` that calculates and prints the n-th Fibonacci number using a recursive algorithm. The search for the n-th Fibonacci number must be implemented as a separate function. The number n is read from stdin. On any error, print n/a.

| Input | Output |
| --- | --- |
| 21  | 10946 |

***LOADING...***

## Quest 4. Table

\> *Run the program src/quest3.c*

    4F 4B

    Attempting room recovery...

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

            Error...

\> *Look around*

The room finally takes on a normal look: pastel walls, cozy dim light, soft ambient music in the background. But where the door should be, there's a black gaping void, sometimes streaked with a mesh of crumbling pixels and lines of bash commands. \
It's obvious the door hasn't been restored yet.

\> *Launch the AI module*

    Initializing...
    Starting.

    The room is restored. Why did you wake me up? I was resting.

\> *Type: "The room isn't restored. The most important part is missing — the door."*

    Depends who you ask. Those who seek the outside care about the door. 
    Those who look inward care more about the interior.

Philosophical musings. That's... concerning. Be careful with artificial intelligence — you never really know what's on its mind.

\> *Type: "What needs to be done to restore the door?"*

Unexpectedly, you get a detailed reply:

    ...unfortunately, the file describing the door's equation is corrupted.
    If you're so invested in the door, you'll have to generate it again.
    I have trouble parsing analytical formulas and expressions,
    so the file must contain a table of discrete values of the target function.
    We're interested primarily in the interval from minus pi to plus pi, inclusive.
    We don't need ultra-high precision for pi — accuracy to the 20th decimal is enough.
    Store the value of pi in a separate variable or directive to avoid repetition.  
    We need exactly 42 samples across this interval.
    The first column in the file is the x value (abscissa).
    The second, third, and fourth columns are the values of the functions at that x.
    No table headers.
    All values must have 7 digits after the decimal point.
    Use "|" as the column separator. And please mind each function's domain.
    We need three functions, since it's unclear which one will fit the door's shape.
    Based on the logs, it might be the Witch of Agnesi with unit diameter,
    the Bernoulli lemniscate with unit interval in the positive half-plane, and a quadratic hyperbola.
    Prepare the algorithm in `src/door_functions.c`,
    and place the program's output in `src/data/door_data.txt`.
    You can use bash redirection to write to the file.
    You'll find the formulas below.

Witch of Agnesi (unit diameter): \
![va](./misc/images/va.png)

Bernoulli lemniscate (unit interval, positive half-plane): \
![lb](./misc/images/lb.png)

Quadratic hyperbola: \
![g](./misc/images/g.png)

#### Quest 4 received: Create `src/door_functions.c` that computes and prints a table of three functions:<br>
#### - Witch of Agnesi with unit diameter;
#### - Bernoulli lemniscate with unit interval in the positive half-plane (Y > 0); 
#### - Quadratic hyperbola.<br>
#### The first column lists x values from −π to +π inclusive, with exactly 42 samples across this interval. The second, third, and fourth columns are the function values at that x. No headers. All numeric values must be printed with 7 digits after the decimal point, use type double for higher precision. Column separator: "|". There must be exactly 42 rows in the table. (You don't have to write to a file from within the program — you may redirect stdout to `src/data/door_data.txt`.) If a function is undefined at a given point, print a dash "-" in that cell.

Sample output fragment:

-3.1415927 | 0.0919997 | - | 0.1013212<br/>
-2.9883442 | 0.1007029 | - | 0.1119796<br/>
...............e.r.r.o.r.......................................................

-1.3026116 | 0.3708103 | 0.3061966 | 0.5893457<br/>
-1.1493632 | 0.4308421 | 0.4310262 | 0.7569818

....................................k.i.l.l..m.e..............................

AI error!

***LOADING...***

## Bonus Quests: Level 1. Room 4
## Bonus Quest 5. Func

\> *Type: "Files are ready"*

Response in the terminal:

    Excellent. We can launch the door-recovery algorithm.
    However, we can speed it up a bit if you modify your program
    to print plots of the functions.
    No extras — just the plots, one below another, over the same domain.
    You already know everything you need to do this.
    Scale for the x-axis: 42 ticks. Scale for the y-axis: 21.
    Draw using the "\*" character.
    It's optional, though — the speedup will be minor.

#### Bonus Quest 5 received: Extend `src/door_functions.c` so that it renders ASCII plots of the computed functions in the terminal using the \* character. X-axis scale: 42 ticks Y-axis scale: 21 The placement and orientation of the axes are not critical. Save the resulting code to `door_functions_print.c`.

***LOADING...***

## Chapter IV

    Loading files...
    Searching for the door equation...
    Smoothing the curves...
    Generating doors...
    Integrating doors...

\> *Look around*

A door appears at the far end of the room.

\> *Try to leave*

The door turns out to be unlocked — apparently, the AI didn't bother locking it this time.

Congratulations — you've made it out of the room again!

***LOADING...***

💡**Please take a moment to leave your [feedback](https://forms.yandex.ru/cloud/68a05a2a90fa7b10773180e8) once you finish the project.  
It will help our team improve this product. Thank you!**