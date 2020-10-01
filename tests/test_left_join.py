from left_join.left_join import left_join

def test_1():
    dict1 = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'garb',
        'guide':'usher'
        }


    dict2 = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
        }
    expected=[['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', "NULL"], ['guide', 'usher', 'follow']]
    actual= left_join(dict1,dict2)
    assert expected == actual


def test_2():
    
    dict1 = {
        'child':'kid',
        'hello':'welcome',
        }

    dict2 = {
        'child':'old',
        'sun':'moon',
   }
    expected =[['child', 'kid', 'old'], ['hello', 'welcome', "NULL"]]
    actual = left_join(dict1,dict2)
    assert expected == actual

def test_3():
    dict1 = {
        'kid':'child',
        'sun':'moon',
        }

    dict2 = {
    'hello':'welcome',
   }
    expected = [["kid","child","NULL"], ['sun', 'moon', "NULL"]]
    actual = left_join(dict1,dict2)
    assert expected == actual


def test_4():
    dict1 = {}

    dict2 = {
    'sun':'moon',
   }
    expected=[]
    actual= left_join(dict1,dict2)
    assert expected==actual