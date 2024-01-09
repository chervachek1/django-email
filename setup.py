from setuptools import setup, find_packages

setup(
    name='django_email',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'Django',
        'python-dotenv',
        'requests',
    ],
)
