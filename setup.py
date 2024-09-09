from setuptools import setup, find_packages

setup(
    name='papertools',
    version='1.0',
    packages=find_packages(),
    author='PaperTarsier692',
    url='https://www.github.com/PaperTarsier692/papertools',
    long_description='Small collection of various Python tools.', long_description_content_type='text/markdown',
    requires=[
        'Groq>=0.11.0'
    ]
)
