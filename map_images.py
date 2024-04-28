import glob
import csv
import shutil

output_folder = 'archive/images/'
output_file = './labels.csv'

ext = 'jpg'

root_path = 'archive/'

# get all the files in a directory and subdirecotries
images = glob.glob(f'{root_path}**/*.{ext}', recursive=True)

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Type1'])
    for image in images:
        split_path = image.replace('\\', '/').split('/')
        name = split_path[-1].replace(f'.{ext}', '')
        parent = split_path[-2]
        writer.writerow([name, parent])
        # copy the image
        shutil.copy(image, f'{output_folder}')


