#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by SammaySarkar
# Copyright (c) 2016 SammaySarkar
#
# License: MIT
#

"""This module exports the Au3check plugin class."""

from SublimeLinter.lint import Linter, util


class Au3check(Linter):
    """Provides an interface to au3check."""

    syntax = 'autoit'
    cmd = 'au3check.exe -q'
    executable = None
    version_args = ''
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.0.0, < 4.0.0'
    tempfile_suffix = '-'

    multiline = True
    regex = r'''(?xi)
            # "sourcefile/includefile"(line,col) : errortype: msg
            # offending code
            # ~~~~~~~~~caret
            ^.+?\"\((?P<line>\d+)\,(?P<col>\d+)\)\s:\s
            (?:(?P<warning>warning)|(?P<error>error)):\s(?P<message>.+)\r?\n
            ^.*$\r?\n
            ^.*\^\r?\n
            '''

    line_col_base = (1, 1)
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
