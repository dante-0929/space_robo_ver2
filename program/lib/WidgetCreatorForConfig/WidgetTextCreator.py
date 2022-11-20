class TextCreator:
    def __init__(self, config_ini):
        self.config_ini = config_ini

    def uppercase_before_spacer_put(self, string: str) -> str:
        if type(string) != str:
            raise TypeError()
        count = 0
        string_reply = ''
        for k, item in enumerate(string):
            if item.isupper() and 0 < count:
                string_reply = string_reply + ' ' + item
            else:
                count += 1
                string_reply = string_reply + item
        return string_reply

    def create_response_data(self):
        reply_data = {}
        for i in list(self.config_ini):
            print('[' + i + ']')
            reply_data[i] = {}
            for j, k in enumerate(list(self.config_ini[i])):
                print(j)
                reply_data[i][k] = self.uppercase_before_spacer_put(str(k))

        print(reply_data)
        return reply_data
