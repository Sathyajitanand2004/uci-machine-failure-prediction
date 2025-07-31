
# Predictive Maintenance - Machine Failure Prediction (CI/CD with Azure & Docker)

This project is an **end-to-end MLOps pipeline** for **predictive maintenance**, focused on predicting **machine failure** using manufacturing sensor data. The entire pipeline is containerized using **Docker**, integrated with **GitHub Actions** for CI/CD, and deployed to **Azure Web Services**.

##  Project Overview

Predictive maintenance uses machine learning to predict the likelihood of machine failure before it occurs, allowing timely maintenance and reduced downtime. This project uses a **Gradient Boosting Classifier** trained via a custom **ML pipeline**.

###  Features:
- Fully automated **CI/CD** using GitHub Actions.
- Modular ML pipeline: data ingestion, preprocessing, training, evaluation.
- Web app for real-time prediction with HTML + JS frontend.
- Dockerized application with Azure App Service deployment.
- Clean project structure following best practices.

---

##  Project Structure

```

predictive\_maintanance/
│
├── .github/workflows/
│   └── main\_MachinePredictionSj.yml       # CI/CD pipeline config
├── artifacts/                             # Saved model artifacts
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw\_data.csv / train\_data.csv / test\_data.csv
├── src/                                   # Core ML pipeline code
│   ├── components/                        # Custom modules
│   │   ├── data\_ingestion.py
│   │   ├── data\_transformation.py
│   │   └── model\_training.py
│   ├── pipeline/
│   │   ├── train\_pipeline.py
│   │   └── predict\_pipeline.py
│   ├── exception.py / logger.py / utils.py
├── static/                                # JS/CSS for UI
│   └── js/script.js
├── templates/
│   └── index.html                         # Frontend UI
├── app.py                                 # Flask API
├── Dockerfile                             # Docker container setup
├── requirements.txt                       # Python dependencies
├── setup.py                               # Package setup
└── README.md                              # This file
```


---

## Tech Stack

| Tool/Tech              | Purpose                                  |
|------------------------|------------------------------------------|
| Python                 | Core programming language                |
| Flask                  | Web framework for API                    |
| Scikit-learn           | Machine Learning                         |
| CatBoost / GradientBoost| Model training and evaluation            |
| Docker                 | Containerization                         |
| Azure App Service      | Model deployment                         |
| GitHub Actions         | CI/CD automation                         |
| HTML, JS               | Frontend interface                       |

---

##  Dataset

The dataset includes sensor readings from a manufacturing process:

| Feature Name             | Description                 |
|--------------------------|-----------------------------|
| `Type`                   | Type of product             |
| `Air temperature [K]`    | Air temperature             |
| `Process temperature [K]`| Process temperature         |
| `Rotational speed [rpm]`| Motor speed                 |
| `Torque [Nm]`            | Torque applied              |
| `Tool wear [min]`        | Tool wear in minutes        |

---

##  Model Info

- **Type**: Classification
- **Algorithm**: `GradientBoostingClassifier`
- **Target**: Machine failure (Binary: 1 - Fail, 0 - No Fail)
- **Model Accuracy**: - `98.65 %`
-   **Precision**: - `98.59 %`
-   **recall**: - `98.65 %`
-   **f1_score**: - `98.60 %`
-   **roc_auc**: -`96.81 %`
  ---  

##  Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/predictive_maintanance.git](https://github.com/Sathyajitanand2004/uci-machine-failure-prediction.git
cd predictive_maintanance
````

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

---

##  Docker Deployment

### Build Docker image

```bash
docker build -t predictive-maintenance-app .
```

### Run Docker container

```bash
docker run -p 5000:5000 predictive-maintenance-app
```

---

##  Azure Deployment

1. Push code to GitHub.
2. Create an Azure App Service with Docker enabled.
3. Configure GitHub Actions with `main_MachinePredictionSj.yml` to auto-deploy on push.
4. Done! The app is live at:

```
https://<your-app-name>.azurewebsites.net
```

---

##  CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline:

* Lints and tests the code.
* Builds Docker image.
* Pushes to Azure Container Registry (ACR).
* Deploys to Azure Web App.

---

##  Sample Prediction UI

The web interface takes sensor values and returns real-time machine failure prediction.

![Web UI Screenshot](https://github.com/Sathyajitanand2004/uci-machine-failure-prediction/blob/main/Screenshot%20(497).png?raw=true)

![Web UI Screenshot](https://github.com/Sathyajitanand2004/uci-machine-failure-prediction/blob/main/Screenshot%20(498).png?raw=true)

---

##  Project By:

* **SATHYAJITANAND V** - [GitHub](https://github.com/sathyajitanand2004)

---

