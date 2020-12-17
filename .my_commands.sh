#!/bin/bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# echo "$SCRIPTPATH"
cd
# reldir=`dirname "${BASH_SOURCE[0]}"`
# cd $reldir
# SCRIPTPATH=`pwd`

function create() {
    CURDIR=`pwd`
    cd "$SCRIPTPATH"
    python main.py "$@" "$CURDIR" || python3 main.py "$@" "$CURDIR"
    cd "$CURDIR"
}