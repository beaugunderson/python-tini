from pathlib import Path

from setuptools import setup

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="tini",
    author="Beau Gunderson",
    author_email="beau@beaugunderson.com",
    url="https://github.com/beaugunderson/python-tini",
    description="Read simple .ini/configuration files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["config", "configuration", "ini"],
    version="4.0.0",
    license="MIT",
    py_modules=["tini"],
    install_requires=[
        "configparser >= 3.5.0b2",
        "six >= 1.10.0",
    ],
    setup_requires=["setuptools-markdown"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
)
