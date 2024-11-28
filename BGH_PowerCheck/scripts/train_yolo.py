from ultralytics import YOLO

def main():
    model = YOLO('C:/Practicas_Profesionalizantes_2_2024/BGH_PowerCheck/scripts/yolov8m.pt')  # Carga el modelo YOLO
    model.train(
        #data='dataset.yaml',  # Archivo de configuración del dataset
        data='C:/Practicas_Profesionalizantes_2_2024/BGH_PowerCheck/scripts/dataset.yaml',
        epochs=1,            # Número de épocas
        batch=16,             # Tamaño del batch
        imgsz=640,            # Tamaño de las imágenes
        save=True,            # Asegura que los pesos se guarden
        save_period=1,        # Guarda los pesos después de cada época
        project="C:/Practicas_Profesionalizantes_2_2024/BGH_PowerCheck/scripts/runs/detect", # Carpeta de salida
        #name='cable_detector'
        name='placa_detector'
    )

if __name__ == "__main__":
    main()
