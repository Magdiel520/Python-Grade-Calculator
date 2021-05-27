# Grade Calculator

# 1. Students dictionaries:

# Joao:
joao = {"name": "Joao da Silva",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# Maria:
maria = {"name": "Maria de Souza",
         "assignment": [92, 96, 94, 90],
         "test": [90, 90],
         "lab": [97.90, 98.72]
         }

# Jose:
jose = {"name": "Jose Natalino",
        "assignment": [97, 82, 93, 90],
        "test": [98, 77],
        "lab": [80, 80]
        }

# Camila:
camila = {"name": "Camila Paz",
          "assignment": [87, 72, 63],
          "test": [0, 87],
          "lab": [8, 60]
          }


# Function that calculates average grade
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


# Function that calculates total average grade
def calculate_total_average(students, assignment=None):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])

    # Returns the result based on percentage of grade impact:
    # 10% of marks scored from submission of Assignments;
    # 70% of marks scored from Tests
    # 20% of marks scored in Labs
    return (0.1 * assignment) + (0.7 * test) + (0.2 * lab)


# Letter grade of each student:
def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score <= 69:
        return "D"


# Function to calculate the class average
def class_average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
        return get_average(result_list)


# List of named students:
students = [joao, maria, jose, camila]

# Iterating through the students list and calculating each average mark
# and letter grade:
for i in students:
    print(i["name"])
    print("Average marks of %s is : %s " % (i["name"], calculate_total_average(i)))
    print("Letter Grade of %s is : %s" % (i["name"], assign_letter_grade(calculate_total_average(i))))
    print("=" * 60)
    print()

# Calculating the class average
class_av = class_average_is(students)
print("Class Average is %s" % (class_av))
print("Letter Grade of the class is %s " % (assign_letter_grade(class_av)))
