#!/usr/bin/python3
import unittest
import console
from console import HBNBCommand

class test_console(unittest.TestCase):
    """Class to test the console methods"""
    
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = console
        self.value = console

    def test_create(self):
        console = HBNBCommand()
        result = console.onecmd("create Place name='Awesome place' city='San Francisco'")
        self.assertIn("Awesome place", result)
        
    def test_show(self):
        console = HBNBCommand()
        console.onecmd("create User email='test@test.com' password='test'")
        result = console.onecmd("show User 1")
        self.assertIn("test@test.com", result)
        
    def test_destroy(self):
        console = HBNBCommand()
        console.onecmd("create State name='California'")
        result = console.onecmd("destroy State 1")
        self.assertEqual("", result.strip())
        
    def test_all(self):
        console = HBNBCommand()
        console.onecmd("create Place name='Awesome place' city='San Francisco'")
        console.onecmd("create Place name='Amazing place' city='New York'")
        result = console.onecmd("all Place")
        self.assertIn("Awesome place", result)
        self.assertIn("Amazing place", result)
        
    def test_update(self):
        console = HBNBCommand()
        console.onecmd("create User email='test@test.com' password='test'")
        result = console.onecmd("update User 1 email 'new@test.com'")
        self.assertEqual("", result.strip())
        result = console.onecmd("show User 1")
        self.assertIn("new@test.com", result)
