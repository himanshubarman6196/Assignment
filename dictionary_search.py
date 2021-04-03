import requests
import json
import logging

logging.basicConfig(level = logging.INFO)


class Search:
    """ global variable for base url for api """
    base_url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/'

    def __init__(self,word):
        self.word = word


    def search_meaning(self):
        try:
            search_word_url = f'{self.base_url}{self.word}'
            """ sending get request to the api endpoint """
            response = requests.request("GET", search_word_url)
            """ if status code is 200 the output will be found """
            if response.status_code == 200:
                """ convert json string to python object by json.loads() """
                a = json.loads(response.text)
                for word in a:
                    for partofspeech in word['meanings']:
                        for defination in partofspeech['definitions']:
                            logging.info(f"{word.get('word')}, {partofspeech.get('partOfSpeech')} ,{defination.get('definition')}")
            """ if status code is 500 interal server error 
            if status code is 404 endpoint is not found
            if status code is 400 then Bad request
             """
            if requests.status_code == 400 or 404 or 500:
                logging.warning(f"issue could not fetch data from api")
        except Exception as e:
            return e
        return True



if __name__ == '__main__':
    search_keyword = input("Please enter the keyword - >")
    if search_keyword:
        search_obj = Search(search_keyword).search_meaning()
    else:
        logging.warning(f"Search field is required")
    