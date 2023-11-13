#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSaveMethod
    TestUserToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Test that User instantiation works with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the objects."""
        self.assertIn(User(), models.storage.all().values())

    # (similar changes for other test methods)


class TestUserSaveMethod(unittest.TestCase):
    """Unittests for testing the save method of the User class."""

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


class TestUserToDictMethod(unittest.TestCase):
    """Unittests for testing the to_dict method of the User class."""

    # (similar changes for other test methods)


if __name__ == "__main__":
    unittest.main()
