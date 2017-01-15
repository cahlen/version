"""
This module contains comparison functions for semantic version strings.
"""

def _parse_version(version_string):
    """
    Parses version string and returns a list of integers.
    """
    version_split = version_string.split('.')
    return [int(x) for x in version_split]

def equals(first_version, second_version):
    """
    Checks if two version strings are equal.
    Returns boolean True or False.
    """
    if first_version == second_version:
        return True
    else:
        return False

def greaterthan(version_one, version_two):
    """
    Checks if version_one is strictly greater than version_two.
    Returns boolean True or False.
    """

    # Parse strings for integer comparison
    a_version = _parse_version(version_one)
    b_version = _parse_version(version_two)

    # Additional variables to enhance code readability
    # and append a zero if only major and minor are defined.
    if len(a_version) == 3 and len(b_version) == 3:
        a_major, a_minor, a_patch = a_version
        b_major, b_minor, b_patch = b_version
    elif len(a_version) == 2 and len(b_version) == 3:
        a_major, a_minor = a_version
        b_major, b_minor, b_patch = b_version
        a_patch = 0
    elif len(a_version) == 3 and len(b_version) == 2:
        a_major, a_minor, a_patch = a_version
        b_major, b_minor = b_version
        b_patch = 0
    else:
        a_major, a_minor = a_version
        b_major, b_minor = b_version
        a_patch, b_patch = 0, 0

    # Compare versions
    if a_major > b_major:
        return True
    elif (a_major == b_major or
          a_major > b_major) and \
              a_minor > b_minor:
        return True
    elif ((a_major == b_major or
           a_major > b_major) and \
               (a_minor == b_minor or \
                a_minor > b_minor)) and \
                    a_patch > b_patch:
        return True
    else:
        return False

def greaterthan_or_equal(version_one, version_two):
    """
    Checks if version_one is greater than or equal to version_two.
    Returns boolean True or False.
    """
    if greaterthan(version_one, version_two) or \
       equals(version_one, version_two):
        return True
    else:
        return False

def lessthan(version_one, version_two):
    """
    Checks if version_one is strictly less than version_two.
    Returns boolean True or False.
    """
    if not greaterthan_or_equal(version_one, version_two):
        return True
    else:
        return False

def lessthan_or_equal(version_one, version_two):
    """
    Checks if version_one is less than or equal to version_two.
    Returns boolean True or False.
    """
    if not greaterthan(version_one, version_two):
        return True
    else:
        return False

def pessimistic(version_one, version_two):
    """
    Checks if version_one is within pessimistic versioning range
    of version_two.  Two or three digit versions are acceptable but
    must be consistent.

    e.g., pessimistic("2.1.23", "2.1.2") returns True
          pessimistic("2.2.23", "2.1.2") returns False
          pessimistic("2.24", "2.1") returns True
          pessimistic("3.0", "2.1") returns False
    """

    # Parse strings for integer comparison
    a_version = _parse_version(version_one)
    b_version = _parse_version(version_two)

    # Additional variables to enhance code readability
    if len(a_version) == 3:
        a_major, a_minor, a_patch = a_version
        b_major, b_minor, b_patch = b_version
    else:
        a_major, a_minor = a_version
        b_major, b_minor = b_version

    # Check 3-digit formats
    if len(a_version) == 3:
        if (a_major == b_major) and \
           (a_minor == b_minor):
            if a_patch > b_patch:
                return True
            else:
                return False
        else:
            return False

    # Check 2-digit formats
    else:
        if (a_major == b_major) and \
           (a_minor > b_minor):
            return True
        else:
            return False
