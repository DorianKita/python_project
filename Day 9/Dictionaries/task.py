student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    result = student_scores[key]

    if result >= 91:
        student_grades[key] = "Outstanding"


print(student_grades)