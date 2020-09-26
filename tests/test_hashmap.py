from hashtable.hashtable import HashMap,Node,LinkedList

def test_hashtable_hash():
    hm = HashMap()
    actual = hm.hash("1")
    expected = 931
    assert actual == expected

def test_hashtable_add():
    hm = HashMap()
    hm.add("1", "sachin")
    actual = hm.get("1")
    expected = "sachin"
    assert actual == expected

def test_hashtable_get():
    hm = HashMap()
    actual = hm.add("1", "sachin")
    expected = True
    assert actual == expected
