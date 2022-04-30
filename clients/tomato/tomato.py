from cgitb import handler
from ssl import HAS_NEVER_CHECK_COMMON_NAME
from speech import SpeechPatternRecognizer
from handler import Handler
from tomatoFx import mappings

spr = SpeechPatternRecognizer()
handler = Handler("127.0.0.1", 5050, mappings)

