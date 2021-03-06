import re, copy

class DictUtils(object):

  @staticmethod
  def setif(bool, object, key, value):
    if bool:
      object[key] = value

  @staticmethod
  def ensureKey(obj, key, default):
    key = int(key) if re.match(r'\d+', key) else key.lower()
    if not key in obj:
        obj[key] = default
    return obj[key]

  @staticmethod
  def ensureKeys(obj, keys, default):
    keys = keys.split('.') if isinstance(keys, str) else keys
    if len(keys) == 1:
      return DictUtils.ensureKey(obj, keys[0], default)
    else:
      subObj = DictUtils.ensureKey(obj, keys[0], {})
      return DictUtils.ensureKeys(subObj, keys[1:], default)

  @staticmethod
  def hasKeys(obj, keys):
    for key in keys:
      if key not in obj:
        return False
    return True

  @staticmethod
  def getKey(obj, value):
    for key in obj.keys():
      if obj[key] == value:
        return key

  @staticmethod
  def get(document, path, default = None):
    if not DictUtils.has(document, path):
      return default
    current = document
    for elem in path.split('.'):
      if re.match(r'\d+', elem) and isinstance(current, list):
        current = current[int(elem)]
      else:
        if elem in current:
          current = current[elem]
    return current

  @staticmethod
  def has(document, path, raiseErorr = False):
    current = document
    for elem in path.split('.'):
      if re.match(r'\d+', elem) and isinstance(current, list):
        if int(elem) < len(current):
          current = current[int(elem)]
        else:
          if raiseErorr:
            raise Exception("No index %s in %s" % (elem, current))
          return False
      else:
        if elem in current:
          current = current[elem]
        else:
          if raiseErorr:
            raise Exception("No key %s in %s" % (elem, current))
          return False
      if current == None:
        if raiseErorr:
          raise Exception("Empty value %s in %s" % (elem, current))
        return False
    return True

  @staticmethod
  def count(document, path, default = 0):
    if DictUtils.has(document, path):
      return len(DictUtils.get(document, path))
    return default

  @staticmethod
  def addAttributes(obj, attrs, ignore = []):
    for attrName in attrs.getNames():
      if not attrName in ignore:
        obj[attrName.lower()] = attrs.getValue(attrName)

  @staticmethod
  def extend(obj, element, ignore = []):
    for propName in element.iterkeys():
      if not propName in ignore:
        obj[propName.lower()] = element[propName]

  @staticmethod
  def deepExtend(a, b):
    if not isinstance(b, dict):
        return b
    result = copy.deepcopy(a)
    for k, v in b.iteritems():
        if k in result and isinstance(result[k], dict):
                result[k] = DictUtils.deepExtend(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result

  @staticmethod
  def getParentKeys(obj, element):
    keys = []
    for parentKey, elementList in obj.iteritems():
      if isinstance(elementList, dict) and elementList.has_key(element):
        keys.append(parentKey)
      if isinstance(elementList, list) and element in elementList:
        keys.append(parentKey)
    return keys