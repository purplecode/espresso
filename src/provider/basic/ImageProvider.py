import os

class ImageProvider(object):

  def __init__(self, paragraph):
    self.paragraph = paragraph

  def fromFile(self, filepath):
    return self.__insert(os.path.join(os.getcwd(), filepath))

  def __insert(self, file):
    shape = self.paragraph._parent._parent
    shape._parent.add_picture(file, shape.left, shape.top, shape.width, shape.height)
    return ''