import inquirer


def get_subtitle_from_user(subtitles):
  choices = subtitles.get_release_names()
  print(choices)
  questions = [inquirer.List('subtitle', message="Select a subtitle", choices=choices, carousel=True)]
  answers = inquirer.prompt(questions)

  if answers:
    answer = answers['subtitle']
    return subtitles.get_subtitle_with_release_name(answer)

  return None

