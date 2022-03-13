from terratest import TerraTest
import boto3
client = boto3.client('lambda')
my_session = boto3.session.Session()
region = my_session.region_name

class TestModule(TerraTest):
    module_dir = "../examples/aws_personal_health_dashboard"
    def test_lambda(self):
        lambda_name = self.terraform_outputs['lambda_function_name']
        response = client.get_function(FunctionName=lambda_name)
        lambda_response_name = response["Configuration"]["FunctionName"]
        print("Lambda Name: " + str(lambda_response_name))
        assert lambda_name == lambda_response_name, 'Lambda function not created'   