# MongoDB 
Source available, cross platform.

Stores data in JSON-like documents, making the database flexible and scalable.<br>
**IMPORTANT**: Be careful, in Mongo doesn't create a Database and/or a collection (table) untill it gets content.


## NoSQL: 

*NoSQL database are usually adopted on big data and real-time application.*

The design include simplicity of design and simpler horizontal scaling (adding more istances) to cluster of machine.<br>
The data structure adopted on NoSQL databases sometimes makes faster opration compared on relational databases.

### Key-value store
Uses associative array (dictionary) as their fundamental data model; where data is rappresented as a collective of data-value pairs.
Key-value model can be extended to discretely order model that mantains keys in lexicographic order.

### Graph
Designed for data whose relations are well rappresented as a graph, consisting of element connected by a finite number of relations.
> eg. social relations, public transport link 

**MongoDB use JSON-like documents with optional schemas.**


## Main features

- **Ad hoc queries**: queries can be made with field, range query, regular-expression seraches; and can return specific fields of documents, or random sample of results of given size.

- **Indexing**: documents can be indexed with primary and secondary indices.

- **Replication**: a set of replica sets consists of two or more copies of the data.
All the write and read are made on the primary replica by default.
When the primary replica fails, the replica set automatically conducts an election process to determine which secondary should become primary.
    > in mongo there's a daemon called 'arbiter' which has a single responsability: resolve the election of the new primary.
As a consequence, an idealized distributed MongoDB deployments require 3+ separate server even with one just primary and secondary. 

- **Load balancing**: Mongo scales horizzontally, using sharding (horizontal partition of data on a db), the user chooses a sharding key which determines how data will be distribuited.
The data is splitted into ranges (based on the key) and distribuited across multiple shards (a master with more replicant).

- **Aggregation**: Three kind of aggregation -> pipeline, map-reduce, single-purpose.
    Pipeline provides better performance of map-reduce.

- **Javascript**: can be used on in queries, aggregation functions (MapReduce) and sent directly to the database to be executed.

- **Capped collection**: are fixed-size collections, this type maintains insertion order and once the size has been reached behavevs like a circular queue.

- **Transaction**: MongoDB claims to support multi-document ACID transaction, but, that's false as MongoDB violates snapshot isolation.


## Edition

- *Mongo DB Community Server*: free and available for mac/windows/linux
- *Mongo DB Enterprise Server*: you need a MongoDB enterprise advanced subscription
- *Mongo DB Atlas*: runs on AWS, Microsoft azure, Google Cloud Platform.

## Usage, w/ Docker
$ docker run -d -p 27017:27017 --name myMongo -v mongo-data:/data/db mongo:latest
