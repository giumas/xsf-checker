import argparse
import sys
from compliance_checker.runner import ComplianceChecker, CheckSuite
from compliance_checker.cf.util import download_cf_standard_name_table
from compliance_checker import __version__ as ioos_checker_version
from xsf_checker import __version__ as xsf_checker_version


def main():

    if hasattr(CheckSuite, 'templates_root'):
        CheckSuite.templates_root = "xsf_checker.library"

    # Load all available checker classes
    check_suite = CheckSuite()
    check_suite.load_all_available_checkers()

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', default=None, action='append',
                        help='Select the test (defaults: [\"xsf\", \"cf\"]). '
                             'Version can be specified via \"-t <test_standard>:<version>\". '
                             'If `<version>` is omitted (or \"latest\"), the latest version is used.')
    parser.add_argument('-c', '--criteria', nargs='?', default='normal',
                        choices=['lenient', 'normal', 'strict'],
                        help='Define the checking criteria (default: \"normal\").')
    parser.add_argument('-s', '--skip-checks', action='append',
                        help='Specify the tests to skip')
    parser.add_argument('-f', '--format', default=None, action='append', choices=['text', 'html', 'json_new'],
                        help='Set output formats (default: \"text\").')
    parser.add_argument('-o', '--output', default=[], action='append',
                        help=('Set output filenames. '
                              'If \"-\", output to stdout. '
                              'If 1 file is supplied, all the output goes in that file. '
                              'If more outputs are supplied, their number must match the inputs'))

    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Increase output verbosity (up to 3 times).')
    parser.add_argument('--version', action='store_true',
                        help='Display the XSF Checker version information.')
    parser.add_argument('--ioos-version', action='store_true',
                        help='Display the IOOS Compliance Checker version information.')

    parser.add_argument('input', nargs='*',
                        help="Define the input dataset to be checked.")
    parser.add_argument('-l', '--list-tests', action='store_true',
                        help='List the available tests')
    parser.add_argument('-d', '--download-standard-names',
                        help='Specify the CF version of standard name table to download')

    # Add command line args from generator plugins
    check_suite.add_plugin_args(parser)

    args = parser.parse_args()

    check_suite.load_generated_checkers(args)

    if args.version:
        print("XSF Checker version %s" % xsf_checker_version)
        return 0

    if args.ioos_version:
        print("IOOS compliance checker version %s" % ioos_checker_version)
        return 0

    if args.list_tests:
        print("Available checker suites:")
        for checker in sorted(check_suite.checkers.keys()):
            version = getattr(check_suite.checkers[checker],
                              '_cc_checker_version', "???")
            if args.verbose:
                print(" - {} (v{})".format(checker, version))
            elif ':' in checker and not checker.endswith(':latest'):  # Skip the "latest" output
                print(" - {}".format(checker))
        return 0

    if args.download_standard_names:
        download_cf_standard_name_table(args.download_standard_names)

    nr_inputs = len(args.input)
    if nr_inputs == 0:
        parser.print_help()
        return 1

    # Check the number of output files
    if not args.output:
        args.output = '-'
    nr_outputs = len(args.output)
    if (nr_outputs != 1) and (nr_outputs != nr_inputs):
        print('The number of outputs must either be 1 or the same as the number of inputs:\n'
              '- current inputs: %d\n'
              '- current outputs: %d' % (nr_inputs, nr_outputs),
              file=sys.stderr)
        sys.exit(2)

    if args.test is None:
        args.test = ['cf', 'xsf']

    if args.format is None:
        args.format = ['text', ]

    print("Parameters:\n"
          "- Tests: %s\n"
          "- Checks to skip: %s\n"
          "- Criteria: %s\n"
          "- Output format: %s\n"
          "- Verbosity: %s"
          % (args.test, args.skip_checks, args.criteria, args.format, args.verbose)
          )

    # Run the compliance checker
    # 2 modes, concatenated output file or multiple output files
    return_values = []
    had_errors = []

    if nr_outputs == 1:
        if args.format != 'json':
            print("Running on input: %s" % args.input, file=sys.stderr)
        return_value, errors = ComplianceChecker.run_checker(
            args.input,
            args.test,
            args.verbose,
            args.criteria,
            args.skip_checks,
            args.output[0],
            args.format)
        return_values.append(return_value)
        had_errors.append(errors)
    else:
        for output, input in zip(args.output, args.input):
            if args.format != 'json':
                print("Running on input: %s" % args.input, file=sys.stderr)
            return_value, errors = ComplianceChecker.run_checker(
                [input],
                args.test,
                args.verbose,
                args.criteria,
                args.skip_checks,
                output,
                args.format)
            return_values.append(return_value)
            had_errors.append(errors)

    if any(had_errors):
        return 2
    if all(return_values):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
