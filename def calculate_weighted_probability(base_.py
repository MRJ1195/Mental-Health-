def calculate_weighted_probability(base_prob, user_input, weight):
    return (base_prob * weight) + (user_input * (1 - weight))

def calculate_mental_health_score(es, anx, cop, ss, se, sq, en, df, ms, mo, pt, ct, st):
    # Base probabilities (scaled to 10) for mental health attributes
    base_probs = {
        'es': 7,  # Emotional Stability
        'anx': 4, # Anxiety Levels (lower is better)
        'cop': 8, # Coping Mechanisms
        'ss': 6,  # Social Support
        'se': 7,  # Self-Esteem
        'sq': 9,  # Sleep Quality
        'en': 8,  # Energy Levels
        'df': 7,  # Daily Functioning
        'ms': 6,  # Mood Stability
        'mo': 7   # Motivation
    }
    
    # Weights for mental health attributes
    weights = {
        'es': 0.7, 'anx': 0.8, 'cop': 0.7, 'ss': 0.6, 'se': 0.7,
        'sq': 0.8, 'en': 0.7, 'df': 0.8, 'ms': 0.7, 'mo': 0.6
    }

    # Add base probability and weight for suicidal thoughts
    base_probs['st'] = 1  # Low base probability for suicidal thoughts
    weights['st'] = 0.9   # High weight due to its critical nature

    # Adjust probabilities based on user input and weight
    es = calculate_weighted_probability(base_probs['es'], es, weights['es'])
    anx = calculate_weighted_probability(base_probs['anx'], anx, weights['anx'])
    cop = calculate_weighted_probability(base_probs['cop'], cop, weights['cop'])
    ss = calculate_weighted_probability(base_probs['ss'], ss, weights['ss'])
    se = calculate_weighted_probability(base_probs['se'], se, weights['se'])
    sq = calculate_weighted_probability(base_probs['sq'], sq, weights['sq'])
    en = calculate_weighted_probability(base_probs['en'], en, weights['en'])
    df = calculate_weighted_probability(base_probs['df'], df, weights['df'])
    ms = calculate_weighted_probability(base_probs['ms'], ms, weights['ms'])
    mo = calculate_weighted_probability(base_probs['mo'], mo, weights['mo'])
    st = calculate_weighted_probability(base_probs['st'], st, weights['st'])

    # Calculate contributions from each factor
    emotional_stability_contribution = es
    anxiety_contribution = 10 - anx  # Lower anxiety means a higher positive contribution
    coping_contribution = cop
    social_support_contribution = ss
    self_esteem_contribution = se
    sleep_contribution = sq
    energy_contribution = en
    daily_functioning_contribution = df
    mood_stability_contribution = ms
    motivation_contribution = mo

    # Factor in previous and current traumas (negative impact)
    trauma_impact = ((pt * 0.7) + (ct * 0.8)) / 2  # Weighted average of traumas' impact
    overall_impact = (emotional_stability_contribution + anxiety_contribution + 
                      coping_contribution + social_support_contribution + 
                      self_esteem_contribution + sleep_contribution + 
                      energy_contribution + daily_functioning_contribution + 
                      mood_stability_contribution + motivation_contribution - 
                      trauma_impact - (st * 2))  # Doubled impact for suicidal thoughts

    # Return total score
    return overall_impact

def interpret_mental_health_score(score):
    if score <= 0:
        return "Critical - Immediate Professional Help Required"
    elif score <= 2.5:
        return "Severe Mental Health Challenges"
    elif score <= 5:
        return "Moderate Mental Health Struggles"
    elif score <= 7.5:
        return "Stable, With Minor Challenges"
    elif score <= 9:
        return "Generally Positive Mental Health"
    else:
        return "Exceptional Mental Well-Being"

def ask_question(question_text):
    while True:
        try:
            value = float(input(question_text))
            if 0 <= value <= 10:
                return value
            else:
                print("Please enter a value between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 10.")

# Collect user inputs for each mental health attribute (0 to 10 scale)
es = ask_question("Enter your emotional stability score (0 to 10): ")
anx = ask_question("Enter your anxiety levels (0 to 10, lower is better): ")
cop = ask_question("Enter your coping mechanism effectiveness (0 to 10): ")
ss = ask_question("Enter your social support score (0 to 10): ")
se = ask_question("Enter your self-esteem score (0 to 10): ")
sq = ask_question("Enter your sleep quality score (0 to 10): ")
en = ask_question("Enter your energy levels (0 to 10): ")
df = ask_question("Enter your daily functioning score (0 to 10): ")
ms = ask_question("Enter your mood stability score (0 to 10): ")
mo = ask_question("Enter your motivation score (0 to 10): ")

# Collect trauma input
pt = ask_question("Enter your score for the impact of previous trauma (0 to 10): ")
ct = ask_question("Enter your score for the impact of current trauma (0 to 10): ")

# Calculate the mental health score
mental_health_score = calculate_mental_health_score(es, anx, cop, ss, se, sq, en, df, ms, mo, pt, ct)

# Interpret and display the result
print(f"Mental Health Score: {mental_health_score:.2f}")
print(interpret_mental_health_score(mental_health_score))
