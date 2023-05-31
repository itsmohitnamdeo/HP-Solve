import networkx as nx

# Read the knowledge graph from GraphML file
knowledge_graph = nx.read_graphml("graphs/knowledge_graph.graphml")

# Retrieve sentiment nodes from the knowledge graph
sentiment_nodes = [
    node
    for node, node_data in knowledge_graph.nodes(data=True)
    if node_data["type"] == "sentiment"
]

# Perform query on sentiment nodes
positive_sentiments = []
negative_sentiments = []
neutral_sentiments = []

for sentiment_node in sentiment_nodes:
    sentiment_id = sentiment_node
    sentiment = knowledge_graph.nodes[sentiment_node]["sentiment"]
    sentiment_score = knowledge_graph.nodes[sentiment_node]["sentiment_score"]
    post_id = sentiment_node.replace("sentiment_", "")
    content = knowledge_graph.nodes[f"{post_id}"]["content"]

    sentiment_info = {
        "Sentiment ID": sentiment_id,
        "Sentiment": sentiment,
        "Sentiment Score": sentiment_score,
        "Post ID": post_id,
        "Content": content,
    }

    if sentiment_score > 0:
        positive_sentiments.append(sentiment_info)
    elif sentiment_score < 0:
        negative_sentiments.append(sentiment_info)
    else:
        neutral_sentiments.append(sentiment_info)

# Prepare the output string
output_string = "Knowledge Graph Query Results:\n\n"
output_string += "1. Sentiments with Positive Score:\n"
for i, sentiment in enumerate(positive_sentiments, 1):
    output_string += f"- Sentiment ID: {sentiment['Sentiment ID']}\n"
    output_string += f"  - Sentiment: {sentiment['Sentiment']}\n"
    output_string += f"  - Sentiment Score: {sentiment['Sentiment Score']}\n"
    output_string += f"  - Post ID: {sentiment['Post ID']}\n"
    output_string += f"  - Content: {sentiment['Content']}\n\n"

output_string += "2. Sentiments with Negative Score:\n"
for i, sentiment in enumerate(negative_sentiments, 1):
    output_string += f"- Sentiment ID: {sentiment['Sentiment ID']}\n"
    output_string += f"  - Sentiment: {sentiment['Sentiment']}\n"
    output_string += f"  - Sentiment Score: {sentiment['Sentiment Score']}\n"
    output_string += f"  - Post ID: {sentiment['Post ID']}\n"
    output_string += f"  - Content: {sentiment['Content']}\n\n"

output_string += "3. Sentiments with Neutral Score:\n"
for i, sentiment in enumerate(neutral_sentiments, 1):
    output_string += f"- Sentiment ID: {sentiment['Sentiment ID']}\n"
    output_string += f"  - Sentiment: {sentiment['Sentiment']}\n"
    output_string += f"  - Sentiment Score: {sentiment['Sentiment Score']}\n"
    output_string += f"  - Post ID: {sentiment['Post ID']}\n"
    output_string += f"  - Content: {sentiment['Content']}\n\n"

# Save the output to a new file
output_file_path = "data/query_output.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(output_string)

print(f"Output saved to '{output_file_path}' file.")
