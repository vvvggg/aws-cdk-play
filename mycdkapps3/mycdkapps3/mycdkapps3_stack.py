from constructs import Construct

import aws_cdk as cdk
import aws_cdk.aws_s3 as s3


class Mycdkapps3Stack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyCDKAnotherBucket", versioned=True)
