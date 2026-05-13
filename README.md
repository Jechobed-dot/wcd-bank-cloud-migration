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

## IAM Roles

IAM (Identity and Access Management) was used to control access to AWS resources in this project.

### Users Created:
- **Admin User**
  - Full administrative access
  - Used to build and manage all AWS resources

- **Contractor User**
  - Limited access to EC2
  - Can only interact with assigned virtual machine

- **Auditor User**
  - Read-only access
  - Used for monitoring and reviewing resources

### Roles and Permissions:
- Admin: `AdministratorAccess`
- Contractor: Limited EC2 permissions (start/stop/describe)
- Auditor: `ReadOnlyAccess`

This ensures a secure environment following the principle of least privilege.

---

## EC2 Instance

An EC2 virtual machine was created to simulate a contractor working environment.

### Configuration:
- Deployed inside a custom VPC
- Attached to a security group allowing controlled access
- Assigned an IAM role for AWS service interaction

The EC2 instance represents the core compute resource in this cloud migration project.

---

## Lambda Automation (Big Red Button)

AWS Lambda was used to automate EC2 instance management, acting as the “Big Red Button”.

### Functionality:
- Start EC2 instance
- Stop EC2 instance

### Trigger Input Example:
```json id="9zq2vm"
{
  "action": "start"
}
