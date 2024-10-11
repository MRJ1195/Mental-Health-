def calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op):
    # Calculate each factor's contribution
    career_contribution = pc * oc
    relationship_contribution = pr * or_
    health_contribution = ph * oh
    finance_contribution = pf * of
    move_contribution = pm * om
    education_contribution = pe * oe
    leisure_contribution = pl * ol
    personal_growth_contribution = pp * op
    
    # Sum of all contributions
    life_outcome = (career_contribution + relationship_contribution + health_contribution + finance_contribution +
                    move_contribution + education_contribution + leisure_contribution + personal_growth_contribution)
    
    return life_outcome

# Input your values
pc = float(input("Enter the probability of career success (0 to 1): "))
oc = float(input("Enter the outcome of career success (1 to 10): "))
pr = float(input("Enter the probability of relationship success (0 to 1): "))
or_ = float(input("Enter the outcome of relationship success (1 to 10): "))
ph = float(input("Enter the probability of health stability (0 to 1): "))
oh = float(input("Enter the outcome of health stability (1 to 10): "))
pf = float(input("Enter the probability of financial stability (0 to 1): "))
of = float(input("Enter the outcome of financial stability (1 to 10): "))
pm = float(input("Enter the probability of successful move (0 to 1): "))
om = float(input("Enter the outcome of successful move (1 to 10): "))
pe = float(input("Enter the probability of educational attainment (0 to 1): "))
oe = float(input("Enter the outcome of educational attainment (1 to 10): "))
pl = float(input("Enter the probability of leisure satisfaction (0 to 1): "))
ol = float(input("Enter the outcome of leisure satisfaction (1 to 10): "))
pp = float(input("Enter the probability of personal growth (0 to 1): "))
op = float(input("Enter the outcome of personal growth (1 to 10): "))

life_outcome = calculate_life_outcome(pc, oc, pr, or_, ph, oh, pf, of, pm, om, pe, oe, pl, ol, pp, op)
print(f'Calculated Life Outcome: {life_outcome}')
