[//]: ###############################################################################
[//]: # Copyright (c) 2019, Lawrence Livermore National Security, LLC and other
[//]: # RADIUSS-CI project contributors. See top-level COPYRIGHT file for details.
[//]: #
[//]: # SPDX-License-Identifier: MIT
[//]: ###############################################################################

# LC GitLab Pipelines

Sharing experience using LC GitLab for its CI capability.

## Main configuration

###.gitlab-ci.yml

In order to retrieve all the projects submodules, only one variable is needed.

```yaml
variables:
GIT_SUBMODULE_STRATEGY: recursive
```

We can create as many stages as we want.

__Important:__

- Stages are executed sequentially
- A job can only _depend_ on another job if the latter belongs to a previous stage 

```yaml
stages:
- build
- test
```

Starting with a dot we can define job basics _properties_ (not an official name), which can be use to "extend" actual jobs (keyword extends).
Here, I’m specifying the build script location because it will be the same for all build jobs in this case.

```yaml
.build_script:
stage: build
script:
- .gitlab/scripts/build.sh
```

Then I complete the .yml config with includes. I chose to have an include per cluster, because most of the CI configuration depends on cluster type.

__Important:__

includes cannot refer to a location in a submodule

```yaml
include:
- local: .gitlab/ci/build_quartz.yml
```


## Configuration for a cluster
### .gitlab/ci/build_quartz.yml

In the .yml config file associated to quartz, I can define environment variables, tags and and rules specific to this cluster and to be share between build jobs.

In particular I define two ways to deactivate jobs on quartz:

- The ref name (typically the branch) contains "\_qnone"
- The variable CI\_QUARTZ is set to "OFF"

The first mechanism is convenient when triggering remotely. The second is convenient in the GitLab interface. Only one of them needs to be true to cancel the job.

```yaml
.quartz:
tags:
- shell
- quartz
except:
refs:
- /_qnone/
variables:
- $CI_QUARTZ == "OFF"
```


In the end, the build job for a specific compiler only contains a variable declaration, all the rest is shared.
In this case, the build script only rely on SYS\_TYPE and COMPILER environment variables to determine the configuration. This way I have only one build script.

__Important:__

Extends can accept several elements, but check the rules on how the extensions are merged here.

```yaml
build_quartz_clang_3_9_1:
extends: 
- .build_script
- .quartz
variables:
COMPILER: "clang_3_9_1"
```

__Note:__

It is also possible to chain extensions:

```yaml
# First level
.build_script:
stage: build
script:
- .gitlab/scripts/build.sh

.quartz:
tags:
- shell
- quartz

.lassen:
tags:
- shell
- lassen

# Second level
.build_on_quartz:
extends: 
- .build_script
- .quartz  

.build_on_lassen:
extends:
- .build_script
- .lassen

# Effective jobs
build_quartz_clang_3_9_1:
extends: .build_on_quartz
variables:
COMPILER: "clang_3_9_1"

build_quartz_intel_16_0_1:
extends: .build_on_quartz
variables:
COMPILER: "intel_16_0_1"

build_lassen_gcc_6_3_0:
extends: .build_on_lassen
variables:
COMPILER: "clang_3_9_1"

build_lassen_nvcc_clang_coral_2017_09_18:
extends: .build_on_lassen
variables:
COMPILER: "nvcc_clang_coral_2017_09_18"
```


## Concerning Lassen

Git version on lassen is old, to say the least. One concrete example is that by default, GitLab will try not to clone the entire repository but use shallow clone. This is not supported on Lassen.
As a consequence, if you want to run jobs on lassen, you should set GIT\_DEPTH variable to 0 (instead of 50 by default). It can be done in the interface, on in the CI configuration yaml files.

```yaml
variables:
GIT_DEPTH: 0
```

__Note:__ I haven’t tested if we can set this variable specifically for lassen jobs, it seems unlikely, unfortunately.


## Experimental stuff

###Sharing a resource allocation

On quartz, using slurm, it is possible to pre-allocate resources in a specific job and then having all the builds sharing this allocation.
This allows to have one CI job per build without multiplying resource allocations.

```yaml
variables:
QUARTZ_ALLOC_NAME: "unique_name_for_my_build_on_quartz_allocation"

stages:
- allocate
- build
- release
- test

.build_quartz_script:
script:
- export JOBID=$(squeue -h --name=${QUARTZ_ALLOC_NAME} --format=%A)
- srun $( [[ -n "${JOBID}" ]] && echo "--jobid=${JOBID}" ) -t 10 -N 1 -n 1 -c 4 scripts/gitlab/build.sh

allocate_resources_build_quartz:
tags:
- shell
- quartz
stage: allocate
script:
- salloc -N 1 -c 36 -p pdebug -t 10 --no-shell --job-name=$QUARTZ_ALLOC_NAME

# Note : make sure this is run even on build phase failure (when: always)
release_resources_build_quartz:
tags:
- shell
- quartz
stage: release
script:
- export JOBID=$(squeue -h --name=${QUARTZ_ALLOC_NAME} --format=%A)
- ([[ -n "${JOBID}" ]] && scancel ${JOBID})
when: always

.build_quartz:
tags:
- shell
- quartz
stage: build
extends: .build_quartz_script
```

__Important:__

The only information needed between the different jobs is the name of the allocation (no environment variable, no file).
It is important to ensure that the resource release job is always run, still a good estimation of the allocation time limit will optimize the time spent waiting for resources.
This is not possible of lassen-like systems as of today.
