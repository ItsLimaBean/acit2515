from multiprocessing.sharedctypes import Value
from question_library import QuestionLibrary
class Game:
    def __init__(self):
        library = QuestionLibrary()
        category = input("Enter a category: ")
        difficulty = input("Enter a difficulty: ")
        
        number = -1
        while number <= 0:
            number = int(input("How many questions?: ") or "0")

        self.questions = library.get_questions(category=category, difficulty=difficulty, number=number)
        self.score = 0

    def play(self):
        for q in self.questions:
            print(str(q))
            answer = 0
            while answer < 1 or answer > 4:
                try:
                    answer = int(input("Enter answer number: "))
                except ValueError:
                    answer = 0
                    
            scores = { "easy": 1, "medium": 2, "hard": 3}

            if q.answer_id == answer:
                gained = scores[q.difficulty]
                print(f"Correct! You gained {gained} score!")

                self.score += gained
            else:
                print("Incorrect!")

            print(f"You have a total of {self.score} score!\n")

        print(f"You finished with a score of {self.score}!")


if __name__ == "__main__":
    game = Game()
    game.play()