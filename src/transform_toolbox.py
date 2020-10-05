from sklearn.preprocessing import LabelEncoder, StandardScaler, Normalizer
from sklearn.pipeline import make_pipeline
import pandas as pd
import time

def label_encode_data(df, columns):
    result = df.copy()
    
    label_encoder = LabelEncoder()
    
    for col in columns:
        result[col] = label_encoder.fit_transform(df[col])

    return result

def setup_pipeline(pipeline):
    return make_pipeline(*pipeline)

def normalize_data_pipeline(df, pipeline):
    transformer = setup_pipeline(pipeline)
    result = transformer.fit_transform(df)
    return pd.DataFrame(result, columns = df.columns)

def export_to_kaggle_csv(df, predictions):
    timestr = time.strftime("%Y%m%d_%H%M%S")
    output_file_name = "prediction_" + timestr + ".csv"

    my_submission = pd.DataFrame({'id': df["id"], 'price': predictions})
    my_submission.to_csv('output/' + output_file_name, index=False)
    print(f"Exportados los datos a: output/'{output_file_name}'")
    