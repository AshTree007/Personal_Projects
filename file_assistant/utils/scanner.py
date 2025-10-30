import os
import time

def scan_folder(path):
    files = {}
    # os.walk goes through all subfolders
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        filenames = [f for f in filenames if not f.startswith(".")]
        for filename in filenames:
            file_path = os.path.join(root, filename)
            try:
                stats = os.stat(file_path)
                modified = time.ctime(stats.st_mtime)
                files[file_path] = modified  # store full path as key
            except FileNotFoundError:
                # Skip files that disappear during scanning
                pass
    return files