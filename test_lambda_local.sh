#!/bin/bash

<<docblock
Execute sam local deploy on input test files.  If no arguments are
provided to this script it will run on test_inputs/event.json.
One or more arguments can also be specified to this script to
execute and test local deployments on multiple files.
docblock


sam build

events=$@
if [ -z "$events" ]; then
    events=test_inputs/event.json
fi

for event in $events; do
    # Execute sam and pretty print output
    output=$(sam local invoke -e $event)
    echo $event returned output:
    echo $output | \
        python -c "import json; \
        import sys; \
        js = json.load(sys.stdin); \
        print(json.dumps(js,indent=2))"
    # $output contains the statusCode - maybe
    # add some type of default checking, or
    # add expected response field to the input

done
