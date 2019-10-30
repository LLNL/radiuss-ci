# RADIUSS CI

The RADIUSS project promotes and supports key High Performance Computing (HPC) open-source software developed at the LLNL. These tools and libraries cover a wide range of features a team would need to develop a modern simulation code targeting HPC plaftorms.

RADIUSS CI project aims at providing sensible default configurations and tools for GitLab CI.

## Getting Started

This project may be used as a submodule (for its tools) or remotely (for its configuration files).

### Prerequisites

The pipeline generator is a python tools which requires pyyaml@5.1 at least.

Example of python configuration:

```
virtualenv radiuss-ci
. radiuss-ci/bin/activate
pip install pyyaml
pip freeze | grep pyyaml
```

### Installing

This project requires no installation.

## Running the tests

TODO: Explain how to run python tests once available.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/LLNL/radiuss-ci/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

version: 1.0.0

TODO: Not even sure how to handle versioning here.

## Authors

David A Beckingsale, Adrien M Bernede

See also the list of [contributors](https://github.com/LLNL/radiuss-ci/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

All new contributions must be made under the MIT License.

See [LICENSE](https://github.com/LLNL/radiuss-ci/blob/master/LICENSE),
[COPYRIGHT](https://github.com/LLNL/radiuss-ci/blob/master/COPYRIGHT), and
[NOTICE](https://github.com/LLNL/radiuss-ci/blob/master/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE-793462


## Acknowledgments


