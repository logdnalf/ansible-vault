#
# Copyright (C) 2019, Tomohiro NAKAMURA <quickness.net@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, unicode_literals

import os
import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_black(monkeypatch):
    monkeypatch.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    stderr = subprocess.run(
        [sys.executable, "-m", "black", ".", "--check"], stderr=subprocess.PIPE
    ).stderr
    assert "reformatted" not in str(stderr), "Please run `./venv/bin/python3 -m black .`."
