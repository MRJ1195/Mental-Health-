
from typing import Dict, List, Tuple

def calculate_weighted_probability(base_prob: float, user_input: float, weight: float) -> float:
    return (base_prob * weight) + (user_input * (1 - weight))

def calculate_mental_health_score(
    es: float, anx: float, cop: float, ss: float, se: float, sq: float,
    en: float, df: float, ms: float, mo: float, pt: float, ct: float, st: float
) -> float:
    # Base probabilities (scaled to 10) and weights for mental health attributes
    attributes: List[Tuple[str, float, float]] = [
        ('es', 7, 0.7),   # Emotional Stability
        ('anx', 4, 0.8),  # Anxiety Levels (lower is better)
        ('cop', 8, 0.7),  # Coping Mechanisms
        ('ss', 6, 0.6),   # Social Support
        ('se', 7, 0.7),   # Self-Esteem
        ('sq', 9, 0.8),   # Sleep Quality
        ('en', 8, 0.7),   # Energy Levels
        ('df', 7, 0.8),   # Daily Functioning
        ('ms', 6, 0.7),   # Mood Stability
        ('mo', 7, 0.6),   # Motivation
        ('st', 1, 0.9),   # Suicidal Thoughts
    ]

    # Calculate weighted probabilities
    weighted_probs: Dict[str, float] = {
        attr: calculate_weighted_probability(base_prob, locals()[attr], weight)
        for attr, base_prob, weight in attributes
    }

    # Calculate contributions
    contributions = sum(
        10 - weighted_probs['anx'] if attr == 'anx' else weighted_probs[attr]
        for attr, _, _ in attributes[:-1]  # Exclude 'st' from regular contributions
    )

    # Factor in traumas and suicidal thoughts
    trauma_impact = ((pt * 0.7) + (ct * 0.8)) / 2
    overall_impact = contributions - trauma_impact - (weighted_probs['st'] * 2)

    return overall_impact

def interpret_mental_health_score(score: float) -> str:
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

def ask_question(question_text: str) -> float:
    while True:
        try:
            value = float(input(question_text))
            if 0 <= value <= 10:
                return value
            else:
                print("Please enter a value between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 10.")

# Main execution
if __name__ == "__main__":
    questions = [
        "Enter your emotional stability score (0 to 10): ",
        "Enter your anxiety levels (0 to 10, lower is better): ",
        "Enter your coping mechanism effectiveness (0 to 10): ",
        "Enter your social support score (0 to 10): ",
        "Enter your self-esteem score (0 to 10): ",
        "Enter your sleep quality score (0 to 10): ",
        "Enter your energy levels (0 to 10): ",
        "Enter your daily functioning score (0 to 10): ",
        "Enter your mood stability score (0 to 10): ",
        "Enter your motivation score (0 to 10): ",
        "Enter your score for the impact of previous trauma (0 to 10): ",
        "Enter your score for the impact of current trauma (0 to 10): ",
        "Enter your score for suicidal thoughts (0 to 10): "
    ]

    inputs = [ask_question(q) for q in questions]

    mental_health_score = calculate_mental_health_score(*inputs)
    print(f"Mental Health Score: {mental_health_score:.2f}")
    print(interpret_mental_health_score(mental_health_score))