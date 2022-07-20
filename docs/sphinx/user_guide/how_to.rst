.. ##
.. ## Copyright (c) 2022, Lawrence Livermore National Security, LLC and
.. ## other RADIUSS Project Developers. See the top-level COPYRIGHT file for details.
.. ##
.. ## SPDX-License-Identifier: (MIT)
.. ##

.. _user_how_to-label:

******
How To
******

===========================
List the Spack specs tested
===========================

RADIUSS CI uses Spack specs to express the types of builds that should be
tested. We aim at sharing those specs so that projects build with similar
configurations. However we allow projects to add extra specs to test locally.

Shared specs for machine ``ruby`` can be listed directly in Radiuss-Shared-CI:

.. code-block:: bash

  cd radiuss-shared-ci
  git grep SPEC ruby-build-and-test.yml

Extra ``ruby`` specs, specific to one project, are defined locally to the
project in ``.gitlab/ruby-build-and-test-extra.yml``

.. code-block:: bash

  cd <project>
  git grep SPEC .gitlab/ruby-build-and-test-extra.yml

