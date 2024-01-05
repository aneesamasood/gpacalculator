from django.shortcuts import render
from django.forms import formset_factory
from .forms import CourseFormSet
from .forms import CourseForm

def percentage_to_gpa(percentage):
    # Round the percentage before checking the ranges
    rounded_percentage = round(percentage)

    if 90 <= rounded_percentage <= 100:
        return 4.33
    elif 85 <= rounded_percentage <= 89:
        return 4.00
    elif 80 <= rounded_percentage <= 84:
        return 3.67
    elif 77 <= rounded_percentage <= 79:
        return 3.33
    elif 73 <= rounded_percentage <= 76:
        return 3.00
    elif 70 <= rounded_percentage <= 72:
        return 2.67
    elif 67 <= rounded_percentage <= 69:
        return 2.33
    elif 63 <= rounded_percentage <= 66:
        return 2.00
    elif 60 <= rounded_percentage <= 62:
        return 1.67
    elif 57 <= rounded_percentage <= 59:
        return 1.33
    elif 53 <= rounded_percentage <= 56:
        return 1.00
    elif 50 <= rounded_percentage <= 52:
        return 0.67
    else:
        return 0.00
def calculate_gpa(request):
    CourseFormSet = formset_factory(CourseForm, extra=1)
    formset = CourseFormSet(request.POST or None, prefix='course')
    term_gpa = 0
    cumulative_gpa = 0

    if request.method == 'POST':
        if formset.is_valid():
            percentages = [form.cleaned_data.get('percentage') for form in formset]
            gpas = [percentage_to_gpa(percentage) for percentage in percentages]

            total_gpa = sum(gpas)
            num_courses = len(gpas)

            term_gpa = total_gpa / num_courses

            current_gpa = float(request.POST.get('current_gpa'))
            total_credits = float(request.POST.get('total_credits'))

            cumulative_gpa = (current_gpa * total_credits + term_gpa * num_courses) / (total_credits + num_courses)
            cumulative_gpa = round(cumulative_gpa, 2)  # Round the cumulative GPA

    print("Rendering template with term_gpa:", term_gpa, "and cumulative_gpa:", cumulative_gpa)
    return render(request, 'calculate_gpa.html', {'formset': formset, 'term_gpa': term_gpa, 'cumulative_gpa': cumulative_gpa})

