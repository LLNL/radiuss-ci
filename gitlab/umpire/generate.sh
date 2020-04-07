#!/bin/bash

set -o errexit
set -o nounset

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

machine=${1:-""}
machines="butte quartz lassen"

# Build
if [[ -z ${machine} ]]
then
    echo "Script needs one parameter: machine name"
elif [[ ! ${machines} =~ (^|[[:space:]])${machine}($|[[:space:]]) ]]
then
    echo "Machine specified unknown"
    exit 1
fi

cp ${DIR}/child-pipeline.yml ${DIR}/${machine}*.yml ${CI_PROJECT_DIR}
