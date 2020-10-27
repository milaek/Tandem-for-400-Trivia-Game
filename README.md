# Tandem 400

Tandem 400 is a Trivia Game that runs through python using tkinter GUIs.

Test your trivia knowledge over the course of 10 fun trivia questions!

## Installation

Download this Repo onto your computer from GitHub.

## Usage
Open your command line and navigate to the folder in which the downloaded repo is stored.
Then type the following:
```commandline
python Tandem_400_with_GUI.py
```
Use your mouse to click the buttons and submit your desired answers.
The program will exit automatically once you reach the end of a game and choose not to continue.

Note: If using multiple versions of python, please use python3.

## About my Process
Random:

I chose to use python's random library to aid in the randomization of questions and multiple choice answer locations.
This allowed for different groups of questions to be chosen each time a game of trivia was played.
I used the random.sample and random.shuffle functions specifically, the former for its exclusion of duplicates and the latter for its ability to cleanly shuffle a list in place.

Tkinter:

As for the interface, I chose to go with using tkinter GUIs as oppose to having the game run in the command line.
This choice meant I did not have to account for human error in the answer selection. 
Were I assigned to write a trivia program that did not make use of multiple choice, I might have chosen instead to go with the command line.
The GUI is very useful for input that can be replaced with buttons, but not so much for freeform input.
The GUI also allowed me to play more with visual components such as layout and spacing.

Code Structure:

Though I could have chosen to have many of the tkinter object creation lines in the "main" function, I chose instead to section them out into their own sub functions.
This was for legibility purposes, as well as keeping the simplicity of the control structure of "main" intact. 

