#!/usr/bin/env python3

from setuptools import setup

setup(
    name="planet-reader",
    version="1.0",
    description="",
    packages=["planet_reader"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "jinja2",
        "reader",
        "click",
    ],
)
