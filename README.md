# Knowledge Graph using Social Media Posts

This project demonstrates the use of a knowledge graph to analyze social media posts and classify their sentiment. A knowledge graph is a powerful tool that represents information as nodes and edges, allowing for efficient querying and analysis of complex relationships.

## Overview

The project consists of the following components:

- `crawl_social_media.py`: This Python script provides functionality to crawl social media platforms and collect posts for analysis.

- `classify_posts.py`: This Python script demonstrates a classification algorithm to categorize social media posts based on their content or topic.

- `detect_sentiments.py`: This Python script showcases a sentiment analysis algorithm to determine the sentiment expressed in social media posts.

- `build_knowledge_graph.py`: This Python script builds a knowledge graph from the crawled social media data, incorporating post classification and sentiment information.

- `query_knowledge_graph.py`: This Python script allows querying the knowledge graph to retrieve sentiment and classification information for social media posts.

## How it Works

1. The `crawl_social_media.py` script is responsible for interacting with social media APIs and collecting relevant posts. It can be customized to target specific platforms and collect posts based on various criteria.

2. The `classify_posts.py` script takes the collected social media posts and applies a classification algorithm to categorize them based on their content or topic. This step helps organize the data and provide additional context for analysis.

3. The `detect_sentiments.py` script performs sentiment analysis on the social media posts. It uses natural language processing techniques to determine the sentiment expressed in the text, such as positive, negative, or neutral.

4. The `build_knowledge_graph.py` script combines the classified posts and sentiment information to construct a knowledge graph. Each post is represented as a node in the graph, and sentiment labels and classification tags are stored as edges, forming a rich representation of the social media data.

5. The `query_knowledge_graph.py` script allows querying the knowledge graph to retrieve sentiment and classification information for specific social media posts. It utilizes graph querying techniques to efficiently navigate the graph and extract relevant information.

## Example

Let's say we have a social media post that says:

"I just bought an HP laptop, and I love it. It's fast and reliable, and the keyboard is very comfortable to type on."

To classify the sentiment of this post, we can use the following formula:

Sentiment Score = Positive Words - Negative Words

We can create a list of positive and negative words and count how many of these words appear in the post. The sentiment score will be positive if there are more positive words and negative if there are more negative words. If the number of positive and negative words is the same, the sentiment score will be neutral.

For example, let's say our list of positive words includes "love," "fast," "reliable," and "comfortable," and our list of negative words includes "hate," "slow," "unreliable," and "uncomfortable." We count the number of positive and negative words in the post and get:

Positive Words: 4 (love, fast, reliable, comfortable)
Negative Words: 0

Sentiment Score = 4 - 0 = 4

Since the sentiment score is positive, we can classify this post as having a positive sentiment.


## Dependencies

The project requires the following dependencies:

- Python 3.x
- NetworkX: `pip install networkx`
- Matplotlib (optional for visualizations): `pip install matplotlib`

## Usage

1. Clone the repository: `[git clone https://github.com/your-username/knowledge-graph-social-media.git](https://github.com/itsmohitnamdeo/HP-Solve.git)`
2. Navigate to the project directory: `cd knowledge-graph-social-media`
3. Run the `crawl_social_media.py` script to collect social media posts.
4. Run the `classify_posts.py` script to categorize the collected posts.
5. Run the `detect_sentiments.py` script to perform sentiment analysis on the posts.
6. Run the `build_knowledge_graph.py` script to construct the knowledge graph.
7. Run the `query_knowledge_graph.py` script to query the knowledge graph for sentiment and classification information.

## Contributing

Contributions to this project are welcome. Please open an issue or submit a pull request with any improvements or suggestions.

# My Portfolio
- Portfolio: [https://itsmohitnamdeo.github.io](https://itsmohitnamdeo.github.io)

## Contact Information
- Mobile Number: 9131552292
- Email: namdeomohit198@gmail.com
- LinkedIn: [https://www.linkedin.com/in/mohit-namdeo](https://www.linkedin.com/in/mohit-namdeo)
