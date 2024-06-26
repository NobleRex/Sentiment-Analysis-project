from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #polarity between -1 to 1
print(sentiment)