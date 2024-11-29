import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import messagebox, Button
from threading import Thread
from database import crear_bd

# Ruta del modelo YOLO
MODEL_PATH = "C:/Practicas_Profesionalizantes_2_2024/BGH_PowerCheck/scripts/runs/detect/placa_detector315_google_colab/weights/best.pt"

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
    Valida los componentes detectados.
    Retorna una lista de componentes detectados y faltantes.
    """
    detected_classes = [detection['class'] for detection in detections]
    detected_names = [EXPECTED_COMPONENTS[cls] for cls in detected_classes if cls in EXPECTED_COMPONENTS]
    missing_names = [name for idx, name in EXPECTED_COMPONENTS.items() if idx not in detected_classes]

    return detected_names, missing_names

# Función para iniciar la cámara
def iniciar_camara():
    global detener_camara
    detener_camara = False

    # Crear ventana para la cámara
    cam_window = tk.Toplevel()
    cam_window.title("BGH Placas - Ctrl Camara")
    cam_window.geometry("400x300")  # Ajustar la ventana a 400x300

    # Crear un canvas para el fondo con texto "BGH"
    canvas = tk.Canvas(cam_window, width=400, height=300)
    canvas.pack(fill="both", expand=True)

    # Dibujar el patrón "BGH" en el fondo
    for y in range(0, 300, 50):  # Espaciado vertical del texto
        for x in range(0, 400, 100):  # Espaciado horizontal del texto
            canvas.create_text(x, y, text="BGH", font=("Arial", 20), fill="#cccccc", anchor="nw")

    # Crear un frame transparente sobre el canvas para colocar botones
    frame = tk.Frame(cam_window, bg="white", highlightthickness=2, highlightbackground="white")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

    def detener_desde_boton():
        global detener_camara
        detener_camara = True
        cam_window.destroy()

    # Botón para detener la cámara
    btn_detener = Button(frame, text="Detener Camara", font=("Arial", 16), command=detener_desde_boton)
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
                    cls = int(cls)
                    detections.append({"class": cls})

                    # Dibujar rectángulo en componentes detectados
                    if cls in EXPECTED_COMPONENTS:
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Verde para detectados
                        cv2.putText(frame, EXPECTED_COMPONENTS[cls], (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                # Validar componentes
                detected, missing = validate_components(detections)
                y_offset = 20  # Margen superior para el texto

                if not missing:
                    # Mensaje de éxito con texto blanco
                    cv2.putText(frame, "Todos los componentes están presentes.", (10, y_offset + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                else:
                    # Mensaje de faltantes con texto blanco
                    cv2.putText(frame, "Componentes faltantes:", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                    for idx, error in enumerate(missing):
                        cv2.putText(frame, f"- {error}", (10, y_offset + 15 * (idx + 1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

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

# Menú principal con fondo "BGH"
def mostrar_menu():
    menu = tk.Tk()
    menu.title("BGH Placas Ctrl - Menu Principal")
    menu.geometry("400x300")  # Ajustar la ventana a 400x300

    # Crear un canvas para el fondo
    canvas = tk.Canvas(menu, width=400, height=300)
    canvas.pack(fill="both", expand=True)

    # Dibujar el patrón "BGH" en el fondo
    for y in range(0, 300, 50):  # Espaciado vertical del texto
        for x in range(0, 400, 100):  # Espaciado horizontal del texto
            canvas.create_text(x, y, text="BGH", font=("Arial", 20), fill="#cccccc", anchor="nw")

    # Crear un frame transparente sobre el canvas para colocar botones
    frame = tk.Frame(menu, bg="white", highlightthickness=2, highlightbackground="white")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

    # Botón para iniciar la cámara
    btn_iniciar_cam = tk.Button(frame, text="Iniciar Cámara", font=("Arial", 14), command=iniciar_camara)
    btn_iniciar_cam.pack(pady=20)

    # Botón para cerrar sesión
    btn_cerrar_sesion = tk.Button(frame, text="Cerrar Sesión y Salir", font=("Arial", 14), command=lambda: cerrar_sesion(menu))
    btn_cerrar_sesion.pack(pady=10)

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

# Crear ventana de login con fondo "BGH"
root = tk.Tk()
root.title("BGH Placas Ctrl - Login")
root.geometry("400x300")

# Crear un canvas para el fondo
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Dibujar un patrón de texto "BGH" en el fondo
for y in range(0, 300, 50):  # Espaciado vertical del texto
    for x in range(0, 400, 100):  # Espaciado horizontal del texto
        canvas.create_text(x, y, text="BGH", font=("Arial", 20), fill="#cccccc", anchor="nw")

# Crear frame para los campos de entrada
frame = tk.Frame(root, bg="white", highlightthickness=2, highlightbackground="white")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

# Campos de entrada
label_user = tk.Label(frame, text="Usuario", font=("Arial", 12))
label_user.pack(pady=5)
entry_user = tk.Entry(frame, font=("Arial", 12))
entry_user.pack(pady=5)

label_pass = tk.Label(frame, text="Contraseña", font=("Arial", 12))
label_pass.pack(pady=5)
entry_pass = tk.Entry(frame, show="*", font=("Arial", 12))
entry_pass.pack(pady=5)

# Botón de login
btn_login = tk.Button(frame, text="Iniciar Sesión", font=("Arial", 14), command=validate_login)
btn_login.pack(pady=20)

root.mainloop()
