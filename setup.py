import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="Pycalc",
    version="1.0",
    description="Pure-python command-line calculator.",
    license=read("LICENSE"),
    author="Marharyta Hancharenka",
    author_email="Marharyta_Hancharenka@epam.com",
    packages=["pycalc", "tests"],
    long_description=read('README.md'),
    test_suite="tests",
    python_requires='>=3.6',
    entry_points={
          'console_scripts': [
              'pycalc = pycalc.launcher:main',
          ],
       }
    )
