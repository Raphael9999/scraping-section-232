# importing packages required by mymining
import pandas as pd
import re
import yaml
from .exclusion_request import ExclusionRequest

# to load
with open(r'mine232\header.yaml') as file:
    _header = yaml.load(file, Loader=yaml.FullLoader)

class ERList:
    """Extract data for a given list of Exclusion Request from the website

    :param er_ids: List of Exclusion Request ID to extract
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
        for _id in set(self.er_ids):
            # extract info for the given _id to store them
            _er = ExclusionRequest(_id)
            if not(_er.error):
                # no error we can store the data
                self.df = self.df.append(_er.data, ignore_index=True)
                self.extracted.append(_er.id)
            else:
                # add the error so user can fix input
                self.errors.append(_er.id)

        # remove duplicate and sort the list of errors
        self.errors = list(set(self.errors))

    def __init__(self, er_ids):
        self.er_ids = er_ids
        self._extract_data()