#! /usr/bin/python3

import re, sys
from splinter import Browser

# main
# print title & artist to stdout from url provided as first argument
def main():
  if len(sys.argv) != 2: sys.exit('usage: scraper.py <url>')
  url = sys.argv[1]
  info = None
  try:
    validate(url)
    info = scrape(url)
  except Exception as err:
    sys.exit(err)
  else:
    print(info)

# validate
# ensure provided url is valid
def validate(url):
  yt = '^.*(youtu.be\/|v\/|u\/\w\/|watch\?v=|\&v=)([^#\&\?]*).*'
  regex = re.compile(yt)
  match = regex.search(url)
  if match == None: raise Exception('invalid or unsupported url')

# scrape
# perform browser control at url
def scrape(url):
  browser = first_available_browser()
  browser.visit(url)
  info = extract_info(browser)
  browser.quit()
  return info

# first available browser
# return browser object if either chrome or firefox is accessible
def first_available_browser():
  browser = None
  for option in ['chrome', 'firefox']:
    try:
      browser = Browser(option)
      break
    except:
      pass
  if browser == None: raise Exception('ensure browser accessible from path')
  else: return browser

# extract info
# use browser page to find song metadata
def extract_info(browser):
  video = browser.find_by_id('eow-title')
  extras = browser.find_by_id('watch-description-extras')
  artist = ''
  title = video.value
  words = extras.value.split()
  if not words: # best guess from video title
    separator = title.find('-')
    if separator != -1:
      artist = title[:separator].strip()
      title = title[separator+1:].strip()
  elif words[0] == 'Music': # necessary info on page
    artist = extract_artist(words)
    title = extract_title(words)
  return [title, artist]

# extract title
# use word list from youtube to determine song title
def extract_title(words):
  title = ''
  start = None
  end = None
  for i in range(len(words)):
    current = words[i]
    if current[0] == '"': start = i
    elif current[len(current)-1] == '"': end = i+1
    elif current == 'by' and end: break
  for i in range(start, end): title += words[i] + ' '
  return title[1:len(title)-2] # strip quotations & last space

# extract artist
# use word list from youtube to determine song artist
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


if __name__ == '__main__':
  main()
