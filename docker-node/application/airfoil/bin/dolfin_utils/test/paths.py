# -*- coding: utf-8 -*-
"""Utilities for getting dolfin repository paths."""

# Copyright (C) 2014-2014 Martin Sandve Alnæs
#
# This file is part of DOLFIN.
#
# DOLFIN is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOLFIN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DOLFIN. If not, see <http://www.gnu.org/licenses/>.


import os


def find_parent_dir_with_file(filepath, filename):
    "Return the first parent directory containing a file with filename."
    # Start with given file path
    d = os.path.dirname(os.path.abspath(filepath))
    t = ''
    # Look for a particular filename
    while not os.path.isfile(os.path.join(d, filename)):
        d, t = os.path.split(d)
    # Return the directory where we found the file
    return d


def find_parent_dir_with_name(filepath, dirname):
    "Return the first parent directory called dirname."
    # Start with given file path
    d = os.path.dirname(os.path.abspath(filepath))
    t = ''
    # Look for a particular dirname
    while t != dirname:
        d, t = os.path.split(d)
    # Return the found directory
    return os.path.join(d, t)


def find_testdir(filepath):
    "Return the test/ directory filepath is contained in."
    return find_parent_dir_with_name(filepath, "test")


def find_demodir(filepath):
    "Return the demo/ directory filepath is contained in."
    return find_parent_dir_with_name(filepath, "demo")


def find_rootdir(filepath):
    """Return the root directory filepath is contained in.

    Assuming the existence of the files "INSTALL" and "AUTHORS".
    """
    a = find_parent_dir_with_file(filepath, "INSTALL")
    b = find_parent_dir_with_file(filepath, "AUTHORS")
    assert a == b
    return a


def find_cppsourcedir(filepath):
    d = find_rootdir(filepath)
    d = os.path.join(d, "dolfin")
    return d


def find_pysourcedir(filepath):
    d = find_rootdir(filepath)
    d = os.path.join(d, "site-packages")
    return d


def find_docdir(filepath):
    d = find_rootdir(filepath)
    d = os.path.join(d, "doc")
    return d


def find_benchdir(filepath):
    d = find_rootdir(filepath)
    d = os.path.join(d, "bench")
    return d
