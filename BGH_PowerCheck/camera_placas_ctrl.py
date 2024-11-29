import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import messagebox, Button
from threading import Thread
from database import crear_bd

# Ruta del modelo YOLO
MODEL_PATH = "E:/detect/placa_detector80/weights/best.pt"

# Componentes esperados
COMPONENT_NAMES = [
    'SW 1', 'CN 19', 'CN 12', 'CN 15', 'C 251', 
    'CN 14', 'N IN 1', 'CN 18', 'C 498', 'C 497', 
    'C 259', 'C 496', 'NTC 1'
]
EXPECTED_COMPONENTS = {idx: name for idx, name in enumerate(COMPONENT_NAMES)}

detener_camara = False  # Variable global para detener la cámara

# Validar detecciones
def validate_components(detections):
    """
    Valida que todos los componentes esperados estén presentes.
    Retorna True si todo está correcto, de lo contrario una lista de errores.
    """
    errors = []
    detected_classes = [detection['class'] for detection in detections]

    for idx, component_name in EXPECTED_COMPONENTS.items():
        if idx not in detected_classes:
            errors.append(f"{component_name}: Faltante.")

    return True if not errors else errors

# Función para iniciar la cámara
def iniciar_camara():
    global detener_camara
    detener_camara = False

    # Crear ventana para la cámara
    cam_window = tk.Toplevel()
    cam_window.title("BGH Placas - Ctrl Camara")
    cam_window.geometry("400x200")

    def detener_desde_boton():
        global detener_camara
        detener_camara = True
        cam_window.destroy()

    btn_detener = Button(cam_window, text="Detener Camara", font=("Arial", 16), command=detener_desde_boton)
    btn_detener.pack(pady=40)

    # Hilo para procesar video
    def procesar_video():
        global detener_camara
        try:
            model = YOLO(MODEL_PATH)
            print(f"Modelo cargado correctamente desde: {MODEL_PATH}")
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            return

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
            return

        while not detener_camara:
            ret, frame = cap.read()
            if not ret:
                print("Error al capturar el frame.")
                break

            try:
                results = model.predict(frame, conf=0.3)
                detections = []

                for result in results[0].boxes.data.tolist():
                    x1, y1, x2, y2, confidence, cls = result
                    detections.append({"class": int(cls)})

                # Validar componentes
                validation_result = validate_components(detections)
                y_offset = 20  # Margen superior para el texto

                if validation_result is True:
                    cv2.putText(frame, "Todos los componentes están presentes.", (10, y_offset + 25), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    for idx, error in enumerate(validation_result):
                        cv2.putText(frame, error, (10, y_offset + 5 + 15 * idx), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)

                annotated_frame = results[0].plot()
            except Exception as e:
                print(f"Error durante la predicción: {e}")
                annotated_frame = frame

            # Redimensionar y mostrar el frame
            resized_frame = cv2.resize(annotated_frame, (int(annotated_frame.shape[1] * 1.5), int(annotated_frame.shape[0] * 1.5)))
            cv2.imshow("BGH Placas - Ctrl", resized_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                detener_camara = True
                break

        cap.release()
        cv2.destroyAllWindows()

    Thread(target=procesar_video).start()
    cam_window.mainloop()

# Menú principal
def mostrar_menu():
    menu = tk.Tk()
    menu.title("BGH Placas Ctrl - Menu Principal")
    menu.geometry("600x400")

    btn_iniciar_cam = tk.Button(menu, text="Iniciar Cámara", font=("Arial", 14), command=iniciar_camara)
    btn_iniciar_cam.pack(pady=10)

    btn_cerrar_sesion = tk.Button(menu, text="Cerrar Sesión y Salir", font=("Arial", 14), command=lambda: cerrar_sesion(menu))
    btn_cerrar_sesion.pack(pady=20)

    menu.mainloop()

# Función de cerrar sesión
def cerrar_sesion(menu):
    menu.destroy()
    root.quit()

# Login
def validate_login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Correcto", "Bienvenido a BGH Placas Ctrl")
        root.destroy()
        mostrar_menu()
    else:
        messagebox.showerror("Error", "Credenciales Incorrectas")

# Crear ventana de login
root = tk.Tk()
root.title("BGH Placas Ctrl - Login")
root.geometry("400x300")

label_user = tk.Label(root, text="Usuario", font=("Arial", 14))
label_user.pack(pady=10)
entry_user = tk.Entry(root, font=("Arial", 14), width=20)
entry_user.pack(pady=10)

label_pass = tk.Label(root, text="Contraseña", font=("Arial", 14))
label_pass.pack(pady=10)
entry_pass = tk.Entry(root, show="*", font=("Arial", 14), width=20)
entry_pass.pack(pady=10)

btn_login = tk.Button(root, text="Iniciar Sesión", font=("Arial", 14), command=validate_login)
btn_login.pack(pady=20)

# Inicializar la base de datos
crear_bd()
root.mainloop()
