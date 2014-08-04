#!/usr/bin/env python

import argparse

from pptx import Presentation

from src.parser.MetatagsHandler import MetatagsHandler
from src.utils.Logger import Logger
from src.parser.PresentationParser import PresentationParser
from src.provider.basic.ImageProvider import ImageProvider
from src.provider.basic.TextProvider import TextProvider
from src.provider.ArgumentsProvider import ArgumentsProvider


def main(inputFile, outputFile):

  argumentsProvider = ArgumentsProvider({
    'title' : 'Maka Paka',
    'items' : [
      {'name' : 'ItemA', 'estimate' : 1},
      {'name' : 'ItemB', 'estimate' : 2},
      {'name' : 'ItemC', 'estimate' : 3}
    ]
  })

  presentationHandler = MetatagsHandler(argumentsProvider)
  presentationHandler.addProvider('image', ImageProvider())
  presentationHandler.addProvider('text', TextProvider({'test' : 'testText'}))

  presentation = Presentation(inputFile)
  PresentationParser(presentationHandler).parse(presentation)

  presentation.save(outputFile)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('-t', '--template', dest='template', help='PPT template')
  parser.add_argument('-o', '--output', default='output.pptx', dest='output', help='Output presentation')
  parser.add_argument('-l', '--loglevel', dest='loglevel', default='WARN', help='processing log level(DEBUG, INFO, WARN, ERROR)')

  args = parser.parse_args()

  Logger.setLevel(args.loglevel)

  main(args.template, args.output)



