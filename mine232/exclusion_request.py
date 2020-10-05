# importing packages required by mymining
from bs4 import BeautifulSoup
import requests
import re
from .er_tag import ERTag

def _filter_tags(one_tag):
    """Filter the tags from the soup to return the one we need
    :param t: a tag
    :return: boolean, true to keep, false to drop the given tag
    """
    # title
    _b_l =  one_tag.name == 'title'

    # input with a value
    _b_i = ( one_tag.name == 'input' ) and one_tag.has_attr('value')

    # textarea
    _b_t = one_tag.name == 'textarea'

    # a valid name is required for input and text area
    _b_n = True
    if one_tag.has_attr('name'):                 
        # check if the name attribute exist for that tag
        # exclude those names
        _b_n = not( one_tag['name'] in ['', '__RequestVerificationToken'] ) 
    else: 
        _b_n = False

    # *[i].key are discarded, we work with the *[i].value
    if one_tag.has_attr('name'):                 
        # check that the name attribute exist for that tag
        # true if cannot find *[i].Key, False if find it
        _b_k = None == (re.search( r'^BIS232Request.JSONData.(ProductClassification|ChemicalComposition|ProductDimensions|ProductStrength|ProductProcessing.ProcessesPercentage|ProductProcessing.Processes|ToughnessJoules|ToughnessShear|ToughnessTemperature).*Key$', 
                                   one_tag['name'], flags=0))
        # the following keys are excluded by the above regex but are required
        if one_tag['name'] in ['BIS232Request.JSONData.ChemicalComposition[27].Key', 
                               'BIS232Request.JSONData.ProductStrength[2].Key', 
                               'BIS232Request.JSONData.ToughnessTemperature[2].Key']:
            _b_k = True # flip _b_k to keep those exceptions

    # type hidden should be removed
    if one_tag.has_attr('type'):                 
        # check if the type attribute exist for that tag
        # False to discard hidden
        _b_h = one_tag['type'] != 'hidden' 
    else: 
        _b_h = True

    # p tags are used for Submission date and Public Status
    _b_p = False
    if one_tag.name == 'p':
        # exemple: Submission Date: 12/13/2019, True to keep this tag
        _b_p = ( one_tag.text[:17] == 'Submission Date: ' ) or ( one_tag.text[:15] == 'Public Status: ' )
    
    # Attachments
    # to avoid error need to check is the id attribute exist for that tag
    if ( one_tag.name == 'div' ) and one_tag.has_attr('id'):         
        _b_a = one_tag['id'] in ['ERAttachment', 'DMAttachment' ]
    else:
        _b_a = False 

    # Input and textarea with valid name, not hidden, not a *[i].Key, plus: title, p and attachments
    return ( ( _b_i or _b_t ) and _b_n and _b_k and _b_h ) or _b_l or _b_p or _b_a

class ExclusionRequest:
    """Exclusion Request class to query site, receive and store answer

    :param id: Exclusion Request ID to analyse
    :ivar id: Exclusion Request ID passed to the instance creation, numerical
    :ivar url: url to the detail of the Exclusion ID
    :ivar html: html answer of the request to the website
    :ivar soup: Soup of the exclusion request
    :ivar title: Title of the exclusion request
    :ivar tags: List of tags of the exclusion request
    :ivar data: Dictionary with the data title and value extracted from the list of tags
    :ivar error: Website returned an error
    """

    def _get_url(self):
        """Build the url to access the details of the Exclusion Request"""
        # Base URL of the U.S. Dpt of Commerce, Section 232 Steel and Aluminum website
        base_url = 'https://232app.azurewebsites.net/'

        # URL for Details for an exclusion, you need to concatenate the Request ID to the right
        eri_url = base_url + '/Forms/ExclusionRequestItem/'
        
        # non numerical id are invalid
        if self.id != 0:
            self.url = eri_url + str(self.id)
        else:
            self.url = ''

    def _get_request(self):
        """Request website and store response for the Exclusion Request"""
        # try:
        # r2w is the request sent to the website
        r2w = requests.get(self.url) #, timeout=5)
        # html answer of the request to the website
        self.html = r2w.text 
        # Soup for the exclusion request
        self.soup = BeautifulSoup(self.html, features="html.parser")
        # website returned error, 
        # could raise ValueError('Website: An error occurred while processing your request')
        ttl = self.soup.title.string
        # except ConnectionError:
        #     ttl = 'Error'
        self.error = ( ttl == 'Error' ) or ( ttl != ('Exclusion Request ' + str(self.id)) )

    def pretty(self):
        """Return prettified soup made from the html of the exclusion request
        :return: soup.prettify()"""
        return self.soup.prettify()

    def _get_tags(self):
        """Parse the answer from the website"""
        self.title = self.soup.title.string
        # use function to filter the find_all
        self.tags = self.soup.find_all(_filter_tags)

    def _get_data(self):
        """Built a dictionary with the data title and value extracted from the list of tags"""
        self.data = {}
        for _one_tag in self.tags:
            _processed_tag = ERTag(_one_tag)
            self.data[_processed_tag.title] = _processed_tag.value

    def values(self):
        """List of values extracted from the website"""
        return list(self.data.values())

    def captions(self):
        """List of caption, header, title corresponding to the values extracted from the website"""
        return list(self.data.keys())

    def __init__(self, id):
        if str(id ).isnumeric():
            # Exclusion Request ID, is a numerical NNNNN
            self.id = int(id)
        else:
            # non numerical id are invalid
            self.id = 0
            raise  TypeError('Exclusion Request ID must be numerical')
        
        self._get_url()
        self._get_request()
        if not(self.error):
            self._get_tags()
            self._get_data()
