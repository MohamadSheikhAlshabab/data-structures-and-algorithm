def left_join(d1,d2):
    """
    The LEFT JOIN keyword returns all records from the left table (table1),
    and the matched records from the right table (table2).
    The result is NULL from the right side, if there is no match

    """
    try:
        output = []
        for key in d1.keys():
            if key in d2.keys():
                output.append([key,d1[key],d2[key]])
            else:
                output.append([key,d1[key],'NULL'])
        return output
    except Exception as err:
        print(f"There is an error in left_join function\n, {err}")

d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher','hello':'everyone'}
d2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
print(left_join(d1,d2))