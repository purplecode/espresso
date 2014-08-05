from jinja2 import Template as JinjaTemplate

class ContentRenderer(object):

  def __init__(self):
    self.providers = []

  def addProvider(self, provider):
    self.providers.append(provider)

  def render(self, paragraph, templateContent, templateData):
    template = JinjaTemplate(templateContent)
    self.__registerProviders(paragraph, template)
    return template.render(templateData)

  def __registerProviders(self, paragraph, template):
    for provider in self.providers:
      for callable in provider.getCallables():
        template.globals[callable] = self.__getCallable(callable, paragraph, provider)

  def __getCallable(self, callable, paragraph, provider):
    return lambda *args: getattr(provider, callable)(paragraph, *args)
