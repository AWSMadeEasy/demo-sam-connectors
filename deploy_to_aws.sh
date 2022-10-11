#!/bin/bash
set -e  # Exit on error
set -v  # Print command, with variables
set -x  # Print commands, with variables filled in

sam build
sam deploy --stack-name $PY_LAMBDA_FN_STACK --resolve-s3

