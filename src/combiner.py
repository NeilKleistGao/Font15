from fontTools.ttLib import TTFont
from fontTools.merge import Merger
import glob

flat_map = lambda f, xs: [r for x in xs for r in f(x)]

class Combiner:
  __characters = []
  __font: TTFont = None
  def __read_characters(self, path: str) -> list:
    try:
      fp = open(path, "r", encoding="utf-8")
    except OSError:
      print("can't open file {filename}".format(filename = path))
      exit(-1)
    return flat_map(lambda s: [c for c in s], fp.readlines())
  def __init__(self, fonts: list, texts: list) -> None:
    all_texts = flat_map(glob.glob, texts)
    self.__characters = list(set(flat_map(lambda p: self.__read_characters(p), all_texts)))
    merger = Merger()
    self.__font = merger.merge(fonts)
  def generate(self, output: str) -> None:
    self.__font.save(output)
