import json, requests, html2text
from quran import QurAn

class Translations(QurAn):
  def __init__(self):
    self.translated_verse = ""
    self.translation_id = 131

  
  def all_translation_ids(self) -> json:
    """Lists all the available translation IDs (default is 131)"""

    r = requests.get("https://api.quran.com/api/v4/resources/translations")

    parsed_data = json.loads(r.json)

    translations = parsed_data["translations"]
    extracted_info = []
    for translation in translations:
      extracted_info.append({
        "id": translation["id"],
        "name": translation["name"],
        "language_name": translation["language_name"]
    })


    output_json = json.dumps(extracted_info, indent=2)

    return output_json

