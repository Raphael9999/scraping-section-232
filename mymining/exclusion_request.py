# importing packages required by mymining
import requests
from bs4 import BeautifulSoup

class ExclusionRequest:
    """Exclusion Request object

    :param id: Exclusion Request ID to analyse
    :ivar id: Exclusion Request ID passed to the instance creation, numerical
    :ivar url: url to the detail of the Exclusion ID
    :ivar html: html answer of the request to the website
    :ivar soup: Soup of the exclusion request
    :ivar pretty: prettified soup of the exclusion request
    :ivar error: website returned an error
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
        # r2w is the request sent to the website
        r2w = requests.get(self.url)
        # html answer of the request to the website
        self.html = r2w.text 
        # Soup for the exclusion request
        self.soup = BeautifulSoup(self.html, features="html.parser")
        # prettify html of the exclusion request
        self.pretty = self.soup.prettify()
        # website returned error, 
        # could raise ValueError('Website: An error occurred while processing your request')
        ttl = self.soup.title.string
        self.error = ( ttl == 'Error' ) or ( ttl != ('Exclusion Request ' + str(self.id)) )

    def _parse(self):
        """Parse the answer from the website"""
        self.title = self.soup.title.string
        # use function to filter the find_all
        self.tags = self.soup.find_all()

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
        self._parse()
    
