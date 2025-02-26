Install
#######

Requirements
=============

The pymfe package requires the following dependencies:

* numpy
* scipy
* scikit-learn
* pandas
* patsy


Install
=======

The pymfe is available on the `PyPi <https://pypi.org/project/pymfe/>`_. You can install it via `pip` as follow::

  pip install -U pymfe


It is possible to use the development version installing from GitHub::
  
  pip install -U git+https://github.com/ealcobaca/pymfe.git

  
If you prefer, you can clone it and run the `setup.py` file. Use the following
commands to get a copy from Github and install all dependencies::

  git clone https://github.com/ealcobaca/pymfe.git
  cd pymfe
  pip install .


Test and coverage
=================

You want to test/test-coverage the code before to install::

  $ make test-cov

Or::

  $ pytest --cov=pymfe/ tests/
