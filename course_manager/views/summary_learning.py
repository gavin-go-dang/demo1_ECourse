from django.db.models import Count, F, FloatField, OuterRef, Subquery, Sum
from django.db.models.functions import Coalesce, Round
from django.views.generic import TemplateView

from common.views import LoginRequired
from course_manager.models import Lesson, LessonLearned, Register, Course

# Create your views here.


class SummaryLearning(LoginRequired, TemplateView):
    template_name = "summary.html"

    def get_context_data(self, **kwargs):
        context = super(SummaryLearning, self).get_context_data(**kwargs)

        courses = (
            Register.objects.filter(student=self.request.user)
            .select_related("course")
            .prefetch_related("course")
            .values("course", "course__name_course")
        )

        total_lessons = (
            Lesson.objects.filter(course_id__in=courses.values("course"))
            .values("course")
            .annotate(total_lessons=Count("id"))
            .values("course", "total_lessons")
        )

        completed_lessons = (
            LessonLearned.objects.filter(student=self.request.user)
            .values("lesson__course")
            .annotate(completed_lessons=Count("id"))
            .values("lesson__course", "completed_lessons")
        )

        course_completion_rate = (
            total_lessons.annotate(
                name_course=F("course__name_course"),
                completed_lessons=Coalesce(
                    Subquery(
                        completed_lessons.filter(
                            lesson__course_id=OuterRef("course")
                        ).values("completed_lessons")[:1]
                    ),
                    0,
                ),
            )
            .annotate(
                course_completion_rate=Round(
                    F("completed_lessons") * 100.0 / F("total_lessons"), 2
                )
            )
            .values("name_course", "course_completion_rate")
        )
        breakpoint()
        context["courses"] = course_completion_rate
        return context
