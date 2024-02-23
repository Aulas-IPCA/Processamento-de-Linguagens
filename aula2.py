students : list = [
    {
        "student_id" : 123123213,
        "student_name" : "Joseph",
        "student_grade" : 18
    },
    {
        "student_id" : 123,
        "student_name" : "Anna",
        "student_grade" : 11
    },
    {
        "student_id" : 1,
        "student_name" : "Tom",
        "student_grade" : 15
    }
]

def my_function(id : int, uc : str = "VC") -> (int, str) : # type: ignore
    for student in students:
        if student["student_id"] == id:

            grade : int = student["student_grade"]
            name : str = student["student_name"]

            print(f"{name} has {grade} values in the uc {uc}.")

            return grade

result : int = my_function(1, "PL")
print(f"Result = {result}")