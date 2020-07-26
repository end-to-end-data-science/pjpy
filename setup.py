"""Setup for pjpy package."""
import setuptools

import pjpy

NAME = "pjpy"

VERSION = pjpy.__version__

AUTHOR = ''

AUTHOR_EMAIL = 'edesio@usp.br'

DESCRIPTION = 'Machine learning library'

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

LICENSE = 'GPL3'

URL = ''

DOWNLOAD_URL = ''

CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: GNU General Public License v3 ('
               'GPLv3)',
               'Natural Language :: English',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']

INSTALL_REQUIRES = [
    'numpy', 'scipy', 'scikit-learn', 'imbalanced-learn', 'pjml', 'pjautoml'
]

# INSTALL_REQUIRES = [
#     'numpy', 'scipy', 'scikit-learn', 'imbalanced-learn', 'pjml'
# ]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)

package_dir = {'': 'pjpy'}  # For IDEs like Intellij to recognize the package.
