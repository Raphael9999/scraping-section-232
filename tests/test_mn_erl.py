# manipulate path to work dir
import sys, os, datetime 
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
    assert my_erl.get_fromto() == 'empty'

def test_list():
    """List is provided"""
    my_erl = ERList([25663, 25635, 9999999, 25635])
    assert my_erl.er_ids == [25635, 25663, 9999999]
    assert my_erl.errors == [9999999]
    assert my_erl.extracted == [25635, 25663]
    assert my_erl.df.shape[0] == 2
    assert my_erl.df.shape[1] == 242
    assert my_erl.get_fromto() == '25635-25663'

def test_range():
    """Range is provided"""
    my_erl = ERList(from_id=25660, to_id=25663)
    assert my_erl.er_ids == [25660, 25661, 25662]
    assert my_erl.errors == []
    assert my_erl.extracted == [25660, 25661, 25662]
    assert my_erl.df.shape[0] == 3
    assert my_erl.df.shape[1] == 242
    assert my_erl.get_fromto() == '25660-25662'

def test_sleep():
    """List is provided"""
    startt = datetime.datetime.now() #Performance management, start of run time
    my_erl = ERList([25663, 25635], wait=10) # 10s wait
    endt = datetime.datetime.now()
    assert my_erl.er_ids == [25635, 25663]
    assert (endt-startt).total_seconds() >= 10 # the program last more than 10s
    