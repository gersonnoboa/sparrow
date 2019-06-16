from inquirer_presenter import get_inquirer_answer

def get_subtitle_from_user(subtitles):
  choices = subtitles.get_release_names()
  answer = get_inquirer_answer("Select a subtitle", choices)
  return subtitles.get_subtitle_with_release_name(answer)
