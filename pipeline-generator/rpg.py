###############################################################################
# Copyright (c) 2019, Lawrence Livermore National Security, LLC and other
# RADIUSS-CI project contributors. See top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT
###############################################################################

import yaml

class CommonCI:
    """Default features for CI pipeline creation"""
    _machine_name = "undefined"

    def __init__(self,step_to_script,jobs_list):
        """Just requiring a list of targets for a default pipeline"""

        if self._machine_name is "undefined":
            print("The base class should not be directly instantiated")
            raise SystemExit

        self.jobs = jobs_list
        self.duration = 30
        self.pipeline = {}
        self.step_to_script = step_to_script
        self.steps = step_to_script.keys()

    def set_alloc_duration(self,duration):
        """Setting shorter duration (default 30 mins) can speed-up allocation
        time"""
        self.duration = duration

    def configure():
        """Should be reimplemented specifically to each cluster"""

    def make(self):
        """Create a pipeline with config and jobs"""
        machine = self._machine_name
        for job in self.jobs:
            toolchain=job[0]
            level=job[1]
            extras=job[2]
            for step in self.steps:
                key = "{}_{}_{}".format(machine,step,toolchain)
                value = dict()
                value.update({"extends":".{}_{}".format(machine,step)})
                value.update({"variables":{"COMPILER":toolchain}})
                if "allow_failure" in extras:
                    value.update({"allow_failure":True})
                # adding the job to the pipeline
                self.pipeline.update({key:value})

    def dump(self):
        """Dump the pipeline"""
        return yaml.dump(self.pipeline,default_flow_style=False,sort_keys=False)

    def write(self,filename):
        with open(filename,"w+") as file:
            file.write(yaml.dump(self.pipeline,default_flow_style=False,sort_keys=False))


class QuartzCI(CommonCI):
    """Class generating a CI pipeline for Quartz"""
    _machine_name = "quartz"

    def configure(self):
        """The default configuration for quartz"""
        self.pipeline = {}

        stages = ["allocate_resources"]
        for step in self.steps:
            stages.append(step)
        stages.append("release_resources")
        self.pipeline.update({
            'stages': stages
        })

        for step in self.steps:
            script = self.step_to_script[step]
            self.pipeline.update({
                '.quartz_{}_script'.format(step): {
                    'script': [
                        'echo $BUILD_QUARTZ_ALLOC_NAME',
                        'export JOBID=$(squeue -h --name=$BUILD_QUARTZ_ALLOC_NAME --format=%A)',
                        'echo $JOBID',
                        'srun $( [[ -n "$JOBID" ]] && echo "--jobid=$JOBID" ) -t 10 -N 1 -n 1 -c 4 {}'.format(script)
                    ]
                }
            })
        self.pipeline.update({
            '.quartz_common': {
                'variables': {
                    'CLUSTER': 'toss_3_x86_64_ib'
                },
                'tags': [
                    'shell',
                    'quartz'
                ],
                'except': {
                    'refs': ['/_qnone/'],
                    'variables': ['$CI_QUARTZ == "OFF"']
                }
            },
            'allocate_resources_build_quartz': {
                'extends': '.quartz_common',
                'stage': 'allocate_resources',
                'script': ['salloc -N 1 -c 36 -p pdebug -t {} --no-shell --job-name=$BUILD_QUARTZ_ALLOC_NAME'.format(self.duration)]
            },
            'release_resources_build_quartz': {
                'extends': '.quartz_common',
                'stage': 'release_resources',
                'script': [
                    'export JOBID=$(squeue -h --name=$BUILD_QUARTZ_ALLOC_NAME --format=%A)',
                    '([[ -n \"$JOBID\" ]] && scancel $JOBID)'
                ],
                'when': 'always'
            }
        })
        for step in self.steps:
            self.pipeline.update({
                '.quartz_{}'.format(step): {
                    'extends': [
                        '.quartz_common',
                        '.quartz_{}_script'.format(step)
                    ],
                    'stage': '{}'.format(step)
                }
            })


class LassenCI(CommonCI):
    """Class generating a CI pipeline for Lassen"""
    _machine_name = "lassen"

    def configure(self):
        """The default configuration for lassen"""
        self.pipeline = {}
        for step in self.steps:
            script = self.step_to_script[step]
            self.pipeline.update({
                '.lassen_{}_script'.format(step): {
                    'script': [
                        'lalloc 1 {}'.format(script)
                    ]
                }
            })
        self.pipeline = {
            '.lassen_common': {
                'variables': {
                    'CLUSTER': 'blueos_3_ppc64le_ib_p9'
                },
                'tags': [
                    'shell',
                    'lassen'
                ],
                'except': {
                    'refs': ['/_lnone/'],
                    'variables': ['$CI_LASSEN == "OFF"']
                }
            }
        }
        for step in self.steps:
            self.pipeline.update({
                '.lassen_{}'.format(step): {
                    'extends': [
                        '.lassen_common',
                        '.lassen_{}_script'.format(step)
                    ],
                    'stage': '{}'.format(step)
                }
            })


class ButteCI(CommonCI):
    """Class generating a CI pipeline for Butte"""
    _machine_name = "butte"

    def configure(self):
        """The default configuration for butte"""
        self.pipeline = {}
        for step in self.steps:
            script = self.step_to_script[step]
            self.pipeline.update({
                '.butte_{}_script'.format(step): {
                    'script': [
                        'lalloc 1 {}'.format(script)
                    ]
                }
            })
        self.pipeline = {
            '.butte_common': {
                'variables': {
                    'CLUSTER': 'blueos_3_ppc64le_ib'
                },
                'tags': [
                    'shell',
                    'butte'
                ],
                'only': {
                    'variables': ['$CI_BUTTE == "ON"']
                }
            }
        }
        for step in self.steps:
            self.pipeline.update({
                '.butte_{}'.format(step): {
                    'extends': [
                        '.butte_common',
                        '.butte_{}_script'.format(step)
                    ],
                    'stage': '{}'.format(step)
                }
            })
