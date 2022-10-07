import json
import random
from question import Question
class QuestionLibrary:
    def __init__(self, filename="trivia.json"):
        questions = None
        with open(filename, "r") as file:
            questions = json.loads(file.read())

        self.questions = []
        for q in questions:
            self.questions.append(Question(q["question"], q["correct_answer"], q["incorrect_answers"], q["category"], q["difficulty"]))
    
    def get_categories(self):
        categories = []
        for q in self.questions:
            cat = q.category
            if cat not in categories:
                categories.append(cat)

        return categories

    def get_questions(self, category=None, difficulty=None, number=999999):
        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = None
        if category == "":
            category = None

        questions = []
        for q in self.questions:
            if len(questions) >= number:
                break

            if (q.difficulty == difficulty or difficulty == None) and (q.category == category or category == None):
                questions.append(q)
        
        random.shuffle(questions)
        
        return questions

    def __len__(self):
        return len(self.questions)