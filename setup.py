# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-colorpicker',
    description='Aplicação plugável Django para o bootstrap-colorpicker',
    long_description=open('README.md').read(),
    author='ZNC Sistemas',
    author_email='contato@znc.com.br',
    maintainer='ZNC Sistemas',
    maintainer_email='contato@znc.com.br',
    url='https://github.com/znc-sistemas/django-colorpicker',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Utilities',
        'Natural Language :: Portuguese (Brazilian)'
    ],
)
