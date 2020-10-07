# manipulate path to work dir
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import yaml
from mine232 import ExclusionRequest

# create exclusion request 
def test_id():
    """ID is a numerical"""
    my_er = ExclusionRequest(25663)
    assert my_er.id == 25663
    assert my_er.url == 'https://232app.azurewebsites.net//Forms/ExclusionRequestItem/25663'
    assert my_er.html[:33] == '''<!DOCTYPE html>\r\n<html lang="en">'''
    assert str(my_er.soup)[:33] == '''<!DOCTYPE html>\n\n<html lang="en">'''
    assert my_er.pretty()[:32] == '''<!DOCTYPE html>\n<html lang="en">'''
    assert not(my_er.error)

def test_text_id():
    """ID is a numerical text"""
    my_er = ExclusionRequest('25663')
    assert my_er.id == 25663

def test_notfound():
    """ID is a numerical"""
    my_er = ExclusionRequest(9999999)
    assert my_er.id == 9999999
    assert my_er.url == 'https://232app.azurewebsites.net//Forms/ExclusionRequestItem/9999999'
    assert str(my_er.html)[:175] == '''<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8" />\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\r\n    <title>Error</title>'''
    assert my_er.error

def test_non_num_id():
    """ID is non numerical"""
    try:
        my_er = ExclusionRequest('3f')
    except TypeError:
        # success we want an Exception
        assert True 
    else:
        # fail, the id was processed
        assert False

def test_empty_id():
    """ID is empty, empty string"""    
    try:
        my_er = ExclusionRequest('')
    except TypeError:
        # success we want an Exception
        assert True 
    else:
        # fail, the id was processed
        assert False

def test_missing_id():
    """ID is missing, no argument"""    
    try:
        my_er = ExclusionRequest()
    except TypeError:
        # success we want an Exception
        assert True 
    else:
        # fail, the id was processed
        assert False

def test_data():
    """Test data extracted for an exclusion request"""
    _request_id = 25635
    my_er = ExclusionRequest(_request_id)
    assert my_er.id == _request_id

    # load expected result
    with open(r'tests\data' + str(_request_id)+'.yaml', encoding='utf-8') as file: 
        result = yaml.load(file, Loader=yaml.FullLoader)

    assert my_er.data == result

    assert my_er.captions() == list(result.keys())
    assert my_er.values() == list(result.values())