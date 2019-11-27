from django.test import TestCase
from .models import Product, Category
from datetime import datetime
from django.utils import timezone

# Tests for CRUD operations


class ProductTestCase(TestCase):
    def setUp(self):
        """Setting up the database"""
        Category.objects.create(title="test items")
        Product.objects.create(
            name="Lumber Wood",
            description="Purple Heart 4/4 Project Pack: 20 Board Feet of Lumber",
            company_name="go2people",
            school_type="praktijkonderwijs",
            price=80.2,
            expiration_date=datetime.now(tz=timezone.utc),
        )

    def test_create_product(self):
        """Testing that we have successfully created one product"""
        products_count = Product.objects.all().count()
        self.assertEqual(products_count, 1)

    def test_read_product(self):
        """Testing that we are getting the right product"""
        wood = Product.objects.get(name="Lumber Wood")
        self.assertEqual(wood.name, "Lumber Wood")
        self.assertEqual(
            wood.description, "Purple Heart 4/4 Project Pack: 20 Board Feet of Lumber"
        )
        self.assertEqual(wood.company_name, "go2people")
        self.assertEqual(wood.school_type, "praktijkonderwijs")
        self.assertEqual(wood.price, 80.2)

    def test_update_product(self):
        """Testing that we can successfully edit product"""
        wood = Product.objects.get(name="Lumber Wood")
        wood.name = "Walnut Wood"
        self.assertEqual(wood.name, "Walnut Wood")

    def test_delete_product(self):
        """Testing that we can successfully delete product"""
        wood = Product.objects.get(name="Lumber Wood").delete()
        products_count = Product.objects.all().count()
        self.assertEqual(products_count, 0)

    def test_create_category(self):
        """Testing that we have successfully created one category"""
        categories_count = Category.objects.all().count()
        self.assertEqual(categories_count, 1)

    def test_read_category(self):
        """Testing that we are getting the right category"""
        test_category = Category.objects.get(title="test items")
        self.assertEqual(test_category.title, "test items")

    def test_update_category(self):
        """Testing that we can successfully edit category"""
        test_category = Category.objects.get(title="test items")
        test_category.title = "real items"
        self.assertEqual(test_category.title, "real items")

    def test_delete_category(self):
        """Testing that we can successfully delete category"""
        test_category = Category.objects.get(title="test items").delete()
        categories_count = Category.objects.all().count()
        self.assertEqual(categories_count, 0)
