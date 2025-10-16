class Quiz:
    def __init__(self):
        self.quiz_questions = {}
        self.results = 0

    def add_question(self, new_question):
        self.quiz_questions.update(new_question)

    def take_quiz(self):
        for question in self.quiz_questions:
            answer = input(question)
            if answer.strip().lower() == self.quiz_questions[question].lower():
                self.results += 1
            else: 
                self.results += 0
        print(f"You've earned total amount of {self.results} points. GGs!")


quiz = Quiz()
quiz.add_question({"2 + 2 = ?" : "4"})
quiz.add_question({"Capital of France?" : "Paris"})
quiz.take_quiz()