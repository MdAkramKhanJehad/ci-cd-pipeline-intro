from index import multi

def test_multi():
    assert multi(1,2) == 2
    assert multi(1, "asdf") == "Invalid Input"
