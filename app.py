from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            data = CustomData(
                air_temperature=float(request.form.get('air_temperature')),
                process_temperature=float(request.form.get('process_temperature')),
                rotational_speed=float(request.form.get('rotational_speed')),
                torque=float(request.form.get('torque')),
                tool_wear=int(request.form.get('tool_wear')),
                type_category=request.form.get('type_category')
            )
            
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("after Prediction")
            
            # Interpret results
            prediction_value = results[0]
            if prediction_value == 0:
                result_text = "No Failure Predicted"
                result_class = "success"
                result_description = "The machine is operating normally. No immediate maintenance required."
            else:
                result_text = "Failure Predicted"
                result_class = "danger"
                result_description = "The machine may fail soon. Consider scheduling preventive maintenance."
            
            return render_template('index.html', 
                                 results=result_text,
                                 result_class=result_class,
                                 result_description=result_description)
                                 
        except Exception as e:
            error_message = f"Error during prediction: {str(e)}"
            print(error_message)
            return render_template('index.html', error=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)