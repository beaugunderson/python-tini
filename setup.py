from setuptools import setup

setup(
    name='tini',
    author='Beau Gunderson',
    author_email='beau@beaugunderson.com',

    url='https://github.com/beaugunderson/python-tini',

    description='Read simple .ini/configuration files.',
    long_description_markdown_filename='README.md',

    keywords=['config', 'configuration', 'ini'],

    version='1.0',

    py_modules=['tini'],

    install_requires=[
        'configparser >= 3.5.0b2',
        'six >= 1.9.0',
    ],

    setup_requires=[
        'setuptools-markdown'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: BSD License',

        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',

        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ])
