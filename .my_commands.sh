#!/bin/bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# reldir=`dirname $0`
# cd $reldir
# directory=`pwd`

function create() {
    cd "$SCRIPTPATH"
    python main.py "$@" 2>/dev/null || python3 main.py "$@" 2>/dev/null
}