groupmates = [
    {
        "name": "Александр",
        "surname": "Чернов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Амир",
        "surname": "Хамидулин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 2]
    },
    {
        "name": "Арсений",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Федор",
        "surname": "Пензин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Алексей",
        "surname": "Сайганов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 3, 4]
    }
]




def print_students(students, srznach):
    print(u"Имя".ljust(10), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if sum(student['marks'])/len(student['marks']) > srznach:
            print(student["name"].ljust(10), student["surname"].ljust(10),
                  str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates, float(input()))
