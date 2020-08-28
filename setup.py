from setuptools import setup

setup(name='mymining', 
      version='0.0.1',
      description='Package for web data mining',
      author='Raphael Louvrier',
      author_email='rlouvrier@outlook.com',
      packages=['mymining'],
      install_requires=['regex', 
                        'numpy', 
                        'pandas', 
                        'datetime', 
                        'requests', 
                        'beautifulsoup4', 
                        'notebook', 
                        'pylint', 
                        'pep8'])