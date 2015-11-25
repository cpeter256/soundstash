import re, sys 
from splinter import Browser 

class YoutubeScraper:
  def __init__(self):
    self.__browser = None
    self.__open_browser()
 
  def __del__(self):
    if self.__browser: self.__browser.quit()

  def scrape(self, url):
    # inner function validate
    def validate(url):
      yt = '^.*(youtu.be\/|v\/|u\/\w\/|watch\?v=|\&v=)([^#\&\?]*).*'
      regex = re.compile(yt)
      match = regex.search(url) 
      if match == None: raise Exception
    # begin scrape function
    info = ('', '') # (title, artist) tuple
    try:
      validate(url)
      self.__browser.visit(url)
      info = self.__extract_info()
    except Exception as err:
      pass # return blank tuple if scrape unsuccessful
    return info

  def __open_browser(self):
    for option in ['chrome', 'firefox']:
      try:
        self.__browser = Browser(option)
        break
      except:
        pass
    if not self.__browser:
      raise Exception('YoutubeScraper: ensure browser accessible from path')

  def __extract_info(self):
    # inner function extract title
    def extract_title(words):
      title = ''
      start = None
      end = None
      for i in range(len(words)):
        current = words[i]
        if current[0] == '"': start = i
        if current[len(current)-1] == '"': end = i+1
        elif current == 'by' and end: break
      for i in range(start, end): title += words[i] + ' '
      return title[1:len(title)-2] # strip quotations & last space
    # inner function extract artist
    def extract_artist(words):
      artist = ''
      start = None
      end = None
      for i in range(len(words)):
        current = words[i]
        if current == 'by' and not start: start = i+1
        elif start and current[0] == '(': end = i
        elif start and end: break
      for i in range(start, end): artist += words[i] + ' '
      return artist[:len(artist)-1] # strip last space
    # begin __extract_info function
    artist = ''
    title = self.__browser.find_by_id('eow-title').value
    extras = self.__browser.find_by_id('watch-description-extras').value
    if not extras: # best guess from video title
      separator = title.find('-')
      if separator != -1:
        artist = title[:separator].strip()
        title = title[separator+1:].strip()
    else:
      words = extras.split()
      if words[0] == 'Music': # necessary info on page
        artist = extract_artist(words)
        title = extract_title(words)
    return (title, artist)
# end class
