from typing import Sequence, Any, Union
'''module that takes a sequence and returns its first element
'''


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''function that takes a sequence and returns its first element
    '''
    if lst:
        return lst[0]
    else:
        return None
