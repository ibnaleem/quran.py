import requests
import json
import html2text
import string

class Chapters:
    def __init__(self):
        self.__version__ = 1.0
        self.all_simples = []
        self.all_simples_order = []
        self.all_complex = []
        self.all_complex_order = []
        self.arabic_name = []
        self.translated_name = []
        self.mecca_simples = []
        self.mecca_complex = []


    def all_simple(self):
        """Returns a list of all chapter names in the Qur'An in simple notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.name_simples.append(chapter["name_simple"])

            return self.name_simples

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_simple_order(self):

        """Returns a list of all chapter names in the Qur'An in simple notation, in order"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            chapters = parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            for chapter in sorted_chapters:
                self.all_simples_order.append(chapter["name_simple"])

            return self.all_simples_order

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_complex(self):
        """Returns a list of all chapter names in the Qur'An in complex notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.all_complex.append(chapter["name_complex"])

            return self.all_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    
    def all_complex_order(self):

        """Returns a list of all chapter names in the Qur'An, arranged in the order they were revealed, and presented in complex notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            chapters = parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            for chapter in sorted_chapters:
                self.all_complex_order.append(chapter["name_complex"])

            return self.all_complex_order

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_arabic(self):
        """Returns a list of all chapter names in the Qur'An written in Arabic"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.arabic_name.append(chapter["name_arabic"])

            return self.arabic_name

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_translated_names(self):
        """Returns a list of all translated chapter names in the Qur'An"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                ch = chapter["translated_name"]
                self.translated_name.append(ch["name"])

            return self.translated_name

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_mecca_simple(self):
        """Returns a list of all chapters revealed in Mecca (simple notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    self.mecca_simples.append(chapter["name_simple"])
                else:
                    pass

            return self.mecca_simples

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_mecca_complex(self):
        """Returns a list of all chapters revealed in Mecca (complex notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    self.mecca_complex.append(chapter["name_complex"])
                else:
                    pass

            return self.mecca_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")
