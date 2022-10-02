from os import environ
from aws_cdk import Stack, SecretValue
from constructs import Construct
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

from .webservice_stage import WebServiceStage

APP_ACCOUNT= environ.get("APP_ACCOUNT")
AWS_REGION = environ.get("AWS_REGION")
REPOSITORY = environ.get("REPOSITORY")
REPOSITORY_OWNER = environ.get("REPOSITORY_OWNER")

REPOSITORY_SECRET_NAME_IN_SECRETS_MANAGER=environ.get("REPOSITORY_SECRET_NAME_IN_SECRETS_MANAGER")


class PipelineStack(Stack):
  #def __init__(self, scope: core.Construct, id: str, **kwargs):
  def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source_artifact = codepipeline.Artifact()
    cloud_assembly_artifact = codepipeline.Artifact()

    branch = 'master'
    gitHubUsernameRepository = 'thsetz/aws_cdk_pipeline_mkdocs'
 
    source = pipelines.CodePipelineSource.git_hub(f'{REPOSITORY_OWNER}/{REPOSITORY}', 'master', 
          #authentication = SecretValue.secrets_manager(REPOSITORY_SECRET_NAME_IN_SECRETS_MANAGER),
          authentication = SecretValue.secrets_manager("github-access-token-secret2"),
         )
    
    synth_step = pipelines.ShellStep("Synth", 
                    input=source,
                    commands = [ 'npm install -g aws-cdk',
                           'pip install --upgrade pip',
                           'pip install -r pinned_requirements.txt',
                           'pytest tests', 
                           'cdk synth',]
                    )
    

    pipeline = pipelines.CodePipeline(self, 'Pipeline',
      pipeline_name='WebinarPipeline',
      synth=synth_step
      )
    

    
      #synth=pipelines.SimpleSynthAction(
      #  source_artifact=source_artifact,
      #  cloud_assembly_artifact=cloud_assembly_artifact,
      #  install_command='npm install -g aws-cdk && pip install -r requirements.txt',
      #  build_command='pytest unittests',
      #  synth_command='cdk synth'))

    pre_prod_app = WebServiceStage(self, 'Pre-Prod', env={
      'account': APP_ACCOUNT,
      'region': AWS_REGION,
    })
    # pre_prod_stage = pipeline.add_application_stage(pre_prod_app)
    pre_prod_stage = pipeline.add_stage(pre_prod_app)
    #pre_prod_stage.add_actions(pipelines.ShellScriptAction(
    pre_prod_stage.add_pre(pipelines.ShellStep("Integration",
      # action_name='Integ',
      # run_order=pre_prod_stage.next_sequential_run_order(),
      # additional_artifacts=[source_artifact],
      commands=[
        'pip install -r requirements.txt',
        'pytest integtests',
      ],
      # use_outputs={ 'SERVICE_URL': pipeline.stack_output(pre_prod_app.url_output),
      ))

    # pipeline.add_application_stage(WebServiceStage(self, 'Prod', env={
    pipeline.add_stage(WebServiceStage(self, 'Prod', env={
      'account': APP_ACCOUNT,
      'region': 'eu-central-1',
    }))
