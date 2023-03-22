
import os
import sys
import subprocess


def create_all_tiles_from(input_file):
    print(f'create_all_tiles_from({input_file})')

def main(args=sys.argv):
    os.makedirs('data', exist_ok=True)
    os.makedirs('fetch-data-inputs', exist_ok=True)
    fetch_data_in_dir = 'fetch-data-inputs'
    num_inputs_processed = 0
    for file in os.listdir(fetch_data_in_dir):
        if len(file) > 2:
            file = os.path.join(fetch_data_in_dir, file)
            create_all_tiles_from(file)
            num_inputs_processed += 1
    
    if num_inputs_processed < 1:
        print('''
WARNING: 0 input files processed, please fill ./fetch-data-inputs with files
describing GIS data and bounding areas, for example:
   
   - a file named "USGSTopo.json" with the contents {"bbox":[], "url": "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer?f=pitemx"}
     will download tiles within the given bounding box from the WFS server and store them as zoom/x/y.png files

'''.strip())
        print()


if __name__ == '__main__':
    main()

