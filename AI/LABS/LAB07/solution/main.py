import pandas as pd
# from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import stop_words
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import cross_validation
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB





def clean_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    clean = soup.get_text()
    words = re.findall(r'[a-zA-Z]+',clean)
    stops = stop_words.get_stop_words('english')
    cleanwords = [w for w in words if not w in stops]
    sentence=" ".join(cleanwords)
    return sentence






sizeofdata=5000
vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = sizeofdata)
import numpy as np
test = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", \
                   quoting=3 )
print(test.shape)
num_reviews = len(test["review"])
clean_test_reviews = []
print("Cleaning and parsing the test set movie reviews...\n")
for i in range(0,sizeofdata):
    if( (i+1) % 1000 == 0 ):
        print("Review %d of %d\n" % (i+1, num_reviews))
    clean_review = clean_data( test["review"][i])
    clean_test_reviews.append(clean_review)
y=[]
for i in range(0,sizeofdata):
    if ((i + 1) % 1000 == 0):
        print("Sentiment %d of %d\n" % (i + 1, num_reviews))
    y.append(test["sentiment"][i])
test_data_features = vectorizer.fit_transform(clean_test_reviews)
test_data_features = test_data_features.toarray()
y=np.array(y)

x_train, x_test, y_train, y_test=cross_validation.train_test_split(test_data_features,y,test_size=0.20,random_state=0)
print(x_train, y_train)
print(x_test, y_test)
clf = MultinomialNB(alpha=0.00001)
clf.fit(x_train,y_train)
y_pred_class=clf.predict(x_test)

accuracy=metrics.accuracy_score(y_test, y_pred_class)
accuracy=100*accuracy
print("Accuracy of the classifier =",accuracy,"%")

