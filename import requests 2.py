import requests

def get_current_economic_data():
    url = "https://api.stlouisfed.org/fred/series/observations?series_id=GNPCA&realtime_start=1776-07-04&realtime_end=9999-12-31&api_key=abcdefghijklmnopqrstuvwxyz123456&file_type=json"
    response = requests.get(url)
    data = response.json()
    latest_data = data['observations'][-1]  # Get the latest observation
    return float(latest_data['value'])

def calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op, pmi, omi, pj, oj, pecon, oecon):
    # Fetch the latest economic data
    current_economic_data = get_current_economic_data()
    
    # Calculate each factor's contribution
    career_contribution = pc * oc
    relationship_contribution = pr * or_
    health_contribution = ph * oh
    finance_contribution = pf * of * (current_economic_data / 10000)  # Adjusted for current economic data
    move_contribution = pm * om
    education_contribution = pe * oe
    leisure_contribution = pl * ol
    personal_growth_contribution = pp * op
    mental_health_contribution = pmi * omi
    job_stability_contribution = pj * oj
    economy_contribution = pecon * oecon
    
    # Sum of all contributions
    life_outcome = (career_contribution + relationship_contribution + health_contribution + finance_contribution +
                    move_contribution + education_contribution + leisure_contribution + personal_growth_contribution +
                    mental_health_contribution + job_stability_contribution + economy_contribution)
    
    return life_outcome

def ask_question(question_text):
    while True:
        try:
            value = float(input(question_text))
            if 0 <= value <= 1:
                return value
            else:
                print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 1.")

def ask_outcome(question_text):
    while True:
        try:
            value = float(input(question_text))
            if 1 <= value <= 10:
                return value
            else:
                print("Please enter a value between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 1 and 10.")

# Collect values using the new functions
pc = ask_question("Enter the probability of career success (0 to 1): ")
oc = ask_outcome("Enter the outcome of career success (1 to 10): ")
pr = ask_question("Enter the probability of relationship success (0 to 1): ")
or_ = ask_outcome("Enter the outcome of relationship success (1 to 10): ")
ph = ask_question("Enter the probability of health stability (0 to 1): ")
oh = ask_outcome("Enter the outcome of health stability (1 to 10): ")
pf = ask_question("Enter the probability of financial stability (0 to 1): ")
of = ask_outcome("Enter the outcome of financial stability (1 to 10): ")
pm = ask_question("Enter the probability of successful move (0 to 1): ")
om = ask_outcome("Enter the outcome of successful move (1 to 10): ")
pe = ask_question("Enter the probability of educational attainment (0 to 1): ")
oe = ask_outcome("Enter the outcome of educational attainment (1 to 10): ")
pl = ask_question("Enter the probability of leisure satisfaction (0 to 1): ")
ol = ask_outcome("Enter the outcome of leisure satisfaction (1 to 10): ")
pp = ask_question("Enter the probability of personal growth (0 to 1): ")
op = ask_outcome("Enter the outcome of personal growth (1 to 10): ")
pmi = ask_question("Enter the probability of maintaining mental health (0 to 1): ")
omi = ask_outcome("Enter the outcome of mental health (1 to 10): ")
pj = ask_question("Enter the probability of job stability (0 to 1): ")
oj = ask_outcome("Enter the outcome of job stability (1 to 10): ")
pecon = ask_question("Enter the probability of a stable economy (0 to 1): ")
oecon = ask_outcome("Enter the outcome of a stable economy (1 to 10): ")

# Calculate the life outcome
life_outcome = calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op, pmi, omi, pj, oj, pecon, oecon)
print(f'Calculated Life Outcome: {life_outcome}')
