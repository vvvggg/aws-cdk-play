import aws_cdk as core
import aws_cdk.assertions as assertions

from mycdkapps3.mycdkapps3_stack import Mycdkapps3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in mycdkapps3/mycdkapps3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Mycdkapps3Stack(app, "mycdkapps3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
