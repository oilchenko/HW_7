from pathlib import Path
from os import path
import shutil
import sys
import gzip

import clean_folder.file_parser as parser
from clean_folder.normalize import normalize


def handle_file(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    full_name = path.basename(filename)
    name = path.splitext(full_name)[0]
    suffix = filename.suffix[1:]
    filename.replace(target_folder / normalize(name, suffix))

def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''), "")
    
    file_extension = parser.get_extension(filename)
    if file_extension == 'ZIP' or file_extension == 'TAR':
        try:
            file_extension = parser.get_extension(filename)
            shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
        except shutil.ReadError:
            print(f"Помилка обробки архіву ZIP або TAR: {filename}!")
            folder_for_file.rmdir()
            return None
    if file_extension == 'GZ':
            gz_filename_0ext = Path(filename.name.replace(filename.suffix, ''))
            
            archived_file_suffix = gz_filename_0ext.suffix
            archived_filename_0ext = Path(gz_filename_0ext.name.replace(gz_filename_0ext.suffix, ''))
            normalized_archived_filename_0ext = normalize(str(archived_filename_0ext), "")
            archived_filename = normalized_archived_filename_0ext + archived_file_suffix
            
            folder_for_file.mkdir(exist_ok=True, parents=True)
            gz_extraction_path = str(folder_for_file) + "/" + archived_filename
            gz_extraction_path = gz_extraction_path.replace("\\", "/")
            with gzip.open(filename, 'rb') as fr, open(gz_extraction_path, 'wb') as fw:
                bytes_data = fr.read()
                fw.write(bytes_data)
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'\nПомилка видалення папки {folder}')

def main(folder: Path):
    parser.scan(folder)
    
    for file in parser.JPEG_IMAGES:
        handle_file(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_file(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_file(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_file(file, folder / 'images' / 'SVG')

    for file in parser.MP3_AUDIO:
        handle_file(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handle_file(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handle_file(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handle_file(file, folder / 'audio' / 'AMR')

    for file in parser.AVI_VIDEO:
        handle_file(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_file(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_file(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_file(file, folder / 'video' / 'MKV')

    for file in parser.DOC_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'DOCX')
    for file in parser.XLS_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'XLS')
    for file in parser.XLSX_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'XLSX')
    for file in parser.TXT_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'PDF')
    for file in parser.PPT_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'PPT')
    for file in parser.PPTX_DOCUMENTS:
        handle_file(file, folder / 'documents' / 'PPTX')

    for file in parser.MY_OTHER:
        handle_file(file, folder / 'MY_OTHER')

    for file in parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives')
    for file in parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives')
    for file in parser.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

    parser.parser_info()

def path_function():
    try:
        folder = sys.argv[1]
    except IndexError:
        print('Enter valid path to the folder as an argument')
    else:
        folder_for_scan = Path(folder)
        print(f'\nStart in folder: {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

if __name__ == '__main__':
    path_function()