from django.contrib import admin

from ..models import (
    Certificate,
    Course,
    Exam,
    Lesson,
    LessonLearned,
    Question,
    Register,
    ResultTest,
    Topic,
)
from .course_admin import CourseAdmin
from .exam_admin import ExamAdmin
from .lesson_admin import LessonAdmin
from .question_admin import QuestionAdmin
from .test_result_admin import ResultTestAdmin

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ResultTest, ResultTestAdmin)

admin.site.register(Certificate)
admin.site.register(Topic)

admin.site.register(LessonLearned)
admin.site.register(Register)
