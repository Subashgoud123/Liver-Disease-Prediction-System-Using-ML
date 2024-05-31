# Liver-Disease-Prediction-System-Using-ML
# Problem statement 
An early diagnosis of liver problems will increase patient’s survival rate. Liver failures are at high rate 
of risk among Indians. It is expected that by 2025 India may become the World Capital for Liver 
Diseases. The widespread occurrence of liver infection in India is contributed due to deskbound 
lifestyle,increased alcohol consumption and smoking.People who are far away from hospitals are unable to spend travelling charges to checkup in city hospitals.
# Solution using Machine Learning
# Steps
Collecting Data: ...
Preparing the Data: ...
Choosing a Model: ...
Training the Model: ...
Evaluating the Model: ...
Making Predictions.
# Collecting dataset from 
https://www.kaggle.com/datasets/uciml/indian-liver-patient-records

# Preparing data
1. Clean the null values and replace some values with mean values of the field columns
2. Remove unnecessary rows.

# Choosing a model
1. Try all supervised ml models and choose according to the accuracy.
2. Import the models.
3. Fit the spiltted data( input data , target data) into the model.
4. Train the model and test it.
5. The better accuracy  model is the better output.
6. I have choosen Random Forest Classifier
   
Random Forest works in two-phase first is to create the random forest by combining N decision tree, and 
second is to make predictions for each tree created in the first phase. 
The Working process can be explained in the below steps and diagram: 
Step-1: Select random K data points from the training set. 
Step-2: Build the decision trees associated with the selected data points (Subsets). 
Step-3: Choose the number N for decision trees that you want to build. 
Step-4: Repeat Step 1 & 2. 
Step-5: For new data points, find the predictions of each decision tree, and assign the new data points to the 
category that wins the majority votes.
the model fitting is stored in Model.ipynd, rmodule.py file.

# Evaluation 
Evaluate the model by testing the model giving different valid inputs and verify

# Final.py
The final.
