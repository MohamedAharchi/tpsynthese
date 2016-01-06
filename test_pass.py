# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abczz"), "abdaa")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getNextLenght(self):
        password = "aaaaa"
        self.assertEqual(len(pwd.getNext(password), len(password))

# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
