import os
from codecs import open

from setuptools import setup, find_packages

# Based on https://github.com/pypa/sampleproject/blob/master/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

# here = os.path.abspath(os.path.dirname(__file__))
#
# with open(os.path.join(here, 'readme.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="pgen",
    version='1.0.0',
    description="Bla bla bla to be described later",
    long_description='',
    url="https://github.com/qjinni/pgen",
    author="Bartosz Kolada",
    author_email="bartkolada@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing"
    ],
    packages=find_packages(
        include=[
            'content_generator',
            'content_generator/*'
        ]
    ),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "pgen = content_generator.pgen:main",
        ]
    },
    # install_requires=[
    #     "codecs"
    # ]
)