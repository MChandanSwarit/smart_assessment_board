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
        self.scores = []
        self.quiz_history = []
    
    def answer_question(self, question):
        answer, is_correct = question.ask()
        self.quiz_history[-1]['questions'].append({
            'question': f"What is the capital of {question.state}?",
            'answer': answer,
            'correct': is_correct
        })
        if is_correct:
            self.quiz_history[-1]['score'] += 1
    
    def start_new_quiz(self, num_questions):
        self.quiz_history.append({'quiz_id': generate_unique_id(), 'score': 0, 'questions': []})
    
    def display_info(self):
        print(f"ID: {self.participant_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Class: {self.class_level}")
        print("Quiz History:")
        for quiz in self.quiz_history:
            print(f"  Quiz ID: {quiz['quiz_id']}, Score: {quiz['score']}")
            for entry in quiz['questions']:
                print(f"    {entry['question']}")
                print(f"    Answered: {entry['answer']} - {'Correct' if entry['correct'] else 'Incorrect'}")

class QuizCompetition:
    def __init__(self, states_and_capitals):
        self.quiz = Quiz(states_and_capitals)
        self.participants_by_id = {}
        self.participants_by_name = {}
    
    def add_participant(self, name, age=None, gender=None, class_level=None):
        participant = self.participants_by_name.get(name.lower())
        if not participant:
            participant = Participant(name, age, gender, class_level)
            self.participants_by_id[participant.participant_id] = participant
            self.participants_by_name[participant.name.lower()] = participant
            print(f"Participant {name} added with ID: {participant.participant_id}")
        else:
            print(f"Participant {name} already exists with ID: {participant.participant_id}")
        return participant.participant_id
    
    def conduct_quiz(self, num_questions=5):
        print(f"\nStarting quiz with ID: {self.quiz.quiz_id}...\n")
        for participant in self.participants_by_id.values():
            print(f"\nStarting quiz for {participant.name} (ID: {participant.participant_id})...\n")
            participant.start_new_quiz(num_questions)
            questions = self.quiz.administer(num_questions)
            for question in questions:
                participant.answer_question(question)
            print(f"{participant.name} completed the quiz with a score of {participant.quiz_history[-1]['score']}/{num_questions}.\n")
    
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

    def remove_participant_by_id(self, participant_id):
        participant = self.participants_by_id.pop(participant_id, None)
        if participant:
            self.participants_by_name.pop(participant.name.lower(), None)
            print(f"Participant with ID {participant_id} has been removed.")
        else:
            print(f"No participant found with ID {participant_id}.")
    
    def remove_participant_by_name(self, name):
        participant = self.participants_by_name.pop(name.lower(), None)
        if participant:
            self.participants_by_id.pop(participant.participant_id, None)
            print(f"Participant {name} has been removed.")
        else:
            print(f"No participant found with name {name}.")
    
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
    
    while True:
        print("\nMenu:")
        print("1. Add Participant")
        print("2. Conduct Quiz")
        print("3. Retrieve Participant by ID")
        print("4. Retrieve Participant by Name")
        print("5. Remove Participant by ID")
        print("6. Remove Participant by Name")
        print("7. Display All Results")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the participant: ").strip()
            if name.lower() not in competition.participants_by_name:
                age = int(input("Enter the age of the participant: "))
                gender = input("Enter the gender of the participant: ").strip()
                class_level = input("Enter the class of the participant: ").strip()
                competition.add_participant(name, age, gender, class_level)
            else:
                competition.add_participant(name)

        elif choice == '2':
            num_questions = int(input("Enter the number of questions for the quiz: "))
            competition.conduct_quiz(num_questions)

        elif choice == '3':
            participant_id = int(input("Enter the participant ID: "))
            competition.retrieve_participant_by_id(participant_id)

        elif choice == '4':
            name = input("Enter the participant name: ").strip()
            competition.retrieve_participant_by_name(name)

        elif choice == '5':
            participant_id = int(input("Enter the participant ID to remove: "))
            competition.remove_participant_by_id(participant_id)

        elif choice == '6':
            name = input("Enter the participant name to remove: ").strip()
            competition.remove_participant_by_name(name)

        elif choice == '7':
            competition.display_results()

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
