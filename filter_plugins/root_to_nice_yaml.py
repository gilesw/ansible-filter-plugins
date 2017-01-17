import yaml
import pprint
from ansible.utils.unicode import unicode_wrap, to_unicode

def root_to_nice_yaml(*a, **kw):
    '''Output a specific ansible hash indented by the hash name {{ hashname | root_to_nice_yaml( root=\'hashname\' ) }}'''
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(kw)
    #pp.pprint(a)

    # pop our custom arg off so we don't pass it into yaml.safe_dump
    root = kw.get('root',"hash")
    kw.pop("root", None)

    # add our new custom root to the data structure that was passed in
    custom_dict={ root: a[0] }

    transformed = yaml.safe_dump(custom_dict, indent=2, allow_unicode=True, default_flow_style=False, width=400, **kw)
    return to_unicode(transformed)


class FilterModule(object):
    def filters(self):
      return {'root_to_nice_yaml': root_to_nice_yaml}
