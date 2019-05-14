import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g.; 'us-east-1'
region = 'us-west-2'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-07f89fe2d605d3ee9',
			 'i-0c908153b353e9eed',
			]
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'Stopped your instances: ' + str(instances)

#print message will appear in cloudwatch logs
