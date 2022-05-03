from audioop import reverse
from operator import index


def areAlmostEqual(s1, s2):
    if s1 == s2:
        print("true")
        return True
    s1_list = []
    s2_list = []
    for count, number in enumerate(s1):
        if s1[count] != s2[count]:
            print(f"s1 = {s1[count]}, s2= {s2[count]}")
            s1_list.append(s1[count])
            s2_list.append(s2[count])
            print(s1_list, s2_list)

    if len(s1_list) > 2 or len(s2_list) > 2:
        print("False")
        return False
    else: 
        s1_list.reverse()
        if s1_list == s2_list:
            print("true")
            return True
        else:
            print("false")
            return False


areAlmostEqual("attack", "defend")