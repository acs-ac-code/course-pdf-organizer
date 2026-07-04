import os

folder_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate 4"

try:
    files = os.listdir(folder_path)
    count = 0
    for filename in files:
        if "_Club_Mateoteca.pdf" in filename:
            # Create new filename by replacing "_Club_Mateoteca" with "_Mateoteca"
            new_filename = filename.replace("_Club_Mateoteca", "_Mateoteca")
            
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            os.rename(old_path, new_path)
            count += 1
            print(f"Renamed: {filename} -> {new_filename}")

    print(f"\nSuccessfully renamed {count} files.")

except Exception as e:
    print(f"Error during renaming: {e}")
