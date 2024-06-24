from typing import Optional
from pydantic import BaseModel
from pysimplerepl.models.exceptions import FlagNeedsArgumentError

CONST_SHORT_IDENT = '-'
CONST_LONG_IDENT = '--'


class CommandFlag(BaseModel):
    short_name: Optional[str] = None
    long_name: Optional[str] = None
    argument_required: bool = False
    argument_optional: bool = False
    argument: Optional[str] = None
    flagged: bool = False

    @staticmethod
    def _is_short(flag_str: str) -> bool:
        if flag_str.startswith(CONST_SHORT_IDENT) and not flag_str.startswith(CONST_LONG_IDENT):
            return True
        return False

    @staticmethod
    def _is_long(flag_str: str) -> bool:
        if flag_str.startswith(CONST_LONG_IDENT):
            return True
        return False
    
    @staticmethod
    def _split_long(flag_str: str) -> tuple[str, Optional[str]]:
        argument = None
        if '=' in flag_str:
            flag, argument = flag_str.split('=', 1)
            flag = flag.lstrip(CONST_LONG_IDENT)
        else:
            flag = flag_str
            flag = flag.lstrip(CONST_LONG_IDENT)
        return flag, argument
    
    @staticmethod
    def _match_name(flag: str, flag_expected: Optional[str]) -> bool:
        if flag_expected is None:
            return False
        if flag_expected in flag and flag in flag_expected:
            return True
        return False
    
    @classmethod
    def _parse(cls, flag_str: str, next_token: Optional[str] = None) -> tuple[Optional[str], Optional[str]]:
        if cls._is_long(flag_str) is True:
            flag, argument = cls._split_long(flag_str=flag_str)
        elif cls._is_short(flag_str=flag_str) is True:
            flag = flag_str.lstrip(CONST_SHORT_IDENT)
            argument = next_token
        else:
            return None, None
        return flag, argument

    def process(self, flag_str: str, next_token: Optional[str] = None) -> None:
        flag, argument = self._parse(flag_str=flag_str, next_token=next_token)
        if flag is None:
            return None
        if self._match_name(flag, self.short_name) is True or self._match_name(flag, self.long_name) is True:
            if self.argument_required is True and argument is None:
                raise FlagNeedsArgumentError(self.long_name)
            elif self.argument_required is True or self.argument_optional is True:
                self.argument=argument
            self.flagged = True

                
            
        
        