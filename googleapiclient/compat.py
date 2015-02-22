import six

# Long datatype has been integrated into integer datatype in Python 3.
if six.PY3:
    long = int
else:
    long = long