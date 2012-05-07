#!/usr/bin/env python
"""
django_cms_carousel
A slider plugin for django cms (beta)

The main repository is https://bitbucket.org/sjs/django_cms_carousel/src

There are another repository in https://bitbucket.org/esauro/django_cms_carousel which is pretty the same
with pip support.

"""
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

tests_require = [
    'Django==1.3.1',
    ]

install_requires = [
    'Django==1.3.1',
    'django-cms',
    ]

setup(
    name='django_cms_carousel',
    version='0.1',
    url='https://bitbucket.org/sjs/django_cms_carousel/',
    description='A slider plugin for django cms (beta)',
    long_description=__doc__,
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
