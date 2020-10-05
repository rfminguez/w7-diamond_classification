import pandas as pd

class DiamondsData:
    def __init__(self, filename):
        self.diamonds_df = pd.read_csv(filename)

    def get_all(self):
        return self.diamonds_df

    def get_features(self):
        # Descarto:
        # - el campo "id" que es la identificación única para cada diamante
        # - el campo "price" que es el groundtruth y lo que queremos predecir
        columns = [column for column in self.diamonds_df.columns if column != "price" and column != "id"]
        return self.diamonds_df[columns]

    def get_groundtruth(self):
        return self.diamonds_df["price"]
