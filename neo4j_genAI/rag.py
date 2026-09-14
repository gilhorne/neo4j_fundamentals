# RETRIEVAL AUGMENTED GENERATION (RAG)

#  - an approach that enhances the responses of LLMs by providing them with relevent, up-to-date information retrieved from external sources.

# RAG helps generate more accurate and tailored responses, especially when the required information is not present in the LLM's training data.

# --- PROCESS --- 

# The RAG process typically involves three main steps:

# Understanding the User Query : The system first interprets the user’s input or question to determine what information is needed.

# Information Retrieval : A retriever searches external data sources (such as documents, databases, or knowledge graphs) to find relevant information based on the user’s query.

# Response Generation : The retrieved information is inserted into the prompt, and the language model uses this context to generate a more accurate and relevant response.

# --- GROUNDING ---

# The process of providing context to an LLM to improve the accuracy of its responses and reduce the likelihood of hallucinations.

# --- RETRIEVERS ---

# The retreiver is a key component of RAG process. 
# A retriever is responsible for searching and retrieving relevant information from external sources based on the user’s query.

# Neo4j supports various methods fro building retrievers:

# - Full-text search
# - Vector search
# - Text to Cypher

# --- DATA SOURCES ---

# Documents - Textual data sources, such as articles, reports, or manuals, that can be searched for relevant information.

# APIs - External services that can provide real-time data or specific information based on user queries.

# Knowledge Graphs - Graph-based respresentations of information that can provide context and relationships between entities.

# --- VECTOR RAG ---

# --- SEMANTIC SEARCH ---

# Semantic search aims to understand search phrases' intent and contextual meaning, rather than focusing on individual keywords.

# The results are tailored based on the term and the perceived intent.

# --- VECTORS ---

# You can represent data as vectors to perform semantic search.
# You can use vectors to represent many different types of data, including text, images, and audio.

# Vector dimensionality refers to the number of dimensions in a vector. 

# Higher dimensionality captures more fine-grained meaning but is more expensive computationally and similarly. 

# Lower dimensionality is faster and cheaper to compute, but offers less nuance.

# -- EMBEDDINGS --



