
def calculate_mental_health_score(sm, wlb, sq, pa, ss, dn, ew, mha, mp, ls, dep, anx, ptsd, bip, sch):
    # Calculate the mental health score
    factors = [sm, wlb, sq, pa, ss, dn, ew, mha, mp, ls, dep, anx, ptsd, bip, sch]
    mental_health_score = sum(factors) / len(factors)
    return mental_health_score

def interpret_mental_health_score(score):
    if score <= 25:
        return "Needs Significant Improvement"
    elif score <= 50:
        return "Moderately Balanced"
    elif score <= 75:
        return "Generally Positive and Stable"
    else:
        return "Exceptionally Fulfilling and Successful"

def detailed_feedback(factor_name, score, is_critical=False):
    if is_critical:
        if score > 50:
            return f"{factor_name}: This area requires urgent attention and professional help."
        else:
            return f"{factor_name}: Keep monitoring and seek support if needed."
    else:
        if score <= 25:
            return f"{factor_name}: Needs Significant Improvement"
        elif score <= 50:
            return f"{factor_name}: Moderately Balanced"
        elif score <= 75:
            return f"{factor_name}: Generally Positive and Stable"
        else:
            return f"{factor_name}: Exceptionally Fulfilling and Successful"

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

# Collect values for mental health factors
sm = ask_question("Enter the score for Stress Management (0 to 100): ")
wlb = ask_question("Enter the score for Work-Life Balance (0 to 100): ")
sq = ask_question("Enter the score for Sleep Quality (0 to 100): ")
pa = ask_question("Enter the score for Physical Activity (0 to 100): ")
ss = ask_question("Enter the score for Social Support (0 to 100): ")
dn = ask_question("Enter the score for Diet and Nutrition (0 to 100): ")
ew = ask_question("Enter the score for Emotional Well-being (0 to 100): ")
mha = ask_question("Enter the score for Mental Health Access (0 to 100): ")
mp = ask_question("Enter the score for Mindfulness Practice (0 to 100): ")
ls = ask_question("Enter the score for Life Satisfaction (0 to 100): ")

# Collect values for serious mental health issues
dep = ask_question("Enter the score for Depression (0 to 100): ")
anx = ask_question("Enter the score for Anxiety (0 to 100): ")
ptsd = ask_question("Enter the score for PTSD (0 to 100): ")
bip = ask_question("Enter the score for Bipolar Disorder (0 to 100): ")
sch = ask_question("Enter the score for Schizophrenia (0 to 100): ")

# Calculate the mental health score
mental_health_score = calculate_mental_health_score(sm, wlb, sq, pa, ss, dn, ew, mha, mp, ls, dep, anx, ptsd, bip, sch)
mental_health_interpretation = interpret_mental_health_score(mental_health_score)

# Interpret and display the result
print(f'\nMental Health Assessment Results:')
print(f'\nMental Health Score: {mental_health_score:.2f}')
print(mental_health_interpretation)

# Detailed feedback for each factor
print('\nDetailed Feedback:')
print(detailed_feedback("Stress Management", sm))
print(detailed_feedback("Work-Life Balance", wlb))
print(detailed_feedback("Sleep Quality", sq))
print(detailed_feedback("Physical Activity", pa))
print(detailed_feedback("Social Support", ss))
print(detailed_feedback("Diet and Nutrition", dn))
print(detailed_feedback("Emotional Well-being", ew))
print(detailed_feedback("Mental Health Access", mha))
print(detailed_feedback("Mindfulness Practice", mp))
print(detailed_feedback("Life Satisfaction", ls))
print(detailed_feedback("Depression", dep, is_critical=True))
print(detailed_feedback("Anxiety", anx, is_critical=True))
print(detailed_feedback("PTSD", ptsd, is_critical=True))
print(detailed_feedback("Bipolar Disorder", bip, is_critical=True))
print(detailed_feedback("Schizophrenia", sch, is_critical=True))
