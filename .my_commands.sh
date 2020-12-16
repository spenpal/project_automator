#!/bin/bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "$SCRIPTPATH"
cd
# reldir=`dirname "${BASH_SOURCE[0]}"`
# cd $reldir
# directory=`pwd`

function create() {
    cd "$SCRIPTPATH"
    python main.py "$@" || python3 main.py "$@"
}