#!/bin/bash

set -o errexit
set -o nounset

cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1

for file in *.yml
do
    cat ${file} >> ${CI_PROJECT_DIR}/radiuss-umpire-ci.yml
done
