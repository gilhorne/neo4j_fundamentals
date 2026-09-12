# --- ERROR HANDLING ---
#import Neo4jError exception class:
from neo4j.exceptions import Neo4jError

try:
    pass # Placeholder for Cypher statement
    # run Cypher statement
except Neo4jError as e:
    print(e.code)
    print(e.message)
    print(e.gql_status)

# gql_status propety contains an error code that corresponds to an error in the ISO GQL standard.

# --- UNIQUE CONSTRAINT VIOLATIONS ---

# CYPHER:
""" CREATE CONSTRAINT unique_email IF NOT EXISTS
FOR (u:User) REQUIRE u.email IS UNIQUE"""

# if a cypher statement violates a constraint, Neo4j will raise a ConstraintError.

# PYTHON:
#import Neo4j constraint error classes:
from neo4j.exceptions import ConstraintError

#define constraint:
def create_user(tx, name, email):
    try: # Creates user with unique email constraint
        result = tx.run("""
        CREATE (u:User {name: $name, email: $email})
        RETURN u
        """, name = name, email = email)

    except ConstraintError as e: #Catch ConstraintError exception class
        print(e.code)
        print(e.message)
        print(e.gql_status)
