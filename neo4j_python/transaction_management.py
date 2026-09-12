# -- TRANSACTIONS --
# Neo4j is an ACID-compliant transactional database, which means queries are executed as part of a single atomic transaction. This ensures your data operations are consistent and reliable.

# Transaction functions allow you to run multiple queries as a single transaction while accessing results immediately. 

# --- SESSIONS ---
# Open session object to manage the underlying database connections and methods for executing transactions.
with driver.session() as session: # opens session to database
# call transaction functions here

# In a multi-database instance, you can specify the database to use when creating a session using the database parameter.
    session.execute_read()
    session.execute_write()

# If the entire function runs successfully, the transaction is committed automatically. If any errors occur, the entire transaction is rolled back.

# These functions will also retry if the transaction fails due to a transient error, for example, a network issue.

# --- UNIT OF WORK PATTERNS ---
# a pattern that groups related operations into a single transaction

def create_person(tx,name,age): #tx = ManagedTransaction object
    result = tx.run("""
    CREATE (p:Person {name: $name, age: $age})
    RETURN p
    """,
    name=name, age=age)

# first argument is always tx, additional arguments are passed from the call to session.execute_read / session.execute_write

# the run() method on the ManagedTransaction object is called to execute the cypher statement. 

# --- MULTIPLE QUERIES AS SINGLE TRANSACTION ---

def transfer_funds(tx, from_account, to_account, amount):
    # deduct from first account
    tx.run( 
        "MATCH (a:Account {id: $from_}) SET a.balance = a.balance - $amount",
        from_=from_account, amount=amount
    )

    # add to second account
    tx.run(
        "MATCH (a:Account {id: $to_}) SET a.balance = a.balance + $amount",
        to=to_account, amount=amount
    )

# TRANSACTION STATE --- NOTE:
#Transaction state is maintained in the DBMS's memory, so be mindful of running too many operations in a single transaction. Break up very large operations into smaller transactions when possible.


with driver.session() as session: # open session to the database
    def get_anser(tx, answer): # define the transaction function
        result = tx.run("RETURN $answer AS answer", answer=answer) # execute the cypher query

        return result.consume() # returns the TransactionSummary object

    #call transaction function
    summary= session.execute_read(get_answer, answer=42)

    #output the summary:
    print(
        "Result available after", summary.result_available_after, # time it takes for the result to be available in milliseconds.
        "ms and consumed after", summary_result_consumed_after, "ms" # time it takes for the result to be consumed in milliseconds.
    )







