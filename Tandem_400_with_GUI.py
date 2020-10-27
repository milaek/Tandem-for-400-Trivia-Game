import json
import random
import tkinter as tk

# GUI Window dimensions
WIDTH = 600
HEIGHT = 250
WINDOW_PADDING = 30
# GUI Item dimensions
BUTTON_LOCATION_HEIGHT = 200
PADDING = 5
ITEM_HEIGHT = 25
ITEM_MULTI_LINE_HEIGHT = 55
# Number of Trivia Questions to run
NUM_QUESTIONS = 10


# helper function that creates and shuffles a complete multiple choice list
def make_multiple_choice(incorrect, correct):
    """
    Takes the incorrect and correct answers and shuffles them for use in a multiple choice question.
    :param incorrect: the list of dummy answers to be used in the multiple choice
    :param correct: the correct answer to the trivia question
    :return: a shuffled list of all possible answers, the index of the correct answer within shuffled list
    """
    choices = incorrect + [correct]
    random.shuffle(choices)
    correct_index = choices.index(correct)
    return choices, correct_index


def opening_screen():
    """Creates and shows the opening screen"""
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{WINDOW_PADDING}+{WINDOW_PADDING}")

    tk.Label(root,
             text="Welcome to another round of Trivia!\n\nLet's begin.",
             ).place(x=0, y=HEIGHT // 2 - ITEM_MULTI_LINE_HEIGHT, width=WIDTH, height=ITEM_MULTI_LINE_HEIGHT)

    tk.Button(root,
              text="Begin Trivia",
              command=root.destroy
              ).place(x=WIDTH // 4, y=BUTTON_LOCATION_HEIGHT, width=WIDTH // 2, height=ITEM_HEIGHT)

    root.mainloop()


def run_question(question):
    """
    Runs one question of trivia, taking user input in the form of a letter associated with the answer.
    :param question: the question and associated possible answers to use
    :return: 1 if correct, 0 if incorrect
    """
    # set up for question
    multiple_choice, correct_index = make_multiple_choice(question["incorrect"], question["correct"])

    # tk object
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{WINDOW_PADDING}+{WINDOW_PADDING}")
    tk.Label(root,
             text=question["question"],
             ).place(x=0, y=ITEM_HEIGHT+PADDING, width=WIDTH, height=ITEM_HEIGHT)
    v = tk.IntVar()
    v.set(0)

    # create a button for each multiple choice item
    for i, possible_answer in enumerate(multiple_choice):
        tk.Radiobutton(root, text=possible_answer, variable=v, value=i+1
                       ).place(x=WIDTH//4, y=(2+i)*(ITEM_HEIGHT+PADDING), width=WIDTH//2, height=ITEM_HEIGHT)

    tk.Button(root,
              text="Submit", command=root.destroy
              ).place(x=WIDTH//4, y=BUTTON_LOCATION_HEIGHT, width=WIDTH//2, height=ITEM_HEIGHT)
    root.mainloop()

    user_answer = v.get()-1

    # check for correct answer, setup to show user correct/incorrect screen
    if user_answer == correct_index:
        message = f"Correct!\n\nThe answer was {multiple_choice[correct_index]}"
        to_return = 1
    else:
        message = f"Incorrect!\n\nThe correct answer was {multiple_choice[correct_index]}"
        to_return = 0

    # show a screen telling the user if they were correct or not, as well as the correct answer
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{WINDOW_PADDING}+{WINDOW_PADDING}")
    tk.Label(root, text=message,
             ).place(x=0, y=HEIGHT//2-ITEM_MULTI_LINE_HEIGHT, width=WIDTH, height=ITEM_MULTI_LINE_HEIGHT)
    tk.Button(root, text="Next", command=root.destroy
              ).place(x=WIDTH//4, y=BUTTON_LOCATION_HEIGHT, width=WIDTH//2, height=ITEM_HEIGHT)
    root.mainloop()
    return to_return


def trivia_over(correct_counter):
    """
    Tallies the final percentage correct, and shows the user their score. Asks user if they would like to play again.
    :param correct_counter: the number of trivia question the user got correct
    :return: bool. True if user wants to play again, else False
    """
    # calculate score percentage
    percent_correct = int(correct_counter / NUM_QUESTIONS * 100)

    # make end screen and ask if user would like to play again
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{WINDOW_PADDING}+{WINDOW_PADDING}")
    v = tk.IntVar()
    tk.Label(root, text=f"Trivia Round Over!\n\nYou got {correct_counter} out of {NUM_QUESTIONS} questions correct. "
                        f"That's {percent_correct}%!",
             ).place(x=0, y=HEIGHT // 2 - (ITEM_MULTI_LINE_HEIGHT+PADDING), width=WIDTH, height=ITEM_MULTI_LINE_HEIGHT)
    tk.Label(root, text=f"Would you like to play again?",
             ).place(x=0, y=HEIGHT // 2, width=WIDTH, height=ITEM_MULTI_LINE_HEIGHT)
    # yes or no buttons
    tk.Radiobutton(root, text="Yes", indicatoron=0, variable=v, value=1, command=root.destroy
                   ).place(x=WIDTH // 4 - 5, y=BUTTON_LOCATION_HEIGHT, width=WIDTH // 4, height=ITEM_HEIGHT)
    tk.Radiobutton(root, text="No", indicatoron=0, variable=v, value=2, command=root.destroy
                   ).place(x=WIDTH // 2 + 5, y=BUTTON_LOCATION_HEIGHT, width=WIDTH // 4, height=ITEM_HEIGHT)
    root.mainloop()

    # check for if user chose to end the game or play again
    if v.get() == 1:
        return True
    return False


def final_message():
    """Displays the final screen of the game"""
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{WINDOW_PADDING}+{WINDOW_PADDING}")

    tk.Label(root, text="Thanks for playing!",
             ).place(x=0, y=HEIGHT // 2 - ITEM_HEIGHT, width=WIDTH, height=ITEM_HEIGHT)

    tk.Button(root, text="End", command=root.destroy
              ).place(x=WIDTH // 4, y=BUTTON_LOCATION_HEIGHT, width=WIDTH // 2, height=ITEM_HEIGHT)
    root.mainloop()


def main():
    """
    Runs a NUM_QUESTIONS question long game of trivia as many times as the user desires.
    """
    # parse the json file and turn it into a list of dicts
    with open("Apprentice_TandemFor400_Data.json") as f:
        trivia_source = json.load(f)

    # games will continue until user chooses to stop
    play = True
    while play:
        # counter that will be adjusted during game for correct responses
        correct_counter = 0

        # get the questions for use in this game of trivia. no repeats.
        questions = random.sample(trivia_source, NUM_QUESTIONS)

        # show opening screen
        opening_screen()

        # run each question, adding to the correct counter as correct answers are given
        for question in questions:
            correct_counter += run_question(question)

        # show the final score, ask user if they would like to play again
        play = trivia_over(correct_counter)

    # show final message when user is done playing trivia
    final_message()


# call to run main
if __name__ == "__main__":
    main()
