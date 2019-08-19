from django.test import TestCase
from apps.task_test.models import CityAreaModel
from django.utils.translation import gettext_lazy

__all__ = ('TestCityAreaModelsCase', )


class TestCityAreaModelsCase(TestCase):
    """
    Первый тест для данного приложения
    """

    @classmethod
    def setUpClass(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        CityAreaModel.objects.create(title='Some City Area or Disctrict')
        return super(TestCityAreaModelsCase, cls).setUpClass()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_title_verbose_name(self):
        """
        проверка - в качестве verbose_name задаётся функция gettext_lazy - для дальнейшего перевода
        :return: True - именно она, иначе - False
        """
        area = CityAreaModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertTrue(type(title.verbose_name), gettext_lazy)

    def test_title_max_length(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        area = CityAreaModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertEqual(title.max_length, 255)

    def test_title_unique(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        area = CityAreaModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertTrue(title.unique)

    def test_title_blank(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        area = CityAreaModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertFalse(title.blank)

    def test_title_null(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        area = CityAreaModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertFalse(title.null)
