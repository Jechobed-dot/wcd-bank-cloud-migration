# WCD Bank Cloud Migration Project (AWS DevOps Simulation)

## Project Overview
This project simulates the migration of WCD Bank’s on-premises infrastructure to AWS cloud services. The goal is to design and implement a secure, scalable, and automated cloud environment using AWS services.

A key feature of this project is a “Big Red Button” automation system that allows starting and stopping an EC2 virtual machine using AWS Lambda.

---

## Architecture Overview
The cloud environment consists of the following components:

- **VPC** – Isolated network environment
- **Subnets** – Public and private network segmentation
- **Internet Gateway** – Enables internet access
- **EC2 Instance** – Virtual machine for contractor use
- **IAM Roles and Users** – Access control and security
- **Lambda Function** – Automation for EC2 start/stop (Big Red Button)
- **CloudWatch** – Monitoring and logs (optional)

---

## Big Red Button (Lambda Automation)
A Lambda function is used to control the EC2 instance.

It performs two actions:
- Start EC2 instance
- Stop EC2 instance

### Example Test Event:
```json
{
  "action": "start"
}

{
  "action": "stop"
}

---

## Other Resources used to carry this out
IAM Roles
Admin User: Full access to all AWS services
Contractor User: Limited access to EC2 instance only
Auditor User: Read-only access for monitoring and review
EC2 Instance
A virtual machine deployed inside a custom VPC
Used by contractors for work tasks
Controlled using Lambda automation
Testing Process
Deploy Lambda function
Go to Lambda console → Test tab
Send "start" or "stop" event
Check EC2 console to confirm state change
Tools Used
AWS EC2
AWS VPC
AWS IAM
AWS Lambda
AWS CloudWatch
GitHub
Conclusion

This project demonstrates a basic cloud migration setup with infrastructure provisioning, identity management, and automation using AWS services. It simulates real-world DevOps practices such as Infrastructure as Code concepts, role-based access control, and event-driven automation.
