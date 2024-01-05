# gpaapp/utils.py
def calculate_grade_points(percentage):
    # Add your specific grading scale logic here
    if 90 <= percentage <= 100:
        return 4.33
    elif 85 <= percentage < 90:
        return 4.00
    elif 80 <= percentage < 85:
        return 3.67
    elif 75 <= percentage < 80:
        return 3.33
    elif 70 <= percentage < 75:
        return 3.00
    elif 65 <= percentage < 70:
        return 2.67
    elif 60 <= percentage < 65:
        return 2.33
    elif 50 <= percentage < 60:
        return 2.00
    else:
        return 0.0

