# Python AWS Lambda Function, using DevSpaces

Deploy an AWS lambda function using SAM.

## Environmental variables

Users will need to configure environmental variables to use this repo.  You will need to define your AWS credentials and region, and provide a name for the AWS CloudFormation [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html).

`export AWS_ACCESS_KEY_ID=AKAIIYOURKEY`

`export AWS_SECRET_ACCESS_KEY=qKIFEWFSECRETKEY`

`export PY_LAMBDA_FN_STACK='helloworldstack'`

## Local testing

Test the lambda function locally with `./test_lambda_local.sh`.  Running with no args will pass in `test_inputs/event.json` as the function input.  Pass a list of args to json files (i.e. `./test_local_lambda.sh test1.json test2.json` or `./test_local_lambda.sh test_inputs/*`) to test multiple inputs.

Local testing of arm64 containers on x86 requires Docker and emulation configuration.  See notes on [installing AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html).
`docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`

## Deploy

Use `deploy_to_aws.sh` to deploy to production.

```sh
PY_LAMBDA_FN_STACK='sjb-test-stack-2' ./build.sh
```

## Cleanup resources

Remove the stack using `clean.sh` to remove the current stack defined at `$PY_LAMBDA_FN_STACK`.  Be wary of stray resources when changing this variable.

## Editing the example

Add your own python code to `/python/app.py` in function `lambda_handler`.

## TODO

This probably should be parameterized in samconfig.toml
`export AWS_DEFAULT_REGION=us-east-1`
