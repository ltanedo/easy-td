from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='package name',
    version='0.4.1',
    description='short description',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='repository url',
    author='My name',
    author_email='my@e.mail',
    license='MIT',
    packages=['PackageName','PackageName.SubModule'],
    zip_safe=False,
    install_requires=[
        'dependecy1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)