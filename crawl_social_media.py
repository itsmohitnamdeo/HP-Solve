import json
import facebook

# Facebook API credentials
access_token = "EAAXbF86DDZCgBABZBkstT2D96rJoDFrUKZClVZBOZA8Q4WQI1Os8TepUDCaZBEQlzS5rysGTyQByec3WVGoux3bxPzR0lNGnsSiVfrKnwYFH9zzfbrRSpHsPO4yYN5NtrweKHPLuSYv8RtJ53Y4rzFvM1HRP8iUz44FPU0nctNSEly6BEKB8R6QGdxZBoknZAFdpY2Daz6Y4rzMFrihLLUimMnh5NkZCTONqEcw6EVZANGhYcw6alEBustvxN2ZBezO2pIZD"
user_id = "1697590277346059"

# Create a GraphAPI object
graph = facebook.GraphAPI(access_token)

# Define the query parameters
query = "HP printer"
limit = 10

# Request posts from the HP page
response = graph.request(f"{user_id}/feed", args={"q": query, "limit": limit})

# Extract the data from the response
posts = response.get("data", [])

# Process the posts to get the desired output format
formatted_posts = []
for post in posts:
    formatted_post = {
        "post_id": post["id"],
        "username": post["from"]["name"],
        "content": post["message"],
        "timestamp": post["created_time"]
    }
    formatted_posts.append(formatted_post)

# Save the formatted posts to a JSON file
with open("data/posts.json", "w") as file:
    json.dump(formatted_posts, file, indent=4)

# After crawling social media posts
print("Crawling social media posts...")

# After saving the data
print("Finished crawling", len(formatted_posts), "posts.")
print("Data saved to data/temp.json.")
