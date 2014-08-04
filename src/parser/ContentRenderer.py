from jinja2 import Template as JinjaTemplate

class ContentRenderer(object):

  def __init__(self):
    self.providers = {}

  def addProvider(self, name, providerClass):
    self.providers[name] = providerClass

  def render(self, paragraph, templateContent, templateData):
    template = JinjaTemplate(templateContent)
    self.__registerProviders(paragraph, template)
    return template.render(templateData)

  def __registerProviders(self, paragraph, template):
    for name, provider in self.providers.iteritems():
      template.globals[name] = lambda: provider(paragraph)
