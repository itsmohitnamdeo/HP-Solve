import json

positive_words = ["love", "fast", "reliable", "comfortable"]
negative_words = ["hate", "slow", "unreliable", "uncomfortable"]

# Load the classified posts data
with open("data/classified_posts.json") as file:
    classified_posts = json.load(file)

# Perform sentiment analysis on each post
sentiment_data = []
for post in classified_posts:
    text = post["content"].lower()
    positive_count = sum(text.count(word) for word in positive_words)
    negative_count = sum(text.count(word) for word in negative_words)
    sentiment_score = positive_count - negative_count
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    sentiment_data.append({
        "post_id": post["post_id"],
        "content": post["content"],
        "sentiment": sentiment,
        "sentiment_score": sentiment_score
    })

# Sort the sentiment data based on sentiment score in descending order
sentiment_data = sorted(sentiment_data, key=lambda x: x["sentiment_score"], reverse=True)

# Save the arranged sentiment data
with open("data/sentiment_data.json", "w") as file:
    json.dump(sentiment_data, file, indent=4)
