Contributors: Lindsay Hall & James Cilwik

Professor Samantha Connolly

CS021 - Intro to Computer Programming (Python)

Introduction
---
For our final project, we developed a basic sudoku game. We implemented a variety of
features into the game, including difficulty modes and the ability to restart, quit, or play again.
To begin, a player chooses from three difficulty levels at the start. Greater difficulty levels
correspond to more numbers being removed from the grid. The user is provided with a 9x9 grid,
from which they will choose one of the labeled rows and columns, then guess what number
belongs in that box. Once the user gives a valid input, they are told whether their guess was
correct, incorrect, or in a box that already contains a number. As with many online sudoku
puzzles, the user can get the answer wrong three times before they lose the game. When they
have lost or won the game, they have the option to play again or quit entirely and their wins are
added to a win counter. The time it took to complete the puzzle is also printed.

Modules Used
---
- Random module: used to remove values from one of four valid sudoku boards randomly
- Copy Module: used to make a deep copy of the original board to avoid mutating it
within a function
- System Module: used to allow the user to quit the game entirely, rather than just start a
new round/play again
- Pandas Module (pip-installed): used to format the board with column and row headers
- Time module: used to time the user when completing the puzzle.

Division of Labor
---
  Both of us put an equal amount of effort and time into the code. Some of this time was
spent working on our own and copying the codes we created into a document for the other
person to test out. We also met in person, both in and out of class, to work the code together and
brainstormed solutions to some of the issues we ran into. There were no parts that one person
spent more time on than the other. In future assignments, it might be easier to use Github when
sharing and writing code together.

Testing Instructions
---
The easiest way to begin testing the program is by following all prompts on the screen.
Feel free to try entering invalid inputs for any input. Our program has sufficient input validation
and should be able to handle this. Secondly, pressing q at any input will quit you from the game.
When asked for the row to enter a number into, press r to restart. Restarting will take you back to
the prompt asking for the difficulty level. Try adding a number to the board that is already filled.
Our program will not accept this. To test losing, make three incorrect inputs. Once you lose, you
will be asked if you want to play again. The easiest way to test the winning sequence is to change
the variable which gives the number of blank spaces on the board. This is found on line 106.
Changing this to one removes only one space from the board. Entering the final correct number
on the board will display a winning statement, the win counter, and the option to play again.

Sources
---
Add Colour to Text in Python | Data Science and Machine Learning. (n.d.). Kaggle.
https://www.kaggle.com/general/273188

copy — Shallow and deep copy operations. (n.d.). Python Documentation. Retrieved April 30,
2023, from
https://docs.python.org/3/library/copy.html?highlight=deepcopy#copy.deepcopy

Jain, Y. (n.d.). How to Print Colored Text in Python - Studytonight. Study Tonight. Retrieved
April 30, 2023, from
https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python

“Pandas.DataFrame — Pandas 1.2.4 Documentation.” Pandas.pydata.org,
pandas.pydata.org/docs/reference/api/pandas.DataFrame.html.

Time — Time access and conversions. (n.d.). Python Documentation. Retrieved April 30, 2023,
from https://docs.python.org/3/library/time.html
