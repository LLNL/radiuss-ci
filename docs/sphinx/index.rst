.. ## Copyright (c) 2019-2021, Lawrence Livermore National Security, LLC and
.. ## other RADIUSS Project Developers. See the top-level COPYRIGHT file for details.
.. ##
.. ## SPDX-License-Identifier: (MIT)

Welcome to RadiussCI's documentation!
=====================================

RADIUSS CI is a sub project form the RADIUSS initiative focusing on sharing
resource and documentation on Continuous Integration among RADIUSS projects.

LLNL's RADIUSS project (Rapid Application Development via an Institutional
Universal Software Stack) aims to broaden usage across LLNL and the open source
community of a set of libraries and tools used for HPC scientific application
development.

Uberenv and CI Shared Documentation
===================================

In RADIUSS, we designed a streamlined process to build your project with its
dependencies using Spack and Uberenv, and add a basic CI to test those builds
in Gitlab.

Before getting started, it is a good idea to read the `LC specific
documentation for Gitlab <https://gitlab.llnl.gov>`_. In particular, the
"Getting Started" and "Setup Mirroring" sub-pages *will help*.

The main steps are:

1. Get Uberenv. See :ref:`env`.
2. Setup CI. See :ref:`ci`.
3. Create build_and_test script.

.. toctree::
   :maxdepth: 2
   :caption: Shared Documentation

   uberenv
   ci
   spack-ci

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
