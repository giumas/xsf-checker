XSF Checker
===========

.. image:: https://github.com/giumas/xsf-checker/raw/master/xsf_checker/app/media/favicon.png
    :alt: logo

|

.. image:: https://travis-ci.org/giumas/xsf-checker.svg?branch=master
    :target: https://travis-ci.org/giumas/xsf-checker
    :alt: Travis-CI Status

.. image:: https://ci.appveyor.com/api/projects/status/j1xd7od61oph2q3d?svg=true
    :target: https://ci.appveyor.com/project/giumas/xsf-checker
    :alt: AppVeyor Status

.. image:: https://api.codacy.com/project/badge/Grade/39c7c36f8021462db8e514fba2774c2f
    :target: https://www.codacy.com/app/hydroffice/xsf-checker/dashboard
    :alt: codacy

|

* GitHub: `https://github.com/giumas/xsf-checker <https://github.com/giumas/xsf-checker>`_
* License: Apache 2.0 (See `Apache license <https://www.apache.org/licenses/LICENSE-2.0>`_)

|

General info
------------

The XSF Checker is a python based tool to check for completeness and community standard compliance of local or
remote netCDF files against the eXtended Sounder Format.

The python module can be used as a command-line tool or as a library that can be integrated into other software.

The python module is coded similar to a Python standard Unit Test.
A Check Suite runs checks against a dataset based on a metadata standard, returning a list of Results which are then
aggregated into a summary.

For the CF compliance checks, XSF Checker uses the IOOS `Compliance Checker <https://github.com/ioos/compliance-checker>`_.

|

How to install
--------------

To install the *compliance-checker* dependency, follow the instructions on this
`wiki <https://github.com/ioos/compliance-checker/wiki>`_.

