from clasificador import classify
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
from sklearn import preprocessing
from  getting_tweets import search

def btc():
    value_btc = [(46545.4+42201.5)/2,
            (45770.9+42293.9)/2,
            (43516.6+30261.7)/2,
            (42425.9+35010.4)/2,
            (42108.3+35010.4)/2,
            (38776.0+35314.9)/2,
            (38248.7+31192.4)/2,
            (39851.7+34474.6)/2,
            (39740.8+36540.7)/2]
    return value_btc

def run():
    days = list(range(17,26))
    date = [['2021-05-'+str(day),'',''] for day in days]
    row = 0
    for day in days:
        stats = classify(str(day))
        for i in range(2):
            date[row][i+1] = stats[i]
        row += 1
    # print(date)
    values = btc()
    date = np.array(date)
    #datetime = list(range(len(date[:,0])))
    sells = date[:,1]
    buy = date[:,2]
    
    df = {"Values": values,
        "Sell": sells,
        "Buy": buy 
        }
    df = pd.DataFrame(df)
    #print(df)
    analisis(df)

def analisis(dataset):
    x = dataset[['Values']]   
    #x = dataset[['Sell']]
    y = dataset.iloc[:,2].values
    #y = dataset.iloc[:,0].values
    z = dataset.iloc[:,1].values
    print(x)
    print(x.shape)
    print(y)
    print(y.shape)

    # x_encoded =  preprocessing.LabelEncoder().fit_transform(x)
    # print(x_encoded)

    # X_train,X_test, Y_train, Y_test = TTS(x ,y, test_size=0.2, random_state = 0) 
    # regressor = LR()
    # regressor.fit(X_train,Y_train)

    plt.scatter(x,y,color='blue')
    plt.scatter(x,z,color='red')
    #plt.plot(X_train, regressor.predict(X_train), color='black')
    plt.title('Advice vs Price')
    plt.xlabel('Price')
    plt.ylabel('Advice')
    plt.show()


if __name__ == '__main__':
    run()
