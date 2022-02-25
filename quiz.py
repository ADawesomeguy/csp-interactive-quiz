from random import sample # Used to scramble arrays
from statistics import mode # Used to calculate the most common answer
import tkinter as tk

'''
A dictionary that stores the quiz questions, answers, and what they mean
'''
quizzes = {
    "superhero": {
        "questionsList": [
            {
                "question": "What do you like to do in your free time?",
                "answers": [
                    "Spend time by yourself",
                    "Hang out with friends",
                    "Play around with video games and tech",
                    "Do athletics like gymnastics"
                ]
            },
            {
                "question": "What's your favorite sport?",
                "answers": [
                    "Motorsport",
                    "Extreme sports",
                    "Watersports",
                    "Gymnastics"
                ]
            },
            {
                "question": "How rich are you?",
                "answers": [
                    "I-own-the-biggest-company-in-the-world rich",
                    "I grew up on a farm",
                    "I-own-the-second-biggest-company-in-the-world rich",
                    "My dad changes work a lot"
                ]
            },
            {
                "question": "What's your dream job?",
                "answers": [
                    "Playboy martial artist",
                    "Firefighter",
                    "Playboy engineer",
                    "Martial artist"
                ]
            },
            {
                "question": "If you could go anywhere, where would you go?",
                "answers": [
                    "Your mom's house",
                    "Wherever people need help",
                    "Ibiza",
                    ""
                ]
            }
        ],
        "resultList": [
            "Batman",
            "Superman",
            "Iron Man",
            "Black Widow"
        ]
    },
    "scientist": {      
        "questionsList": [
            {
                "question": "What do you like to do in your free time?",
                "answers": [
                    "Spend time by yourself",
                    "Hang out with friends",
                    "Play around with video games and tech",
                    "Do athletics like gymnastics"
                ]
            },
            {
                "question": "What's your favorite sport?",
                "answers": [
                    "Motorsport",
                    "Extreme sports",
                    "Watersports",
                    "Gymnastics"
                ]
            },
            {
                "question": "How rich are you?",
                "answers": [
                    "I-own-the-biggest-company-in-the-world rich",
                    "I grew up on a farm",
                    "I-own-the-second-biggest-company-in-the-world rich",
                    "My dad changes work a lot"
                ]
            },
            {
                "question": "What's your dream job?",
                "answers": [
                    "Playboy martial artist",
                    "Firefighter",
                    "Playboy engineer",
                    "Martial artist"
                ]
            },
            {
                "question": "If you could go anywhere, where would you go?",
                "answers": [
                    "Your mom's house",
                    "Wherever people need help",
                    "Ibiza",
                    ""
                ]
            }
        ],
        "resultList": [
            "Albert Einstein",
            "Niels Bohr",
            "Marie Curie",
            "Johannes Kepler"
        ]
    }
}

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
Ask for which quiz they would like to take and ask
questions based on that
'''
def ask_questions():
    global quizzes

    answers = []

    quizType = ""
    # Loop through answers to which question they're asking
    while True:
        print("What quiz would you like to take?\n1. Superhero\n2. Scientist")
        quizType = int(input())
        if (quizType not in [1, 2]):
            print("Bruv, that's not a type.")
            continue
        elif quizType == 1:
            quizType = "superhero"
        else:
            quizType = "scientist"
        break

    
    questionsList = sample(quizzes[quizType]["questionsList"], len(quizzes[quizType]["questionsList"]))

    # Loop through each questions and scramble the questions and the answers,
    # get input
    for question in questionsList:
        print("\n")
        print(question['question']) # Print the current question
        scrambledAnswers, scrambledResults = scramble_answers_results(question['answers'], quizzes[quizType]['resultList'])
        for index, answer in enumerate(scrambledAnswers): # Print each answer
            print(str(index + 1) + ". " + answer)
        answer = int(input())
        answer -= 1
        answers.append(scrambledResults[answer]) # Add the person corresponding to the answer choice to an array

    print("\n")
    print("You are " + mode(answers) + "!") # Return the most frequent answer choice in the array for the result

ask_questions()