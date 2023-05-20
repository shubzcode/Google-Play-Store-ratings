import csv
from textblob import TextBlob
from google_play_scraper import reviews

# Appp name input Hare (Package name)
package_name = "com.clubhouse.app"

# Retrieve app infoemation reviews from the Google Play Store
reviews_list, _ = reviews(package_name, lang='en', count=100)

#  the output file name store in local storage in PC
output_file = "clubhouse_reviews007.csv"

# Perform sentiment analysis and save reviews to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Review", "Sentiment"])
    for review in reviews_list:
        text = review['content']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_label = "Positive"
        elif sentiment < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        writer.writerow([text, sentiment_label])
