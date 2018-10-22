from compliance_checker.base import BaseCheck, BaseNCCheck, Result

import logging

logger = logging.getLogger(__name__)

from xsf_checker import __version__


class XSFCheck(BaseNCCheck):
    register_checker = True
    _cc_spec = 'xsf'
    _cc_spec_version = '1.0'
    _cc_checker_version = __version__
    _cc_url = 'https://github.com/giumas/xsf-checker'
    _cc_display_headers = {
        3: 'Required',
        2: 'Recommended',
        1: 'Suggested'
    }

    @classmethod
    def beliefs(cls):
        """Not applicable"""
        return {}

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        pass
