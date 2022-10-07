import random
class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        if difficulty not in ["easy", "medium", "hard"]:
            raise AttributeError

        self.answers = [correct_answer] + incorrect_answers
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1

        self.question = question
        self.category = category
        self.difficulty = difficulty

        

    def __str__(self):
        str = f"{self.question}\n"
        for ans in enumerate(self.answers, start=1):
            str += f"{ans[0]}. {ans[1]}\n"
        
        return str