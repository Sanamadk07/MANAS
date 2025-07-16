# commands/files.py

import os
from core.tts import speak

def handle_files(command):
    if 'create folder' in command:
        # Expected format: "create folder foldername"
        parts = command.split()
        if len(parts) >= 3:
            folder_name = " ".join(parts[2:])
            try:
                os.makedirs(folder_name, exist_ok=True)
                speak(f"Folder named {folder_name} has been created.")
            except Exception as e:
                speak("Sorry, I couldn't create the folder.")
                print(f"Error creating folder: {e}")
        else:
            speak("Please specify the folder name.")
        return True

    elif 'delete file' in command:
        # Expected format: "delete file filename"
        parts = command.split()
        if len(parts) >= 3:
            file_name = " ".join(parts[2:])
            if os.path.exists(file_name):
                try:
                    os.remove(file_name)
                    speak(f"File {file_name} has been deleted.")
                except Exception as e:
                    speak("Sorry, I couldn't delete the file.")
                    print(f"Error deleting file: {e}")
            else:
                speak(f"The file {file_name} does not exist.")
        else:
            speak("Please specify the file name to delete.")
        return True

    elif 'list files' in command or 'list folder' in command:
        path = '.'
        parts = command.split()
        if len(parts) >= 3:
            path = " ".join(parts[2:])
        try:
            files = os.listdir(path)
            if files:
                speak(f"Files and folders in {path} are:")
                for f in files:
                    speak(f)
            else:
                speak(f"No files found in {path}.")
        except Exception as e:
            speak("Sorry, I couldn't list files.")
            print(f"Error listing files: {e}")
        return True

    return False
