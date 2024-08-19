import random

def generate_unique_id(min_value=1000, max_value=9999):
    return random.randint(min_value, max_value)

class Question:
    def __init__(self, state, capital):
        self.state = state
        self.capital = capital
    
    def ask(self):
        answer = input(f"What is the capital of {self.state}? ").strip()
        is_correct = answer.lower() == self.capital.lower()
        if is_correct:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {self.capital}.\n")
        return answer, is_correct

class Quiz:
    def __init__(self, states_and_capitals):
        self.quiz_id = generate_unique_id()
        self.questions = [Question(state, capital) for state, capital in states_and_capitals.items()]
    
    def administer(self, num_questions=5):
        return random.sample(self.questions, min(num_questions, len(self.questions)))

class Participant:
    def __init__(self, name, age, gender, class_level):
        self.participant_id = generate_unique_id()
        self.name = name
        self.age = age
        self.gender = gender
        self.class_level = class_level
        self.score = 0
        self.quiz_history = []
    
    def answer_question(self, question):
        answer, is_correct = question.ask()
        self.quiz_history.append({
            'question': f"What is the capital of {question.state}?",
            'answer': answer,
            'correct': is_correct
        })
        if is_correct:
            self.score += 1
    
    def display_info(self):
        print(f"ID: {self.participant_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Class: {self.class_level}")
        print(f"Score: {self.score}")
        print("Quiz History:")
        for entry in self.quiz_history:
            print(f"  {entry['question']}")
            print(f"  Answered: {entry['answer']} - {'Correct' if entry['correct'] else 'Incorrect'}")

class QuizCompetition:
    def __init__(self, states_and_capitals):
        self.quiz = Quiz(states_and_capitals)
        self.participants_by_id = {}
        self.participants_by_name = {}
    
    def add_participant(self, name, age, gender, class_level):
        participant = Participant(name, age, gender, class_level)
        self.participants_by_id[participant.participant_id] = participant
        self.participants_by_name[participant.name.lower()] = participant
        print(f"Participant {name} added with ID: {participant.participant_id}")
    
    def conduct_quiz(self, num_questions=5):
        print(f"\nStarting quiz with ID: {self.quiz.quiz_id}...\n")
        for participant_id, participant in self.participants_by_id.items():
            print(f"\nStarting quiz for {participant.name} (ID: {participant.participant_id})...\n")
            questions = self.quiz.administer(num_questions)
            for question in questions:
                participant.answer_question(question)
            print(f"{participant.name} completed the quiz with a score of {participant.score}/{num_questions}.\n")
    
    def retrieve_participant_by_id(self, participant_id):
        participant = self.participants_by_id.get(participant_id)
        if not participant:
            print(f"No data found for participant ID: {participant_id}")
        else:
            participant.display_info()
    
    def retrieve_participant_by_name(self, name):
        participant = self.participants_by_name.get(name.lower())
        if not participant:
            print(f"No data found for participant name: {name}")
        else:
            participant.display_info()

    def display_results(self):
        print("\nQuiz Results:")
        for participant in self.participants_by_id.values():
            print("\n----------------------------")
            participant.display_info()
            print("----------------------------\n")

def main():
    states_and_capitals = {
        "Andhra Pradesh": "Amaravati",
        "Arunachal Pradesh": "Itanagar",
        "Assam": "Dispur",
        "Bihar": "Patna",
        "Chhattisgarh": "Raipur",
        "Goa": "Panaji",
        "Gujarat": "Gandhinagar",
        "Haryana": "Chandigarh",
        "Himachal Pradesh": "Shimla",
        "Jharkhand": "Ranchi",
        "Karnataka": "Bengaluru",
        "Kerala": "Thiruvananthapuram",
        "Madhya Pradesh": "Bhopal",
        "Maharashtra": "Mumbai",
        "Manipur": "Imphal",
        "Meghalaya": "Shillong",
        "Mizoram": "Aizawl",
        "Nagaland": "Kohima",
        "Odisha": "Bhubaneswar",
        "Punjab": "Chandigarh",
        "Rajasthan": "Jaipur",
        "Sikkim": "Gangtok",
        "Tamil Nadu": "Chennai",
        "Telangana": "Hyderabad",
        "Tripura": "Agartala",
        "Uttar Pradesh": "Lucknow",
        "Uttarakhand": "Dehradun",
        "West Bengal": "Kolkata",
    }

    competition = QuizCompetition(states_and_capitals)
    
    num_participants = int(input("Enter the number of participants: "))
    for i in range(1, num_participants + 1):
        name = input(f"Enter the name of Participant {i}: ").strip()
        age = int(input(f"Enter the age of Participant {i}: "))
        gender = input(f"Enter the gender of Participant {i}: ").strip()
        class_level = input(f"Enter the class of Participant {i}: ").strip()
        competition.add_participant(name, age, gender, class_level)
    
    competition.conduct_quiz(num_questions=5)
    competition.display_results()

    while True:
        retrieve_data = input("Do you want to retrieve a participant's quiz data? (yes/no): ").strip().lower()
        if retrieve_data == 'yes':
            search_by = input("Search by ID or Name? (id/name): ").strip().lower()
            if search_by == 'id':
                participant_id = int(input("Enter the participant ID: ").strip())
                competition.retrieve_participant_by_id(participant_id)
            elif search_by == 'name':
                name = input("Enter the participant name: ").strip()
                competition.retrieve_participant_by_name(name)
            else:
                print("Invalid input. Please enter 'id' or 'name'.")
        elif retrieve_data == 'no':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
