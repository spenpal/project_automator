#!/bin/bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

function create() {
    # shellcheck disable=SC2164
    cd "$SCRIPTPATH"
    python3 main.py "$@"
}