def calculateBonus(grade, years):
    if grade == 'A':
        bonus = 2.0
    elif grade == 'B':
        bonus = 1.5
    else:
        bonus = 0.0
        
    if years > 5:
        bonus += 0.5
        
    return f"{bonus} เดือน"

print(calculateBonus('A', 6))