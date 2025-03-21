Papis-dmenu
===========

|Pypi| |RTD| |Python| |ghbadge|


|gifimage|


This project implements a picker based on
`dmenu <https://tools.suckless.org/dmenu/>`_
for papis.

Usage
-----

Just use it as a
`picktool <https://papis.readthedocs.io/en/latest/configuration.html#config-settings-picktool>`_

::

  papis --set picktool dmenu open

Installation
------------

::

  pip install -e .

There is a version in PyPi

::

  pip3 install papis-dmenu

or

::

  sudo pip3 install papis-dmenu

TODO
----
- [ ] Gradually type the project
- [ ] Implement some more tests
- [ ] Document a bit


.. |TRAVIS| image:: https://travis-ci.org/papis/papis-dmenu.svg?branch=master
   :target: https://travis-ci.org/papis/papis-dmenu
.. |Python| image:: https://img.shields.io/badge/Python-3%2B-blue.svg
   :target: https://www.python.org
.. |Pypi| image:: https://badge.fury.io/py/papis-dmenu.svg
   :target: https://badge.fury.io/py/papis-dmenu
.. |RTD| image:: https://readthedocs.org/projects/papis-dmenu/badge/?version=latest
   :target: http://papis-dmenu.readthedocs.io/en/latest/?badge=latest
.. |gifimage| image:: https://papis.github.io/images/papis-dmenu.gif
   :target: http://papis-dmenu.readthedocs.io/en/latest/?badge=latest
.. |ghbadge| image:: https://github.com/papis/papis-dmenu/workflows/CI/badge.svg

