import os
from datetime import datetime, timedelta

target_directory = "F:\\Videos"

# Initialize an empty list to hold old video files
old_video_files = []

# Get current time
current_time = datetime.now()

# Loop through the directory tree
for dirpath, dirnames, filenames in os.walk(target_directory):
    for filename in filenames:
        if filename.endswith(('.mp4', '.avi', '.mkv')):
            full_path = os.path.join(dirpath, filename)
            
            # Get the creation time and convert it to a datetime object
            creation_time = datetime.fromtimestamp(os.path.getctime(full_path))
            
            # Calculate the age of the file
            file_age = current_time - creation_time

            # Check if the file is older than one year
            if file_age > timedelta(days=365):
                old_video_files.append(full_path)
                print(f"Old file found: {full_path}")

# Delete the old video files
for file_path in old_video_files:
    try:
        os.remove(file_path)
        print(f"Successfully Deleted: {file_path}")
    except Exception as e:
        print(f"Failed to delete {file_path}: {e}")

