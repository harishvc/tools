#Cypher Queries

##Table of Contents
  * [Cypher Queries](#cypher-queries)
    * [Q1: What is the schema](#q1-what-is-the-schema)
    * [Q2: Delete all nodes and relations](#q2-delete-all-nodes-and-relations)

##Q1: What is the schemea
$>:schema

##Q2: Delete all nodes and relations
$> MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r;

##Q3: Find nodes that don't have any relationship
$> start n=node(*) match n-[r?]-() where r is null return n

[![Analytics](https://ga-beacon.appspot.com/UA-55381661-1/tools/cmd/readme)](https://github.com/igrigorik/ga-beacon)
