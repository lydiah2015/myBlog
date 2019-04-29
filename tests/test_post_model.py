from app.models import Post
from unittest import TestCase

class TestPostModel(TestCase):
    def setUp(self):
        self.post=Post()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.post,Post)