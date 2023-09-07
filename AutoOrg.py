import os
import shutil
import time
import traceback

# Get the user's home directory
user_home = os.path.expanduser("~")

# Define the source directory (Downloads folder)
source_directory = os.path.join(user_home, "Downloads")

# Define the destination directories (default music, picture, and video folders)
music_destination = os.path.join(user_home, "Music")
picture_destination = os.path.join(user_home, "Pictures")
video_destination = os.path.join(user_home, "Videos")

# Function to periodically scan the "Downloads" folder and organize files
def organize_downloads():
    while True:
        for item in os.listdir(source_directory):
            item_path = os.path.join(source_directory, item)
            if os.path.isfile(item_path):
                filename = os.path.basename(item_path)
                file_extension = os.path.splitext(filename)[1].lower()

                if file_extension in ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.ape', '.amr', '.mid', '.midi', '.au', '.ra', '.rm', '.ac3'):
                    destination_path = os.path.join(music_destination, filename)
                elif file_extension in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico'):
                    destination_path = os.path.join(picture_destination, filename)
                elif file_extension in ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.m4v', '.webm'):
                    destination_path = os.path.join(video_destination, filename)
                else:
                    # For other file types, you can choose to move them to a different folder or skip them.
                    # Here, we'll skip them.
                    continue

                try:
                    shutil.move(item_path, destination_path)
                    print(f"Moved '{filename}' to '{destination_path}'")
                except PermissionError:
                    print(f"PermissionError occurred while moving '{filename}', retrying...")
                    time.sleep(1)
                except Exception as e:
                    print(f"An error occurred while moving '{filename}': {str(e)}")
        time.sleep(1)  # Sleep before checking again

if __name__ == "__main__":
    try:
        print("File monitoring started.")
        # Start a separate thread to periodically scan and organize the "Downloads" folder
        import threading
        threading.Thread(target=organize_downloads).start()

        while True:
            time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n\n{traceback.format_exc()}"
        desktop = os.path.join(user_home, "Desktop")
        log_file_path = os.path.join(desktop, "file_monitoring_error.txt")
        with open(log_file_path, "w") as log_file:
            log_file.write(error_message)
        print(f"Error logged to {log_file_path}")