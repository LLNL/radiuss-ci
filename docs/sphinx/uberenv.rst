.. _uberenv:

=============
Uberenv Guide
=============

This documents the usage of Uberenv for the developer. Indeed, uberenv can be used to generate custom host-config files, driven by a Spack spec. This host-config file will point to the dependencies installed with Spack, making the build process of the project straightforward.

Generating <Project> host-config files
======================================

This mechanism will generate a cmake configuration file that reproduces the configuration `Spack <https://github.com/spack/spack>`_ would have generated in the same context. It contains all the information necessary to build <Project> with the described toolchain.

In particular, the host-config file will setup:

* flags corresponding with the target required (Release, Debug).
* compilers path, and other toolkits (cuda if required), etc.
* paths to installed dependencies.

This provides an easy way to build <Project> based on `Spack <https://github.com/spack/spack>`_ and encapsulated in `Uberenv <https://github.com/LLNL/uberenv>`_.

Uberenv role
------------

Uberenv helps by doing the following:

* Pulls a blessed version of Spack locally.
* If you are on a known operating system (like TOSS3), we have defined compilers and system packages so you don't have to rebuild the world, _e.g._ CMake, or MPI.
* Overrides <Project> Spack packages with the local ones if any. (see ``scripts/uberenv/packages``).
* Covers both dependencies and project build in one command.

Uberenv will create a directory ``uberenv_libs`` containing a Spack instance with the required <Project> dependencies installed. It then generates a host-config file (``<config_dependent_name>.cmake``) at the root of <Project> repository.

Before to start
---------------

Machine specific configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the machine/system, <Project> may or may not provide a spack configuration allowing to use uberenv right away.

Check in the machines/systems supported in ``scripts/uberenv/spack_configs``. Per machine, <Project> will provide ``compilers.yaml``, ``packages.yaml``, and ``config.yaml``. The latter being possibly shared with other machines/systems.

Vetted specs
^^^^^^^^^^^^

Then, one can easily check what specs are tested in CI. For example, when looking for the gcc versions tested on quartz:

.. code-block:: bash

  git grep "SPEC" .gitlab/quartz-jobs.yml | grep "gcc"

MacOS case
^^^^^^^^^^

It is not trivial to provide a universal configuration for MacOS.
Instead, the developper will likely have to complete the ``packages.yaml`` file in order to adapt the location and version of externally installed dependencies.


Using Uberenv to generate the host-config file
----------------------------------------------

.. code-block:: bash

  $ python scripts/uberenv/uberenv.py

.. note::
  On LC machines, it is good practice to do the build step in parallel on a compute node. Here is an example command: ``srun -ppdebug -N1 --exclusive python scripts/uberenv/uberenv.py``

Unless otherwise specified Spack will default to a compiler. It is recommended to specify which compiler to use: add the compiler spec to the ``--spec=`` Uberenv command line option.

On blessed systems, compiler specs can be found in the Spack compiler files in our repository: ``scripts/uberenv/spack_configs/<system type>/compilers.yaml``.

Some options
^^^^^^^^^^^^

We already explained ``--spec=`` above:

* ``--spec=%clang@9.0.0``
* ``--spec=%clang@8.0.1+cuda``

The directory that will hold the Spack instance and the installations can also be customized with ``--prefix=``:

* ``--prefix=<Path to uberenv build directory (defaults to ./uberenv_libs)>``

Building dependencies can take a long time. If you already have a Spack instance you would like to reuse (in supplement of the local one managed by Uberenv), you can do so with the ``--upstream=`` option:

* ``--upstream=<path_to_my_spack>/opt/spack ...``

Using host-config files to build <Project>
------------------------------------------

When a host-config file exists for the desired machine and toolchain, it can easily be used in the CMake build process:

.. code-block:: bash

  $ mkdir build && cd build
  $ cmake -C  <path_to>/<host-config>.cmake ..
  $ cmake --build -j .
  $ ctest --output-on-failure -T test

CI usage
--------

In `RAJA <https://github.com/LLNL/RAJA>`_, `Umpire <https://github.com/LLNL/Umpire>`_ and `CHAI <https://github.com/LLNL/CHAI>`_, Uberenv is used in CI context to automate both the installation of dependencies and the generation on the host-config files.

All this is managed through a single script, that is usable outside of CI.

.. code-block:: bash

  $ SPEC="%clang@9.0.0 +cuda" scripts/gitlab/build_and_test.sh --deps-only

.. code-block:: bash

  $ HOST_CONFIG=<path_to>/<host-config>.cmake scripts/gitlab/build_and_test.sh

.. note::
  Making the CI scripts usable outside CI context is recommended since, by definition, it has been vetted. It also ensures that this script is usable in interactive mode, making it easier to test.

