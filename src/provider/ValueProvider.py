from src.utils.DictUtils import DictUtils

class ValueProvider(object):

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def getValue(self, path):
    return DictUtils.get(self.dictionary, path)
