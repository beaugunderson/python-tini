from setuptools import setup

setup(name='tini',
      py_modules=['tini'],
      version='1.0',
      description='Read simple .ini/configuration files.',
      long_description_markdown_filename='README.md',
      author='Beau Gunderson',
      author_email='beau@beaugunderson.com',
      url='https://github.com/beaugunderson/python-tini',
      keywords=['config', 'configuration', 'ini'],
      install_requires=[
          'configparser >= 3.5.0b2',
          'six >= 1.9.0',
      ],
      setup_requires=[
          'setuptools-markdown'
      ],
      classifiers=[])
