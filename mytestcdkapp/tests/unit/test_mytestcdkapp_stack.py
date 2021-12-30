import aws_cdk as core
import aws_cdk.assertions as assertions

from mytestcdkapp.mytestcdkapp_stack import MytestcdkappStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mytestcdkapp/mytestcdkapp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MytestcdkappStack(app, "mytestcdkapp")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
