from datetime import datetime, timedelta
import os

def find_old_files(path, days=30):
    now = datetime.now()
    cutoff = now - timedelta(days=days)
    old_files = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                mtime = datetime.fromtimestamp(os.stat(file_path).st_mtime)
                if mtime < cutoff:
                    old_files.append(file_path)
            except FileNotFoundError:
                pass
    return old_files
