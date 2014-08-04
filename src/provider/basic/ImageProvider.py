import os
from src.provider.ContentProvider import ContentProvider

class ImageProvider(ContentProvider):

  callable = 'image'

  def getCallable(self, paragraph, filepath):
    self.__insert(paragraph, os.path.join(os.getcwd(), filepath))
    return ''

  def __insert(self, paragraph, filepath):
    shape = paragraph._parent._parent
    shape._parent.add_picture(filepath, shape.left, shape.top, shape.width, shape.height)