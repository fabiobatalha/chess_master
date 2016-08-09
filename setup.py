#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = []

tests_require = []

setup(
    name="chessmaster",
    version="1.0",
    description="Chess Master Test",
    author="Fabio Batalha",
    author_email="scielo-dev@googlegroups.com",
    maintainer="Fabio Batalha",
    maintainer_email="fabiobatalha@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
    ],
    dependency_links=[],
    tests_require=tests_require,
    test_suite='tests',
    install_requires=install_requires
)