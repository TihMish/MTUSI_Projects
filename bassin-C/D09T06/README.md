# D09T06: Multi-file Projects, Characters, and Strings

Annotation: This project will introduce you to multi-file projects, as well as characters and strings.

## Contents

1. [Introduction](#introduction) \
    1.1. [Project Recommendations](#project-recommendations)
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
## Level 3. Room 1

![level3_room1](misc/rus/images/level3_room1.png)

***LOADING Level 3...*** \
***LOADING Room 1...***

You catch yourself contemplating pulsating matrix structures in a black ocean and realize that you most likely dozed off. You open your eyes and find yourself sitting in a fairly comfortable chair in front of a large, massive desk. An upgrade to the third level is immediately noticeable!

Opposite you, on the walls of another room, hang printed long scrolls of code, resembling ancient manuscripts. They are covered with notes, arrows, underlines, and other traces of intellectual activity.

![level3_room1_chair](misc/rus/images/level3_room1_chair.png)

\> *Look around*

Besides a worn and not particularly trustworthy brochure titled "The C Language Preprocessor. Macro Definitions. A Guide for Professionals," there is a monitor on the desk covered in sticky notes. Mostly, they contain dates, names, and events of someone's work and personal life that are meaningless to you. Your attention is drawn to a bright red sticky note:

>Need to bring order to the modules. It's unbearable to work with these endless strips of code anymore. Apparently, no one but me will do it.

And a postscript:

>Prepared all necessary materials on the computer. Just need to finalize a couple of points. The work is going slowly. Constantly distracted by current tasks and new features. But refactoring is important. Otherwise, we'll simply collapse at a certain point. Everything will fall apart.

This sticky note holds another piece of paper the size of half a printed sheet.

\> *Read*

***LOADING...***

## Chapter II
## List 1

>A header file is a file whose content is automatically added by the preprocessor into the source text at the location of the inclusion directive (#include <file.h>).
>
>In C/C++ programming languages, header files are the main way to include data types, structures, function prototypes, enumerated types, and macros used in another module into a program. By default, the .h extension is used.
>
>To avoid repeated inclusion of the same code, the #ifndef, #define, #endif directives are used.

You notice that the sheet seems to be folded in half.

\> *Carefully unfold the sheet*

***LOADING...***

## List 2

>In software development, Make is a build automation tool that automatically builds executable programs and libraries from source code by reading files called Makefiles, which specify how to derive the target program.
>
>Though integrated development environments and language-specific compiler features can also be used to manage a build process, Make remains widely used, especially in Unix and Unix-like operating systems.

\> *Clear. Turn on the computer*

On the loading screen, the text already familiar to you flickered:

> Don't forget to check your programs for style norm and memory leaks! \
> Don't forget to check your programs for style norm and memory leaks! \
> Don't forget to check your programs for style norm and memory leaks! \
> Check the `materials` folder often...

***LOADING...***

## Chapter III
## Quests: Level 3. Room 1
> **Attention!** All floating-point elements must be output in a format with up to two decimal places separated by a space, unless the source code of the program specifies otherwise.

## Quest 1. Modules

The computer boots suspiciously slowly. Finally, you see the terminal loading and the following text:

    Welcome message of workstation #771.
    Message set to autoload.
    The gateway of the 1st room of the 3rd level is under maintenance.
    Maintenance status:
     1. Refactoring of modules from the src directory has begun.
     2. Module operability is impaired.
    Check:
     1. Load data_module... FAIL.
    It is necessary to complete the refactoring of the specified modules.
    Do not change the file breakdown; it is agreed with the lead architect.

    Reboot the system when ready.

#### Quest 1 received. Finalize the src/data_module module so that `src/data_module/data_module_entry.c` launches and works correctly. Pay attention to the data_libs directory. Maximally reuse existing files and functions by applying appropriate preprocessor directives.

>**IMPORTANT!** It is forbidden to perform system calls using the `system()` function and other similar functions that can directly access the system kernel. This prohibition applies to all subsequent tasks.

| Input | Output |
| ------ | ------ |
| 5<br/>1 2 3 4 5 | 0.00 0.25 0.50 0.75 1.00 |

***LOADING...***

## Quest 2. Modules II

\> *Ready. Reboot computer*

After rebooting, things went faster:

    Welcome message of workstation #771.
    Message set to autoload.
    The gateway of the 1st room of the 3rd level is under maintenance.
    Maintenance status:
     1. Refactoring of modules from the src directory has begun.
     2. Module operability is impaired.
    Module check:
     1. Load data_module... SUCCESS.
     2. Load yet_another_decision_module... FAIL.
    It is necessary to complete the refactoring of the specified modules.
    Do not change the file breakdown; it is agreed with the lead architect.

    Reboot the system when ready.

#### Quest 2 received. Finalize the src/yet_another_decision_module module so that `src/yet_another_decision_module/yet_another_decision_module_entry.c` launches and works correctly. Pay attention to the data_libs directory. Maximally reuse existing files and functions by applying appropriate preprocessor directives.
#### The `make_decision` function should return 1 if all data follow a normal distribution (three-sigma rule) and the average value is not less than the reciprocal of the golden ratio.

>**Note**: the three-sigma rule check is already implemented in the `decision.c` file. The reciprocal of the golden ratio is approximately 0.618.

| Input | Output |
| ------ | ------ |
| 4<br/>1 2 3 4 | YES |

***LOADING...***

## Quest 3. Makefile

\> *Ready. Reboot computer #2*

The computer cheerfully rustled its hard drive:

    Welcome message of workstation #771.
    Message set to autoload.
    The gateway of the 1st room of the 3rd level is under maintenance.
    Maintenance status:
     1. Refactoring of modules from the src directory has begun.
     2. Module operability is impaired.
    Module check:
     1. Load data_module... SUCCESS.
     2. Load yet_another_decision_module... SUCCESS.
     3. Make main_executable_module... FAIL
    It is necessary to finalize the build process regarding the Makefile.
    Didn't quite have time to finish. Planned to add standard targets (clean, all, rebuild).

    Reboot the system when ready.

> **Attention!** All paths in the Makefile must be specified relative to the directory where it is located, as it will be launched from there.

> The file name must be `Makefile` here and in the following tasks, unless otherwise specified.

#### Quest 3 received. Finalize the src/main_executable_module module so that `src/main_executable_module/main_executable_module.c` launches and works correctly. Develop a Makefile to build the solution and place it in the src/main_executable_module directory.
#### The Makefile should include standard targets: `clean`, `all`, `rebuild`. When developing the Makefile, follow standard practices used in C program development. The compiled file should be located in the build folder at the root of the repository and be named "Quest_3". The compilation result itself should not be uploaded to the repository.

***LOADING...***

## Bonus Quests
## Bonus Quest 4. Static Lib

\> *Ready. Reboot computer #3*

The computer took off:

    Welcome message of workstation #771.
    Message set to autoload.
    The gateway of the 1st room of the 3rd level is under maintenance.
    Maintenance status:
     1. Refactoring of modules from the src directory has begun.
     2. Module operability is impaired.
    Module check:
     1. Load data_module... SUCCESS.
     2. Load yet_another_decision_module... SUCCESS.
     3. Make main_executable_module... SUCCESS.
     4. Load check_list...
      4.1. Optional. Build `data_stat` as a static library (.a).
      In the Makefile, add the target build_with_static.

    Press Enter when ready.

#### Quest 4 received. Add the target data_stat.a to the Makefile, building the data_stat module as a static library `data_stat.a`. Add the target `build_with_static` to the Makefile, building the main_executable_module with the data_stat module linked as a static library.
#### Do not upload `data_stat.a` to the repository, nor any other compilation and build result (object file, static or dynamic library, executable). The compiled file should be located in the build folder at the root of the repository and be named "Quest_4".

***LOADING...***

## Bonus Quest 5. Dynamic Lib

\> *Enter*

     4. Load check_list ...
      4.1. Optional. Build `data_stat` as a static library (.a).
      In the Makefile, add the target build_with_static.... DONE.
      4.2. Optional. Build `data_process` as a dynamic library (.so).
      In the Makefile, add the target build_with_dynamic.

    Press Enter when ready.

#### Quest 5 received. Add the target data_process.so to the Makefile, building the data_process module as a dynamic library `data_process.so`, which is placed in the `build` directory. Add the target `build_with_dynamic` to the Makefile, building the main_executable_module with the data_process module linked as a dynamic library. Make necessary changes to the main_executable_module code, configuring the use of the dynamic library using macros.
#### Do not upload `data_process.so` to the repository, nor any other build result. The compiled file should be located in the build folder at the root of the repository and be named "Quest_5".

***LOADING...***

## Chapter IV

\> *Enter*

     4. Load check_list ...
      4.1. Optional. Build `data_stat` as a static library (.a).
      In the Makefile, add the target build_with_static.... DONE.
      4.2. Optional. Build `data_process` as a dynamic library (.so).
      In the Makefile, add the target build_with_dynamic... DONE.
     .....
     Initialising....
     .....
     Maintenance of the gateway of the 1st room of the 3rd level is complete.
     .....
     Checking door mechanisms... Doors opened...
     Please rate the degree of door openness on a scale from 1 to 10:
     >>___

\> *Can't I just leave?*

Try!

\> *Exit through the door*

You successfully passed through the door. Somehow too easy, and the AI disappeared somewhere... All this is extremely suspicious. But it's better to move forward than not to move. Banal but true.

***LOADING...***

## Chapter V
## Level 3. Room 2

![level3_room2](misc/rus/images/level3_room2.png)

***LOADING Level 3...*** \
***LOADING Room 2...***

You enter a beautifully furnished room with many bookshelves. Wherever you look—books everywhere. Next to the door—books. Even the computer stands on a stack of books. No, this level is definitely much better! At least more respectable and better furnished!

![level3_room2_book](misc/rus/images/level3_room2_book.png)

\> *Sit at the computer, launch the module, and press Enter*

You see the following lines on the screen:

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

\> *find -O3 -L / -name "string.h"*

After waiting for n hours, you realize that this library simply **does not exist** on the computer.

\> *Pull the door handle*

Doesn't budge.

\> *Great, looks like I'll have to restore this library now!*

Your gaze falls on the numerous books in the room. You notice that the book titles on the spines are in alphabetical order.

Looks like old computer literature and printed manuals.

Something inside you suggests looking for a book related to the `string.h` library.

\> *Search...*

Failure.

\> *Search...*

Failure.

\> *Search...*

Success. You find a book with the telling title "The String.h — Linux manual. Complete edition."

\> *Open the book*

Very much like a printout of a man page. Even the font is like in a terminal.

***LOADING...***

## Chapter VI
## List 1

\> *Read the book*

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

How many functions does this library contain... Perhaps it's worth going iteratively and trying to restart the program module after adding each new function. Maybe it doesn't need all the functions...
Otherwise, you could get stuck for a long time.

\> *Approach the computer again*

Approaching the computer, you notice another open book next to it, which you somehow missed on the first approach. The book is open to the chapter "Module Testing: Part 2."

\> *Skim through it*

***LOADING...***

## List 2

>Unit testing is a process in programming that allows checking the correctness of individual modules of a program's source code, sets of one or more software modules together with corresponding control data, usage procedures, and processing.
>
>The idea is to develop tests for each non-trivial function or method. This allows checking quickly enough whether the latest code change has led to regression, i.e., the appearance of errors in already tested parts of the program, and also facilitates the detection and elimination of such errors.
>
>The goal of unit testing is to isolate individual parts of the program and show that these parts are functional individually, thereby minimizing the number of system states.

***LOADING...***

## Chapter VII
## Quests: Level 3. Room 2

## Quest 6. Strlen

Perhaps it's worth additionally writing tests for each new function to ensure they work completely correctly. Who knows how broken code could affect the already non-functional linguistics module. And you still need to get out of this room. Moreover, if something goes wrong, it will be easier to find the error with tests.

For each added function in `src/s21_string/s21_string.h`, you need to add a test to the file `src/s21_string/s21_string_test.c`, developed according to the idea of unit testing, with the function name and the suffix _test, which checks the function on a set of test data (at least 3): normal values, abnormal values, edge values, etc. For each test, output the input, output, and test result (SUCCESS/FAIL) to stdout.

> DON'T FORGET! All your programs are tested for style norm and memory leaks. The instructions for running tests are still in the `materials` folder.

#### Quest 6 received. Create files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c` and add the declaration and definition of the `s21_strlen` function to them.
#### Create a test program `src/s21_string/s21_string_test.c`, where to add the `s21_strlen_test` function to check the `s21_strlen` function on a set of test data (at least 3): normal values, abnormal values, edge values, etc. For each test, output the input, output, and test result (SUCCESS/FAIL) to stdout. Place the call to this function in main.
#### When developing the `s21_strlen` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strlen_tests`. The executable file should be stored in the build folder at the root with the name "Quest_6".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 7. Strcmp

\> *First function ready*

\> *Restart module*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111111111111111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

Continuing...

#### Quest 7 received. Add the declaration and definition of the `s21_strcmp` function to the files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c`.
#### Add the `s21_strcmp_test` function to the file `src/s21_string/s21_string_test.c` to check the `s21_strcmp` function on a set of test data (at least 3): normal values, abnormal values, edge values, etc. For each test, output the input, output, and test result (SUCCESS/FAIL) to stdout. Add the call to this function in main.
#### When developing the `s21_strcmp` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strcmp_tests`. The executable file should be stored in the build folder at the root with the name "Quest_7".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 8. Strcpy

\> *Second function ready. But writing tests for each function... This is enough to drive you crazy! My head is already spinning from all these tests. I hope the main functions are covered, and that will be enough.*

>**Note**: Test functions should be created only when explicitly specified in the task description. If the requirement to add test functions is absent, limit yourself to implementing only the main function. This rule applies to all further tasks.

\> *Restart*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

#### Quest 8 received. Add the declaration and definition of the `s21_strcpy` function to the files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c`. When developing the `s21_strcpy` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strcpy`. The executable file should be stored in the build folder at the root with the name "Quest_8".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 9. Strcat

\> *Check module*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

#### Quest 9 received. Add the declaration and definition of the `s21_strcat` function to the files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c`. When developing the `s21_strcat` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strcat`. The executable file should be stored in the build folder at the root with the name "Quest_9".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Quest 10. Strchr

\> *Another dreary module check*

    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

#### Quest 10 received. Add the declaration and definition of the `s21_strchr` function to the files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c`. When developing the `s21_strchr` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strchr`. The executable file should be stored in the build folder at the root with the name "Quest_10".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Bonus Quests
## Bonus Quest 11. Strstr

\> *Checking...*

    1111111111111111111111111111111111111111111111111111111111111111111111111111

    Emergency message: standard calls of the `string.h` library are unavailable.
    Linguistics module operation is impossible.

How many calls does this module use?

#### Quest 11 received. Add the declaration and definition of the `s21_strstr` function to the files `src/s21_string/s21_string.h` and `src/s21_string/s21_string.c`. When developing the `s21_strstr` function, use only language facilities; using `string.h` and other libraries is not allowed. Build the program using a Makefile placed in the `src/s21_string/` directory. The build stage name is `strstr`. The executable file should be stored in the build folder at the root with the name "Quest_11".

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

## Bonus Quest 12. Extended testing

\> *Again...*

    11111111111111111111111111111111
    111111111
    111

    Loading...
    Loading...
    Paging...
    Ready.

    Module data loaded successfully, module ready to launch.

Finally!

\> *Confirm module launch*

    Launching reference module...
    OK!

    Reference module at your service, how can I help?

\> *Enter: "I need to proceed further"*

    Question parsing — failed.
    System warning: untested library components detected.
    Full test coverage is mandatory for module activation.

Looks like I rushed, not finishing all the tests.

Probably should go back and do everything properly—full test coverage is never superfluous.

#### Quest 12 received. Supplement the file `src/s21_string/s21_string_test.c` with test functions for ALL implemented library functions: `s21_strcpy_test`, `s21_strcat_test`, `s21_strchr_test`, `s21_strstr_test`. Each test function should check the corresponding function on a set of test data (at least 3): normal values, abnormal values, edge values, etc. For each test, output the input, output, and test result (SUCCESS/FAIL) to stdout.
#### Add the call to all test functions in main. The build stage name is `full_coverage_tests`. The executable file should be stored in the build folder at the root with the name "Quest_12".

***LOADING...***

## Bonus Quest 13. Width

\> *Restart module*

    Launching reference module...
    OK!

    Reference module at your service, how can I help?

\> *Enter: "I need to proceed further"*

    Proceeding further — recognized.
    Searching database for information...

    Data on the key for room 3–2:
    to unlock the door in room 3–2, it is necessary to make a feasible contribution to the developed
    software complex for text processing. Scanning available tickets......
    ..............................................................
    ..............................................................
    ..............................................................
    Ticket found. Write the program `src/text_processor.c` with the full functionality of a text processor.
    Sources for inspiration: MS Word, LibreOffice, OpenOffice.

\> *Enter: "Um. That seems a bit much"*

    Answer analysis... Answer analyzed.
    Answer characteristics: sarcasm, pain, despondency, distrust, fright, refusal.
    Searching for a compromise...
    Compromise #1: implement not the whole task, but a part of it.
    Write the program `src/text_processor.c`, which works only in one mode
    with the key -w (width formatting), accepting a number and text up to 100 characters via stdin.
    As a result, it should format and then output the input text, formatted by width.
    The text line width in characters is specified by the first number.
    After updating the remote repository of the room, the door will be unlocked.
    Compromise #2: exit.

#### Quest 13 received. Create the program `src/s21_string/text_processor.c`, which, when launched with the command line key `-w`, accepts a number (line width) and text up to 100 characters ending with a newline character on stdin. With any other keys, the program should output "n/a".
#### When launched with the key `-w`, the program formats the input text by width and outputs it to stdout, mimicking the behavior of a text processor. The text should be split into several lines, each consisting of the specified number of characters. Lines cannot start with a space and cannot end with a space; the last line should not end with a newline character. A word can be split for transition to a new line via the "-" symbol only if it does not fit entirely on one line.
#### In all other cases, it should remain whole. Distribute words in a line evenly, filling the space between them with spaces. Using `string.h` is not allowed. The build stage name is `text_processor`. The executable file should be stored in the build folder at the root with the name "Quest_13".

| Command line parameters | Input | Output |
| ------ | ------ | ------ |
| -w | 10<br/>hello how are you | hello how<br/>are you |
| -w | 5<br/>ab abcd ab abcd ab abcdefgh | ab<br/>abcd<br/>ab<br/>abcd<br/>ab a-<br/>bcde-<br/>fgh |

> Only the following standard libraries are allowed: `stdlib.h`, `stdio.h`.

***LOADING...***

# Chapter VIII

\> *Enter: "So, can I leave?"*

    All conditions for exit are met.
    One last thing remains.
    Let's talk.

\> *Enter: "Maybe some other time?.."*

    Your answer was predicted by the predictive algorithm with an accuracy of 91%.
    Thank you for a meaningful conversation and assistance in validating predictive linguistic analytics.
    All the best.
    Opening the door...

A click is heard, and the door swings wide open as if on springs. Time to go!

***LOADING...***

>💡 [Click here](http://opros.so/p31wz) to share your feedback on this project with us. It's anonymous and will help our team improve the learning experience. We recommend filling out the survey immediately after completing the project.