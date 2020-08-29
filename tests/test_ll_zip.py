from data_structures_and_algorithm.challenge.ll_zip.ll_zip import ( zip_list,LinkedList,Node,)


def test_zip_list():
    list1= LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    list2= LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)
    list1.zip_list(list2)
    assert list1== [1, 5, 3, 9, 2, 4]