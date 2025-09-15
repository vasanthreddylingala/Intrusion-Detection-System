import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Sample Training Data
X_train = np.random.rand(100, 9)
y_train = np.random.randint(0, 4, 100)  # Labels: 0 (No Attack), 1 (DDoS), 2 (Fuzzy), 3 (Impersonation)

# Train Model
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save Model & Scaler
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model & Scaler saved successfully!")