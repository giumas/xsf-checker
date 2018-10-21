import argparse
import sys
# from compliance_checker.runner import ComplianceChecker, CheckSuite
# from compliance_checker.cf.util import download_cf_standard_name_table
from xsf_checker import __version__ as xsf_checker_version
from compliance_checker import __version__ as ioos_checker_version


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='store_true',
                        help='Display the XSF Checker version information.')
    parser.add_argument('--ioos-version', action='store_true',
                        help='Display the IOOS Compliance Checker version information.')

    args = parser.parse_args()

    if args.version:
        print("XSF Checker version %s" % xsf_checker_version)
        return 0

    if args.ioos_version:
        print("IOOS compliance checker version %s" % ioos_checker_version)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
