###############################################################################
# Copyright (c) 2019, Lawrence Livermore National Security, LLC and other
# RADIUSS-CI project contributors. See top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT
###############################################################################

set(CMAKE_CXX_COMPILER "/usr/tce/packages/gcc/gcc-4.9.3/bin/g++" CACHE PATH "")

set(CUDA_TOOLKIT_ROOT_DIR "/usr/tce/packages/cuda/cuda-8.0" CACHE PATH "")
set(CMAKE_CUDA_COMPILER "/usr/tce/packages/cuda/cuda-8.0/bin/nvcc" CACHE PATH "")
