import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import messagebox, Button
from PIL import Image, ImageTk  # Para manejar imágenes en formatos adicionales como JPG

from threading import Thread
from database import crear_bd  # Asumiendo que tienes funciones para la base de datos

# Configuración global

#MODEL_PATH = "scripts/runs/detect/cable_detector/weights/best.pt"
MODEL_PATH = "C:/Practicas_Profesionalizantes_2_2024/BGH_PowerCheck/scripts/runs/detect/placa_detector2/weights/best.pt"
EXPECTED_CONNECTIONS = {
    "Posicion1": "Amarillo",
    "Posicion2": "Rojo",
    "Posicion3": "Negro",
    "Posicion4": "Azul",
    "Posicion5": "Marron"
}
detener_camara = False  # Variable global para detener la cámara

# Validar conexiones detectadas
def validate_connections(detections):
    """
    Valida las conexiones detectadas.
    Retorna True si todo está correcto, de lo contrario retorna una lista de errores.
    """
    errors = []
    connected_positions = {detection['position']: detection['color'] for detection in detections}

    for position, expected_color in EXPECTED_CONNECTIONS.items():
        detected_color = connected_positions.get(position)
        normalized_expected_color = expected_color.strip().lower()
        normalized_detected_color = detected_color.strip().lower() if detected_color else None

        if detected_color is None:
            errors.append(f"{position}: No debe estar Vacia, y debe ser {expected_color}.")
        elif normalized_detected_color != normalized_expected_color:
            errors.append(f"{position}: {detected_color} no es valido, debe ser {expected_color}.")
    
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
            print("Error: No se pudo abrir la camara.")
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
                    color_name = list(EXPECTED_CONNECTIONS.values())[int(cls)]
                    detections.append({"position": f"Posicion{int(cls)+1}", "color": color_name})

                # Validar conexiones
                validation_result = validate_connections(detections)
                y_offset = 20  # Margen superior para el texto

                if validation_result is True:
                    cv2.putText(frame, "Conexion Correcta", (10, y_offset + 25), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2, cv2.LINE_AA)
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

    btn_iniciar_cam = tk.Button(menu, text="Iniciar Camara", font=("Arial", 14), command=iniciar_camara)
    btn_iniciar_cam.pack(pady=10)

    btn_fallidos = tk.Button(menu, text="Registros Fallidos", font=("Arial", 14), command=lambda: messagebox.showinfo("Registros", "Funcionalidad en desarrollo"))
    btn_fallidos.pack(pady=10)

    btn_correctos = tk.Button(menu, text="Detecciones Correctas", font=("Arial", 14), command=lambda: messagebox.showinfo("Registros", "Funcionalidad en desarrollo"))
    btn_correctos.pack(pady=10)

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
