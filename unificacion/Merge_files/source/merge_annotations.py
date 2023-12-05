try:
    import os
    import subprocess
    from datetime import datetime
    import shutil
except ImportError as e:
    print('{} Mssg: cannot import library: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e))


class merge():
    def __init__(self, config):
        self.root = config['rootdir']
        print('root', self.root)
        self.config = config['data']
        self.path_desordenadas = self.config['path_principal']
        self.path_juntas = self.config['path_merge']
        self.subfolder_names = ['train', 'val', 'test']
        if not os.path.exists(self.path_juntas):
            os.mkdir(self.path_juntas)
       
    def merge_folders(self):
        try:
            print('{} Mssg: Start merge annotations.'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            # Crear las carpetas de destino si no existen
            destination_folders = {name: os.path.join(self.path_juntas, name) for name in self.subfolder_names}
            for dest_folder in destination_folders.values():
                os.makedirs(dest_folder, exist_ok=True)
                # Crear subcarpetas 'images' y 'labels'
                os.makedirs(os.path.join(dest_folder, 'images'), exist_ok=True)
                os.makedirs(os.path.join(dest_folder, 'labels'), exist_ok=True)

            # Recorrer cada carpeta de fecha
            date_folders = [f for f in os.listdir(self.path_desordenadas) if os.path.isdir(os.path.join(self.path_desordenadas, f))]

            for date_folder in date_folders:
                for subfolder_name in self.subfolder_names:
                    # Ruta de la subcarpeta actual
                    current_subfolder_path = os.path.join(self.path_desordenadas, date_folder, subfolder_name)

                    # Dividir en imágenes y etiquetas
                    for subsubfolder_name in ['images', 'labels']:
                        subsubfolder_path = os.path.join(current_subfolder_path, subsubfolder_name)
                        if os.path.exists(subsubfolder_path):
                            # Copiar todos los archivos de esta subcarpeta a la carpeta de destino correspondiente
                            for filename in os.listdir(subsubfolder_path):
                                src_file = os.path.join(subsubfolder_path, filename)
                                dst_file = os.path.join(destination_folders[subfolder_name], subsubfolder_name, filename)
                                shutil.copy2(src_file, dst_file)

            print('{} Mssg: Finished merge annotations.'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        except subprocess.CalledProcessError as e:
            print('{} Mssg: Error merge annotations: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e))