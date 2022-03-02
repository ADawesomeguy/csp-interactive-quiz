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
                    "Romania"
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
                    "Imagine",
                    "Look at stuff under microscopes",
                    "Mix stuff",
                    "Look at stars"
                ]
            },
            {
                "question": "How many Nobel prizes have you won?",
                "answers": [
                    "0",
                    "0",
                    "0",
                    "0 (lol ur slacking)"
                ]
            },
            {
                "question": "How old are you?",
                "answers": [
                    "<15",
                    "15-20",
                    "20-30",
                    "30+"
                ]
            },
            {
                "question": "What's your dream job?",
                "answers": [
                    "Physicist",
                    "Particle Physics",
                    "Radioactivity",
                    "Astrophysicist"
                ]
            },
            {
                "question": "If you could go anywhere, where would you go?",
                "answers": [
                    "Germany/Austria",
                    "Denmark",
                    "Poland",
                    "Germany again"
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

def getData():
    return quizzes