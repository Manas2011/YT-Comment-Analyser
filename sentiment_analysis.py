import pandas as pd
from textblob import TextBlob

# Load the cleaned comments
df = pd.read_csv("cleaned_comments.csv")

# Fill missing comments with an empty string
df["cleaned_comment"].fillna("", inplace=True)

def get_sentiment(comment):
    analysis = TextBlob(str(comment))  # Ensure the comment is a string
    # Determine the sentiment polarity
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

# Apply sentiment analysis to each cleaned comment
df["sentiment"] = df["cleaned_comment"].apply(get_sentiment)

# Save the results to a new CSV file
df.to_csv("sentiment_comments.csv", index=False)

print("Sentiment analysis completed and saved to sentiment_comments.csv")
