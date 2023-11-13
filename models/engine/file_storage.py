#!/usr/bin/python3
"""
Defines the storage system (File System) for the project.
It utilizes JSON format for object serialization and deserialization.
"""

import json
from json.decoder import JSONDecodeError
from models.engine.error_file import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    This class serves as an Object-Relational Mapping to
    interface with our storage system.
    """

    # class private variables
    __objects: dict = {}
    __file_path: str = "file.json"
    models = (
            "BaseModel",
            "User", "City", "State", "Place",
            "Amenity", "Review"
            )

    def __init__(self):
        """
        Constructor for the FileStorage class.
        """
        pass

    def all(self):
        """Returns all instances stored"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Stores a new object in the storage system.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects stored and persists them in the file.
        """
        serialized = {
                key: value.to_dict()
                for key, value in self.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """De-serialize persisted objects"""
        try:
            deserialized = {}
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                    key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialized.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass

    def find_instance_by_id(self, model, obj_id):
        """Finds and returns an element of a model by its id"""
        f_storage = FileStorage
        if model not in f_storage.models:
            raise NotFoundModelError(model)

        key = model + "." + obj_id
        if key not in f_storage.__objects:
            raise NotFoundInstanceError(obj_id, model)

        return f_storage.__objects[key]

    def delete_instance_by_id(self, model, obj_id):
        """
        Deletes an instance of a model based on its ID.
        """
        f_storage = FileStorage
        if model not in f_storage.models:
            raise NotFoundModelError(model)

        key = model + "." + obj_id
        if key not in f_storage.__objects:
            raise NotFoundInstanceError(obj_id, model)

        del f_storage.__objects[key]
        self.save()

    def find_all_instances(self, model=""):
        """
        Finds all instances or instances of a specific model.
        """
        if model and model not in FileStorage.models:
            raise NotFoundModelError(model)
        outcome = []
        for key, value in FileStorage.__objects.items():
            if key.startswith(model):
                outcome.append(str(value))
        return outcome

    def update_instance(self, model, instance_id, data_mem, value):
        """
        Updates an instance based on provided arguments.
        """
        f_storage = FileStorage
        if model not in f_storage.models:
            raise NotFoundModelError(model)

        key = model + "." + instance_id
        if key not in f_storage.__objects:
            raise NotFoundInstanceError(instance_id, model)
        if data_mem in ("id", "updated_at", "created_at"):
            return
        inst = f_storage.__objects[key]
        try:
            # if an instance has that value
            # cast it to its type
            value_type = type(inst.__dict__[data_mem])
            inst.__dict__[data_mem] = value_type(value)
        except KeyError:
            # if an instance doesn't has the data_mem
            # assign the value with its type
            inst.__dict__[data_mem] = value
        finally:
            inst.updated_at = datetime.utcnow()
            self.save()
