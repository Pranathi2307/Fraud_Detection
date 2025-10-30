import streamlit as st
import pandas as pd
import pickle

# Title
st.title("💳 Credit Card Fraud Detection App")

# Load model
with open('fraud_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.write("Enter transaction details below:")

# Input fields
amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)
merchant = st.number_input("Enter Merchant ID", min_value=0, step=1)
transaction_type = st.selectbox("Transaction Type", ["purchase", "refund"])
location = st.selectbox("Location", [
    "Chicago", "Dallas", "Houston", "Los Angeles", "New York",
    "Philadelphia", "Phoenix", "San Antonio", "San Diego", "San Jose"
])

# Create input dataframe with 14 columns (as in your training data)
columns = [
    'Amount', 'MerchantID', 'TransactionType_purchase', 'TransactionType_refund',
    'Location_Chicago', 'Location_Dallas', 'Location_Houston',
    'Location_Los Angeles', 'Location_New York', 'Location_Philadelphia',
    'Location_Phoenix', 'Location_San Antonio', 'Location_San Diego',
    'Location_San Jose'
]

# Initialize with zeros
input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

# Fill numeric values
input_data['Amount'] = amount
input_data['MerchantID'] = merchant
input_data[f'TransactionType_{transaction_type}'] = 1
input_data[f'Location_{location}'] = 1

# Predict button
if st.button("Predict"):
    prob = model.predict_proba(input_data)[0][1]  # probability of fraud class (1)

    # Custom threshold
    threshold = 0.3

    if prob >= threshold:
        st.error(f"🚨 Fraud Transaction Detected! (Probability: {prob:.2f})")
    elif amount >= 100000:
        st.warning("⚠️ High-value transaction! Please verify manually.")
    else:
        st.success(f"✅ Transaction is Safe. (Probability: {prob:.2f})")
