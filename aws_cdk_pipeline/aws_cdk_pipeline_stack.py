import aws_cdk.aws_lambda as lmb

from aws_cdk import Stack, CfnOutput # Duration,; aws_sqs as sqs,
from constructs import Construct
from os import path
import aws_cdk.aws_apigateway as apigw
#from aws_cdk import core


class AwsCdkPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))
        
        # alias = lmb.Alias(self, 'HandlerAlias',
        #     alias_name='Current',
        #     version=handler.current_version)

        gw = apigw.LambdaRestApi(self, 'Gateway',
            description='Endpoint for a simple Lambda-powered web service',
            # handler=handler)
            handler=handler.current_version)

        self.url_output = CfnOutput(self, 'Url',
            value=gw.url) 

        # TODO
        
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwsCdkPipelineQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
