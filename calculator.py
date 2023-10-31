def calculate_score(severity, fidelity, coverage, actionability, relevancy):
    weight = {
        'Severity': 1,
        'Fidelity': 1,
        'Coverage': 1,
        'Actionability': 1,
        'Relevancy': 1
    }

    total_weight = sum(weight.values())
  
    score = (weight['Severity'] * severity + 
             weight['Fidelity'] * fidelity + 
             weight['Coverage'] * coverage + 
             weight['Actionability'] * actionability +
             weight['Relevancy'] * relevancy) / total_weight
  
    return round(score, 2)

def categorize_score(score):
    if score >= 8:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"

severity = float(input("Enter Severity score (0-10). This reflects how impactful the event is: "))
fidelity = float(input("Enter Fidelity score (0-10). This reflects how accurate the detection is: "))
coverage = float(input("Enter Coverage score (0-10). This reflects how much of the environment is monitored: "))
actionability = float(input("Enter Actionability score (0-10). This reflects how actionable the alert data is: "))
relevancy = float(input("Enter Relevancy score (0-10). This reflects how relevant the event is to your specific environment: "))

final_score = calculate_score(severity, fidelity, coverage, actionability, relevancy)
category = categorize_score(final_score)

print(f"The SIEM rule score is: {final_score}")
print(f"The SIEM rule is categorized as {category} severity.")
