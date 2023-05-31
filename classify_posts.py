import json

def classify_posts(posts):
    positive_words = ["love", "great", "excellent"]
    negative_words = ["hate", "terrible", "awful"]
    
    classified_posts = []
    
    for post in posts:
        sentiment_score = 0
        positive_count = 0
        negative_count = 0
        
        content = post["content"]
        words = content.lower().split()
        
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
        
        sentiment_score = positive_count - negative_count
        
        if sentiment_score > 0:
            sentiment = "positive"
        elif sentiment_score < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        classified_post = {
            "post_id": post["post_id"],
            "username": post["username"],
            "content": content,
            "timestamp": post["timestamp"],
            "sentiment": sentiment
        }
        
        if "category" in post:
            classified_post["category"] = post["category"]
        
        classified_posts.append(classified_post)
    
    return classified_posts


# Load the posts from the data/posts.json file
with open("data/posts.json", "r") as file:
    posts = json.load(file)

# Classify the posts
classified_posts = classify_posts(posts)

# Save the classified posts to the data/classified_posts.json file
with open("data/classified_posts.json", "w") as file:
    json.dump(classified_posts, file, indent=4)

# Print the classified posts
print(json.dumps(classified_posts, indent=4))
