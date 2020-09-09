# manipulate path to work dir
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import yaml
from mine232 import ERList

