A machine learning–based web application built with Streamlit to predict whether a credit card transaction is fraudulent or safe based on transaction details such 
as amount, merchant, transaction type, and location.

Features:-
Uses a trained Random Forest Classifier for fraud detection
Interactive Streamlit web interface for user input
Real-time predictions with fraud probability
Deployed on Streamlit Cloud for public access

Dataset:-
The model was trained on a synthetic credit card transactions dataset, containing:
Amount — Transaction amount
MerchantID — Unique merchant identifier
TransactionType — Purchase or refund
Location — City of the transaction
IsFraud — 1 (fraud), 0 (safe) 

Tech Stack:-
Python
Pandas, NumPy
Scikit-learn
Streamlit

LiveDemo:-https://frauddetection-hjd3ujspij5mmhstaaz7pj.streamlit.app/

Model Training:-
The model (fraud_model.pkl) was trained using:
RandomForestClassifier (class_weight='balanced')
Preprocessed and one-hot encoded features for transaction type and location
Evaluation metrics like accuracy, precision, recall, and confusion matrix
