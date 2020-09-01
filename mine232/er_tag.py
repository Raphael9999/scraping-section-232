# importing packages required by mymining
from bs4 import BeautifulSoup
import re
import yaml

with open(r'mine232\prod_class.yaml') as file:
    prod_class_dict = yaml.load(file, Loader=yaml.FullLoader)

class ERTag:
    """Exclusion Request tag class to analyse an individual tag of the website reply

    :param tag: Tag to analyse
    :ivar tag: Tag passed to the instance creation, numerical
    :ivar attributes: Dictionary with tag attributes and values, missing atttributes/empty values are omitted
    """

    def _get_attributes(self):
        try:
            self.attributes = self.tag.attrs
            self.attributes['tag.name'] = self.tag.name
            self.attributes['tag.text'] = self.tag.text
        except TypeError:
            # unable to use .attrs, attributes dictionary is empty
            self.attributes = {}

    def _clean_attribute(self, attribute):
        """Clean one attribute of the tage
        :param attribute: attribute to be cleaned
        :param remove: 1, list of substring to remove from the attribute's value
        :param drop: 2, regular expression triggering a drop of the attribute's value
        :param keep: 3, list of attribute's value to keep
        """
        _l_remove = ['BIS232Request', 'JSONData', # remove for readability    
                     'RequestVerificationToken']  # those tags are not needed, -> blanking 
        # check if the name attribute exist, otherwise cant read it
        if attribute in self.attributes:
            # _lv local variable for the name's value
            _lv = str(self.attributes[attribute]) 

            # remove all substrings from 'remove' that match the value
            for ls in _l_remove:
                _lv = _lv.replace(ls, '', 1)
            
            # strip is trim
            _lv = _lv.strip('_').strip('.')

            # we only want attribute with a value
            if _lv != '':
                #use regex to replace carriage return, line break, tab..., strip extra spaces
                _lv = re.sub(r"[\r\n\t]", '', _lv).strip() 
                self.clean[attribute] = _lv

    def _drop_clean(self):
        if ( self.title == '' and self.name == '' ): 
            # or ( str(self.value) = '' ): # no, as empty values are legit
            self.clean = {}
            self.name  = ''
            self.title = ''
            self.value = ''
        # if len(self.clean) <= 1:
        #     # need at least 2 attributes name+value to add to extraction
        #     self.clean = {}

    def _clean_attributes(self):
        """Clean the attibutes dictionary into the clean dictionary"""
        _l_att_name = [ 'name', 'value', 'id', 'title', 'type', 'checked', 'tag.text']
        self.clean = {}
        for ap in _l_att_name:
            self._clean_attribute(ap)

    def _get_name(self):
        # general case, exception to overwrite that here under
        if 'name' in self.clean:
            self.name = self.clean['name']
        elif 'title' in self.clean:
            # no name available, fall back use title
            self.name = self.clean['title']
        elif 'id' in self.clean: 
            # special case with 'DMAttachment' and 'ER.. where id is used for name
            self.name = self.clean['id']
        elif self.attributes['tag.name'] == 'p':
            if self.attributes['tag.text'][:17] == 'Submission Date: ':      #exemple:Submission Date: 12/13/2019
                self.name = 'Submission.Date'
            if self.attributes['tag.text'][:15] == 'Public Status: ':        #exemple:Public Status: Pending-Objection Window Open
                self.name = 'Public.Status'
        elif self.attributes['tag.name'] == 'title':
            self.name = 'ID'
        else:
            self.name = ''

    def _get_title(self):
        # General case
        if 'title' in self.clean:
            self.title = self.clean['title']
        else:
            self.title = ''

        if self.name[:22] == 'ProductClassification[' and self.name[-7:] == '].Value':
            #dictionary for product classification provide the title for that value
            self.title = prod_class_dict[self.name]         
        
        # Force the title for the following names as they are exceptions to the global pattern
        name_title_dict = {'Product'            : 'Product',
                           'MetalClass'         : 'Metal Class',
                           'RequestingOrg.State': 'Requesting Organization State',
                           'ID'                 : 'Request ID',
                           'DMAttachment'       : 'BIS Decision Memo',
                           'ERAttachment'       : 'Attachment',
                           'Submission.Date'    : 'Submission Date',
                           'Public.Status'      : 'Public Status'}
        if self.name in name_title_dict: 
            self.title = name_title_dict[self.name]
        
        # Fix typo in the title of the ToughnessShear[*].Value, replace Joule with Shear
        if self.name[:15] == 'ToughnessShear[' and self.name[-7:] == '].Value':
            self.title = self.clean['title'].replace('Joule', 'Shear', 1)
        
        # Fix typo in the title of the bendadility %, replace with mm
        if self.name[:37] == 'ProductProcessing.Processes[0].Value.':
            self.title = self.clean['title'].replace('Percentage', 'mm', 1)
        
        # Fall back, use the name if no title is available, there should not be any
        if self.title == '' and self.name != '': 
            self.title = 'NAME: ' + self.name

    def _get_value(self):
        if   self.title == 'Request ID':
            self.value = self.clean['tag.text'][18:]
        elif self.tag.name == 'textarea':
            # for textarea, there is no value attribute, the comment is found with text
            self.value = self.clean['tag.text']
        elif self.title == 'BIS Decision Memo':
            self.value = 'True'
        elif self.title == 'Attachment':
            # cannot find any difference between 22561 with ER and 44558 w/o ERAttachment
            self.value = 'True'
        elif self.title == 'Submission Date':
            self.value = self.clean['tag.text'][17:]
        elif self.title == 'Public Status':
            self.value = self.clean['tag.text'][15:] 
        # Checkbox
        elif ( 'type' in self.clean ) and ( self.clean['type'] == 'checkbox' ):
            # if 'checked' is there, then true, otherwise it is missing and false
            self.value = str('checked' in self.clean)
        # General case
        elif 'value' in self.clean:
            self.value = self.clean['value']
        # Could not find a value, probably empty
        else:
            self.value = ''

    def __init__(self, tag):
        self.tag = tag
        self._get_attributes()
        self._clean_attributes()
        self._get_name()
        self._get_title()
        self._get_value()
        self._drop_clean()
