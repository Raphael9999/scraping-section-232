# manipulate path to work dir
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from mine232 import ERList

def test_empty():
    """Nothing is provided"""
    my_erl = ERList()
    assert my_erl.er_ids == []
    assert my_erl.errors == []
    assert my_erl.extracted == []
    assert my_erl.df.shape[0] == 0
    assert my_erl.df.shape[1] == 242
    assert my_erl.fromto == 'empty'

def test_list():
    """List is provided"""
    my_erl = ERList([25663, 25635, 9999999, 25635])
    assert my_erl.er_ids == [25635, 25663, 9999999]
    assert my_erl.errors == [9999999]
    assert my_erl.extracted == [25635, 25663]
    assert my_erl.df.shape[0] == 2
    assert my_erl.df.shape[1] == 242
    assert my_erl.fromto == '25635-25663'

def test_range():
    """Range is provided"""
    my_erl = ERList(from_id=25660, to_id=25663)
    assert my_erl.er_ids == [25660, 25661, 25662]
    assert my_erl.errors == []
    assert my_erl.extracted == [25660, 25661, 25662]
    assert my_erl.df.shape[0] == 3
    assert my_erl.df.shape[1] == 242
    assert my_erl.fromto == '25660-25662'