from setuptools import setup, find_packages

setup(
    name="xts_cipher", 
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy", 
    ],
    description='A Python package for encryption and decryption using the XOR-Transposition-Substitution (XTS) cipher algorithm.',
    long_description=open('README.md').read(),  # Read from your README file
    long_description_content_type='text/markdown',  # Specify that the long description is in Markdown
    author='Krunal Chandrakant Dalvi',
    author_email='dalvikrunal15@gmail.com',
    url='https://github.com/KrunalDalvi/xts_cipher',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
