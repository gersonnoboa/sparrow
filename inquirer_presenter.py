import inquirer


def get_inquirer_answer(message, choices):
  questions = [inquirer.List('presenter', message=message, choices=choices, carousel=True)]
  answers = inquirer.prompt(questions)

  if answers:
    answer = answers['presenter']
    return answer

  return None

