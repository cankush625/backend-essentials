#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings.base")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # This allows easy placement of apps within the interior
    # backend directory.
    sys.path.append(os.path.join(CURRENT_PATH, "backend_essentials"))

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
