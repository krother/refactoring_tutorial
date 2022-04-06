
# Refactoring 101

*This is the abstract of my 2022 PyCon tutorial.*

## Abstract

In this tutorial, you will refactor a space travel text adventure.
Starting with a working but messy program, you will improve the structure of the code.
You will identify redundant code segments, split long functions into shorter ones, extract data structures and encapsulate behavior into classes. The outcome will be a program that is more readable, easier to maintain, and, hopefully, still works.

The tutorial will be delivered as a guided tour with many hands-on exercises.
Together, we collect strategies that can be applied to Python projects that grow bigger and bigger.
The refactoring tutorial is suitable for junior Python developers.

## Description

### Goal of the tutorial:

As a participant, I want to refactor a piece of unknown Python code, so that you I apply the same techniques to a larger codebase later.

### Motivation:

When you are working on your first real-world Python project, the codebase is typically much larger than any textbook or course example. Over time, software entropy kicks: functions grow longer and longer, the same code gets copy-pasted to multiple places and slowly mutates there, and code that seemed a brilliant idea a few weeks back is now incomprehensible.

### Prerequisites:

You should be well fluent in the basic Python data structures, in particular lists and dictionaries.
You should also have written functions on your own. It helps if you know how a class looks like and how to recognize a generator function. If you have tried writing any of the above and are not happy about the outcome, you have come to the right place.

The tutorial works with any Python installation >= 3.6. It requires a code editor like PyCharm, VSCode or Spyder (no notebooks). We will use the pytest library.

The tutorial focuses on programming strategies, so you don't need any advanced elements of the Python language. 
In particular, we will ignore type hints, decorators, asyncio, Dataclasses, ABC's, metaclasses or pattern matching even if these are great and would help. You do not need any deep knowledge of particular Python packages.

### Structure:

1. What is refactoring?
2. Clone or download the space travel game and make sure it runs
3. Run the tests
4. Identify problematic pieces of code using a checklist of "code smells"
5. Split a long function into multiple shorter ones (apply one of the most fundamental refactoring techniques for warming up)
6. Extract data structures (2-3 separate examples)
7. Encapsulate behavior into a class (this will take longer, because we need to discuss pros and cons of different alternatives)
8. Run the tests again (and emphasize that points 3.+8. are the most important ones on the list; still thinking about special effects here)
9. Discuss common strategies (functional, class-based and hybrid paradigms, design patterns, testability.
10. Closing remarks

The tutorial will be broken down in elementary steps that work both in onsite and online formats.
The complete materials will be available under an Open Source License

