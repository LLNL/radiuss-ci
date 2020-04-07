#!/bin/bash

set -o errexit
set -o nounset

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cp ${DIR}/*.yml ${CI_PROJECT_DIR}
