import sys
import config
from combiner import Combiner

class Option:
  config_path = ""
  # * true: success
  def __parse(self) -> bool:
    if len(sys.argv) < 2:
      return False
    self.config_path = sys.argv[1]
    return True
  def __help(self) -> None:
    print("Usage: python font15.py path/to/15config.json")
  def __init__(self) -> None:
    if not self.__parse():
      self.__help()
      exit(-1)

def __main__():
  option = Option()
  cfg = config.Config(option.config_path)
  combinator = Combiner(cfg.get_fonts(), cfg.get_texts())
  combinator.generate(cfg.get_output())

__main__()
