# importing packages required by mymining
import pandas as pd
import re
import yaml
from .exclusion_request import ExclusionRequest
import time # for sleep

# to load
with open(r'mine232\header.yaml') as file:
    _header = yaml.load(file, Loader=yaml.FullLoader)

class ERList:
    """Extract data for a given list of Exclusion Request from the website

    :param ids: List of Exclusion Request ID requested, take precedent over the from-to
    :param from_id: ID to start the extraction from, will not be used if a list of ids is provided
    :param to_id: ID before wich the extraction ends, will not be used if a list of ids is provided
    :ivar ids: List of Exclusion Request ID requested, take precedent over the from-to
    :ivar from_id: ID to start the extraction from, will not be stored if a list of ids is provided
    :ivar to_id: ID before wich the extraction ends, will not be stored if a list of ids is provided
    :ivar er_ids: List of Exclusion Request ID to extract
    :ivar df: DataFrame containing the extracted data from the list of exclusion requests id
    :ivar errors: List of Exclusion Request ID that could not be extracted and returned and error
    :ivar extracted: List of Exclusion Request ID that were successfully extracted
    """

    def _extract_data(self):
        # initiate empty data
        self.df = pd.DataFrame(columns=_header)
        self.errors = []
        self.extracted = []
        for _id in self.er_ids:
            # extract info for the given _id to store them
            try:
                _er = ExclusionRequest(_id)
                time.sleep(self.wait)
            except ConnectionError:
                _er.error = True
            if not(_er.error):
                # no error we can store the data
                self.df = self.df.append(_er.data, ignore_index=True)
                self.extracted.append(_er.id)
            else:
                # add the error so user can fix input
                self.errors.append(_er.id)

        # remove duplicate and sort the list of errors
        self.errors = list(set(self.errors))
    
    def get_fromto(self):
        """smallest-largest of the id, to name the file
        :return: smallest-largest or empty"""
        if len(self.extracted) > 0:
            _ft = str(self.extracted[0])+'-'+str(self.extracted[-1])
        else:
            _ft ='empty'
        return _ft

    def __init__(self, ids=None, from_id=0, to_id=0, wait=0):
        if ids == None:
            # default list of IDs is empty
            ids = []
        # store input
        self.ids = ids
        self.from_id = from_id
        self.to_id = to_id
        self.wait = wait

        if self.to_id != 0 and self.ids == []:
            # ids take precedent over the from-to range
            self.er_ids = list(range(self.from_id, self.to_id))
        elif self.ids != []:
            self.er_ids = list(set(self.ids))
            # cannot combine .sort() above
            self.er_ids.sort()
        else:
            self.er_ids = []

        self._extract_data()
