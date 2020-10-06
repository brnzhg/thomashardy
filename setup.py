from setuptools import setup

setup(
    name='testing',
    version='0.1',
    py_modules=['testing'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        testing=testing:cli
    ''',
)

# pyspellchecker
# pydictionary
# sqlalchemy

# - Click