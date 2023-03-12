# Code for saving the machine learning model which will then be connected with the GUI
import joblib
joblib.dump(rf,'model_credit-card_fraud_detection')
model = joblib.load('model_credit-card_fraud_detection')
model.predict(new_data)
