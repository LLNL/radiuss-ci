##############################################################################
# Copyright (c) 2016-19, Lawrence Livermore National Security, LLC and Umpire
# project contributors. See the COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)
##############################################################################
set(CMAKE_CXX_COMPILER "/usr/tce/packages/clang/clang-9.0.0/bin/clang++" CACHE PATH "")
set(CMAKE_CXX_FLAGS "-stdlib=libc++ -DGTEST_HAS_CXXABI_H_=0" CACHE PATH "")
set(CMAKE_C_COMPILER "/usr/tce/packages/clang/clang-9.0.0/bin/clang" CACHE PATH "")
set(CMAKE_C_FLAGS "-DGTEST_HAS_CXXABI_H_=0" CACHE PATH "")
