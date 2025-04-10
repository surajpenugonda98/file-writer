import os
import logging

LOG_FILE = 'file_writer.log'
OUTPUT_FILE = 'output.txt'
CONTENT = 'This is the content to write into the file.'

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def write_to_file(file_path: str, content: str) -> None:
    try:
        # Ensure the directory exists
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            logging.info(f"Successfully wrote content to '{file_path}'.")

    except Exception as e:
        logging.error(f"Failed to write to file '{file_path}': {str(e)}")
        raise  # Re-raise for further handling if needed

if __name__ == "__main__":
    try:
        write_to_file(OUTPUT_FILE, CONTENT)
    except Exception as error:
        print(f"An error occurred: {error}")
