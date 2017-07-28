import os
import re

from setuptools import setup, find_packages

# reading the package version without loading the package.
with open(os.path.join(os.path.dirname(__file__), 'grapes', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

dependencies = [
    'sqlalchemy',
    'pymlconf'
]


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="grapes",
    version=package_version,
    author="Hamed Akhlaghi",
    author_email="akhlaghi65@gmail.com",
    url="https://github.com/hamedaakhlaghi/grapes",
    description="Simple food accounting",
    maintainer="Vahid Mardani",
    maintainer_email="vahid.mardani@gmail.com",
    packages=find_packages(),
    platforms=["any"],
    long_description=read('README.md'),
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'grapes = grapes:main'
        ]
    },
    license='Freeware',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Topic :: Database :: Front-Ends',
        'Topic :: Desktop Environment',
        'Topic :: Office/Business :: Groupware',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Programming Language :: Python :: 3.5',
    ],
)
