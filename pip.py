import pickle
import joblib
import numpy as np

sample_input = np.random.rand(1, 9)  # Assuming your model expects 9 features
prediction = model.predict(sample_input)
print(prediction)
model = joblib.load("model.pkl")  # Ensure this path is correct
print(type(model))  # Should output: <class 'sklearn.ensemble._forest.RandomForestClassifier'>
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
print(type(model))