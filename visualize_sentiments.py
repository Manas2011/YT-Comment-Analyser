import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sentiment analysis results
df = pd.read_csv("sentiment_comments.csv")

# Plot the sentiment distribution
sns.countplot(x="sentiment", data=df)
plt.title("Sentiment Analysis of YouTube Comments")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")
plt.show()
