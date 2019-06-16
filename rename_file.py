import os
from inquirer_presenter import get_inquirer_answer


def rename_file(new_name):
  files = os.listdir()
  answer = get_inquirer_answer("Select video file to rename", files)

  if answer:
    new_filename = get_new_filename(new_name, answer)
    
    if not new_filename: 
      return False

    os.rename(answer, new_filename)
    
    return True
  
  return False


def get_new_filename(new_name, old_filename):
  file_extension = get_file_extension(old_filename)

  if not file_extension:
    return None

  return f'{new_name}.{file_extension}'


def get_file_extension(file):
  string_components = file.split(".")

  if len(string_components) >= 1:
    components_length = len(string_components)
    return string_components[components_length - 1]

  return None
