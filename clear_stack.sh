#!/bin/bash
set -e

if [ -z "$PY_LAMBDA_FN_STACK" ]; then
    echo Environment variable PY_LAMBDA_FN_STACK is not defined
    exit 1
fi

sam delete --stack-name $PY_LAMBDA_FN_STACK
