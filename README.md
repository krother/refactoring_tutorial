
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

- [ ] long Python modules
- [ ] long functions that do not fit on a screen page
- [ ] duplicate sections
- [ ] code sections that are similar
- [ ] code with many indentation levels
- [ ] names of functions that are not descriptive
- [ ] mixture of languages (e.g. HTML / SQL inside Python code)
- [ ] code that mixes different domains together (e.g. user interface + business logic)
- [ ] code that could be expressed more simply
- [ ] code that you find hard to read

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

## 6. Extract Functions

**The most fundamental refactoring technique is to split a long function into shorter ones.**

We will make our toplevel function `travel()` easy to read.
For that, we chop it into smaller pieces.
By creating smaller functions, we either clean up the mess right away or at least create a smaller mess that is contained locally.

We will use the following recipe:

### 6.1 Recipe: Extract a function

1. Find a piece of code you want to move into a function
2. Give the function a name and create a `def` line
3. Move the code into the new function
4. Make a parameter out of every variable not created inside the function
5. Add a return statement at the end with every variable used later
6. Add a function call where you took the code
7. Run the tests

Let's do this on a few examples:

### 6.2 Exercise: extract display_inventory

The paragraph labeled **display inventory** on top ov `travel()` makes a good refactoring candidate.
Create a new function using the signature:

    def display_inventory(credits, engines, copilot)

This function does not need a return statement.

Do not forget to run the tests afterwards.

### 6.3 Exercise: extract display_destinations

Extract a function `display_destinations()` from the code paragraph labeled similarly.

Find out what arguments the function needs.
This function also does not need a return statement.

Work through the recipe.

### 6.4 Exercise: extract select_planet

Extract a function `select_planet()` from the last code paragraph from the `travel()` function.
This function needs a single parameter and a single return value.

Complete the function call and the extracted function:

    planet = select_planet(...)


----

## 7. Extract and Modify

Sometimes, you need to modify a function to move it elsewhere.

### 7.1 Exercise: extract visit_planets

To get a short and clean `travel()` function, it would be good to move the huge block with nested `if` statements out of the way.
Let's extract a function `visit_planets()`. 
Start with the recipe for extracting a function.

Use the signature:

    def visit_planet(planet, engines, copilot, credits, crystal_found):
        ...

and the function call:

    planet, engines, copilot, credits, crystal_found, destinations = visit_planet(planet, engines, copilot, credits, crystal_found)

**When you refactor the code, the tests should fail!**

### 7.2 The function does not work

When you follow the recipe for extracting functions, the tests break.
Something does not quite fit.
The code block contains a `return` statements (in the black hole section).

We need to modify the code to keep things working.
Let's introduce an extra variable `dead`:

1. in the beginning of `travel()`, set the new variable `dead = False`
2. add `dead` to the arguments of `visit_planet()`
3. add `dead` to the function call to `visit_planet()`
4. add `dead` to the return statement in `visit_planet()`
5. replace the single `return` statements by `dead = True`
6. add `dead` to the conditions terminating the `while` loop in travel
7. run the tests

The tests should pass now.

### 7.3 The function is not pretty

The function signature of `visit_planet()` is not very pretty. 
It contains a long list of boolean arguments.
Our signature exposes a problem with our data structures. 
This is a good thing.

We will clean up the data structure in the next section.

An alternative, would be to create a nested function or use global variables for the booleans.
I prefer the long arguments, because you can move the function around more easily, but the alternatives are fine as well.

In all cases, our fix is **temporary**.


### 7.4 How many functions should you extract?

In an ideal world, **each function does exactly one thing**.
What does that mean?

In his [Clean Code Lectures](), Uncle Bob (Robert C. Martin) speaks :

    Q: When is a function doing exactly one thing?
    
    A: When you cannot make two functions out of it.

That means we could probably extract even more functions, especially from `visit_planet()`.
Although this is a good idea, we do not have to do that **right now**. 
There are other, more important refactorings to take care of.

Feel free to experiment with extracting functions on your own.

----

## 8. Extract Data Structures

After extracting a module and functions, the `travel()` function became a lot shorter already. 
But there are still many things to improve.
Let's focus on the data structures:

### 8.1 Exercise: Extract boolean flags

The progress of the game is controlled by a bunch of booleans: `copilot`, `credits`, `crystal_found` etc.
These booleans are passed around together several times.
This is a clear sign that they belong together and should be a data structure.

What Python data structure can we use to store the presence or absence of multiple items?

Let's use a Python `set` that we call `flags`.
We need to modify a lot of code.

First, instead of setting multiple booleans to `False` in `travel()`, define an empty set.

    flags = set()

To check a flag, we would use its name as a string. So the `while` condition in `travel()` would become:

    while not 'crystal_found' in flags or 'dead' in flags:

Now, we need to change the function `display_inventory()` as well:

1. replace the boolean arguments by a single argument `flags`
2. modify the function call accordingly
3. modify the function body to use the `in` operator when checking state, e.g. `if 'credits' in flags:`

We need to do the same with `visit_planet()`

1. replace the boolean arguments by a single argument `flags`
2. modify the function call accordingly
3. remove the booleans from the return values (the set is mutable). `visit_planet()` only returns `planet` and `destinations`.
4. remove the booleans from the assigned return in `travel()` as well
5. modify the function body to use the `in` operator when checking state, e.g. `if 'credits' in flags:`
6. modify the function body of `visit_planet()`. Whenever one of the booleans is modified, add to the set, e.g. `flags.add('crystal_found')`

Finally, run the tests again. The tests should pass.

*Note that looking up things in the set uses string comparison. This is not very performant, of course, but in a text adventure I frankly don't care. If performance becomes important, one could replace the strings by integers or Enums. Also, if you believe performance is important, how about writing a performance test for it first?*

### 8.2 Exercise: Extract a dictionary

The destinations can be placed in a data structure as well.
With each planet in `visit_planet()` there is always a list of destinations returned.

Let's use the following dictionary instead:

    STARMAP = {
        'earth': ['centauri', 'sirius'],
        'centauri': ['earth', 'orion'],
        'sirius': ...,
        'orion': ...,
        'BH#0997': ['sirius'],
        'oracle': ['earth']
    }

1. place the dictionary on top of the Python file
2. fill in the two missing positions
3. remove the individual definitions of `destinations`
4. instead, at the end of the `visit_planet()` function, look up the destinations with `return STARMAP[planet]`
5. run the tests

The tests should pass.

----

## 9. Extract a Class

By now, the `visit_planet()` function has not changed much. 
We managed to save a couple of lines by extracting the `STARMAP` dictionary.
But there is still has a huge nested `if` block.
Let's see what we can do.

### 9.1 Are more dictionaries a good idea?

Should we maybe extract the descriptions of each planet into *another* dictionary?
We would get:

PLANET_DESCRIPTIONS = {
    'earth': TEXT['EARTH_DESCRIPTION],
    'sirius': TEXT['SIRIUS_DESCRIPTION],
    ...
}

You could do this, and it would further simplify `visit_planet()`. 
But seeing multiple dictionaries with the same keys is a clear hint that there is a deeper structure in our code.
We will extract a class.

### 9.2 Exercise: The Planet class

We find a couple of things that the planets have in common:

* every planet has a name
* every planet has a description
* every planet has connections to other planets
* some planets have a puzzle

These are attributes of the new class.

Let's define a new class with the following signature:

    class Planet:

        def __init__(self, name, description, puzzle=None):
            self.name = name
            self.description = description
            self.puzzle = puzzle

For the destinations, we can use the `@property` decorator, so we can continue using the `STARMAP` dict:

        @property
        def destinations(self):
            return STARMAP[self.name]

Add this code after the definition of `STARMAP`. 

Run the tests to make sure you didn't mess up anything (even though we do not use the class yet).

### 9.3 Exercise: Add a method

We will convert the function `visit_planet()` into a method of the new `Planet` class.

Move the entire code from `visit_planet()` into a new method with the signature:

    def visit(self, flags):

As the first thing, have the planet print its own description:

        print(self.description)

That removes a few lines from the function and makes the code easier to read.

The tests won't pass at this point. You may want to run them to make sure you are editing the right file.


### 9.4 Exercise: Create instances

Let's create a dictionary of planets.
We will do so on the module level:

    PLANETS = {
        'earth': Planet('earth', TEXT['EARTH_DESCRIPTION']),
        ...
    }

Seeing this structure next to `STARMAP` suggests that this could be refactored further, but I'll leave that up to you.

We use the `Planet` instances in the `travel()` function. 
The code should be

    planet = PLANETS['earth']
    ...
    while ...:
        planet.visit(flags)
        display_destinations(planet)
        planet = select_planet(planet.destinations)

Note that you need to modify these methods slightly.

At this point, the tests should pass.

### 9.5 Exercise: Breaking down the visit function

Finally, we have restructured our code to a point where we can decompose the huge block of `if` statements.

We first create a function for each of the little puzzles where the player has to enter stuff:

    def star_quiz(...):

    def buy_hyperdrive(...):

    def hire_copilot(...):

    def black_hole(...):

Next, we pass these functions as callbacks in the `puzzle` argument when creating `Planet` objects.
One entry in the `PLANETS` dict would look like:

    'sirius`: Planet('sirius', TEXT['SIRIUS_DESCRIPTION'], star_quiz)

Now in the `visit()` method, all you need to do is call the callback:

    if puzzle:
        puzzle(flags)

And the multiple `if` statements should evaporate.

You might want to get rid of the planet `oracle` at this point.
It is not really a planet, rather an extension of the black hole quiz, so the code can be stuffed into the `black_hole()` puzzle function.

----

## 10. Other Refactoring Strategies

### 10.1 Names matter

*"Planet"* is not an accurate name from an astronomic point of view.
On the other hand, I would refuse to call anything *"System"* on a computer, because it may mean anything.

From a game design point of view, *"Room"* or *"Location"* could be better. These are good questions to discuss with the domain experts and colleagues on your team. Finding common vocabulary is one good side effect successful refactoring may have.

### 10.2 Programming paradigms

When refactoring Python code, you often have multiple options.
It helps if you have a **programming paradigm** in mind that you are working towards, such as:

* functional programming with stateless functions that can be recombined
* strictly object-oriented programming
* hybrid architecture with core classes and toplevel functions
* look for specific **Design Patterns** that describe well what your code is doing
* practice TDD and write additional tests when extracting larger units of code

In my experience, refactoring is much about executing a few standard techniques consistently.

You find a great list of refactoring techniques on [refactoring.guru](https://refactoring.guru/) by Alexander Shvets.

### 10.3 Embrace future change

In refactoring, you always want to separate things that are likely to change from things that don't.
What might change in a text adventure?

* connections between planets
* puzzles on the planets
* new planets
* almost any text
* a graphical or web interface (replacing the `print()` statements would justify a complete rewrite in this case)

With well-refactored code, any of the above should require changing a single location in the code.

In the end, our rectorings should make it easy to add more planets, puzzles or write a completely new adventure.

**Give it a try and have fun programming!**

----

## 11. Closing Remarks

Refactoring is like washing. It is most effective if repeated regularly.

Of course, one could wait for two weeks, so that taking a shower is really worth it.
But in practice this is not such a good idea, at least not if you are working with other people.

It is the same with refactoring.
