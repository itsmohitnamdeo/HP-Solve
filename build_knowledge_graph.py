import json
import networkx as nx

# Load sentiment data from JSON file
with open("data/sentiment_data.json", "r") as file:
    sentiment_data = json.load(file)

# Build the knowledge graph based on sentiment data
knowledge_graph = nx.Graph()

# Add nodes to the graph
for sentiment in sentiment_data:
    post_id = sentiment["post_id"]
    sentiment_id = f"sentiment_{post_id}"
    knowledge_graph.add_node(post_id, type="post", content=sentiment["content"])
    knowledge_graph.add_node(sentiment_id, type="sentiment", sentiment=sentiment["sentiment"],
                             sentiment_score=sentiment["sentiment_score"])
    
    # Add optional keys if they exist in the sentiment data
    if "timestamp" in sentiment:
        knowledge_graph.nodes[post_id]["timestamp"] = sentiment["timestamp"]
    if "category" in sentiment:
        knowledge_graph.nodes[post_id]["category"] = sentiment["category"]

    # Add edges between sentiment and post
    knowledge_graph.add_edge(sentiment_id, post_id)

# Save the knowledge graph as a GraphML file
nx.write_graphml(knowledge_graph, "graphs/knowledge_graph.graphml")

print("Knowledge graph built and saved successfully.")
