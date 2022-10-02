# Overview

WIP.


mkdocs template based on:
   - https://realpython.com/python-project-documentation-with-mkdocs/
   - https://github.com/quantorconsulting/mkdocs_build_plantuml

AWS Pipeline based on:
   - [src](https://github.com/aws-samples/aws-deployment-pipeline-reference-architecture)
   - [doc](https://pipelines.devops.aws.dev/)

   - [path to git src for java](https://github.com/aws-samples/aws-deployment-pipeline-reference-architecture/tree/main/examples/cdk-application-pipeline)

   - [Faster Deployments with CDK Pipelines (video)](https://youtu.be/1ps0Wh19MHQ)
Available on: https://thsetz.github.io/aws_cdk_pipeline_mkdocs/
~

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

To install the python environment:

```console
foo@bar:~$ bash init.sh 
foo@bar:~$ source .venv/bin/activate
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your requirements.txt file and rerun the `init.sh` command.

## Useful commands

 * `make list`       list all Make targets
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

