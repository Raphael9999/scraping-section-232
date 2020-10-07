# scraping-section-232
Web scraping for Section 232

Section232.ipynb was used for exploration purpose and built understanding of the BeautifulSoup
documents\ documents related to the exploration

main is the program to run the extraction

extract_list, similar to main, will extract a given list of exclusion requests instead of a sequence

combine, will aggregate extracted csv together and provide a list of missing exclusion request if any

output.txt, use to store overflowing terminal $ python main.py > output.txt

result\ directory where the extracted results are placed

env\ virtual environment

tests\ directory for the automated testing of mine232, using pytest

mine232\, requirements.txt, setup.py is a package containing the class used in the main

mine232\upd_prod_class, update the yaml file containing the caption for the product classification
mine232\upd_header, update the yaml file containing the static caption for the exclusion request