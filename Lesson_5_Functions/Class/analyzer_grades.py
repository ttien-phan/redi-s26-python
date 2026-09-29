def analyze_grades(*grades):
    average = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)

    result = f"Average: {average}, Highest: {highest}, Lowest: {lowest}"

    return result



print(analyze_grades(15,12,18,10))