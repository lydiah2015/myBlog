from app import create_app
from flask import Flask
from unittest import TestCase

class TestFlaskObject(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isinstance(self):
        app=create_app("test")
        self.assertIsInstance(app,Flask)

    