.. _getting_started:

===============
Getting Started
===============

Here are some preliminary steps to follow to setup Uberenv, depending on how you get Uberenv.

Getting Uberenv by clone/fetch/copy
===================================

1. Get uberenv.py script.

    Clone/Fetch/Copy it from `LLNL/uberenv <https://github.com/LLNL/uberenv>`_ into a ``uberenv`` directory, not as a submodule.

2. Edit uberenv/project.json.

    Set your project package name, and other parameters like Spack reference commit/tag (we suggest the latest release tag).

3. Add radiuss-spack-configs submodule.

    * Use ``git submodule add`` to get `radiuss-spack-config <https://github.com/LLNL/radiuss-spack-config>`_.

    * Create a symlink ``uberenv/spack_configs`` that points to ``radiuss-spack-configs``.

4. Add custom packages.

    If you need to make local modifications to your project package or a dependency package, you may put it in a corresponding directory in ``uberenv/packages/<package_name>/package.py``.

5. Make sure that <project>/package.py generates a hostconfig cmake file.

    This is usually done adding a specific stage to the package (see for example the hostconfig stage in Umpire, CHAI, etc.).


Getting Uberenv as a submodule
==============================

1. Get uberenv.py script.

    Use ``git submodule add`` to get `uberenv <https://github.com/LLNL/uberenv>`_ into a ``uberenv`` directory.

2. Edit .uberenv.json.

    Create ``.uberenv.json`` in a directory that is a parent of ``uberenv``. Set your project package name, and other parameters like Spack reference commit/tag (we suggest the latest release tag).

3. Add radiuss-spack-configs submodule.

    * Use ``git submodule add`` to get `radiuss-spack-config <https://github.com/LLNL/radiuss-spack-config>`_ in a second submodule or custom location.

    * In ``.uberenv.json`` set ``spack_configs_path`` to point to ``<some_path>/radiuss-spack-configs``.

4. Add custom packages.

    * If you need to make local modifications to your project package or a dependency package, you may put it in a corresponding directory: ``<some_path>/packages/<package_name>/package.py``.

    * In ``.uberenv.json`` set ``spack_packages_path`` to point to ``<some_path>/packages``

5. Make sure that <project>/package.py generates a hostconfig cmake file.

    This is usually done adding a specific stage to the package (see for example the hostconfig stage in Umpire, CHAI, etc.).
