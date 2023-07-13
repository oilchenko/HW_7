from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
XLS_DOCUMENTS = []
XLSX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
PPT_DOCUMENTS = []
PPTX_DOCUMENTS = []
MY_OTHER = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

REGISTERED_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'XLS': XLS_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'PPT': PPT_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []

EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTERED_EXTENSIONS[ext]
                container.append(fullname)
                EXTENSIONS.add(ext)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)
    print(f"\nScan function has scanned the folder {folder}")

def print_function(object, object_title):
    print("\n" + object_title)
    for _ in object:
        print(_, end="\n")

def parser_info():
    print_function(JPEG_IMAGES, "Images jpeg:")
    print_function(JPG_IMAGES, "Images jpg:")
    print_function(PNG_IMAGES, "Images png:")
    print_function(SVG_IMAGES, "Images svg:")

    print_function(MP3_AUDIO, "Audio mp3:")
    print_function(OGG_AUDIO, "Audio ogg:")
    print_function(WAV_AUDIO, "Audio wav:")
    print_function(AMR_AUDIO, "Audio amr:")
    
    print_function(AVI_VIDEO, "Video avi:")
    print_function(MP4_VIDEO, "Video mp4:")
    print_function(MOV_VIDEO, "Video mov:")
    print_function(MKV_VIDEO, "Video mkv:")
    
    print_function(DOC_DOCUMENTS, "Documents doc:")
    print_function(DOCX_DOCUMENTS, "Documents docx:")
    print_function(XLS_DOCUMENTS, "Documents xls:")
    print_function(XLSX_DOCUMENTS, "Documents xlsx:")
    print_function(TXT_DOCUMENTS, "Documents txt:")
    print_function(PDF_DOCUMENTS, "Documents pdf:")
    print_function(PPT_DOCUMENTS, "Documents ppt:")
    print_function(PPTX_DOCUMENTS, "Documents pptx:")

    print_function(ZIP_ARCHIVES, "zip archives:")
    print_function(GZ_ARCHIVES, "gz archives:")
    print_function(TAR_ARCHIVES, "tar archives:")
    
    print_function(MY_OTHER, "My other:")

    print_function(EXTENSIONS, "Types of files in scanned folder:")
    
    print_function(UNKNOWN, "Unknown types of files:")
    
    print_function(FOLDERS[::-1], "List of folders:")