import yaml
from .exclusion_request import ExclusionRequest

class UpdateHeader():
    """Update the header.yaml file that is used by the er_list module"""
    def __init__(self):
        my_request = ExclusionRequest(25663) 
        self.header = my_request.captions()
        with open(r'mine232\header.yaml', 'w') as file:
            # sort_key is False to preserve order of the list
            documents = yaml.dump(self.header, file, sort_keys=False)
