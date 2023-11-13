#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSaveMethod
    TestStateToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        """Test that State instantiation works with no arguments."""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the objects."""
        self.assertIn(State(), models.storage.all().values())

    # (similar changes for other test methods)


class TestStateSaveMethod(unittest.TestCase):
    """Unittests for testing the save method of the State class."""

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


class TestStateToDictMethod(unittest.TestCase):
    """Unittests for testing the to_dict method of the State class."""

    # (similar changes for other test methods)


if __name__ == "__main__":
    unittest.main()
