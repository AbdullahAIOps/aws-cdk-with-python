from aws_cdk import (
    # Duration,
    core,
    aws_lambda as _lambda,
    aws_s3 as s3
)
from constructs import Construct

class CdklabStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # Create an S3 bucket        
        bucket = s3.Bucket(self,"MyFirstBucket",versioned=True, removal_policy=core.RemovalPolicy.DESTROY)
        # Create a Lambda function        
        lambda_function = _lambda.Function(self, "MyLambdaFunction",
        runtime=_lambda.Runtime.PYTHON_3_8,
        handler="index.handler",
        code=_lambda.Code.from_asset("lambda"))
    # Grant the Lambda function read/write permissions to the bucket
        bucket.grant_read_write(lambda_function) 
