from mypackage import myModule

def test_top_n():
    '''
    Maked sure top_n works correctly

    '''
    '''assert means giving it a few test cases and giving it the answer
    and making sure that it does the right thing or comes out with the right expected
    thing.'''

    assert myModule.top_n([8,3,27,4], 3) == [8,7,4] 'incorrect'
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'
