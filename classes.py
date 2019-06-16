class Subtitles:
  def __init__(self, subtitles):
    self.subtitles = subtitles


  def get_release_names(self):
    return list(map(self.get_titles_from_subtitle, self.subtitles))


  def get_titles_from_subtitle(self, subtitle):
    return subtitle.release_name


  def get_subtitle_with_release_name(self, release_name):
    for subtitle in self.subtitles:
      if subtitle.release_name == release_name:
        return subtitle


class Subtitle:
  def __init__(self, release_name, srt_name, zip_download_link, score, download_count):
    self.release_name = release_name
    self.srt_name = srt_name
    self.zip_download_link = zip_download_link
    self.score = score
    self.download_count = download_count


  def get_subtitle_raw_name(self):
    string_components = self.srt_name.split(".")

    if len(string_components) >= 1:
      return string_components[0]
      
    return None
