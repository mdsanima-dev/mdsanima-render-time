#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Help developmend release workflow.

.. important::

    This file is not a part of Blender Addon.
    Embedded in the ``package.json`` script.

Bumping version in ``package.json`` file.
Bumping version in ``__init__.py`` file.
Autogenerate ``CHANGELOG.md`` based on commits.
Committing ``package.json``, ``__init__py`` and ``CHANGELOG.md`` files.
Creating tagging release and signed commit with GPG keys.

Check version in ``package.json`` then replece this version in ``__init__.py``
file.

:usage: ``./make_release.py``
"""


import json
import pathlib


HERE = pathlib.Path(__file__).parent


def go_check():
    """Loading data from ``package.json`` file.
    Execute after the version is bumped by ``postbump`` options.

    :return: new version to replece
    :rtype: str
    """
    path_to_file = HERE / "package.json"
    with open(path_to_file) as dt:
        data_package = json.load(dt)
    new_version = data_package["version"]
    return new_version


def go_read_write(old_version: str, new_version: str):
    """Replace old version with new version ``__init__.py`` file.

    :param old_version: line number with old version
    :type old_version: str
    :param new_version: line number with new version
    :type new_version: str
    """
    path_to_file = HERE / "__init__.py"
    with open(path_to_file, "r", encoding="utf-8") as r:
        replace_version = r.read().replace(old_version, new_version)
    with open(path_to_file, "w", encoding="utf-8") as w:
        w.write(replace_version)


def go_bump():
    """Reading file ``__init__.py`` and then split lines. Searching matching
    lines and replacing this line with new version. Print info in the console.
    """
    path_to_file = HERE / "__init__.py"
    with open(path_to_file, "r", encoding="utf-8") as r:
        lines = r.read().splitlines()
    lines_len = len(lines)
    for line in range(lines_len):
        if str('"version":') in str(lines[line]):
            print("[MDSANIMA RT] -> bumping __init__.py")
            print("[MDSANIMA RT] => matching line", line + 1, lines[line])
            new_version = go_check()
            print("[MDSANIMA RT] => checking new version =>", new_version)
            new_version_comma = str(new_version).replace(".", ", ")
            new_line_version = '    "version": (' + new_version_comma + "),"
            go_read_write(str(lines[line]), str(new_line_version))
            print("[MDSANIMA RT] => replace line", line + 1, new_line_version)


if __name__ == "__main__":
    go_bump()
