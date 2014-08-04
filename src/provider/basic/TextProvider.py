from src.utils.DictUtils import DictUtils
from src.provider.ContentProvider import ContentProvider

class TextProvider(ContentProvider):

  callable = 'text'

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def getCallable(self, paragraph, path):
    return DictUtils.get(self.dictionary, path.strip(), "#undefined#")

