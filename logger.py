import sys

LOG_FILE = "Logs.txt"


def reset_logs():
    open(LOG_FILE, "w").close()

def Write_Logs__To_text_File(content: str) -> None:
    """Write a line to the Logs.txt file."""
    File_Object = open(LOG_FILE, "a")
    File_Object.write(content)
    File_Object.write("\n")
    File_Object.close()

def error_message(content: str) -> None:
    """Write a error message to stderr and exit the program."""
    print(content, file=sys.stderr)
    Write_Logs__To_text_File("Error")
    sys.exit(1)