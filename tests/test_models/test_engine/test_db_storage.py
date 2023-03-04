#!/usr/bin/python3

"""
This module contains the TestDBStorageDocs and TestDBStorage classes,
which test the DBStorage class in models/engine/db_storage.py.
"""

import json
import os
import inspect
import unittest
import pep8
from datetime import datetime

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine import db_storage

# Define classes
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDatabaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Database classes"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test that tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DatabaseStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DatabaseStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DatabaseStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DatabaseStorage methods"""
        for func in self.dbs_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDatabaseStorage(unittest.TestCase):
    """Test the DatabaseStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing database storage")
    def test_all_returns_dictionary(self):
        """Test that all() method returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing database storage")
    def test_all_no_class(self):
        """Test that all() method returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing database storage")
    def test_new(self):
        """Test that new() method adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "Not testing db storage")
    def test_save(self):
        """"""
