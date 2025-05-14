import pytesseract
from PIL import Image
import io
import re

def parse_image_ocr(image_file):
    image = Image.open(image_file.stream)
    text = pytesseract.image_to_string(image)

    # Very basic regex parsing of typical poker hand lines
    players = re.findall(r'Player\s\d+:\s(.*?)\s(.*?) chips', text)
    actions = re.findall(r'(Player\s\d+)\s(actions|bets|calls|raises|folds).*', text)
    pot_match = re.search(r'Pot:\s*(\d+)', text)

    return {
        "raw_text": text,
        "players": players,
        "actions": actions,
        "pot": int(pot_match.group(1)) if pot_match else 0
    }