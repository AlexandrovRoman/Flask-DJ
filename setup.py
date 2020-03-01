from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.readlines()

setup(
    name='Flask-DJ',  # Required
    version='0.0.1',  # Required
    description='Django (mvc) structure for your Flask project',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/AlexandrovRoman/Flask-DJ',  # Optional
    author='Alexandrov Roman',  # Optional
    author_email='AlexandrovRomanisi@ya.ru',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='mvc django flask structure',  # Optional
    packages=find_packages(),  # Required
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'startapp = Flask_DJ:start',
        ],
    },
)
