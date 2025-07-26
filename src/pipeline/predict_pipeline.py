import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')  # Note: matches the typo in DataTransformationConfig
            
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
            
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 air_temperature: float,
                 process_temperature: float,
                 rotational_speed: float,
                 torque: float,
                 tool_wear: int,
                 type_category: str,
                 ):
        
        self.air_temperature = air_temperature
        self.process_temperature = process_temperature
        self.rotational_speed = rotational_speed
        self.torque = torque
        self.tool_wear = tool_wear
        self.type_category = type_category
        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Air temperature [K]": [self.air_temperature],
                "Process temperature [K]": [self.process_temperature],
                "Rotational speed [rpm]": [self.rotational_speed],
                "Torque [Nm]": [self.torque],
                "Tool wear [min]": [self.tool_wear],
                "Type": [self.type_category],
               
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

# Example usage function
def make_prediction(air_temp, process_temp, rot_speed, torque, tool_wear, 
                   type_cat):
    """
    Convenience function to make a prediction with individual parameters
    
    Args:
        air_temp (float): Air temperature in Kelvin
        process_temp (float): Process temperature in Kelvin
        rot_speed (float): Rotational speed in rpm
        torque (float): Torque in Nm
        tool_wear (int): Tool wear in minutes
        type_cat (str): Type category
        
    
    Returns:
        numpy.ndarray: Prediction result
    """
    try:
        # Create custom data object
        data = CustomData(
            air_temperature=air_temp,
            process_temperature=process_temp,
            rotational_speed=rot_speed,
            torque=torque,
            tool_wear=tool_wear,
            type_category=type_cat,
            
        )
        
        # Convert to dataframe
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:")
        print(pred_df)
        
        # Make prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        return results
        
    except Exception as e:
        raise CustomException(e, sys)

# Example of how to use the pipeline
if __name__ == "__main__":
    try:
        # Sample data point for prediction
        sample_prediction = make_prediction(
            air_temp=300.5,           # Air temperature in K
            process_temp=309.9,       # Process temperature in K
            rot_speed=1397,           # Rotational speed in rpm
            torque=45.9,              # Torque in Nm
            tool_wear=210,              # Tool wear in minutes
            type_cat="H",             # Type L , H , M category( drop down box)
            
        )
        
        print(f"Prediction result: {sample_prediction}")
        
    except Exception as e:
        print(f"Error occurred: {e}")