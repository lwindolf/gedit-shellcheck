# -*- coding: utf-8 -*-
#    ShellCheck plugin for Gedit
#    Copyright (C) 2017 Lars Windolf <lars.windolf@gmx.de>
#    Copyright (C) 2016 Xavier Gendre <gendre.reivax@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import shlex
import subprocess
import sys
import tempfile

from gi.repository import Gedit

__all__ = ("ShellCheck", )

class ShellCheck(object):
    """Helper class to handle ShellCheck."""

    def __init__(self):
        # Locate binary
        self._shellcheck_bin = None

        try:
            output = subprocess.check_output(
                        ["whereis", "-b", "shellcheck"],
                        universal_newlines=True)
        except subprocess.CalledProcessError:
            output = ""
        except OSError:
            output = ""
        finally:
            output = output.strip().split('\n')

        if len(output) == 1:
            if len(output[0].split()) > 1:
                # Found a binary for 'shellcheck'
                self._shellcheck_bin = output[0].split()[1]

    def run(self, doc):
        """Run the ShellCheck program on the content of the GeditDocument
        Return a JSON string containing the ShellCheck
        report or an empty object if an error occurred.
        """

        if not self._shellcheck_bin:
            print("ShellCheck Plugin: cannot find shellcheck binary", file=sys.stderr)
            return "{}"

        text = doc.get_text(
                doc.get_start_iter(),
                doc.get_end_iter(),
                True).encode()

        with tempfile.NamedTemporaryFile() as f:
            f.write(text)
            f.flush()

            cmd = ' '.join([
                self._shellcheck_bin,
                '-f json',
                f.name])
            cmd_array = shlex.split(cmd)

            try:
                p = subprocess.Popen(cmd_array, universal_newlines=True, stdout=subprocess.PIPE)
                out, err = p.communicate()
            except OSError as e:
                print(' '.join(["ShellCheck Plugin:", e.strerror]),
                        file=sys.stderr)
                return "{}"

        return out.strip()
