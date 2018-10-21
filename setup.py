import codecs
import os
import re

from setuptools import setup, find_packages


# ------------------------------------------------------------------
#                         HELPER FUNCTIONS

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M, )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


# ------------------------------------------------------------------
#                          POPULATE SETUP

setup(
    name="xsf_checker",
    version=find_version("xsf_checker", "__init__.py"),
    license="Apache 2.0 license",

    packages=find_packages(exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests", "*.test*",
    ]),
    package_data={

    },
    zip_safe=False,
    setup_requires=[
        "setuptools",
        "wheel",
    ],
    install_requires=[
        "compliance-checker>=4.1.1",
    ],
    python_requires='>=3.5',
    entry_points={
        "gui_scripts": [
            "XSFChecker = xsf_checker.app:main",
        ],
        "console_scripts": [
            "xsf_checker = xsf_checker.cli:main",
        ],
    },
    test_suite="tests",

    description="A library and tools to check file compliance for the eXtended Sounder Format.",
    long_description=read(os.path.join(here, "README.rst")),
    url="https://github.com/giumas/xsf-checker",
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="hydrography ocean mapping acoustic backscatter mosaic reflectivity",
    author="Giuseppe Masetti, Cyrille Poncelet",
    author_email="gmasetti@ccom.unh.edu, cyrille.poncelet@ifremer.fr",
)
