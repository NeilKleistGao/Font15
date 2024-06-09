import json

class Config:
  __output = ""
  __fonts = []
  __include = []
  def __check_data(self, data: any, key: str, ty: type) -> None:
    try:
      if type(data[key]) != ty:
        print("the data ${key} is not correct.".format(key = key))
        exit(-1)
    except:
      print("can't read ${key}".format(key = key))
      exit(-1)
  def __init__(self, path: str) -> None:
    try:
      fp = open(path, "r", encoding="utf-8")
    except OSError:
      print("can't open file {filename}".format(filename = path))
      exit(-1)
    content = "\n".join(fp.readlines())
    fp.close()
    data = json.loads(content)
    self.__check_data(data, "output", type(self.__output))
    self.__output = data["output"]
    self.__check_data(data, "fonts", type(self.__fonts))
    self.__fonts = data["fonts"]
    self.__check_data(data, "include", type(self.__include))
    self.__include = data["include"]
