import unittest
import sys, os

from main import *


class TestMain(unittest.TestCase):
    def test_1(self):
        one_to_many = [(l.name, l.memory, la.title)
                       for la in langs
                       for l in libs
                       if l.lang_id == la.id]
        self.assertEqual(B1(one_to_many),[['Matplotlib', 'JavaScript'], ['Maven', 'Java']])

    def test_2(self):
        one_to_many = [(l.name, l.memory, la.title)
                       for la in langs
                       for l in libs
                       if l.lang_id == la.id]
        self.assertEqual(B2(one_to_many),[['C#', 350], ['C++', 481], ['Java', 489], ['C#', 678], ['JavaScript', 754], ['Python', 890]])

    def test_3(self):
        many_to_many_temp = [(la.title, lal.lang_id, lal.lib_id)
                             for la in langs
                             for lal in libs_langs
                             if la.id == lal.lang_id]

        many_to_many = [(l.name, l.memory, lang_title)
                        for lang_title, lang_id, lib_id in many_to_many_temp
                        for l in libs if l.id == lib_id]
        self.assertEqual(B3(many_to_many),[['Leaflet', 'C++'], ['Leaflet', 'Delphi'],
                                           ['Matplotlib', 'JavaScript'], ['Matplotlib', 'Delphi'],
                                           ['Maven', 'Java'], ['Maven', 'Delphi'], ['Pandas', 'Python'],
                                           ['Pandas', 'Delphi'], ['SFML', 'C#'], ['VCL', 'C#'], ['Voca', 'JavaScript']])
