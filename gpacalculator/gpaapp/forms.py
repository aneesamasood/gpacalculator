# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['percentage']

CourseFormSet = inlineformset_factory(parent_model=Course, model=Course, form=CourseForm, extra=1)

