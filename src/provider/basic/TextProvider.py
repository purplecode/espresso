from src.utils.DictUtils import DictUtils

class TextProvider(object):

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def get(self, path):
    return DictUtils.get(self.dictionary, path, "#undefined#")
