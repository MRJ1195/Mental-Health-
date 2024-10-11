def calculate_weighted_probability(base_prob, user_input, weight):
    return (base_prob * weight) + (user_input * (1 - weight))

def calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op, pmi, omi, pj, oj):
    # Base probabilities (scaled to 100)
    base_probs = {
        'pc': 70, 'pr': 50, 'ph': 90, 'pf': 60, 'pm': 40,
        'pe': 80, 'pl': 60, 'pp': 70, 'pmi': 90, 'pj': 50
    }
    weights = {
        'pc': 0.6, 'pr': 0.7, 'ph': 0.8, 'pf': 0.7, 'pm': 0.5,
        'pe': 0.7, 'pl': 0.6, 'pp': 0.7, 'pmi': 0.8, 'pj': 0.6
    }

    # Adjust probabilities
    pc = calculate_weighted_probability(base_probs['pc'], pc, weights['pc'])
    pr = calculate_weighted_probability(base_probs['pr'], pr, weights['pr'])
    ph = calculate_weighted_probability(base_probs['ph'], ph, weights['ph'])
    pf = calculate_weighted_probability(base_probs['pf'], pf, weights['pf'])
    pm = calculate_weighted_probability(base_probs['pm'], pm, weights['pm'])
    pe = calculate_weighted_probability(base_probs['pe'], pe, weights['pe'])
    pl = calculate_weighted_probability(base_probs['pl'], pl, weights['pl'])
    pp = calculate_weighted_probability(base_probs['pp'], pp, weights['pp'])
    pmi = calculate_weighted_probability(base_probs['pmi'], pmi, weights['pmi'])
    pj = calculate_weighted_probability(base_probs['pj'], pj, weights['pj'])

    # Calculate contributions
    career_contribution = pc * (oc / 100)
    relationship_contribution = pr * (or_ / 100)
    health_contribution = ph * (oh / 100)
    finance_contribution = pf * (of / 100)
    move_contribution = pm * (om / 100)
    education_contribution = pe * (oe / 100)
    leisure_contribution = pl * (ol / 100)
    personal_growth_contribution = pp * (op / 100)
    mental_health_contribution = pmi * (omi / 100)
    job_stability_contribution = pj * (oj / 100)

    # Sum of all contributions
    life_outcome = (career_contribution + relationship_contribution + health_contribution + finance_contribution +
                    move_contribution + education_contribution + leisure_contribution + personal_growth_contribution +
                    mental_health_contribution + job_stability_contribution) / 10

    return life_outcome

def interpret_life_outcome(score):
    if score <= 20:
        return "Needs Significant Improvement"
    elif score <= 40:
        return "Moderately Balanced"
    elif score <= 60:
        return "Generally Positive and Stable"
    elif score <= 80:
        return "Highly Positive and Enriching"
    else:
        return "Exceptionally Fulfilling and Successful"

def ask_question(question_text):
    while True:
        try:
            value = float(input(question_text))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 100.")

def ask_outcome(question_text):
    while True:
        try:
            value = float(input(question_text))
            if 1 <= value <= 100:
                return value
            else:
                print("Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 1 and 100.")

# Collect values using the new functions
pc = ask_question("Enter the probability of career success (0 to 100): ")
oc = ask_outcome("Enter the outcome of career success (1 to 100): ")
pr = ask_question("Enter the probability of relationship success (0 to 100): ")
or_ = ask_outcome("Enter the outcome of relationship success (1 to 100): ")
ph = ask_question("Enter the probability of health stability (0 to 100): ")
oh = ask_outcome("Enter the outcome of health stability (1 to 100): ")
pf = ask_question("Enter the probability of financial stability (0 to 100): ")
of = ask_outcome("Enter the outcome of financial stability (1 to 100): ")
pm = ask_question("Enter the probability of successful move (0 to 100): ")
om = ask_outcome("Enter the outcome of successful move (1 to 100): ")
pe = ask_question("Enter the probability of educational attainment (0 to 100): ")
oe = ask_outcome("Enter the outcome of educational attainment (1 to 100): ")
pl = ask_question("Enter the probability of leisure satisfaction (0 to 100): ")
ol = ask_outcome("Enter the outcome of leisure satisfaction (1 to 100): ")
pp = ask_question("Enter the probability of personal growth (0 to 100): ")
op = ask_outcome("Enter the outcome of personal growth (1 to 100): ")
pmi = ask_question("Enter the probability of maintaining mental health (0 to 100): ")
omi = ask_outcome("Enter the outcome")