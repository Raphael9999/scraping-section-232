# manipulate path to work dir
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from mine232 import ExclusionRequest

# create exclusion request 
def test_id():
    """ID is a numerical"""
    my_er = ExclusionRequest(25663)
    assert my_er.id == 25663
    assert my_er.url == 'https://232app.azurewebsites.net//Forms/ExclusionRequestItem/25663'
    assert str(my_er.html)[:193] == '''<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8" />\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\r\n    <title>Exclusion Request 25663</title>'''
    assert str(my_er.soup)[:136] == '''<!DOCTYPE html>\n\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n<meta content="width=device-width, initial-scale=1.0" name="viewport"/>'''
    assert str(my_er.pretty())[:188] == '''<!DOCTYPE html>\n<html lang="en">\n <head>\n  <meta charset="utf-8"/>\n  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>\n  <title>\n   Exclusion Request 25663\n  </title>'''
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