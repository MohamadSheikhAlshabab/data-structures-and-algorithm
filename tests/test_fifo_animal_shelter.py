from data_structures_and_algorithm.challenge.fifo_animal_shelter.fifo_animal_shelter import Queue,Animal_Shelter,Dog,Cat
import pytest

def test_Happy_path_cats_enqueue():
        shelter=Animal_Shelter()
        shelter.enqueue('sherry','cat')
        shelter.enqueue('lolo','cat')       
        actual = shelter.cats.__str__()
        expected = '<sherry-><lolo->None'
        assert actual == expected



def test_Happy_path_dogs_enqueue():
        shelter=Animal_Shelter()
        shelter.enqueue('poppy','dog')
        shelter.enqueue('matrix','dog')
        actual = shelter.dogs.__str__()
        expected = '<poppy-><matrix->None'
        assert actual == expected


def test_Happy_path_dogs_dequeue():
        shelter=Animal_Shelter()
        shelter.enqueue('matrix','dog')
        shelter.enqueue('hunter','dog')
        actual = shelter.dequeue('dog')
        expected = 'matrix'
        assert actual == expected
        


def test_Happy_path_cats_dequeue():
        shelter=Animal_Shelter()
        shelter.enqueue('sherry','cat')
        shelter.enqueue('lolo','cat')
        actual = shelter.dequeue('cat')
        expected = 'sherry'
        assert actual == expected


def test_fail_capital_letter_dequeue():
        shelter=Animal_Shelter()
        shelter.enqueue('lolo','CAT')
        shelter.enqueue('blacky','CAT')
        actual = shelter.dequeue('CAT')
        expected = 'lolo'
        assert actual == expected



def test_fail_capital_letter_dequeue():
        shelter=Animal_Shelter()
        shelter.enqueue('matrix','DOG')
        shelter.enqueue('max','DOG')
        actual = shelter.dequeue('DOG')
        expected = 'matrix'
        assert actual == expected


def test_edge_case_new_type():
        shelter=Animal_Shelter()
        shelter.enqueue('max','DOG')
        shelter.enqueue('lolo','CAT')
        actual = shelter.dequeue('mouse')
        expected = None
        assert actual == expected