### EC2 Autoscaling

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


---------------------------------------------
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



