import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the comments
df = pd.read_csv("comments.csv")

def preprocess(comment):
    if not isinstance(comment, str):  # Check if the comment is a string
        return ''  # Or return a placeholder like '' if you prefer
    
    # Convert to lowercase
    comment = comment.lower()
    # Tokenize
    tokens = word_tokenize(comment)
    # Remove stop words and non-alphanumeric tokens
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Apply preprocessing to each comment
df["cleaned_comment"] = df["comment"].apply(preprocess)

# Save the cleaned comments to a new CSV file
df.to_csv("cleaned_comments.csv", index=False)

print("Preprocessing completed and saved to cleaned_comments.csv")
