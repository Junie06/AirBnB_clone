#!/usr/bin/python3
"""
Test suite for console
"""
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    def test_help_command(self):
        """Test the 'help' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
        self.assertEqual('Prints the string representation of an '
                         'instance based on the class name and id.\n', output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
        self.assertEqual('Creates a new instance of a given class, '
                         'saves it (to the JSON file) and prints the id.\n', output.getvalue())

    def test_create_command(self):
        """Test the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        self.assertIsInstance(output.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
        self.assertEqual(output.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')

    def test_show_command(self):
        """Test the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
        self.assertEqual(output.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(output.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel 1111")
        self.assertEqual(output.getvalue(), '** no instance found **\n')

    def test_destroy_command(self):
        """Test the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(output.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(output.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel 1111")
        self.assertEqual(output.getvalue(), '** no instance found **\n')

    def test_all_command(self):
        """Test the 'all' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
        self.assertIsInstance(output.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
        self.assertIsInstance(output.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')

    def test_update_command(self):
        """Test the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
        self.assertEqual(output.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(output.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel 1111")
        self.assertEqual(output.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        model_id = output.getvalue()
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"update BaseModel {model_id}")
        self.assertEqual(output.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"update BaseModel {model_id} first")
        self.assertEqual(output.getvalue(), '** value missing **\n')

    def test_quit_command(self):
        """Test the 'quit' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("quit")
        self.assertEqual(output.getvalue(), '')

def test_EOF_command(self):
    """Test the 'EOF' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("EOF")
    self.assertEqual(output.getvalue(), '\n')

def test_emptyline_command(self):
    """Test the 'emptyline' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("")
    self.assertEqual(output.getvalue(), '')

def test_BaseModel_all_command(self):
    """Test the 'BaseModel.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.all()")
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.all")
    self.assertIn('**', output.getvalue())

def test_Review_all_command(self):
    """Test the 'Review.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[User]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.all")
    self.assertIn('**', output.getvalue())

def test_User_all_command(self):
    """Test the 'User.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.all")
    self.assertIn('**', output.getvalue())

def test_State_all_command(self):
    """Test the 'State.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    self.assertNotIn('[User]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.all")
    self.assertIn('***', output.getvalue())

def test_Place_all_command(self):
    """Test the 'Place.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    self.assertNotIn('[User]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.all")
    self.assertIn('**', output.getvalue())

def test_Amenity_all_command(self):
    """Test the 'Amenity.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[City]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    self.assertNotIn('[User]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.all")
    self.assertIn('**', output.getvalue())

def test_City_all_command(self):
    """Test the 'City.all()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.all()")
    self.assertNotIn('[BaseModel]', output.getvalue())
    self.assertNotIn('[State]', output.getvalue())
    self.assertNotIn('[Review]', output.getvalue())
    self.assertNotIn('[Place]', output.getvalue())
    self.assertNotIn('[Amenity]', output.getvalue())
    self.assertNotIn('[User]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.all")
    self.assertIn('**', output.getvalue())

def test_BaseModel_count_command(self):
    """Test the 'BaseModel.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_User_count_command(self):
    """Test the 'User.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_State_count_command(self):
    """Test the 'State.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_Place_count_command(self):
    """Test the 'Place.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_City_count_command(self):
    """Test the 'City.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_Amenity_count_command(self):
    """Test the 'Amenity.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_Review_count_command(self):
    """Test the 'Review.count()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.count()")
    self.assertIsInstance(int(output.getvalue().strip()), int)

def test_BaseModel_show_command(self):
    """Test the 'BaseModel.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create BaseModel")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.show({model_id})")
    self.assertIn('[BaseModel]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_User_show_command(self):
    """Test the 'User.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create User")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.show({model_id})")
    self.assertIn('[User]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_City_show_command(self):
    """Test the 'City.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create City")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.show({model_id})")
    self.assertIn('[City]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_State_show_command(self):
    """Test the 'State.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create State")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.show({model_id})")
    self.assertIn('[State]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_Place_show_command(self):
    """Test the 'Place.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Place")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.show({model_id})")
    self.assertIn('[Place]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_Amenity_show_command(self):
    """Test the 'Amenity.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Amenity")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.show({model_id})")
    self.assertIn('[Amenity]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_Review_show_command(self):
    """Test the 'Review.show()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.show()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Review")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.show({model_id})")
    self.assertIn('[Review]', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.show(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_Review_destroy_command(self):
    """Test the 'Review.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Review")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_BaseModel_destroy_command(self):
    """Test the 'BaseModel.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create BaseModel")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_User_destroy_command(self):
    """Test the 'User.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create User")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_Place_destroy_command(self):
    """Test the 'Place.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Place")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_destroy_state_command(self):
    """Test the 'State.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create State")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_destroy_city_command(self):
    """Test the 'City.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create City")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_destroy_amenity_command(self):
    """Test the 'Amenity.destroy()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.destroy()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Amenity")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.destroy({model_id})")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.show({model_id})")
    self.assertEqual(output.getvalue(), '** no instance found **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.destroy(idf)")
    self.assertEqual(output.getvalue(), '** no instance found **\n')

def test_update_base_model_command(self):
    """Test the 'BaseModel.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("BaseModel.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create BaseModel")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"BaseModel.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_user_command(self):
    """Test the 'User.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("User.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create User")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"User.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_place_command(self):
    """Test the 'Place.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Place.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Place")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Place.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_state_command(self):
    """Test the 'State.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("State.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create State")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"State.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_city_command(self):
    """Test the 'City.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("City.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create City")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"City.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_amenity_command(self):
    """Test the 'Amenity.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Amenity.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Amenity")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Amenity.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())

def test_update_review_command(self):
    """Test the 'Review.update()' command."""
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.update()")
    self.assertEqual(output.getvalue(), '** instance id missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("Review.update(1111)")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd("create Review")
    model_id = output.getvalue().strip()
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.update({model_id})")
    self.assertEqual(output.getvalue(), '** attribute name missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.update({model_id}, first)")
    self.assertEqual(output.getvalue(), '** value missing **\n')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.update({model_id}, first, 3)")
    self.assertEqual(output.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.show({model_id})")
    self.assertIn('first', output.getvalue())
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.update({model_id},{{'second': 5, 'third': three}})")
    with patch('sys.stdout', new=StringIO()) as output:
        HBNBCommand().onecmd(f"Review.show({model_id})")
    self.assertIn('third', output.getvalue())
    self.assertIn('second', output.getvalue())
