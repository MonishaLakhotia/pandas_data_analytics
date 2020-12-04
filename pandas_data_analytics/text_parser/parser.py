import re
from py_linq import Enumerable

class Parser(object):

  def __init__(self, settings):
    self.settings = settings
    
  def get_match_string(self, match, ordered_groups, group_join_symbol):
    return group_join_symbol.join(Enumerable(ordered_groups).select(lambda g: match.groups[g].value.trim()))

  def parse(self, txt):
    result_dict = {}
    s = self.settings
    for name,v in s.items():
      result_dict[name] = self.get_match_string(re.match(v.patten, txt, flags=v.flags))
    return result_dict
