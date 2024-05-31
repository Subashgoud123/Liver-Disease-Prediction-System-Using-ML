
import joblib
import pandas as pd
import os


def solve(rdata):
    mean = {'Age': 43.77430503624002,
            'Gender': 0.752510786410935,
            'Total_Bilirubin': 2.6878872383517614,
            'Direct_Bilirubin': 1.1910043185354189,
            'Alkaline_Phosphotase': 269.8929529303398,
            'Alamine_Aminotransferase': 67.08599187783459,
            'Aspartate_Aminotransferase': 90.6054105391029,
            'Total_Protiens': 6.523273305491896,
            'Albumin': 3.2072029024080475,
            'Albumin_and_Globulin_Ratio': 0.9701843668913785}
    if (rdata[1] == 'Male'):
        rdata[1] = 1
    elif (rdata[1] == "Female"):
        rdata[1] = 0
    if (rdata.count(None) > 4):
        print("Please provide proper data to predict")
    else:
        c = ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
             'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
             'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
             'Albumin_and_Globulin_Ratio']
        d = dict()
        for i, j in zip(rdata, c):
            if (j == 'Age' and i == None):
                i = mean[j]
            elif (j == 'Total_Bilirubin' and i == None):
                i = mean[j]
            elif (j == 'Gender' and i == None):
                i = mean[j]
            elif (j == 'Direct_Bilirubin' and i == None):
                i = mean[j]
            elif (j == 'Alkaline_Phosphotase' and i == None):
                i = mean[j]
            elif (j == 'Alamine_Aminotransferase' and i == None):
                i = mean[j]
            elif (j == 'Aspartate_Aminotransferase' and i == None):
                i = mean[j]
            elif (j == 'Total_Protiens' and i == None):
                i = mean[j]
            elif (j == 'Albumin' and i == None):
                i = mean[j]
            elif (j == 'Albumin_and_Globulin_Ratio' and i == None):
                i = mean[j]
            d[j] = i

        print(rdata)
        print(d)
        c = ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
             'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']

        rdata = pd.DataFrame(d, index=[0])

        file_name = r"model.pkl"

        model = joblib.load(file_name)
        return model.predict(rdata)
