"""
    Setup file for strawberry-sqlalchemy-mapper.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.1.4.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf-8")

if __name__ == "__main__":
    try:
        setup(
            use_scm_version={"version_scheme": "no-guess-dev"},
            name="strawberry-sqlalchemy-mapper",
            version="0.1.1",
            description="The simplest way to implement autogenerated strawberry types for columns and relationships in SQLAlchemy models",
            long_description=README,
            long_description_content_type="text/markdown",
            url="https://github.com/expedock/strawberry-sqlalchemy-mapper",
            author="Expedock",
            author_email="rui@expedock.com",
            license="MIT",
            classifiers=[
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3",
            ],
            packages=["strawberry_sqlalchemy_mapper"],
            include_package_data=True,
            install_requires=[
                "sentinel==0.3.0",
                "sqlalchemy>=1.4",
                "strawberry-graphql>=0.95",
                "importlib-metadata==4.11.1",
            ],
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
