#!/bin/bash

# SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
reldir=`dirname $0`
cd $reldir
directory=`pwd`

function create() {
    # shellcheck disable=SC2164
    cd "$directory"
    python main.py "$@"
}