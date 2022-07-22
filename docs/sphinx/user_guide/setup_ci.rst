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

.. image:: images/UberenvWorkflowCI.pdf
   :scale: 32 %
   :alt: Once Spack and the build script setup, adopting the shared CI should be easy.
   :align: center

The third step in adopting RADIUSS CI infrastructure is to setup the CI.

Once you have provided the effort to adopt the first two steps, you should be
able to benefit from the shared CI infrastructure. In very complex scenario,
you will always be able to use the template as a starting point for a custom
implementation.

=================
Radiuss Shared CI
=================

Now that you have the ``build-and-test`` script, you simply have to follow
the documentation to setup the CI with mostly shared configuration.
