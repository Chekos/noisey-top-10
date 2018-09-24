# La meta de este script es limpiar las letras (archivos de texto) que serán utilizadas en el análisis para Noisey.
# Las barras de progreso son completamente decorativas y no sirven ninguna función.

import re
import os
import sys
from tqdm import tqdm


def limpia_textos(filepath: str = sys.argv[1]):
    """
    Esta funcion toma la dirección de un archivo y 1) elimina corchetes "[]", 2) elimina espacios y líneas vacías, 
    """
    
    # abrir archivo, usamos utf-8 para asegurarnos de que se lean bien las palabras con tilde.
    with open(filepath, "r", encoding = "utf-8") as file:
        texto = file.read()
        
    texto = re.sub(r'\[[^)]*\]', "", texto)
    texto = texto.replace("\n\n\n\n\n", "\n")
    texto = texto.replace("\n\n\n\n", "\n")
    texto = texto.replace("\n\n\n", "\n")
    texto = texto.replace("\n\n", "\n")
    
    
    # salvar el archivo limpio    
    path, filename = os.path.split(filepath)
    parent_dir, data_dir = os.path.split(path)
    filename, extension = os.path.splitext(filename)
    filepath_out = os.path.join(parent_dir, "processed", f"{filename}-limpio{extension}")

    with open(filepath_out, "w", encoding = "utf-8",) as clean_file:
        clean_file.write(texto)
        
    return filepath_out, filename
    
if __name__ == "__main__":
    
    filepath_out, filename = limpia_textos(filepath = sys.argv[1])
    
    print("#"*59)
    print("_"*30)
    print(f"Limpiando el archivo {filename}")
    for i in tqdm(range(5_000_000)):
        pass
    print("_"*59)
    print(f"Guardando el archivo {filepath_out}")
    for i in tqdm(range(5_000_000)):
        pass
    print("#"*59)
    


