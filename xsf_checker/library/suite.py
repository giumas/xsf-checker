"""
XSF Checker suite runner
"""

from compliance_checker import suite


class XSFCheckSuite(suite.CheckSuite):

    def __init__(self):
        super().__init__()

    def checker_html_output(self, check_name, groups, source_name, limit):
        """Overwrite the original method"""
        print("######")
        from jinja2 import Environment, PackageLoader
        self.j2 = Environment(loader=PackageLoader('xsf_checker', 'library/data/templates'))
        template = self.j2.get_template('ccheck.html.j2')

        template_vars = self.build_structure(check_name, groups, source_name, limit)
        return template.render(**template_vars)
