#!/usr/bin/env python
import os
import pathlib
import sys

if __name__ == "__main__":
    ROOT_DIR = pathlib.Path(__file__).resolve().parent
    SRC_DIR = ROOT_DIR / "src"
    sys.path.insert(0, str(SRC_DIR))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
