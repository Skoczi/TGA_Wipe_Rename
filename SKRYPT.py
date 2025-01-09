import os

def rename_files_in_folder(folder_path, base_name):
    try:
        # Pobierz listę plików w folderze
        files = [f for f in os.listdir(folder_path) if f.lower().endswith('.tga')]
        files.sort()  # Upewnij się, że pliki są posortowane

        for index, file_name in enumerate(files):
            new_name = f"{base_name}_{index:03}.tga"  # Tworzenie nowej nazwy, numeracja od 000
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_name)

            os.rename(old_file_path, new_file_path)
            print(f"Zmieniono nazwę: {file_name} -> {new_name}")

        print("Zmiana nazw zakończona sukcesem.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Przykład użycia:
folder_path = input("Podaj ścieżkę do folderu z plikami TGA: ")
base_name = input("Podaj nową podstawową nazwę plików (np. NAZWA1_ILOSCKLATEK): ")
rename_files_in_folder(folder_path, base_name)