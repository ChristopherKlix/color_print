import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='color_print', # Replace with your own username
    version='0.0.1',
    author='Christopher Klix',
    author_email='christopher.klix@googlemail.com',
    description='A simple color print function for console output.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/christopherklix/color_print',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
