import torch, os
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np

class TTDataset(Dataset):
    def __init__(self, data_path:str, mode:str="T"):
        self.train = True if mode.upper() == "T" else False
        file_name = "train.csv" if self.train else "test.csv"
        data = pd.read_csv(os.path.join(data_path, file_name), encoding="UTF-8")
        if self.train : self.label = data["Survived"].values
        Pclass = data["Pclass"].values
        Sex = data["Sex"].values
        Age = data["Age"].values
        SibSp = data["SibSp"].values
        Parch = data["Parch"].values
        Ticket = data["Ticket"].values
        Fare = data["Fare"].values
        Cabin = data["Cabin"].values
        for i in Cabin:
            print(type(i), np.isnan(i))
        Embarked = data["Embarked"].values

    def __len__(self):
        return

    def __getitem__(self, idx):
        return
    

if __name__ == "__main__":
    dataset = TTDataset("./Titanic")
    print("")