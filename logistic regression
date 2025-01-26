from sklearn.linear_model import LogisticRegression
# Splitting the data into features and target variable
X = df['Message']
y = df['encoded_label']
# Vectorizing the text data using TfidfVectorizer (you could also use CountVectorizer)
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2,
random_state=42)
# Initializing the Logistic Regression model
logreg = LogisticRegression()
# Training the model
logreg.fit(X_train, y_train)
# Making predictions
y_pred = logreg.predict(X_test)
# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Logistic Regression: {accuracy * 100:.2f}%")
# Displaying the classification report
print(classification_report(y_test, y_pred))
