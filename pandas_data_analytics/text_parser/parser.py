import re
from py_linq import Enumerable

def str_flags_to_regex_flags(str_flags):
    flag_map = {
        "i": re.IGNORECASE,
        "x": re.VERBOSE,
        "m": re.MULTILINE,
        "s": re.DOTALL,
        "u": re.UNICODE,
        "l": re.LOCALE,
        "d": re.DEBUG,
        "a": re.ASCII,
        "t": re.TEMPLATE
    }
    def r(acc, ele):
        acc = acc | ele
        return acc
    return Enumerable(str_flags)\
      .select(lambda f: flag_map[f])\
      .aggregate(r)

class Parser(object):

  def __init__(self, settings):
    self.settings = settings
    
  def get_match_string(self, match, ordered_groups, group_join_symbol):
    m = re.sub('.*?Patient #: (\d+) Capture:.*', '\\1', '  Patient #: 234234 Capture:23 ')
    return group_join_symbol.join(Enumerable(ordered_groups).select(lambda g: match.groups[g].value.trim()))

  def parse(self, txt):
    result_dict = {}
    s = self.settings
    for v in s['fields']:
      list_of_replace_strings = Enumerable(v.get('ordered_groups',[1]))\
        .select(lambda ele: '\\' + str(ele)).to_list()
      result_dict[v['name']] = re.sub(v['pattern'], v.get('group_join_symbol','').join(list_of_replace_strings)\
          ,txt, flags=str_flags_to_regex_flags(v['flags']))
    return result_dict
