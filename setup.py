from setuptools import setup, find_packages

setup(
    name='supercli',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_point='''
    [console_scripts]
    super=supercli:supercli
    '''
)


