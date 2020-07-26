Install
#######

Requirements
=============

The `pjpy` package requires the following dependencies:

* numpy
* scipy
* pjdata


Install
=======

The `pjpy` is available on the `PyPi <https://pypi.org/project/pjpy/>`_
. You can install it via `pip` as follow::

  pip install -U pjpy


It is possible to use the development version installing from GitHub::
  
  pip install -U git@github.com:end-to-end-data-science/pjpy.git

  
If you prefer, you can clone it and run the `setup.py` file. Use the following
commands to get a copy from Github and install all dependencies::

  git clone git@github.com:end-to-end-data-science/pjpy.git
  cd pjpy
  pip install .


Test and coverage
=================

If you want to test/test-coverage the code before to install::

  $ make install-dev
  $ make test-cov

Or::

  $ make install-dev
  $ pytest --cov=pjpy/ tests/

