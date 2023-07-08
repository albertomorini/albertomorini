# AWS on w3school

## EC2 Autoscaling

Auto scaling can be added as a buffer on top of your instances.

- minimum capacity: of instance that will always be running
- desidered number: of instances in the scaling group (minimum if not specified)
- maximum capacity

### Load balancing

Single point of contact for incoming web traffic, to traffic hits the Load Balancer first then, spreading out the load between the resources.
- It ensures that one resource won't get overloeaded

### Monolithic App & Microservices
- applications made of multiple components
- the components communicate with each other
- the communication can transmit data, fulfill request, and keep the application running.

#### Monoligic
Architecture with tightly coupled components, like database, servers.
Can be vulnerable if one components fails (worst scenario, whole service goes down).

#### Microserfices
Can help to maintain the service if one component fails.
The components are not tightly coupled.
Two services that can make this integration: AWS Simple Notification Service - AWS Simple Queue service

##### SNS - simple notitifaction service
Distributed system and microservices can decoupled with messaging between them through AWS SNS.

different type of endpoints:
- HTTP
- Email/Email-JSON
- AWS SQS
- Applications
- AWS lambda
- SMS (depending on region)

push messages to subscribers

##### SQS - simple queue service
queuing system, receives have to pull the messages to be processed and deleted from the queue


## SERVER LESS:

with EC2 you have to maintain the server, deploy your code, provision of virtual server instances

> AWS cloud Lambda is the serverless service of aws	
Pay what you use translates to that you only pay when your code is running.

How it works:
1. Deploy your code to Lambda
2. Make the code ready to trigger an event
3. The code only runs when triggered
4. Pay only when your code is running

Used to: build and deploy apps, monitor and maintain apps

Can run: NodeJS, Python, Java, Kotlin, C# etc.

### Containers

let your package code in a single object, isolating the code and removing the dependencies to other components.
~ essential concept in mocro service architectures.

Containerized approach: the container remains consistent regardless of deployment

is important to design for scale when using containers --> there could be tens of hosts with hundreds of containers as the environment grows.



## Regions

- Data regulations -> government's law etc
- customer proximity -> a near one is faster
- service availability
- pricing


## AWS Elastic Beanstalk
a web infrastructure management service.
handles deployment and scaling for web app and services.

deploys the resources necessary to perform:
- adjust capacity
- load balancing
- automatic scaling
- application health monitor

### CloudFormation
- you can treat your infrastucture as code


## AWS VPC
You can isolate your AWS resouyrces in an isolated network.
The boundaries created around the resourece let AWS restrict the network traffic.

- resources can be organized in subnets
- public traffic can be allowed to you VPC, by InternetGateway
	- encrypts the traffic internet

### AWS direct connect
Let you make a dedicated private connection between DataCenter and VPC.

The link is not shared with others, only you and your data can travel through the connection.


### subnet and access

Subnet is a section of a VPC, allows to group resources.

Can be both public and private subnets

**Network access control list**

Is a firewall that controls the traffic (at subnet level), both inbound and 
outbound.

#### Stateless packet filtering
- have no memory and will forget the request once checked
- their job is to check the packets that go in and out and use the set rules to approve or deny them

**stateful**: just remember the actiton taken with Packets in the past 


## AWS route 53

Route 53 is a DNS web service, it routes end-users to internet apps hosted in AWS.

Connects users and thei rqeust to AWS resources and external resources.


### Example with CloudFront

The company has 3 EC2 instances in auto scaling group, the group is attached to an application load balancer

1. User request data from the website application
2. Route 53 uses DNS resolution to identify the IP address
3. data is sent back to the user
4. user request is sent to the nearest Edge location through CloudFront
5. CloudFront connects to the application load balancer
6. the load balancer sends the packet to the EC2 instance


## AWS STORAGE

###EBS
- elastic block store, is a service that provides storage volumes.
- Important to backup the data with AWS EBS snapshots

**Snasphost**: is incremental data backup.
The first backup of a volume backups all data, the next ones copies only a block of data that has changed since previous snapshot.

Data is stored as blocks, faster performance than AWS S3, data can be modified.

### S3

Object-level storage, allows uploading any type of file and can set access permission to a file.

**Object-level**:
- Data = any type of file
- Metadata = information aboout what the data is
- key = unique identifier


There are many types of S3.
- One zone-ia: stores data in one availability zone
- s3 intelligent-tiering: moves the objet to S3 standard-IA if it not accessed for 30 days 
- glacier: the cheapest and slower one

data stored as object, not suffer loss or corruption for a long time, data cannot be modified (unless reuploaded)


### Dynamo

is a non-relational, NoSQL database.

Support simple structured data, store data in documents, cheaper than AWS RDS and faster.

> AWS RDS supports complex data, stores data in database tables


### Redshift

is a big data analytics service, gather information from many source and assists getting connection across data.

- powered by SQL, AWS-designed hardware and machine learning.
- Takes source from: operational database, S3 data lake, BI and anlytics apps, data marketplaces

### AWS neptune
a graph database service, create graph from data for various pourposes.
