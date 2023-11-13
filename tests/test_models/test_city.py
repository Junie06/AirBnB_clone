#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCityInstantiation
    TestCitySaveMethod
    TestCityToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test that City instantiation works with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the objects."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that id is a public attribute and of type string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at is a public attribute and of type datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that updated_at is a public attribute and of type datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test that state_id is a public class attribute and of type string."""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test that name is a public class attribute and of type string."""
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        """Test that two cities have unique ids."""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """Test that two cities have different created_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test that two cities have different updated_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a City instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        """Test that City instantiation ignores unused arguments."""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that City instantiation works with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that City instantiation with None kwargs raises TypeError."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySaveMethod(unittest.TestCase):
    """Unittests for testing the save method of the City class."""

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


class TestCityToDictMethod(unittest.TestCase):
    """Unittests for testing the to_dict method of the City class."""

    # (similar changes for other test methods)


if __name__ == "__main__":
    unittest.main()
