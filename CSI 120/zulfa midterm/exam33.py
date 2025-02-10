# Prompt the user to enter their exam score
score_input = input("Enter your exam score (0-100): ")
score = int(score_input)
    
# Check if the score is within the valid range
if 0 <= score <= 100:
        if 90 <= score <= 100:
            grade = "A - Excellent!"
        elif 80 <= score <= 89:
            grade = "B - Good job!"
        elif 70 <= score <= 79:
            grade = "C - You Passed!"
        elif 60 <= score <= 69:
            grade = "D - Needs improvement!"
        elif 0 <= score < 60:
            grade = "F - Failed. Try again!"
else:
        grade = "Invalid input. Please enter a score between 0 and 100."

print(grade)
