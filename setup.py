#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author='Stefan Fischer',
    author_email='sfischer13@ymail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
    ],
    description='SSV stands for separator separated values.',
    include_package_data=True,
    install_requires=requirements,
    keywords='ASCII collision CSV delimiter separator SSV table text TSV value',
    license='MIT',
    long_description=readme + '\n\n' + history,
    name='ssv',
    package_dir={'ssv': 'ssv'},
    packages=['ssv'],
    python_requires='>=3.3',
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sfischer13/python-ssv',
    version='0.1.1',
    zip_safe=False)
