from setuptools import setup, find_packages

setup(
    name='mp3_title_extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'eyed3',
    ],
    entry_points={
        'console_scripts': [
            'mp3_title_extractor = mp3_title_extractor.extractor:main',
        ],
    },
)