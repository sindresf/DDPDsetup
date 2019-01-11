#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '0.0.1'

long_description = '''Data Driven Predictions And Decisions (DDPD) is a project meant to help with
the process of trying to decide where to optimally place a new well in an existing field, or
the first well in a new field. Using Equinor's vast collection of production data, statistics and machine learning,
predictors for the wells cumulative production over its lifetime will give decision makers aid wherever they might
be looking.'''

requirements = [
    'fire',
    'numpy',
    'pandas',
    'mlflow',
    'matplotlib',
    'scikit-learn',
    'entrypoints',
    'Flask',
    'h5py',
    'jupyter',
    'notebook',
    'packaging',
    'pylint',
    'pytest',
    'PyYAML',
    'scipy',
    'seaborn',
    'bokeh',
    'shap',
    'statsmodels',
    '',
]


setup(
    name='DDPD',
    version=VERSION,
    author='Team Go-Time',
    author_email='ssfj@equinor.com',
    url='https://github.com/sindresf/DDPDsetup',
    download_url='https://github.com/sindresf/DDPDsetup',
    description='Setup project for work within DDPD',
    long_description=long_description,
    license=None,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Equinor Researchers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=requirements,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [
            'ddpd_main=main:main',
        ],
    },
    options={},
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
    zip_safe=True,
)
