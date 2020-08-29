from data_structures_and_algorithms.Data_Structures.linked_list import LinkedList,Node
import pytest

@pytest.fixture
def data():
    linkedlist=LinkedList()
    return {'linked':linkedlist}

def test_empty_list():
    expected=None
    actual = LinkedList().items()
    assert actual==expected

def test_insert(data):
    expected=3
    data["linked"].insert(5)
    data["linked"].insert(55)
    data["linked"].insert(555)
    actual=data["linked"].items()
    assert actual==expected

def test_multi_insert(data):
    data["linked"].insert(5)
    data["linked"].insert(50)
    data["linked"].insert(13)
    data["linked"].insert(222)
    data["linked"].insert(99)
    expected=" {5}->{50}->{13}->{222}->{99}->NULL"
    actual = data["linked"].to_string()
    assert actual==expected
    
def test_insert_string(data):
    data["linked"].insert(5)
    expected=" {5}->NULL"
    actual=data["linked"].to_string()
    assert actual==expected

def test_includes(data):
    expected=True
    data["linked"].insert(5)
    data["linked"].insert(5)
    actual=data["linked"].includes(5)
    assert actual==expected


