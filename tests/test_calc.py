from calc import calc

def test_na():
    assert calc.calculate_depth("") == ["null", "null"]

def test_empty():
    assert calc.calculate_depth([]) == ["null", "null"]

def test_values():
    assert calc.calculate_depth([1,[0,[0,2]],3]) == [2,3]
    assert calc.calculate_depth([1,[2,[3,4]],5]) == ["null", "null"]
    assert calc.calculate_depth([1,0,2,0,3]) == [1,1]
    assert calc.calculate_depth([[1,0,0,0]]) == [2,2]
    assert calc.calculate_depth([1,[5,0,2],0,[7,[2,[0],3]],[[0]]]) == [1,4]
