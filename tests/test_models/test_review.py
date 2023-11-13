#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSaveMethod
    TestReviewToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        """Test that Review instantiation works with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the objects."""
        self.assertIn(Review(), models.storage.all().values())

    # (similar changes for other test methods)


class TestReviewSaveMethod(unittest.TestCase):
    """Unittests for testing the save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down the test."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # (similar changes for other test methods)


class TestReviewToDictMethod(unittest.TestCase):
    """Unittests for testing the to_dict method of the Review class."""

    # (similar changes for other test methods)


if __name__ == "__main__":
    unittest.main()
