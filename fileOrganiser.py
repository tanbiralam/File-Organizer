import os 
import shutil

def organize_files():
    try:
        path = input("Enter folder directory: ")
        if not os.path.exists(path):
            print("Error: The specified directory does not exist.")
            return

        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:] 
            if extension:
                if not os.path.exists(os.path.join(path, extension)):
                    os.makedirs(os.path.join(path, extension))
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
                print(f"Moved {file} to {extension} folder.")
        print("File organization completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    organize_files()
