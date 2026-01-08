import random

class AvengersQuiz:
    def __init__(self):
        self.questions = [
            "What's your preferred method of problem-solving?",
            "How do you handle stress?",
            "What's your ideal weekend activity?",
            "What's your leadership style?",
            "How do you approach technology?"
        ]
        self.options = [
            ["A) Strategic planning", "B) Direct confrontation", "C) Scientific analysis", "D) Diplomatic negotiation"],
            ["A) Stay calm and focused", "B) Channel it into action", "C) Analyze the situation", "D) Seek support from others"],
            ["A) Training and self-improvement", "B) Adrenaline-pumping activities", "C) Inventing or experimenting", "D) Relaxing with friends"],
            ["A) Lead by example", "B) Take charge and give orders", "C) Provide innovative solutions", "D) Foster teamwork and cooperation"],
            ["A) Embrace it fully", "B) Use it when necessary", "C) Constantly innovate with it", "D) Balance tradition and innovation"]
        ]
        self.avengers = {
            "A": "Captain America",
            "B": "Iron Man",
            "C": "Black Widow",
            "D": "Thor"
        }
        self.descriptions = {
            "Captain America": "You're a natural leader with a strong moral compass. Like Steve Rogers, you're strategic, loyal, and always stand up for what's right.",
            "Iron Man": "You're a genius with a flair for the dramatic. Like Tony Stark, you're innovative, confident, and always ready with a witty comeback.",
            "Black Widow": "You're skilled, adaptable, and analytical. Like Natasha Romanoff, you excel at reading situations and finding clever solutions.",
            "Thor": "You're powerful, charismatic, and have a strong sense of duty. Like Thor Odinson, you're a formidable ally and a loyal friend."
# Added comment
        }
        self.answers = []

    def ask_question(self, question, options):
        print("\n" + question)
        for option in options:
            print(option)
        while True:
            answer = input("Enter your choice (A/B/C/D): ").upper()
            if answer in ["A", "B", "C", "D"]:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def run_quiz(self):
        print("Welcome to the 'Which Avenger are you?' quiz!")
        print("Answer the following questions to find out which Avenger you most resemble.")
        
        for i in range(len(self.questions)):
            answer = self.ask_question(self.questions[i], self.options[i])
            self.answers.append(answer)

# Added comment
# Added comment
    def calculate_result(self):
        result_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
        for answer in self.answers:
            result_counts[answer] += 1
        
        max_count = max(result_counts.values())
        possible_results = [k for k, v in result_counts.items() if v == max_count]
        final_result = random.choice(possible_results)
        
        return self.avengers[final_result]

    def display_result(self, result):
        print("\nCalculating your result...")
        print(f"\nYou are most like: {result}!")
        print(self.descriptions[result])

def main():
    quiz = AvengersQuiz()
    quiz.run_quiz()
    result = quiz.calculate_result()
    quiz.display_result(result)

    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for playing the Avengers Quiz!")

if __name__ == "__main__":
    main()