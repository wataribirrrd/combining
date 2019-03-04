def main():
    mail_head = 'こんばんは\n'\
                'はじめまして\n'\
                'はろう\n'
    mail_body = {
        "id":"1",
        "first_name":"Steven",
        "last_name":"Thompson",
        "email":"shopsn0@aaaa.com",
        "gender":"Male",
        "ip_address":"127.11.11.1"
    }

    mail_foot = '以上になります\n'\
                'どうぞよろしくお願いいたします\n'

    mail_full = mail_head \
                + mail_body['first_name']\
                + "\n"\
                + mail_body['gender']\
                + "\n"\
                + mail_foot

    print(mail_full)

if __name__ == "__main__":
    main()