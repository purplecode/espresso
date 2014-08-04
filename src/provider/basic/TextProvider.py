from src.utils.DictUtils import DictUtils
from src.provider.ContentProvider import ContentProvider

class Text(object):

  def __init__(self, paragraph, dictionary):
    self.paragraph = paragraph
    self.dictionary = dictionary

  def get(self, path):
    return DictUtils.get(self.dictionary, path.strip(), "#undefined#")

class TextProvider(ContentProvider):

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def getCallable(self, paragraph):
    return Text(paragraph, self.dictionary)

