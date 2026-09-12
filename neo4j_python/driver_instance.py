# Import the driver and create instance:
from neo4j import GraphDatabase
from neo4j import Result
from neo4j import RoutingControl

NEO4J_URI = "neo4j+s://[IP_ADDRESS]"
NEO4J_USERNAME= "neo4j"
NEO4J_PASSWORD= "[PASSWORD]"

# create an instance of the neo4j driver: 
# Alternative: AsyncGraphDatabase.driver()
driver = GraphDatabase.driver(
    NEO4J_URI, #connection string for Neo4j database
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD) #Neo4j username and password
)

# Create one driver instance and share it acros your entire application.

# verify the connection is correct:
driver.verify_connectivity(    
# execute a query:
# runs cypher query to get the count of all nodes in database:
records, summary, keys = driver.execute_query(
    "RETURN COUNT {()} AS count"))

#Get first record:
# records contains a list of the rows returned
first = records[0]

#Print count entry
# keys from the "RETURN clause are accessed using bracket notation"
print(first['count'])

# release any resourses held by driver:
driver.close()

# --- TO CLOSE DATABASE --- 
# with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver:
#     result, summary, keys = driver.execute_query("RETURN COUNT {()} AS count")


# --- QUERY ---
cypher = """
MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS title, r.role AS role
"""

name = "Tom Hanks"

# Execute the query:
records, summary, keys = driver.execute_query(
    cypher, 
    name=name
)

# best practices is to use parameters within the query to avoid malicious code being injected into the Cypher statment.
print(keys)
print(summary)

# accessing results :
# use square brackets to access any item in the RETURN clause,
for record in records:
    print(record["title"])
    print(record["role"])


# --- TRANSFORMING RESULT ---
result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_= lambda result: [ #allows you to transform the result into an alternative format;
        f"Tom Hanks played {record["role"]} in {record["title"]}"
        for record in result
    ]
)
print(result)

# --- DATAFRAMES ---
driver.execute_query(
    cypher,
    name=name,
    result_tranformer_=Result.to_df
)

# --- READ/WRITE ---
driver.excute_query(
    cypher,
    name=name,
    result_transformer_=Result.to_df,
    routing_=RoutingControl.READ #use 'r'/READ or 'w'/WRITE
)

movie = "Toy Story"

# finds all movies with the specified title and returns
records, summary, keys = driver.execute_query(""" 
MATCH path = (person:Person)-[acted:ACTED_IN]->(movie:Movie {title:$title}) 
    RETURN path, person, acted, movie
    """, title=movie)

# Nodes are returned as a Node object
for record in records:
    node = record["movie"]

# Node object provides access to the element ID, labels and properties
print(node.element_id)
print(node.labels)
print(node.items())

# Accessing properties
print(node["name"])
print(node.get("name", "N/A")) #.get() allows you to define a defualt property if none exist

# --- RELATIONSHIPS ---
# relationships are returned as Relationship objects

acted_in = record["acted"]

print(acted_in.element_id) #provides access to the relationship element id.
print(acted_in.type) #returns type of relationship
print(acted_in.items()) #returns relationship properties as name_value pairs

#Accessing properties
print(acted_in['roles'])
print(acted_in.get("roles", "(Unknown)"))

print(acted_in.start_node) #returns the Node object at the start of the relationship
print(acted_in.end_node)   #returns the Node object at the end of the relationship

# --- PATHS ---
# a sequence of nodes and relationships returned as a path onject

path = record["path"]

print(path.start_node)
print(path.end_node)
print(len(path)) #returns number of nodes in path
print(path.relationships) #returns a tuple of Relationship objects within the path

#Use iter(path) tp iterate over the relationships in a path




