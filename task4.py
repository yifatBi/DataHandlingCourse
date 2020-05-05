# 1
def range_dict(a, b):
    return {str(i): [i] for i in range(a, b + 1)}


# 2
def list_to_last_letter_map(str_list):
    dictionary = {}
    for word in str_list:
        current_key = word[:1]
        dictionary[current_key] = (dictionary.get(current_key) or []) + [word[1:]]
    return dictionary


# 3
def most_common_value_in_dict(d):
    values = list(d.values())
    return max(set(values), key=values.count)


# 4
def swap_student_courses(name_to_courses):
    course_with_students = {}
    for student, courses in name_to_courses.items():
        for course in courses:
            course_with_students[course] = (course_with_students.get(course) or []) + [student]
    return course_with_students
