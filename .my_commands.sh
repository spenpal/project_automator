#!/bin/bash

reldir=`dirname $0`
cd $reldir
directory=`pwd`

function create() {
    cd "$directory"
    python main.py "$@" 2>/dev/null || python3 main.py "$@" 2>/dev/null
}