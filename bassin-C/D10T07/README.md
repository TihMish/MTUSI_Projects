# D10T07. Structures and Callbacks

Abstract: this project will introduce you to structures and unions in C, as well as callback functions, with additional coverage of function calls, variables, argument lists, and dynamic structures.

## Contents

1. [Introduction](#introduction) \
    1.1. [Project Recommendations](#project-recommendations)
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

## Introduction
### Project Recommendations
How to study at "School 21":  
- Throughout the course, you will independently gather information. Use all available search tools, such as Google and GigaChat. Be attentive to your sources: verify, think, analyze, compare. 
- Peer-to-peer learning (P2P) is a process where learners exchange knowledge and experience, acting simultaneously as teachers and students. This approach allows learning not only from the instructor but also from each other, leading to a deeper understanding of the material.
- Don’t hesitate to ask for help: around you are peers who are also navigating this path for the first time. Don’t be afraid to respond to requests for help. Your experience is valuable and useful—share it boldly with other participants. 
- Do not copy; if you use help, always understand fully why, how, and for what purpose. Otherwise, your learning will have no meaning. 
- If you are stuck on something and feel you've tried everything, but still don’t know where to go—just take a break! Believe it, this advice has helped many developers in their work. Get some fresh air, reset your mind, and maybe next time the right solution will come to you!
- The learning process is just as important as the result. You must not only solve the problem but understand HOW to solve it. 
- Keep track of time while working on the project. You should complete at least one challenge per day. 
- Remember that each task, upon project completion, goes through a series of checks: peer review using a checklist, testing with autotests, code style check, static analyzer check, and check for correct memory handling. 

How to work with the project:
- Useful video materials can be found in the Projects (Media) section on the Platform. 
- Before starting, clone the project from GitLab into a repository with the same name.
- All code files must be created in the `src/` folder of the cloned repository.
- After cloning the project, create a `develop` branch and do all development in it. Then push to GitLab in the `develop` branch as well.

## Chapter I
## Level 3. Room 3

![level3_room3](misc/rus/images/level3_room3.png)

***LOADING Level 3...*** \
***LOADING Room 3...***

\> *Look around*

The same third level. Another room with a table, computer, lamp, and no books. Except this time, where there should be one door, there are now fifteen. Each has a strange electronic lock with a keypad. Very suspicious. But at least there's a lamp—it always feels cozier with one.

\> *Try the first door*

Locked.

\> *Try the second door*

Bolted.

\> *Try the third door*

Won't budge.

\> *Try the fourth door*

Nope.

\> *For i = 5, while i <= 15 -> Try the i-th door and increment i*

Wasted processor time...

\> *Look around again*

You notice that next to the stack of papers on the table lies a newspaper clipping left by someone. Did the AI leave it somehow, or was it someone before you? Though it's odd to think that the AI reads newspapers, let alone cuts out clippings.

\> *Glance over the clipping*

***LOADING...***

## Chapter II
## List 1. MCO

The sheet is yellowed and clearly well-worn. Also cut out very sloppily.

>Mars Climate Orbiter was launched on December 11, 1998, on a Delta II rocket. The spacecraft reached Mars after 9 months. Mars Climate Orbiter was supposed to fire its braking thrusters on September 23, 1999, and enter a highly elliptical orbit with a 14-hour period, then over two months use a series of aerobraking maneuvers in the upper Martian atmosphere to circularize the orbit. At the calculated time at an altitude of 193 km, the spacecraft fired its engines for braking. After 5 minutes, MCO was scheduled to go behind Mars, and no further signals were received from it. Data analysis suggested the spacecraft passed over Mars’ surface at an altitude of 57 km instead of the planned 110 km and disintegrated in the atmosphere. Such a large deviation was caused by a software error in the mission: the thrust commands in the Mars Climate Orbiter software used the unit of force "newton," while the ground software that generated these commands used the imperial unit (pound-force)...

\> *Take the first sheet from the stack under the newspaper clipping*

***LOADING...***

## List 2. Instructions

The sheet looks like a page torn from some programming book... Probably worth reading carefully.

>A structure is a user-defined type that allows storing and moving multiple values of different types together. A structure is defined as follows:

    struct [structure name] {
    element definition;
    element definition;
    ...
    element definition;
    } [one or more variables];

>Using structures allows grouping related data and provides the ability to later modify the passed data without changing function headers.
>
>The memory occupied by a structure equals the sum of memory occupied by all its elements. Thus, structures in C are zero-cost abstractions. Structure elements are placed in memory in the order they are defined.

\> *Take the next sheet*

>A union is a data type that allows reusing memory to store values of different types. A union is defined as follows:

    union [union name] {
    element definition;
    element definition;
    ...
    element definition;
    } [one or more variables];

>The memory occupied by a union is defined as the memory required to store its largest element...

Further text is illegible.

>One application of unions and structures is so-called tagged unions. These are structures that can store one of several allowed data types and contain a tag—an integer by which you can determine which specific data type is currently in the union.

\> *Take the next sheet*

>A singly linked list is a data structure consisting of sequentially linked nodes containing homogeneous data. Each list element has a pointer to the next element; the last one stores a null pointer (0/NULL in C). Lists have variable length, allow easy merging of multiple lists, but occupy more memory and require more elementary operations to traverse than arrays.

***LOADING...***

## Chapter III
## Quests: Level 3. Room 3

## Quest 1. The Doors

\> *Carefully examine the room for additional clues*

Empty.

\> *Carefully examine the table for additional clues*

You notice a small orange paper under the keyboard. Such papers are often used as reminder sticky notes.

\> *Take and read*

Are you sure? This could be personal...

![level3_room3_sticker](misc/rus/images/level3_room3_sticker.png)

\> *Yes. That never bothered anyone before. And I don't have much choice*

>`src/dmanager_module.c` — door management module. \
>Do not touch the door initialization function; it breaks the room core logic. \
>Do not open all doors; it crashes the transmission protocol. \
>For management, allocate a door sorting function in ascending order and a function to close "open" doors.
>
>Door structure: integer id and numeric status (0 — closed, 1 — open).

Looks like a reminder left by someone long before you. Should pay attention to this door management module; it might help.

#### Received Quest 1. Create a door structure in `src/door_struct.h`. The structure consists of an integer door id and an integer status (0 — closed, 1 — open). Fix the program `src/dmanager_module.c` so that it sorts the initialized array of doors in ascending order by door id using any algorithm and outputs it in the format: "door id, door status". Additionally, set the status to "closed" for all doors.
#### Do not modify the door initialization function. Follow a structured approach. The program must be built using Makefile. Stage name — `door_struct`. The executable must be located in the repository root in the build folder and named "Quest_1".

>**IMPORTANT!** It is forbidden to execute system calls using the `system()` function and other similar functions that can directly access the system kernel. This prohibition applies to all subsequent tasks.

>**Attention:** the solution will be checked for memory leaks and code style norms; instructions as usual in materials.

*Expected output (door id, status):*
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

***LOADING...***

## Quest 2. Linked List

So, doors seem to be initialized. But how to exit? Which door should have its status set to "open"? If done for all doors, judging by the notes, it might cause some catastrophe.

\> *Flip the paper*

And here's the continuation.

>The required door changes every day. \
>The current door number is computed via a polynomial function by the room's internal modules. Source code of the module implementation is unavailable. \
>Through reverse engineering, it was revealed that this module cannot work with arrays. In its operation, the module used a dynamically linked library implementing a singly linked list. This library is critically important for the module's operation, but the binary library file was corrupted.

One of the sheets mentioned something about a singly linked list. Should learn more about this list and also figure out memory allocation for it.

#### Received Quest 2. Develop the program `src/list.c`, containing implementations of functions for working with a singly linked list of doors:
#### 1. `struct node* init(struct door door)` — initialize a singly linked list structure based on the passed `struct door`;
#### 2. `struct node* add_door(struct node* elem, struct door door)` — insert a new element `struct door` into the singly linked list after the passed node `elem`;
#### 3. `struct node* find_door(int door_id, struct node* root)` — search for a door in the list by its id;
#### 4. `struct node* remove_door(struct node* elem, struct node* root)` — remove an element from the list;
#### 5. `void destroy(struct node* root)` — free memory occupied by the list structure.<br>

#### Declarations of these functions and the singly linked list structure should be placed in `src/list.h`. Write unit tests to check the operation of `add_door` and `remove_door` functions of the singly linked list in `src/list_test.c`. The method functions should return SUCCESS on successful test completion and FAIL on error. Tests must be built using Makefile. Stage name — `list_test`. The executable must be located in the repository root in the build folder and named "Quest_2".

>**Attention:** this quest will be tested with the `cppcheck` utility.

***LOADING...***

## Quest 3. Stack for key

Okay, the necessary library for the current door number search module is written. You see a rapidly filling progress bar of algorithm activity on the screen. After a few seconds, the number of the door you need appears on the screen. With relief and satisfaction from the completed task, you head to the door.

\> *Try the handle*

Locked... \
However, you notice a small screen opening on the door. Large letters are displayed:

> NO DYNAMIC INT STACK AND/OR STACK OPERATIONS

You return to the computer and ponder what this could mean. Too bad there are no more helpful notes...

Digging into your memory, you recall that a **stack** is a type of dynamic data structure often implemented as a list. Apparently, to open the door, you also need to write a dynamic stack that contains integers. For the stack, you need to implement its standard interface: operations to push data onto the stack (`push`) and pop data from it (`pop`). And don't forget to save all implementations in `src/stack.c`, and function and structure declarations in `src/stack.h`. Also, write unit tests in `src/stack_test.c` to verify the stack and its functions. Otherwise, who knows what might happen if the stack doesn't work correctly...

#### Received Quest 3. Develop the program `src/stack.c`, containing implementations of functions for working with a dynamic stack (`init`, `push`, `pop`, `destroy`). Declarations of functions and the dynamic stack structure storing integers should be placed in `src/stack.h`.
#### Write unit tests to check the operation of `push` and `pop` functions of the stack in `src/stack_test.c`. The method functions should return SUCCESS on successful test completion and FAIL on error. Tests must be built using Makefile. Stage name — `stack_test`. The executable must be located in the repository root in the build folder and named "Quest_3".

>**Attention:** this quest will be tested with the `cppcheck` utility. This task does not include autotesting!

***LOADING...***

## Chapter IV

\> *Push task "Quest 3" to the repository*

Seems everything is done with structures; can move on to the next tasks.

\> *Approach the neighboring door and try the handle*

The door gives way, and you step into the next room.

***LOADING...***

## Chapter V
## Level 3. Room 4

![level3_room4](misc/rus/images/level3_room4.png)

***LOADING Level 3...*** \
***LOADING Room 4...***

\> *Look around*

You enter a new room without books, strange paintings on the walls, and with only one door. Everything would be fine and quite usual if not for the huge living tree growing in the middle of the room. And why are all the rooms on this level so strange...

Approaching the workstation, you see an open report in the command terminal—apparently from one of the engineers. And a couple of yellowed sheets that fell from the tree.

\> *Study the report*

    Recently I had to develop a kernel-mode driver.
    This angered many of my colleagues and was deemed a poor engineering move.

    Like any other code fragment I write,
    this driver had several serious bugs
    that caused some interesting side effects.
    In particular, this driver prevented loading a number of other drivers
    and eventually led to system failure.

    Later I learned that many drivers assume their initialization procedure always succeeds
    and cannot handle failure.
    ...
    Several years ago, an AI codenamed `virtual_j00ru` was developed to document
    such cases in a special journal, and many are still relevant in current OS versions.
    ...
    Eventually, these buggy drivers ceased to be a problem:
    `virtual_j00ru` excelled at its task, saving me many years of life.
    I decided that AI could not only help fix problematic drivers
    but also assist me and many others in numerous other things:
    analyze code, find logical errors,
    make a weekly shopping list, find necessary information, etc.
    So I focused on expanding its functionality.
    I had a lot of work ahead, the first part being adding various structures for...

***LOADING...***

## Chapter VI
## List 1

> DON'T FORGET! All your programs are tested for style norms and memory leaks. The test run instructions are still in the materials folder.

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
    A tree is a data structure providing a hierarchical tree-like structure.
    Mathematically, it is an acyclic connected directed graph,
    in which each vertex (called a node) has zero or more outgoing edges
    and zero or one incoming edge.

    The structure of one element (leaf, node) is described as follows:
typedef struct s_btree
{
struct s_btree *left;
struct s_btree *right;
int item;
} t_btree;


    A binary tree is a tree where nodes have at most two outgoing edges.

![Binary_tree](misc/images/binary_tree.png) \
Fig. 1. Binary tree

    PRESS PAGE DOWN TO CONTINUE

***LOADING...***

## List 3

    Definitions:
    A Binary Search Tree (BST) is a binary tree with a specific order imposed on its nodes.
    The order is often defined by the following induction:
    1. The left subtree of the root contains only nodes with values smaller than the root.
    2. The right subtree of the root contains only nodes with values larger than the root.
    3. All subtrees are also binary search trees.

Characteristics:

|   | average | worst case |
| ------ | ------ | ------ |
| Memory consumption | O(n)      | O(n)    |
| Search         | O(log n)      | O(n)    |
| Insertion       | O(log n)      | O(n) |
| Deletion       | O(log n)      | O(n) |

    Thus, a binary search tree is a binary tree in which all nodes are ordered
    such that left children have a value less than their parent, and right
    children have a value greater than their parent. Consequently, both searching for a given node and in-order traversal
    are efficient (logarithmic and linear respectively).

![Binary_search_tree](misc/images/binary_search_tree.png) \
Fig. 2. Binary search tree

    END OF CURRENT DOCUMENT
    PRESS ANY KEY TO RETURN...

    Validating module...
    System segmentation fault...
    AI documentation module found but not loaded correctly...
    Hint: Try to sort modules in the right order

***LOADING...***

## Chapter VII
## Quests: Level 3. Room 4

>**Attention!** All executables, as before, must be located in the build folder of the project root directory.

## Quest 4. Print Module

The report unexpectedly stops, and you see an error message. Studying it further, you realize the output module is damaged (who would have thought!) and needs replacement.\
The system suggests adding your own module.

\> *Search for documentation on the computer*

Luck is smiling on you today. There is some information about output and documentation modules on the computer.

![level3_room4_leaf](misc/rus/images/level3_room4_leaf.png)

\> *Read the documentation*

You load the documentation and study it.

...

After examining the documentation more closely, you realize the system simply lacks an output function. The signature of the requesting module looks like this:

`void print_log(char (*print) (char), char* message);`

Studying the documentation further, you understand the system kernel works on callback functions, and you need to figure out the screen output implementation and call it in the module.

#### Received Quest 4. In the file `src/print_module.c`, complete the `print_log` function so that it uses the function passed to it as a parameter to output a message of the following type: "[LOG] current_time message". The current time should be in HH:MM:SS format. Modify `src/main_module_entry_point.c` if necessary. The program must be built using Makefile. Stage name — `print_module`, executable name — "Quest_4".

***LOADING...***

## Quest 5. Checking Module

\> *Push changes to the repository*

    System segmentation fault...
    Loading module structure seems to be broken
    System: Output stream module load... Success
                    LOADING...
                      SUCCESS
        Continue reading from where you left off?
                        N/Y

The continuation of the report presents several built-in data structures for use in the AI code. As in any large software project, these common data structures and primitives are provided for reuse in the code. Developers should reuse them whenever possible.

The following sections of the documentation describe the following common data structures, namely: Linked lists, Queues, Maps, Binary Trees. Each section contains information with description, application area, and algorithm complexity.

        SELECT DOCUMENT YOU WANT TO READ
                    >...

                    ERROR...

The text abruptly stops, and the system begins checking the integrity of the remaining data.

                UNRECOGNIZED OPERATION...
                FILTER MODULE: MISSED

Among the large error log, the system highlighted several lines:

    System segmentation fault...
    Loading module structure seems to be broken
    missed or unknown header: stdarg.h
    missed or unknown header: varargs.h
    va_start can’t be used
    va_arg can’t be used
    va_end can’t be used
    use 'man stdarg' to get more information

\> *What is this?*

Who are you even asking...

According to the documentation, apparently you need to write an AI module function described by the following signature:

`int* check_available_documentation_module(int (*validate) (char*), int document_count, ...);`

Judging by the signature, the function should apply a callback mechanism to each passed parameter.

#### Received Quest 5. In the file `src/documentation_module.c`, complete the `check_available_documentation_module` function so that it applies the validation function (also passed as a parameter) to each document passed to it. The result should be an array of document availability, represented as an array of integers (0 — document unavailable, 1 — document available).
#### Extend the functionality of `src/main_module_entry_point.c` so that it implements human-readable output of document availability using the obtained array (format: [document name : (un)available]). For the checked documents, set the output field width modifier to 15 units. Note that the function accepts a variable number of arguments. The program must be built using Makefile. Stage name — `documentation_module`, executable name — "Quest_5".

***LOADING...***

## Bonus Quests
## Bonus Quest 6. BST

\> *What to do?*

Apparently, you need to follow the system's subtle hints and sort the AI modules using a binary search tree. Each module has its own numeric id from 0 to 10. From information found on the computer, the documentation module has identifier 4.

Fortunately for you, the tree element (leaf) structure is already given in the documentation.

First, write a node creation function in `src/bst.c` (the function should save the value in the node and initialize the initial states of child nodes). The function signature should look like:

`t_btree *bstree_create_node(int item)`

The t_btree type must be described in the corresponding header file. Finally, test the node creation function in `src/bst_create_test.c` using unit testing, as you've done before.

#### Received Quest 6. Create a program `src/bst.c`, implementing the function `bstree_create_node` to create a binary search tree node. Place the node type description in `src/bst.h`. Using unit testing, verify the developed function in `src/bst_create_test.c` (at least two input values with output confirming creation). The program must be built using Makefile. Stage name — `bst_create_test`, executable name — "Quest_6".

***LOADING...***

## Bonus Quest 7. Growing tree

\> *Done*

Now that the function for creating one element is ready, you can proceed to create the entire tree by inserting successive nodes.

The function signature should look like this and still be located in `src/bst.c`:

`void bstree_insert(t_btree *root, int item, int (*cmpf) (int, int));`

As can be understood from the signature, node values must be compared using a callback function — `cmpf`.

Finally, the function must also be tested in `src/bst_insert_test.c` with at least two different sets of input values and output showing where the leaf is inserted.

#### Received Quest 7. Extend the program `src/bst.c` by implementing the binary search tree node insertion function `bstree_insert`. Using unit testing, verify the developed function in `src/bst_insert_test.c` (at least two different sets of input values with output showing the leaf insertion location). Provide an implementation of the comparator function. The program must be built using Makefile. Stage name — `bst_insert_test`, executable name — "Quest_7".

***LOADING...***

## Bonus Quest 8. Three styles of traversing

\> *Seems only tree traversal remains*

Need to write tree traversal functions. Since there is no information on the exact order in which the AI documentation modules must be arranged for correct loading, you need to write 3 different traversal functions:
- infix — elements will be displayed in ascending order (left subtree -> root -> right subtree);
- prefix — elements will be displayed in the same order they are stored (root -> left subtree -> right subtree);
- postfix — elements will be displayed in descending order (left subtree -> right subtree -> root).

The function signatures are as follows, and all must be implemented in `src/bst.c`:

`void bstree_apply_infix(t_btree *root, void (*applyf) (int));`

`void bstree_apply_prefix(t_btree *root, void (*applyf) (int));`

`void bstree_apply_postfix(t_btree *root, void (*applyf) (int));`

`applyf` is also a callback function to which the node value must be passed. Such a function could, for example, print values to the screen.

For tests, take input sets from the previous test and format tree output in three different ways in `src/bst_traverse_test.c`.

#### Received Quest 8. Extend the program `src/bst.c` by implementing binary search tree traversal functions `bstree_apply_infix`, `bstree_apply_prefix`, `bstree_apply_postfix`.
#### Using unit testing, verify the written functions in `src/bst_traverse_test.c` (take input sets from the previous test and format tree output in three different ways). Prepare an implementation of the `applyf` function as a function that prints the node value to the terminal. The program must be built using Makefile. Stage name — `bst_traverse_test`, executable name — "Quest_8".

***LOADING...***

## Chapter VIII

\> *Push solution to the repository*

Finally, lines of checks run in the terminal, and you're ready to finish reading the report.

    Validating module...
    ...
    Success
    ...

After waiting about 15 minutes for the modules to finish validation completely, you realize the computer has frozen and isn't responding to any actions.

\> *Press the restart button on the computer*

The screen goes dark, and you notice light smoke coming from the system unit nearby. Seems it overheated or something overheated it...

You don't get to finish the thought, as the door to the room, with a crash resembling an explosion, tears off its hinges and falls toward the tree.

"Well, the exit is open, the computer is broken. Unfortunately, couldn't finish reading the report. And the AI has vanished again. Hope it never returns. Turns out I can deal with doors perfectly fine without it," you think and step over the threshold.

***LOADING...***

>💡 [Click here](http://opros.so/p31wz) to share feedback on this project with us. It's anonymous and will help our team improve the learning experience. We recommend filling out the survey immediately after completing the project.