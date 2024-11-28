from ultralytics import YOLO

def main():
    model = YOLO('yolov8l.pt')  # Puedes cambiar el modelo aquí (yolov8s.pt, yolov8l.pt, etc.)
    model.train(
        data='dataset.yaml',
        epochs=200,               # Incrementar el número de épocas
        batch=8,
        imgsz=832,                # Tamaño de imagen más alto
        save=True,
        save_period=10,
        optimizer='AdamW',
        lr0=0.005,
        cos_lr=True,              # Activar tasa de aprendizaje cosenoidal
        mosaic=0.5,               # Valor corregido para Mosaic
        fliplr=0.5,
        mixup=0.3,                # Incrementar el Mixup
        scale=0.8,                # Mayor rango de escalado
        conf=0.35,                # Menor umbral de confianza
        iou=0.7,                  # Ajustar IoU
        project="runs/detect",
        name='cable_detector_v2'
    )

if __name__ == "__main__":
    main()
