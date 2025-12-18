"""Setup script for qfinlib package.

NOTE: This project uses Poetry for dependency management.
This setup.py is kept for backward compatibility but is optional.
Use `poetry install` or `poetry build` instead.
"""
from setuptools import setup, find_packages

setup(
    name="qfinlib",
    version="0.1.0",
    description="A comprehensive quantitative finance library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="qfinlib contributors",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
    ],
)
