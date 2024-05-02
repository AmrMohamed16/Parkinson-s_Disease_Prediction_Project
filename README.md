# Parkinson's Disease Prediction Project using Support Vector Machine SVM
Parkinson's Disease Prediction Project using Support Vector Machine (SVM) for Artificial Intelligence (1) [CS324P] at Faculty of Computers &amp; Information Sciences, Mansoura University

# Table of Content

* [Contributors](#Contributors)
* [Brief](#Brief)
* [DataSet](#DataSet)
* [How It Works](#HowItWorks)
* [Tools](#Tools)
* [Remarks](#Remarks)
* [Usage](#Usage)
* [Sample Run](#SampleRun)


# Contributors

* [Amr Khaled](https://github.com/GOAT-AK)

* [Amr Mohamed](https://github.com/AmrMohamed16)




# Brief

Parkinson's disease is a neurodegenerative disorder that affects movement. Early detection of Parkinson's disease is crucial for timely intervention and management. This project aims to provide a reliable tool for predicting the presence of Parkinson's disease using voice recordings.


# DataSet

The dataset used in this project is the [Parkinson's Data Set](https://www.kaggle.com/datasets/thecansin/parkinsons-data-set) from Kaggle. This dataset is composed of a range of biomedical voice measurements from 
31 people, 23 with Parkinson's disease (PD). Each column in the table is a 
particular voice measure, and each row corresponds one of 195 voice 
recording from these individuals ("name" column). The main aim of the data 
is to discriminate healthy people from those with PD, according to "status" 
column which is set to 0 for healthy and 1 for PD.


# How It Works

 • The dataset is loaded from a CSV file (parkinsons.data).
 
 • The 'name' column is cleaned and converted to a numeric type.
 
 • The dataset is split into features (X) and target labels (Y).
 
 • Standard scaling is applied to the features.
 
 • The SVM model is trained on the training data.
 
 • The GUI allows users to input voice recording features.
 
 • Predictions are made based on the user input.

 

# Tools & Libraries

  I.	VSCode(IDE)
  
  II.	Python 3.x
  
  III. numpy
  
  IV. pandas 
  
  V.  scikit-learn
  
  VI.	 tkinter




# Remarks

* This python program was run and tested on the VSCode[VSCode](https://code.visualstudio.com/download)

* Ensure the required libraries are installed by running:
  
  ```bash
  pip install numpy pandas scikit-learn
# Usage

To begin utilizing this application, follow these steps:

1. Clone this repository:
   
   ```bash
   git clone https://github.com/AmrMohamed16/Parkinson-s_Disease_Prediction_Project.git

2. Navigate to the cloned repository:

   ```bash
   cd Parkinson-s_Disease_Prediction_Project

3. Run the Python script:

   ```bash
   Parkinson's Disease.py

# Sample Run

* The Person Has Parkinsons 



<hr>

* The Person Dose Not Have Parkinsons


<hr>
  
  
