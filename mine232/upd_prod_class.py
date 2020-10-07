import requests                               #for querying the webite
from bs4 import BeautifulSoup                 #for reading and parsing the html
import re                                     #for regular expression
import yaml

def _get_prodclass(ltag):                         
    """function to select ProductClassification tags"""
    if ltag.has_attr('name'):                 
        #to avoid error need to check is the name attribute exist for that tag
        #lrex, true if it is a BIS232Request.JSONData.ProductClassification*Key
        lrex = None != (re.search( r'^BIS232Request.JSONData.ProductClassification.*Key$', ltag['name'], flags=0)) 
    else:                                     
        #exclude tag without name attribute
        lrex = False                
    return lrex

class UpdateProdClass:
    """Update the prod_class.yaml file that is used by the er_tag module"""
    def __init__(self):
        #Base URL of the U.S. Department of Commerce, Section 232 website
        _url = 'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/22561'    

        # one time process to fill in the ProductClassification dictionary for title from the .Key
        # is the request sent to the website, 22561 is as good as any other
        r = requests.get(_url)                
        rhtml = r.text # Request html answer
        rsoup = BeautifulSoup(rhtml, features="html.parser") 
        dpc = {} # initiate dictionary for title for product classification value
        lit = rsoup.find_all(_get_prodclass) # list of tags matching the selection function
        for t in lit: # Loop the list of input tag for ProductClassification
            dat = t.attrs # Dictionary of attibutes of that tag
            for ls in ('BIS232Request.', 'JSONData.'):   #for readability sake replace with '' 
                dat['name'] = dat['name'].replace(ls, '', 1)
            if   dat['value'] != '':
                # most of the time, the caption is in value of ProductClassification[i].Key
                ls = dat['value']    
            elif dat['title'] != '': 
                # else it is in title of ProductClassification[i].Key 
                ls = dat['title']   
            else: 
                ls = ''
            # save the title for ProductClassification[i].Value in dictionary
            dpc[dat['name'].replace('.Key', '.Value', 1)] = ls

        self.prodclass = dpc

        with open(r'mine232\prod_class.yaml', 'w') as file:
            # sort_key is False to preserve 1..9 before 10..30
            documents = yaml.dump(dpc, file, sort_keys=False)