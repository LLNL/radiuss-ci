.. _uberenv:

=============
Uberenv Guide
=============

This documents the usage of Uberenv for the developer. Indeed, uberenv can be used to generate custom host-config files, driven by a Spack spec. This host-config file will point to the dependencies installed with Spack, making the build process of the project straight-forward.

Generating <Project> host-config files
======================================

This mechanism will generate a cmake configuration file that reproduces the configuration `Spack <https://github.com/spack/spack>` would have generated in the same context. It contains all the information necessary to build <Project> with the described toolchain.

In particular, the host config file will setup:
* flags corresponding with the target required (Release, Debug).
* compilers path, and other toolkits (cuda if required), etc.
* paths to installed dependencies. However, <Project> only directly depends on CMake.

This provides an easy way to build <Project> based on `Spack <https://github.com/spack/spack>` and encapsulated in `Uberenv <https://github.com/LLNL/uberenv>`_.

Uberenv role
------------

Uberenv helps by doing the following:

* Pulls a blessed version of Spack locally
* If you are on a known operating system (like TOSS3), we have defined compilers and system packages so you don't have to rebuild the world (CMake typically in <Project>).
* Overrides <Project> Spack packages with the local one if it exists. (see ``scripts/uberenv/packages``).
* Covers both dependencies and project build in one command.

Uberenv will create a directory ``uberenv_libs`` containing a Spack instance with the required <Project> dependencies installed. It then generates a host-config file (``<config_dependent_name>.cmake``) at the root of <Project> repository.

Using Uberenv to generate the host-config file
----------------------------------------------

.. code-block:: bash

  $ python scripts/uberenv/uberenv.py

.. note::
  On LC machines, it is good practice to do the build step in parallel on a compute node. Here is an example command: ``srun -ppdebug -N1 --exclusive python scripts/uberenv/uberenv.py``

Unless otherwise specified Spack will default to a compiler. It is recommended to specify which compiler to use: add the compiler spec to the ``--spec`` Uberenv command line option.

On blessed systems, compiler specs can be found in the Spack compiler files in our repository: ``scripts/uberenv/spack_configs/<System type>/compilers.yaml``.

Some examples uberenv options:

* ``--spec=%clang@9.0.0``
* ``--spec=%clang@8.0.1+cuda``
* ``--prefix=<Path to uberenv build directory (defaults to ./uberenv_libs)>``

It is also possible to use the CI script outside of CI:

.. code-block:: bash

  $ SPEC="%clang@9.0.0 +cuda" scripts/gitlab/build_and_test.sh --deps-only

Building dependencies can take a long time. If you already have a Spack instance you would like to reuse (in supplement of the local one managed by Uberenv), you can do so changing the uberenv command as follow:

.. code-block:: bash

  $ python scripts/uberenv/uberenv.py --upstream=<path_to_my_spack>/opt/spack

Using host-config files to build <Project>
------------------------------------------

When a host-config file exists for the desired machine and toolchain, it can easily be used in the CMake build process:

.. code-block:: bash

  $ mkdir build && cd build
  $ cmake -C  <path_to>/<host-config>.cmake ..
  $ cmake --build -j .
  $ ctest --output-on-failure -T test

It is also possible to use the CI script outside of CI:

.. code-block:: bash

  $ HOST_CONFIG=<path_to>/<host-config>.cmake scripts/gitlab/build_and_test.sh