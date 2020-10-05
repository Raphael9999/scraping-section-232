# manipulate path to work dir
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import yaml

from mine232 import ExclusionRequest
from mine232 import ERTag

def test_notfound():
    """ID is a numerical"""
    my_er = ExclusionRequest(9999999)
    assert my_er.id == 9999999
    assert my_er.error

def test_tag_value():
    """ID is a numerical"""
    _request_id = 25635
    my_er = ExclusionRequest(_request_id)
    assert my_er.id == _request_id

    # load expected result
    with open(r'tests\data' + str(_request_id)+'.yaml', encoding='utf-8') as file: 
        result = yaml.load(file, Loader=yaml.FullLoader)

    for it in my_er.tags:
        # extract tag data and verify it matches expected result
        my_tag = ERTag(it)        
        assert str(my_tag.value) == str(result[my_tag.title])