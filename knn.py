# Importing K-Nearest Neighbors classifier
from sklearn.neighbors import KNeighborsClassifier
# Initializing the KNN classifier
knn_classifier = KNeighborsClassifier()
# Training the model
knn_classifier.fit(X_train, y_train)
# Making predictions
y_pred = knn_classifier.predict(X_test)
# Evaluating the model
print(f"Accuracy of KNN: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred))
