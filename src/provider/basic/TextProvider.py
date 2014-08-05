from src.utils.DictUtils import DictUtils
from src.provider.ContentProvider import ContentProvider

class TextProvider(ContentProvider):

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def getCallables(self):
    return ['text']

  def text(self, paragraph, path):
    return DictUtils.get(self.dictionary, path.strip(), "#undefined#")

