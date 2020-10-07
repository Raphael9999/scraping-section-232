import setuptools

setuptools.setup( name='mine232', 
                  version='0.1.0',
                  description='Package for data mining of Section 232',
                  author='Raphael Louvrier',
                  author_email='rlouvrier@outlook.com',
                  packages=setuptools.find_packages(), # packages=['mine232'],
                  install_requires=['regex', 
                                    'numpy', 
                                    'pandas', 
                                    'datetime', 
                                    'requests', 
                                    'beautifulsoup4', 
                                    'notebook', 
                                    'pylint', 
                                    'pep8',
                                    'pyyaml'],
                  python_requires='>=3.6.5',)