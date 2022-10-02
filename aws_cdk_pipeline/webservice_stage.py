from constructs import Construct
from aws_cdk import Stage

from .aws_cdk_pipeline_stack import AwsCdkPipelineStack

class WebServiceStage(Stage):
  def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = AwsCdkPipelineStack(self, 'WebService')

    self.url_output = service.url_output
