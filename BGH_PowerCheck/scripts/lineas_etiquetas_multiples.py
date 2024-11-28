import os

def count_instances(label_folder):
    total_instances = 0
    file_instances = {}

    for file in os.listdir(label_folder):
        if file.endswith('.txt'):
            path = os.path.join(label_folder, file)
            with open(path, 'r') as f:
                lines = f.readlines()
                file_instances[file] = len(lines)  # Contar líneas en el archivo
                total_instances += len(lines)
    
    return total_instances, file_instances

# Ruta a las etiquetas
label_folder = "D:/CIENCIA-DE-DATOS-IA-4TO-CUATRIMESTRE/Practica-profecionalizantes-2/Sistema-BGH-Cable-Detection/BGH_PowerCheck/datasets/train/labels/correct"

# Contar instancias
total_instances, file_instances = count_instances(label_folder)

# Mostrar resultados
print(f"Total de instancias: {total_instances}")
print("Instancias por archivo:")
for file, count in file_instances.items():
    print(f"{file}: {count}")
