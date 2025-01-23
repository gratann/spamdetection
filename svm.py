# Importing Support Vector Machine classifier
from sklearn.svm import SVC
# Initializing the SVM classifier
svm_classifier = SVC(random_state=42)
# Training the model
svm_classifier.fit(X_train, y_train)
# Making predictions
y_pred = svm_classifier.predict(X_test)
# Evaluating the model
print(f"Accuracy of SVM: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred))
