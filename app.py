from src.MLProject.components.data_ingestion import DataIngestion

def main():
    try:
       
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        print(f"Train data saved at: {train_path}")
        print(f"Test data saved at: {test_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
