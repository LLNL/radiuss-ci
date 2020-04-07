#!/bin/bash

set -o errexit
set -o nounset

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

cp child-pipeline.yml ${machine}*.yml ${CI_PROJECT_DIR}
