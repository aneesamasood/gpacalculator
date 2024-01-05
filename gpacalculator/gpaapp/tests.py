# gpaapp/tests.py
from django.test import TestCase
from .models import Course

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            name='Math 101',
            grade=90.0,
            current_gpa=3.5,
            target_gpa=4.0,
            gpa_scale=4.0
        )
        self.assertEqual(course.name, 'Math 101')
        self.assertEqual(course.grade, 90.0)
        self.assertEqual(course.current_gpa, 3.5)
        self.assertEqual(course.target_gpa, 4.0)
        self.assertEqual(course.gpa_scale, 4.0)

