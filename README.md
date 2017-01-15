# version

This module contains comparison functions for semantic version strings.

### Usage:

```python
Python 2.7.5
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import version as v
>>> v.greaterthan("2.1.3", "2.0.0")
True
>>> v.greaterthan_or_equal("1.1.1", "1.1.1")
True
>>> v.greaterthan("4.2.1", "1.2.4")
True
>>> v.lessthan("1.2.3", "0.2.4")
False
>>> v.lessthan_or_equal("1.1.2", "2.3.4")
True
>>> v.pessimistic("1.2.832", "1.2.4")
True
>>> v.pessimistic("1.3.0", "1.2.4")
False
```

With the general comparison functions you can mix and match between
two and three digit versions. 
e.g., 

```python
>>> v.greaterthan("3.2", "1.2.4")
True
```

With pessimistic comparison you must be consistent with version formats.
e.g.,

```python
>>> v.pessimistic("3.2", "3.0")
True
>>> v.pessimistic("4.3", "3.0")
False
>>> v.pessimistic("1.2.40", "1.2.5")
True
>>> v.pessimistic("2.2.40", "1.2.5")
False
```
