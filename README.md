# Web scraping for Section 232

## Description
**Files**
* main is the program to run the extraction.  
* output.txt, use to store overflowing terminal `$ python main.py > output.txt`
* extract_list, similar to main, will extract a given list of exclusion requests instead of a sequence  
* Section232.ipynb was used for exploration purpose and built understanding of the BeautifulSoup and information extracted
* combine, will aggregate extracted csv together and provide a list of missing exclusion request if any
* .\mine232\, requirements.txt, setup.py is a package containing the class used in the main
* .\mine232\upd_prod_class, update the yaml file containing the caption for the product classification
* .\mine232\upd_header, update the yaml file containing the static caption for the exclusion request

**Folder Structure**
* .\documents\ documents related to the exploration
* .\env\ virtual environment
* .\result\ where the extracted files are placed
* .\tests\ directory for the automated testing with pytest

## Installation

## Example
__main__: 
* Update gfrom request ID you start the scrapping from, 
* gto request ID you end the scrapping at, 
* inc size of the batch of exclusion request extracted, too small/large will slow the process,
* run main.py, 
* results will be saved in .\result\

__extract_list__:
* Update glist with the list of specific request ID you would like to extract,
* run extract_list.py, 
* results will be saved in .\result\

__combine__:
* Update if needed the all_filenames list to contains the list of all the files you want to combine in a single csv
* run combine.py
* the combined file will be saved in .\result\

## License
MIT License

Copyright (c) [2021] [Raphael Louvrier]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 