import abc

class ContentProvider(object):

  @abc.abstractmethod
  def getCallable(self, paragraph):
    pass
