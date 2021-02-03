import re
from typing import Optional, Union, Dict

from telegram import Message
from telegram.ext.filters import MessageFilter


class StandupFilter(MessageFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pattern = re.compile(r".*(стенд[ау]+п).*", re.DOTALL)

    def filter(self, message: Message) -> Optional[Union[bool, Dict]]:
        text = message.text.lower()
        return bool(re.match(self.pattern, text))
