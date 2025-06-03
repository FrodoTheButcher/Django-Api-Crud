from setuptools import setup, find_packages

setup(
    name='core-services',  
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    description='Reusable service layer for Django apps',
    author='Your Name',
    author_email='you@example.com',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
