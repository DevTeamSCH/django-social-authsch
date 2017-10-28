import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-authsch',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app for AuthSCH.',
    long_description=README,
    url='https://git.sch.bme.hu/kszk/devteam/django-authsch',
    author='Barnabas Czeman',
    author_email='barni2000@sch.bme.hu',
    install_requires=[
        'social-auth-core',
        'social-auth-app-django',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
