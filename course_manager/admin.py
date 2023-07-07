from django.contrib import admin
from .models import (
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

# Register your models here.
admin.site.register(Certificate)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(ResultTest)
admin.site.register(LessonLearned)
admin.site.register(Register)
