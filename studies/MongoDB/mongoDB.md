# MongoDB 
Source available, cross platform.


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


