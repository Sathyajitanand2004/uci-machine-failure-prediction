
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer

from src.components.data_ingestion import DataIngestionConfig
from src.components.data_ingestion import DataIngestion

# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.data_ingestion_method()

#     data_transformation=DataTransformation()
#     train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

#     modeltrainer=ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))