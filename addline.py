import os
import glob

# Function to modify HTML files
def modify_html_files():
    # Define the lines to add to each HTML file
    lines_to_add = [
        '<!-- usage. -->\n<script src="https://raw.githubusercontent.com/r8r7/amplify/main/games/scripts/everypage.js"></script>\n',
        '<script src="https://raw.githubusercontent.com/r8r7/amplify/main/games/scripts/everypage2.js"></script>\n<!-- usage. -->\n'
    ]

    # Define the directory where your HTML files are located
    directory = 'C:/Users/peros/Documents/GitHub/r8r7games/amplify/games'

    # Use glob to find all HTML files in the directory and its subdirectories
    html_files = glob.glob(directory + '/**/index.html', recursive=True)

    # Loop through each HTML file and add the lines
    for file_path in html_files:
        with open(file_path, 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            for line in lines_to_add:
                file.write(line + content)

        print(f"Added lines to {file_path}")

# Call the function to modify HTML files
modify_html_files()
