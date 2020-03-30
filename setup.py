from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'PyPI_README.md'), encoding='utf-8') as f:
    long_description = f.read()

about = {}
with open(path.join(here, 'flask_dj', '__project_info__.py')) as f:
    exec(f.read(), about)

packages = ["flask_dj"]
requirements = [
        'waitress>=1.4.3',
        'flask>=1.1.1',
        'Flask-Migrate>=2.5.2',
        'Flask-Script>=2.0.6',
        'Flask-SQLAlchemy>=2.4.1',
        'WTForms>=2.2.1',
        'SQLAlchemy>=1.3.13',
        'Flask-WTF>=0.14.3',
        'Flask-Login>=0.5.0'
    ]

setup(
    name=about["__title__"],  # Required
    version=about["__version__"],  # Required
    description=about["__description__"],  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/AlexandrovRoman/Flask-DJ',  # Optional
    author=about["__author__"],  # Optional
    author_email=about["__author_email__"],  # Optional
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        f'License :: OSI Approved :: {about["__license__"]}',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=about["__keywords__"],  # Optional
    packages=packages,  # Required
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'flask-dj = flask_dj:command',
        ],
    },
    project_urls={
        "Source": "https://github.com/AlexandrovRoman/Flask-DJ",
        "Docs": "https://flask-dj.readthedocs.io/en/latest/"
    }
)
