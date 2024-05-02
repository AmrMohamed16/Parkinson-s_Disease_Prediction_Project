# #------------- PLUTO | O.O.T.S.S --------------
# #------------- GOAT | T.M.W.H.N.L -------------
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import re
import tkinter as tk
from tkinter import messagebox

# loading the data from csv file to a Pandas DataFrame
parkinsons_data = pd.read_csv('archive/parkinsons.data')

# cleaning the 'name' column , Cleans the 'name' column by removing non-digit characters
parkinsons_data['name'] = parkinsons_data['name'].apply(lambda x: re.sub(r'\D', '', x))

# Convert the 'name' column to numeric type
parkinsons_data['name'] = pd.to_numeric(parkinsons_data['name'])

# number of rows and columns in the dataframe
parkinsons_data.shape

# getting more information about the dataset
parkinsons_data.info()

# checking for missing values in each column
parkinsons_data.isnull().sum()

# getting some statistical measures about the data
parkinsons_data.describe()

# distribution of target Variable
parkinsons_data['status'].value_counts()

# grouping the data based on the target variable
parkinsons_data.groupby('status').mean()

X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

scaler = StandardScaler()

# Fit the scaler with feature names
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

# Function to predict Parkinson's disease
def predict_parkinsons():
    input_data = [float(entry.get()) for entry in entry_fields]
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = model.predict(std_data)
    if prediction[0] == 0:
        messagebox.showinfo("Prediction", "The Person does not have Parkinsons Disease")
    else:
        messagebox.showinfo("Prediction", "The Person has Parkinsons")

# GUI
root = tk.Tk()
root.title("Parkinson's Disease Prediction")

# Labels
labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']

entry_fields = []
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entry_fields.append(entry)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_parkinsons)
predict_button.grid(row=len(labels)+1, columnspan=2)

root.mainloop()




