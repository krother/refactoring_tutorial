
# Refactoring 101

## Goal of this Tutorial

In this tutorial, you will refactor a space travel text adventure.

Starting with a working but messy program, you will improve the structure of the code.
Throughout the tutorial, you will apply standard techniques that make your code more readable and easier to maintain.
This tutorial is suitable for junior Python developers.

----

## 1. What is Refactoring?

When you are working on your first real-world Python project, the codebase is typically much larger than any textbook or course example. Over time, software entropy kicks in: functions grow longer and longer, the same code gets copy-pasted to multiple places and slowly mutates there, and code that seemed a brilliant idea a few weeks back is now incomprehensible. Refactoring aims to prevent your code from becoming a mess.

**Refactoring is improving the structure of code without changing its functionality.**

In practice, this means thing like:

* remove redundant code segments
* split long functions into shorter ones
* extract data structures 
* encapsulate behavior into classes

In this tutorial, you can try all of these. Let's go!

----

## 2. Getting Started

Clone or download the space travel game from [github.com/krother/refactoring_tutorial](https://github.com/krother/refactoring_tutorial):

    git clone git@github.com:krother/refactoring_tutorial.git

The game is a text-based command-line app that should run in any Python editor/environment.
Make sure it runs:

    python space_game.py

Play the game for a few minutes to get a feeling what it is about.

----

## 3. Run the Tests
   
A fundamental rule in refactoring is: **do not start without automated tests**. 
The space game already has tests in `test_space_game.py`. We will use the [pytest](https://pytest.org) library. 
Please make sure it is installed:

    pip install pytest

You can run the tests from the `refactoring_tutorial/` folder:

    pytest test_space_game.py

You should see a message like:

    ============================= test session starts ==============================
    platform linux -- Python 3.8.10, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
    rootdir: /home/kristian/projects/refactoring_tutorial
    plugins: flake8-1.0.7, Faker-8.9.1, asyncio-0.15.1, cov-2.10.1, dash-1.18.1, anyio-3.5.0
    collected 12 items                                                             
    
    test_space_game.py ............                                          [100%]
    
    ============================== 12 passed in 0.04s ==============================

To see the game output, do:

   pytest -s test_space_game.py::test_travel

----

## 4. Identify problematic Code

Now take a look at the main file `space_game.py`.
Look for problematic sections that you would want to refactor.
Note that the code has been linted (with [black](https://pypi.org/project/black/)).
We are not looking for missing spaces or other style issues.

Look for the following:

- [] long Python modules
- [] long functions that do not fit on a screen page
- [] duplicate sections
- [] code sections that are similar
- [] code with many indentation levels
- [] names of functions that are not descriptive
- [] mixture of languages (e.g. HTML / SQL inside Python code)
- [] code that mixes different domains together (e.g. user interface + business logic)
- [] code that could be expressed more simply
- [] code that you find hard to read

Mark everything you find with a `#TODO` comment.

----

## 5. Extract a Module

Let's do our first refactoring.
The first half of the code consists of a huge dictionary `TEXT`.
Let's move that variable into a new Python file in the same folder.

1. create an empty Python file `text_en.py`
2. cut and paste the entire dictionary `TEXT`
3. add an import `from text_en import TEXT`
4. run the tests again

The tests should still pass.

This refactoring creates a separation of domains. 
Now it is a lot easier to e.g. add a second language.

----

5. b) Split a long function into multiple shorter ones (apply one of the most fundamental refactoring techniques for warming up)

   - goal: make the main function look nice

Recipe: Extract a function

    1. Find a piece of code you want to move into a function
    2. Give the function a name and create a def line
    3. Move the code into the new function
    4. Make a parameter out of every variable not created inside the function
    5. Add a return statement at the end with every variable used later
    6. Add a function call where you took the code
    7. Run the tests

    !! it is tempting to reorganize variables etc. now. Don't do this yet.

c) Extract a function display_inventory

Use the signature:

   def display_inventory(credits, engines, copilot)

This function does not need a return statement.

d) Extract a function `display_hyperjump_menu()`

Use the code paragraph labeled similarly.

Find out what argument the function needs.
This function also does not need a return statement.

Run the tests.

e) Extract a function `select_planet()` 

Use the last code paragraph from the `travel()` function.
This function needs a single parameter and a single return value.

Find out which.

### Extract and Modify

Extract a function `visit_planets()`

When you follow the recipe, something does not quite fit. The code block contains two `return` statements (in the black hole section) that would break the test. We have to take care of these by modifying the code.

   We will use an extra variable `dead`.

   - at the start of the visit_planets() function, set `dead` to `False`
   - replace the single `return` statements by `dead = True`
   - return the `dead` variable along with all other variables
   - add the new variable `dead = False` in the beginning of the main function `travel`
   - assign to `dead` along with the other values returned from the function call

### How many functions should you extract?

In an ideal world, **each function does exactly one thing**.

Quote Bob: when is a function doing one thing? When you cannot make two functions out of it.

We won't go as far in this tutorial because we have other things to do. And often, there might be more important refactorings.
Not every function has to be split *right away*.

## Extract data structures

After extracting a module and functions, the `travel()` function became a lot shorter already. 
But there are still many things to improve.
Let's focus on the data structures:

### Flags

The progress of the game is controlled by a bunch of booleans: `copilot`, `credits`, `crystal_found` etc.
These booleans are passed around together several times.
This is a clear sign that they belong together and should be a data structure.

What Python data structure can we use to store the presence or absence of multiple items?

Let's use a Python set that we call `flags`.
So instead of setting multiple booleans to false in `travel()`, you would define an empty set.

    flags = set()

To check a flag, we would use its name as a string. So the next line in `travel()` would become:

    while not 'crystal_found' in flags or 'dead' in flags:

Now, change the calls to `display_inventory()` and `visit_planet()` to use `flags`:

- replace the boolean arguments by a single argument `flags`
- remove the boolean arguments from the return values (the set is mutable). `visit_planet()` only returns `planet` and `destinations`.
- modify the function definition and return statement accordingly.
- whenever one of the booleans is checked, use the `in` operator instead, e.g. `if 'credits' in flags:`
- whenever one of the boolean is modified, add to the set, e.g. `flags.add('crystal_found')` (there are quite a few occurences throughout `visit_planet()`)

Finally, run the tests again.

### Destinations

The destinations can be placed in a data structure as well.
There is always a list of destinations that depends on the planet.

Let's use the following dictionary instead:

    STARMAP = {
        'earth': ['centauri', 'sirius'],
        'centauri': ['earth', 'orion'],
        'sirius': ...,
        'orion': ...,
        'BH#0997': ['sirius'],
        'oracle': ['earth']
    }

Fill in the two missing positions. 
Remove the individual definitions of `destinations`.
Instead, at the end of the `visit_planet()` function, look up the destinations with:

    return STARMAP[planet]

Run the tests afterwards.

7. Encapsulate behavior into a class (this will take longer, because we need to discuss pros and cons of different alternatives)
   - decouple

9. Discuss common strategies (functional, class-based and hybrid paradigms, design patterns, testability.


8. Run the tests again (and emphasize that points 3.+8. are the most important ones on the list; still thinking about special effects here)

## 9. Other Refactoring Strategies

When refactoring Python code, you often have multiple options.
It helps if you have a **programming paradigm** in mind that you are working towards, such as:

* functional programming with stateless functions that can be recombined
* strictly object-oriented programming
* hybrid architecture with core classes and toplevel functions

In my experience, refactoring does not require fancy techniques. 
Refactoring is more about executing a few standard techniques consistently.

You find a great list of refactoring techniques on [refactoring.guru](https://refactoring.guru/) by Alexander Shvets.

## 10. Closing Remarks

Refactoring is like washing. It is most effective if repeated regularly.

Of course, one could wait for two weeks, so that taking a shower is really worth it.
But in practice this is not such a good idea, at least not if you are working with other people.

It is the same with refactoring.
