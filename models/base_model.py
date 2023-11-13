#!/usr/bin/python3
"""
Defines the BaseModel class, serving as the base for all models.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for various classes within the application.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance or deserializes a serialized one.

        If no arguments are provided, it initializes a new
        instance with a unique ID,
        creation time, and last update time.

        If keyword arguments are provided, it deserializes the instance
        based on those arguments.
        """

        # initialize if nothing is passed
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # using key words (deserialize)
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = value
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """
        Overrides the string representation of the instance.
        """
        pattern = "[{}] ({}) {}"
        return pattern.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' variable and saves the instance.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """
        Retrieves all current instances of the class.
        """
        return models.storage.find_all_instances(cls.__name__)

    @classmethod
    def create(cls, *args, **kwargs):
        """
        creates an instance of the class and returns its ID.
        """
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def count(cls):
        """
        Gets the number of all current instances of the class.
        """
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def show(cls, inst_id):
        """
        Retrieves an instance by its ID.
        """
        return models.storage.find_instance_by_id(
                cls.__name__,
                inst_id
                )

    @classmethod
    def destroy(cls, inst_id):
        """
        Deletes an instance by its ID.
        """
        return models.storage.delete_instance_by_id(
                cls.__name__,
                inst_id
                )

    @classmethod
    def update(cls, inst_id, *args):
        """
        Updates an instance based on provided arguments.

        If 'args' has one element and it is a dictionary,
        it updates by key-value pairs.

        Otherwise, it updates using the first two elements of 'args'
        as key and value respectively.
        """
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                    cls.__name__,
                    inst_id,
                    *arg
                    )
