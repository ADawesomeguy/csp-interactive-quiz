from random import sample # Used to scramble arrays
from statistics import mode # Used to calculate the most common answer
import tkinter as tk # Used for UI
from tkinter import messagebox # Used to display the message of the result
from data import getData # Custom functino to get quiz data stored in another fle

'''
Init vars
'''
results = [] # Empty results to be added to later

root = tk.Tk() # Root window
root.title("Quiz")
quizTypeVar = tk.StringVar(value = "superhero") # Default to superhero
questionVars = [] # Empty (to be added to later)

quizzes = getData() # Get the data from the data.py file

'''
Frames to be raised over one another
'''
quizTypeFrame = tk.Frame(root) # Initial quiz type question
questionsFrame = tk.Frame(root) # Questions from the quiz itsel

for frame in [quizTypeFrame, questionsFrame]:
    frame.grid(row=0, column=0, sticky='news') # Add all the frames to the grid

'''
Scrambles the answers and results in the same order
so that they still match up
'''
def scramble_answers_results(answers, results):
    # Generate the array of random numbers (e.g. 2, 4, 1, 3)
    scrambledIndices = sample(range(4), 4)

    scrambledAnswers = []
    scrambledResults = []

    # Scramble the answer and result arrays based on the scrambled indices
    for index in range(len(scrambledIndices)):
        scrambledAnswers.append(answers[scrambledIndices[index]])
        scrambledResults.append(results[scrambledIndices[index]])
    
    # Return a tuple with the two values
    return scrambledAnswers, scrambledResults


'''
Adds to the results based on the answer choices
and creates a message box to tell them what they
got
'''
def add_to_results():
    # Get global variables to be used
    global root
    global results

    # Destroy the main window
    root.destroy()

    # Add data from each string var to the results
    for result in questionVars:
        results.append(result.get())
    
    messagebox.showinfo("Result", "You are " + mode(results) + "!") # Shows which superhero/scientist that they got

'''
Moves from asking which quiz type
to asking questions for that quiz
type
'''
def go_to_quiz_questions():
    # Global vars
    global questionsFrame

    # Raise the frame to be visible
    questionsFrame.tkraise()
    
    # Get the questionsList and scramble it
    questionsList = sample(quizzes[quizTypeVar.get()]["questionsList"], len(quizzes[quizTypeVar.get()]["questionsList"]))

    # Loop through each questions and create
    # 1. A label
    # 2. Radio buttons for each answer
    for index, question in enumerate(questionsList):
        # Get scrambled answers and results
        scrambledAnswers, scrambledResults = scramble_answers_results(question['answers'], quizzes[quizTypeVar.get()]['resultList'])
        
        # Create a temp string var to be later added to the array
        tempStringVar = tk.StringVar(root, value = scrambledResults[0])
        tk.Label(questionsFrame, 
            text = question["question"],
            justify = tk.LEFT,
            padx = 20).grid(sticky = "w")

        # Loop through each question to create a radio button
        # and store the result value
        for index, answer in enumerate(scrambledAnswers):
            tk.Radiobutton(questionsFrame, 
                text=answer,
                padx = 20,
                variable=tempStringVar,
                value=scrambledResults[index]).grid(sticky = "w")

        # Add the temporary string var to the array
        questionVars.append(tempStringVar)

    # Create a submit button and add it to the bottom of the grid
    tk.Button(
        questionsFrame,
        text="Submit",
        command=add_to_results
    ).grid()

'''
Ask for the quiz type based on those defined in
the quiz data
'''
def ask_quiz_type():
    # Global vars
    global quizzes
    global quizTypeFrame

    # Create a label on the top
    tk.Label(quizTypeFrame, 
        text = "What quiz would you like to take?",
        justify = tk.LEFT,
        padx = 20).grid()

    # Add a new radio button for
    # each quiz type
    for quizType in quizzes:
        tk.Radiobutton(quizTypeFrame, 
            text=quizType.title(),
            padx = 20,
            value=quizType,
            variable=quizTypeVar).grid(sticky = "w")
    
    # Create a button which, when pressed,
    # will move to the 
    tk.Button(quizTypeFrame,
        text="Select",
        command=go_to_quiz_questions
    ).grid()

    # Raise the newly created quiz type
    # frame
    quizTypeFrame.tkraise()

'''
Ask the quiz type to start the
program
'''
ask_quiz_type()
root.mainloop()