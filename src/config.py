import json

class Config:
  __output = ""
  __fonts = []
  __include = []
  def __init__(self, path: str) -> None:
    fp = open(path, "r", encoding="utf-8") # TODO: check
    content = "\n".join(fp.readlines())
    fp.close()
    data = json.loads(content) # TODO: check
    self.__output = data["output"]
    self.__fonts = data["fonts"]
    self.__include = data["include"]
