from bottle import run, post, response, request as bottle_request  # <--- we add bottle request
import requests

BOT_URL = 'https://api.telegram.org/bot<token>/'

def get_chat_id(data):  
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']
    return chat_id


def get_message(data):  
    """
    Method to extract message id from telegram request.
    """
    message_text = data['message']['text']
    return message_text


def change_text_message(text):  
    """
    To turn our message backwards.
    """
    return text[::-1]


def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)  # don't forget to make import requests lib


def prepare_data_for_answer(data):  
    answer = change_text_message(get_message(data))

    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }

    return json_data


@post('/')
def main():  
    data = bottle_request.json  # <--- extract all request data
    print(data)
    answer_data = prepare_data_for_answer(data)
    send_message(answer_data)  # <--- function for sending answer

    return response  # status 200 OK by default


if __name__ == '__main__':  
    run(host='localhost', port=8080, debug=True)