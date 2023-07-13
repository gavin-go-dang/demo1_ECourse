from django.contrib import admin
from ..models import (
    Certificate,
    Lesson,
    Course,
    Topic,
    Exam,
    Question,
    ResultTest,
    LessonLearned,
    Register,
)

from .courseAdmin import CourseAdmin
from .lessonAdmin import LessonAdmin
from .examAdmin import ExamAdmin
from .questionAdmin import QuestionAdmin


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.register(Certificate)
admin.site.register(Topic)
admin.site.register(ResultTest)
admin.site.register(LessonLearned)
admin.site.register(Register)
