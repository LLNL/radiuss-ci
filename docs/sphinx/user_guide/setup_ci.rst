.. ##
.. ## Copyright (c) 2022, Lawrence Livermore National Security, LLC and
.. ## other RADIUSS Project Developers. See the top-level COPYRIGHT file for details.
.. ##
.. ## SPDX-License-Identifier: (MIT)
.. ##

.. _setup_ci-label:

**************************************
Setup the CI using the shared template
**************************************

The third step in adopting RADIUSS CI infrastructure is to setup the CI.

Once you have provided the effort to adopt the first two steps, you should be
able to benefit from the shared CI infrastructure. In very complex scenario,
you will always be able to use the template as a starting point for a custom
implementation.

=======================================
The same script for CI and local builds
=======================================

In `RAJA <https://github.com/LLNL/RAJA>`_, `Umpire
<https://github.com/LLNL/Umpire>`_ and `CHAI <https://github.com/LLNL/CHAI>`_,
the build-and-test script we described here is used in CI context to automate
both the installation of dependencies and the generation on the host-config
files.

.. ##All this is managed through a single script, that is usable outside of CI.

.. code-block:: bash

  $ SPEC="%clang@9.0.0 +cuda" scripts/gitlab/build_and_test.sh --deps-only

.. code-block:: bash

  $ HOST_CONFIG=<path_to>/<host-config>.cmake scripts/gitlab/build_and_test.sh

.. note::
  Making the CI scripts usable outside CI context is recommended since, by
  definition, it has been vetted. It also ensures that this script is usable in
  interactive mode, making it easier to test.

=================
RADIUSS Shared CI
=================

Now that you have the ``build-and-test`` script, you simply have to follow
the documentation to setup the CI with mostly shared configuration.
