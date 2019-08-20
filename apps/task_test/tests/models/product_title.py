from django.test import TestCase
from apps.task_test.models import ProductTitleModel
from django.utils.translation import gettext_lazy

__all__ = ('ProductTitleModelsCase', )


class ProductTitleModelsCase(TestCase):
    """
    Первый тест для данного приложения
    """
    title = None

    @classmethod
    def setUpClass(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        ProductTitleModel.objects.create(title="Some Test Area")
        return super(ProductTitleModelsCase, cls).setUpClass()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        some_area = ProductTitleModel.objects.all().first()
        self.title = some_area._meta.get_field('title')
        print(self.title)
        pass

    def test_title_verbose_name(self):
        """
        проверка - в качестве verbose_name задаётся функция gettext_lazy - для дальнейшего перевода
        :return: True - именно она, иначе - False
        """
        # area = ProductTitleModel.objects.all().first()
        print(self.title)
        self.assertTrue(type(self.title.verbose_name), gettext_lazy)

    def test_title_max_length(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        area = ProductTitleModel.objects.all().first()
        title = area._meta.get_field('title')
        self.assertEqual(self.title.max_length, 255)

    def test_title_unique(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        self.assertTrue(self.title.unique)

    def test_title_blank(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        self.assertFalse(self.title.blank)

    def test_title_null(self):
        """
        проверка максимальной длительности названия района, а именно 255
        :return:
        """
        self.assertFalse(self.title.null)

    def test_model_str(self):
        """
        Проверка содержимого строки
        :return:
        """
        area = ProductTitleModel.objects.all().first()
        self.assertEqual(str(area), area.title)
