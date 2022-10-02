#!/usr/bin/env python3
# import os

from os import environ
import aws_cdk as cdk
#from aws_cdk_pipeline.aws_cdk_pipeline_stack import AwsCdkPipelineStack
from aws_cdk_pipeline.pipeline_stack import PipelineStack

APP_ACCOUNT= environ.get("APP_ACCOUNT")
AWS_REGION = environ.get("AWS_REGION")

app = cdk.App()
#AwsCdkPipelineStack( app, "AwsCdkPipelineStack", env={ })

PipelineStack(app, "AwsCdkPipeline", env={ 'account': APP_ACCOUNT, 'region': AWS_REGION })

app.synth()
