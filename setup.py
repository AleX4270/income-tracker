from setuptools import setup

setup(
    name='income_track',
    version='0.1',
    py_modules=['income_track'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        income=main:cli
    ''',
)