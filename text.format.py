import os

def trim_text_files(directory):
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r') as file:
                lines = file.readlines()

            # Remove extra new lines
            trimmed_lines = [line for line in lines if line.strip() != ""]
            
            with open(filepath, 'w') as file:
                file.writelines(trimmed_lines)
                
            print(f"Processed file: {filename}")

if __name__ == "__main__":
    text_directory = "text"  # Specify the path to your text folder
    if os.path.exists(text_directory):
        trim_text_files(text_directory)
    else:
        print(f"The directory {text_directory} does not exist.")
