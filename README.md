# Google-Play-Store-ratings
Google Play Store ratings , Sentiment , Review

import csv
from textblob import TextBlob
from google_play_scraper import reviews

# Appp name input Hare (Package name)
package_name = "com.clubhouse.app"

# Retrieve app infoemation reviews from the Google Play Store
reviews_list, _ = reviews(package_name, lang='en', count=100)

#  the output file name store in local storage in PC
output_file = "clubhouse_reviews008.csv"

# Perform sentiment analysis and save reviews to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Review", "Sentiment", "Ratings"])
    
    for review in reviews_list:
        def jls_extract_def(review):
            return review['content']

        text = jls_extract_def(review)
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            sentiment_label = "Positive"
        elif sentiment < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        rating = int(sentiment * 5)
        writer.writerow([text, sentiment_label, rating])






In this code first I use this library:
•	csv: library is used to read and write CSV files.
•	textblob: library is used to perform natural language processing tasks, such as sentiment analysis.(Text Processing  )
•	google_play_scraper: library is used to scrape reviews from the Google Play Store.

Variables I Used in Code

•	package_name: This variable stores the package name of the app that you want to get reviews. (Application Id From Play Store)
•	output_file: This variable stores the name of the CSV file that you want to save the reviews to.(named :- clubhouse_reviews008)




The sentiment label for each review:


•	textblob: library is used to perform natural language processing tasks, such as sentiment analysis.(Text Processing  )

Here is an example of how the algorithm would work:
•	Text: "I love this movie!"
•	Sentiment score: 1
•	Label: Positive
•	Text: "This movie was terrible."
•	Sentiment score: -1
•	Label: Negative
•	Text: "I thought the movie was okay."
•	Sentiment score: 0
•	Label: Neutral



if sentiment > 0:
sentiment_label = "Positive"
elif sentiment < 0:
sentiment_label = "Negative"
else:
sentiment_label = "Neutral"






To save the reviews to the CSV file: CSV= Comma separated value 
writer.writerow([text, sentiment_label, rating])




Output
Open CSV file upload on github repo
