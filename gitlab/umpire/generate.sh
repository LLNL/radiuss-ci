#!/bin/bash

set -o errexit
set -o nounset

cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1

for file in *.yml
do
    cp ${file} ${CI_PROJECT_DIR}/radiuss-${file}
done
