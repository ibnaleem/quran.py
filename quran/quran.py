import json, requests
from typing import Any
from requests import Response

class QurAn:
    def __init__(self):
        self.__version__ = 1.0


class Chapters:
    def __init__(self):
        self.url = 'https://api.quran.com/api/v4/chapters?language=en'
        self.response = requests.get(self.url)
        self.parsed_data = self._parse_data()

    def _parse_data(self, response: Response = None) -> Any:
        """
        Helper method that parses data in JSON format

        Args:
            response (Response): The response object to parse into JSON.
        
        Returns:
            Any: the parsed response object as a JSON object. The return value is set to Any to avoid type errors.

        """

        if response is None:
            data = self.response.json()
        else:
            data = response.json()

        dumped_data = json.dumps(data)
        parsed_data = json.loads(dumped_data)

        return parsed_data

    def all_simple(self) -> list:
        """Returns a list of all chapter names in the Qur'An in simple notatiom"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                arr.append(chapter["name_simple"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_simple_order(self) -> list:
        """Returns a list of all chapter names in the Qur'An in simple notation, in order"""
        
        if self.response.status_code == 200:

            chapters = self.parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            
            arr = []
            for chapter in sorted_chapters:
                arr.append(chapter["name_simple"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_complex(self) -> list:
        """Returns a list of all chapter names in the Qur'An in complex notation"""

        if self.response.status_code == 200:
            
            arr = []
            for chapter in self.parsed_data["chapters"]:
                arr.append(chapter["name_complex"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    
    def all_complex_order(self) -> list:

        """Returns a list of all chapter names in the Qur'An, arranged in the order they were revealed, and presented in complex notation"""

        if self.response.status_code == 200:

            chapters = self.parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            arr = []
            for chapter in sorted_chapters:
                arr.append(chapter["name_complex"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_arabic(self) -> list:
        """Returns a list of all chapter names in the Qur'An written in Arabic"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                arr.append(chapter["name_arabic"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_translated_names(self) -> list:
        """Returns a list of all translated chapter names in the Qur'An"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                ch = chapter["translated_name"]
                arr.append(ch["name"])

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_mecca_simple(self) -> list:
        """Returns a list of all chapters revealed in Mecca (simple notation)"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    arr.append(chapter["name_simple"])
                else:
                    pass

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_mecca_complex(self) -> list:
        """Returns a list of all chapters revealed in Mecca (complex notation)"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    arr.append(chapter["name_complex"])
                else:
                    pass

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_madinah_simple(self) -> list:
        """Returns a list of all chapters revealed in Madinah (simple notation)"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                if chapter["revelation_place"] == "madinah":
                    arr.append(chapter["name_simple"])
                else:
                    pass

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def all_madinah_complex(self) -> list:
        """Returns a list of all chapters revealed in Madinah (complex notation)"""

        if self.response.status_code == 200:
            arr = []
            for chapter in self.parsed_data["chapters"]:
                if chapter["revelation_place"] == "madinah":
                    arr.append(chapter["name_complex"])
                else:
                    pass

            return arr

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_translated_name(self, name: str) -> str:
        """
        Returns the translated chapter name (simple or complex name) as a string

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            str: The translation of the chapter name
        """

        if type(name) is not str:
            raise TypeError("'name' must be a string")

        if self.response.status_code == 200:

            arr = []
            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] == name or chapter["name_complex"] == name:
                    ch = chapter["translated_name"]
                    arr.append(ch["name"])
                else:
                    pass

            return ''.join(arr)

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_chapter_number(self, name: str) -> int:
        """
        Returns the numerical position of a Qur'Anic chapter based on its given name. The output precisely correlates to the chapter's sequential placement within the Qur'An.

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            int: The chapter number
        """

        if type(name) is not str:
            raise TypeError("Name must be a string")

        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] == name or chapter["name_complex"] == name:
                    return int(chapter["id"])
                else:
                    pass
        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_arabic(self, name: str) -> str:
        """
        Returns the Arabic translation of a simple or complex name as a string (e.g "Al-Fatihah" returns "الفاتحة")

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            str: The chapter name in Arabic
        """

        if type(name) is not str:
            raise TypeError("Name must be a string")

        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["name_arabic"]

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_revelation_place(self, name: str) -> str:
        """
        Returns the revelation place of a simple or complex chapter name as a string (e.g "Al-Fatihah" returns "")

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            str: The revelation place of the chapter (Makkah or Madinah)
        """

        if type(name) is not str:
            raise TypeError("Name must be a string")


        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["revelation_place"]

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_revelation_order_from_name(self, name: str) -> int:

        """
        Returns the chapter's revelation order as an integer For example, "Al-Fatihah" is the first chapter in the Qur'An but it was the 5th revealed chapter, meaning it's revelation order is 5.

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            int: the chapter's revelation order
        """


        if type(name) is not str:
            raise TypeError("Name must be a string")


        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return int(chapter["revelation_order"])

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_verse_count(self, name: str) -> int:

        """
        Returns the number of verses in a given chapter in simple or complex notation.

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            int: the number of verses in the chapter
        """

        if type(name) is not str:
            raise TypeError("'Name' must be a string")

        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return int(chapter["verses_count"])

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_chapter_from_number(self, number: int) -> tuple:

        """
        Returns the simple and complex name of a chapter from its sequential number in the Qur'An, as a tuple

        Args:
            name (str): The name of the chapter in English literal; could be simple or complex (e.g "Al-Fatihah" or "Al-Fātiĥah")

        Returns:
            tuple: the simple and complex name of the chapter from its sequential number in the Qur'An
        """

        url = f"https://api.quran.com/api/v4/chapters/{number}?language=en"
        response = requests.get(url)
        parsed_data = self._parse_data(response)

        if type(number) is not int:
            raise TypeError("'number' must be an integer")
        
        if number > 114 or number < 0:
            raise ValueError("'number' must be greater than 0 and less than or equal to 114")

        if self.response.status_code == 200:
            chapter = parsed_data["chapter"]
            return chapter["name_simple"], chapter["name_complex"]

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_revelation_order_from_number(self, number: int) -> int:
        """
        Returns the revelation order of a chapter from its sequential number in the Qur'An, as an integer

        Args:
            number (int): The chapter number

        Returns:
            int: the revelation order of the chapter
        """

        if type(number) is not int:
            raise TypeError("'number' must be an integer")

        url = f'https://api.quran.com/api/v4/chapters/{number}?language=en'
        response = requests.get(url)
        parsed_data = self._parse_data(response)

        if self.response.status_code == 200:

            chapter = parsed_data["chapter"]
            return int(chapter["revelation_order"])

        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_name_from_translated_name(self, translated_name: str) -> tuple:
        
        """
        Returns the original chapter name (simple & complex name) from translated name as a tuple. For example, "The Opener" will return ('Al-Fatihah', 'Al-Fātiĥah'). You can use the method .get_translated_name(name="") to retreive the translated name of a chapter. 

        Args:
            translated_name (str): The translated chapter name

        Returns:
            tuple: the simple and complex name of the chapter
        """

        if type(translated_name) is not str:
            raise TypeError("'translated_name' must be a string")


        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                ch = chapter["translated_name"]
                if ch["name"] == translated_name:
                    return chapter["name_simple"], chapter["name_complex"]
                else:
                    pass
        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

    def get_chapter_from_revelation_order(self, revelation_order: int) -> tuple:

        """
        Returns the chapter name (simple & complex) that belongs to the given revelation order, as a tuple

        Args:
            revelation_order (int): the revelation order of the chapter

        Returns:
            tuple: the simple and complex name of the chapter
        """

        if type(revelation_order) is not int:
            raise TypeError("Order must be an integer")
        
        if revelation_order > 114:
            raise ValueError("Out of Scope Error: The Qur'An has 114 chapters, you provided an integer greater than that")
        
        elif 0 > revelation_order:
            raise ValueError("Invalid Integer: A book cannot have negative chapters, check your integer input")

        elif revelation_order == 0:
            raise ValueError("Invalid Integer: A book cannot have zero chapters, provide an integer between 1 and 114 (Chapters in the QurAn)")

        if self.response.status_code == 200:

            for chapter in self.parsed_data["chapters"]:
                if chapter["revelation_order"] == revelation_order:
                    return chapter["name_simple"], chapter["name_complex"]
                else:
                    pass
    
        else:
            print(f"The API is currently down. Response Code: {self.response.status_code}")

class Translations:
  def __init__(self):
    self.url = "https://api.quran.com/api/v4/resources/translations"
    self.response = requests.get(self.url)
    self.translation_id = 131

  
  def all_translations(self) -> list[dict]:

    """
    Returns a list of all available translations, including the trnaslation ID, the translation name (usually named after the author) and the translation language.
    
    Returns:
        list[dict]: list of dictionaries
    
    """

    parsed_data = self.response.json()
    translations = parsed_data["translations"]
    extracted_info = []
    for translation in translations:
      extracted_info.append({
        "id": translation["id"],
        "name": translation["name"],
        "language_name": translation["language_name"]
    })

    return extracted_info