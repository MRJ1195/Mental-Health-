import logging
import gettext
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime
import bcrypt

# Set up logging
logging.basicConfig(filename='mental_health_assessment.log', level=logging.INFO)

# Set up internationalization
gettext.install('mental_health_assessment')
_ = gettext.gettext

# Define FACTOR_NAMES
FACTOR_NAMES = {
    'dep': "Depression",
    'anx': "Anxiety",
    'str': "Stress",
    'slp': "Sleep",
    'eat': "Eating habits",
    'exe': "Exercise",
    'soc': "Social interaction",
    'wrk': "Work/study performance",
    'ptsd': "Post-traumatic stress",
    'bip': "Bipolar symptoms",
    'sch': "Schizophrenia symptoms"
}

def calculate_mental_health_score(**factors):
    # Implement your calculation logic here
    pass

def interpret_mental_health_score(score):
    if score >= 90:
        return "Excellent mental health"
    elif score >= 80:
        return "Good mental health"
    elif score >= 70:
        return "Fair mental health"
    elif score >= 60:
        return "Poor mental health"
    else:
        return "Critical mental health - seek professional help immediately"

def detailed_feedback(factor_name, score, is_critical=False):
    # Implement your feedback logic here
    pass

def ask_question(question_text):
    # Implement your question asking logic here
    pass

def save_results(username, factors, score):
    try:
        if not os.path.exists('user_data'):
            os.makedirs('user_data')
        
        filename = f'user_data/{username}.json'
        
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
        else:
            data = []
        
        data.append({
            'date': datetime.now().isoformat(),
            'factors': factors,
            'score': score
        })
        
        with open(filename, 'w') as f:
            json.dump(data, f)
    except IOError as e:
        logging.error(f"Error saving results for user {username}: {str(e)}")
        print("An error occurred while saving your results. Please try again later.")

def load_results(username):
    filename = f'user_data/{username}.json'
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
    except IOError as e:
        logging.error(f"Error loading results for user {username}: {str(e)}")
        print("An error occurred while loading your results. Please try again later.")
    return []

def plot_history(username):
    data = load_results(username)
    if not data:
        print("No historical data available.")
        return
    
    dates = [datetime.fromisoformat(entry['date']) for entry in data]
    scores = [entry['score'] for entry in data]
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, scores, marker='o')
    plt.title("Mental Health Score History")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'user_data/{username}_history.png')
    plt.close()
    print(f"History plot saved as {username}_history.png")

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def register_user(username, password):
    if not os.path.exists('users'):
        os.makedirs('users')
    
    filename = 'users/users.json'
    
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                users = json.load(f)
        else:
            users = {}
        
        if username in users:
            return False
        
        users[username] = hash_password(password).decode()  # Store as string
        
        with open(filename, 'w') as f:
            json.dump(users, f)
        
        return True
    except IOError as e:
        logging.error(f"Error registering user {username}: {str(e)}")
        print("An error occurred during registration. Please try again later.")
        return False

def authenticate_user(username, password):
    filename = 'users/users.json'
    
    try:
        if not os.path.exists(filename):
            return False
        
        with open(filename, 'r') as f:
            users = json.load(f)
        
        return username in users and verify_password(password, users[username].encode())
    except IOError as e:
        logging.error(f"Error authenticating user {username}: {str(e)}")
        print("An error occurred during authentication. Please try again later.")
        return False

def main():
    print("Welcome to the Mental Health Assessment Tool")
    print("Disclaimer: This tool is not a substitute for professional medical advice. "
          "Please consult a healthcare provider for any medical concerns.")

    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == '1':
            username = input("Enter a username (minimum 3 characters): ")
            password = input("Enter a password (minimum 8 characters): ")
            if len(username) < 3 or len(password) < 8:
                print("Username must be at least 3 characters and password at least 8 characters long.")
                continue
            if register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists or an error occurred. Please try again.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate_user(username, password):
                print("Login successful!")
                break
            else:
                print("Invalid username or password. Please try again.")
        elif choice == '3':
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    factors = {}
    for factor, name in FACTOR_NAMES.items():
        factors[factor] = ask_question(f"Enter the score for {name} (0 to 100): ")

    mental_health_score = calculate_mental_health_score(**factors)
    mental_health_interpretation = interpret_mental_health_score(mental_health_score)

    print(f'\nMental Health Assessment Results:')
    print(f'\nMental Health Score: {mental_health_score:.2f}')
    print(mental_health_interpretation)

    print(f'\nDetailed Feedback:')
    for factor, score in factors.items():
        print(detailed_feedback(FACTOR_NAMES[factor], score, is_critical=factor in ['dep', 'anx', 'ptsd', 'bip', 'sch']))

    save_results(username, factors, mental_health_score)
    plot_history(username)

    print("\nReferences:")
    print("1. World Health Organization. (2022). Mental health: strengthening our response.")
    print("2. National Institute of Mental Health. (2021). Mental Health Information.")

    logging.info(f"Assessment completed for user {username}. Score: {mental_health_score:.2f}")

if __name__ == "__main__":
    main()