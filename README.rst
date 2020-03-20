=======================
Django Amazon Translate
=======================


.. image:: https://img.shields.io/pypi/v/django_amazon_translate.svg
        :target: https://pypi.python.org/pypi/django_amazon_translate

.. image:: https://img.shields.io/travis/leepa/django_amazon_translate.svg
        :target: https://travis-ci.org/leepa/django_amazon_translate

.. image:: https://readthedocs.org/projects/django-amazon-translate/badge/?version=latest
        :target: https://django-amazon-translate.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Utilities for Django to translate both Models and Django gettext files using
Amazon Translate.

Written because doing translation ends up getting forgotten and increasing
accessibility in projects should be easy for everyone.

* Free software: MIT license
* Documentation: https://django-amazon-translate.readthedocs.io.


Quick start
-----------

Add `django_amazon_translate` to the INSTALLED_APPS of your project.

Features
--------

* Translate via a management command to update po files with translated text.
* Translate via Django model translate where if a string is saved and has not
  been edited, it will go ahead and translate on save.

Credits
-------

This package was created with Cookiecutter_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
