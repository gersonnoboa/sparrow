class Subtitles:
  def __init__(self, subtitles):
    self.subtitles = subtitles


class Subtitle:
  def __init__(self, release_name, srt_name, zip_download_link, score, download_count):
    self.release_name = release_name
    self.srt_name = srt_name
    self.zip_download_link = zip_download_link
    self.score = score
    self.download_count = download_count
