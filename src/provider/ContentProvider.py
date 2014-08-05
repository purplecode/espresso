import abc

class ContentProvider(object):

  @abc.abstractmethod
  def getCallables(self):
    pass
