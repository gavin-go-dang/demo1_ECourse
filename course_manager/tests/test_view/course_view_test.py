from django.test import TestCase, Client
from authen.models import User
from course_manager.models import Topic, Course
from django.urls import reverse
from ..factories import TopicFactory, CourseFactory
from factory.django import DjangoModelFactory
from faker import Faker

fake = Faker()


class CourseViewTest(TestCase):
    fixtures = ["data_sample.json"]

    course_data = CourseFactory.build(
        name_course="Subject A1",
        description=fake.text(),
        topic=TopicFactory.create(),
    )

    def setUp(self):
        self.client = Client()
        self.course_url = reverse("course")

    def test_course_view_get(self):
        response = self.client.get(self.course_url, follow=True)
        self.assertEqual(response.status_code, 200)


import io
from django.test import TestCase, RequestFactory
from authen.models import User
from course_manager.views import ListCourse


class ListCourseTestCase(TestCase):
    fixtures = ["data_sample.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

    def test_get_request(self):
        request = self.factory.get("course")
        request.user = self.user

        response = ListCourse.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_get_request_with_query(self):
        request = self.factory.get("course", {"query": "Web"})
        request.user = self.user

        response = ListCourse.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Web Front-end")
