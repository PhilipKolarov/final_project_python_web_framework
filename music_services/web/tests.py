from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from music_services.web.models import Recommendation
from music_services.web.utils import calc_avg_review_score, return_valid_avg_score

UserModel = get_user_model()


class ViewsTests(TestCase):
    def test_getCatalogue_shouldRenderTemplate(self):
        response = self.client.get(reverse('catalogue'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/catalogue.html')

    def test_getServiceCreate_shouldRenderTemplateWhenLoggedIn(self):
        credentials = {
            'username': 'Jo1000',
            'email': 'jo@c.om',
            'password': 'Mp01s9den'
        }

        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.get(reverse('service create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service/service-create.html')

    def test_getServiceCreate_shouldNotRenderTemplateWhenNotLoggedIn(self):
        response = self.client.get(reverse('service create'))
        self.assertEqual(response.status_code, 302)

    def test_getAnnouncementCreate_shouldNotRenderTemplateIfNotStaff(self):
        credentials = {
            'username': 'Jo1000',
            'email': 'jo@c.om',
            'password': 'Mp01s9den'
        }

        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.get(reverse('announcement create'))
        self.assertTemplateUsed(response, '403-forbidden-access.html')


class UtilsTests(TestCase):
    def test_returnValidAverageScore_shouldReturnAccurateAnswer(self):
        total_score = 10
        score_count = 2
        average = total_score/score_count

        result = return_valid_avg_score(total_score, score_count)
        self.assertEqual(result, average)
