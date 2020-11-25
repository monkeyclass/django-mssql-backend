from setuptools import find_packages, setup

CLASSIFIERS = [
    'License :: OSI Approved :: BSD License',
    'Framework :: Django',
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.0',
]

setup(
    name='django-mssql-backend-azure',
    version='2.9.0',
    description='Django backend for Microsoft SQL Server and Azure',
    long_description=open('README.rst').read(),
    author='Monkeyclass',
    author_email='',
    url='https://github.com/monkeyclass/django-mssql-backend-azure',
    download_url='https://github.com/monkeyclass/django-mssql-backend/archive/v_2.9.0.tar.gz'
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'pyodbc>=3.0',
        'msal>=1.2.0'
    ],
    package_data={'sql_server.pyodbc': ['regex_clr.dll']},
    classifiers=CLASSIFIERS,
    keywords='AZURE django',
)
