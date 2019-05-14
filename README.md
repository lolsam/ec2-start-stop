### Lambda function automation to start & stop ec2 instances

Summary: use Lambda functions and CloudWatch together to automate the start & stop of ec2 instances at your desired time. Powering off servers during non-work hours will save hundreds of dollars.

1. Give Lambda a role to perform actions on ec2 instances and send logs to CloudWatch.
2. Create a Lambda function: ec2-start and paste the code
3. Create a Lambda function: ec2-stop and paste the code
- Note: paste the desired instance ids and region according to your needs.
4. Configure two CloudWatch events with target as the Lambda functions that were just created, and run it at your desired time.
  - CloudWatch > Events > Create event rule > Select when to start > Save as ec2-start
  - CloudWatch > Events > Create event rule > Select when to stop > Save as ec2-stop
5. Verify results and output by checking CloudWatch Logs 

![image](https://user-images.githubusercontent.com/30080956/57670542-5e2cf800-75d5-11e9-9655-e034d18b8f19.png)

  
