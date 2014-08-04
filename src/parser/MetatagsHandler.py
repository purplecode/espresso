import re

from src.parser.PresentationHandler import PresentationHandler
from src.parser.ContentRenderer import ContentRenderer
from src.utils.Logger import Logger
from src.utils.DictUtils import DictUtils

class MetatagsHandler(PresentationHandler):

  METATAG_PATTERN = re.compile("\s*(\{\{\s*.*?\s*\}\})\s*")
  EXPRESSION_PATTERN = re.compile("\$([\w\.]+)")

  def __init__(self, textProvider):
    self.textProvider = textProvider
    self.renderer = ContentRenderer()

  def addProvider(self, name, providerClass):
     self.renderer.addProvider(name, providerClass)

  def paragraph(self, paragraph, text):
    metatags = self.METATAG_PATTERN.findall(text)
    for metatag in metatags:
      metatagReplacement = self.__renderMetatag(metatag, paragraph)
      Logger.info('replacing "%s" with "%s"' % (metatag, metatagReplacement))
      text = text.replace(metatag, metatagReplacement)
    paragraph.text = text

  def __renderMetatag(self, metatag, paragraph):
    expressions = self.EXPRESSION_PATTERN.findall(metatag)
    templateData = self.__getTemplateData(expressions)
    templateContent = re.sub('\[|\]', '.', metatag.replace('$', ''))
    return self.renderer.render(paragraph, templateContent, templateData)

  def __getTemplateData(self, expressions):
    templateData = {}
    for expression in expressions:
      value = self.textProvider.get(expression)
      DictUtils.ensureKeys(templateData, expression, value)
    return templateData