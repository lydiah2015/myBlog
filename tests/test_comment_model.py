from app.models import Comment
from unittest import TestCase

class TestCommentModel(TestCase):
    def setUp(self):
        self.comment=Comment()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.comment,Comment)