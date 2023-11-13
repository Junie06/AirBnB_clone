#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSaveMethod
    TestPlaceToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test that Place instantiation works with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the objects."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that id is a public attribute and of type string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at is a public attribute and of type datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that updated_at is a public attribute and of type datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    # (similar changes for other test methods)


class TestPlaceSaveMethod(unittest.TestCase):
    """Unittests for testing the save method of the Place class."""

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


class TestPlaceToDictMethod(unittest.TestCase):
    """Unittests for testing the to_dict method of the Place class."""

    # (similar changes for other test methods)


if __name__ == "__main__":
    unittest.main()
