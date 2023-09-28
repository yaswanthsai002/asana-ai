import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

# Load the data
df = pd.read_csv("app/Asana.csv")

# Split the data into input features (X) and target variable (y)
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

# Encode the target variable
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Initialize the random forest classifier
rfr = RandomForestClassifier()

# Fit the model on the training data
rfr.fit(x_train, y_train)

# Use cross-validation to evaluate the model's accuracy
scores = cross_val_score(rfr, X, y, cv=10)

# Print the mean and standard deviation of the scores
print(f'Mean score: {scores.mean():.3f}')
print(f'Standard deviation: {scores.std():.3f}')

# Evaluate the model's accuracy on the test set
accuracy = rfr.score(x_test, y_test)
print("Random Forest Classifier : ", round(accuracy, 2))

# Save the model and label encoder to a file
with open('app/model.pkl', 'wb') as f:
    pickle.dump((rfr, le), f)
