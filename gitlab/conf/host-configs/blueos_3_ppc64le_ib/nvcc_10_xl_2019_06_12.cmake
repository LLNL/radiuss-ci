###############################################################################
# Copyright (c) 2019, Lawrence Livermore National Security, LLC and other
# RADIUSS-CI project contributors. See top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT
###############################################################################

set(CMAKE_CXX_COMPILER "/usr/tce/packages/xl/xl-2019.06.12/bin/xlc++_r" CACHE PATH "" )

set(CUDA_TOOLKIT_ROOT_DIR "/usr/tce/packages/cuda/cuda-10.1.168" CACHE PATH "" )
set(CMAKE_CUDA_COMPILER "/usr/tce/packages/cuda/cuda-10.1.168/bin/nvcc" CACHE PATH "" )
