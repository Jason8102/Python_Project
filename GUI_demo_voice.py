import os

# Specify the directory where the files are located
directory = "/path/to/directory"

# Get a list of all the .wav files in the directory
wav_files = [f for f in os.listdir(directory) if f.endswith(".wav")]

# Sort the list of files in ascending order based on their file name
sorted_files = sorted(wav_files, key=lambda f: int(f.split("recording")[1].split(".")[0]))

# Print all the file names
print("All files in directory:")
for file in sorted_files:
    print(file)

# Get the largest file name from the sorted list
largest_file = sorted_files[-1]

# Print the largest file name
print("Largest file name: ", largest_file)
