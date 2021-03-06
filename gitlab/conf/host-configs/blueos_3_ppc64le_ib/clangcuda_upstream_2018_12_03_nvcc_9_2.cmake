###############################################################################
# Copyright (c) 2019, Lawrence Livermore National Security, LLC and other
# RADIUSS-CI project contributors. See top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT
###############################################################################

set(CMAKE_CXX_COMPILER "/usr/tce/packages/clang/clang-upstream-2018.12.03/ibm/bin/clang++" CACHE PATH "")
set(CMAKE_C_COMPILER "/usr/tce/packages/clang/clang-upstream-2018.12.03/ibm/bin/clang" CACHE PATH "")

set(CMAKE_EXE_LINKER_FLAGS "-L/usr/tce/packages/cuda/cuda-9.2.148/lib64 -lcudart_static -lcudadevrt -lrt -ldl -lnvToolsExt -pthread -Wl,-rpath=/usr/tce/packages/clang/clang-upstream-2018.12.03/ibm/lib" CACHE PATH "")

