def calculate_weighted_probability(user_input, weight_adjustment, weight_user=0.7, weight_adjustment_factor=0.3):
    # Combine user input and adjustment with weights
    return (user_input * weight_user) + (weight_adjustment * weight_adjustment_factor)

def calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op, pmi, omi, pj, oj):
    # Calculate each factor's contribution
    career_contribution = pc * oc
    relationship_contribution = pr * or_
    health_contribution = ph * oh
    finance_contribution = pf * of
    move_contribution = pm * om
    education_contribution = pe * oe
    leisure_contribution = pl * ol
    personal_growth_contribution = pp * op
    mental_health_contribution = pmi * omi
    job_stability_contribution = pj * oj
    
    # Sum of all contributions
    life_outcome = (career_contribution + relationship_contribution + health_contribution + finance_contribution +
                    move_contribution + education_contribution + leisure_contribution + personal_growth_contribution +
                    mental_health_contribution + job_stability_contribution)
    
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

# Collect initial user inputs
pc_user = ask_question("Enter the probability of career success (0 to 1): ")
oc = ask_outcome("Enter the outcome of career success (1 to 10): ")
pr_user = ask_question("Enter the probability of relationship success (0 to 1): ")
or_ = ask_outcome("Enter the outcome of relationship success (1 to 10): ")
ph_user = ask_question("Enter the probability of health stability (0 to 1): ")
oh = ask_outcome("Enter the outcome of health stability (1 to 10): ")
pf_user = ask_question("Enter the probability of financial stability (0 to 1): ")
of = ask_outcome("Enter the outcome of financial stability (1 to 10): ")
pm_user = ask_question("Enter the probability of successful move (0 to 1): ")
om = ask_outcome("Enter the outcome of successful move (1 to 10): ")
pe_user = ask_question("Enter the probability of educational attainment (0 to 1): ")
oe = ask_outcome("Enter the outcome of educational attainment (1 to 10): ")
pl_user = ask_question("Enter the probability of leisure satisfaction (0 to 1): ")
ol = ask_outcome("Enter the outcome of leisure satisfaction (1 to 10): ")
pp_user = ask_question("Enter the probability of personal growth (0 to 1): ")
op = ask_outcome("Enter the outcome of personal growth (1 to 10): ")
pmi_user = ask_question("Enter the probability of maintaining mental health (0 to 1): ")
omi = ask_outcome("Enter the outcome of mental health (1 to 10): ")
pj_user = ask_question("Enter the probability of job stability (0 to 1): ")
oj = ask_outcome("Enter the outcome of job stability (1 to 10): ")

# Example weight adjustments based on context or recent events (these would be dynamically fetched or calculated in a real scenario)
pc_adjustment = 0.8
pr_adjustment = 0.6
ph_adjustment = 0.9
pf_adjustment = 0.7
pm_adjustment = 0.5
pe_adjustment = 0.8
pl_adjustment = 0.7
pp_adjustment = 0.9
pmi_adjustment = 0.8
pj_adjustment = 0.6

# Calculate final probabilities using weighted average
pc = calculate_weighted_probability(pc_user, pc_adjustment)
pr = calculate_weighted_probability(pr_user, pr_adjustment)
ph = calculate_weighted_probability(ph_user, ph_adjustment)
pf = calculate_weighted_probability(pf_user, pf_adjustment)
pm = calculate_weighted_probability(pm_user, pm_adjustment)
pe = calculate_weighted_probability(pe_user, pe_adjustment)
pl = calculate_weighted_probability(pl_user, pl_adjustment)
pp = calculate_weighted_probability(pp_user, pp_adjustment)
pmi = calculate_weighted_probability(pmi_user, pmi_adjustment)
pj = calculate_weighted_probability(pj_user, pj_adjustment)

# Calculate the life outcome
life_outcome = calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op, pmi, omi, pj, oj)
print(f'Calculated Life Outcome: {life_outcome}')
