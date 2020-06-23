from contents.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 연락처 추가')
        print('2. 연락처 이름 검색')
        print('3. 연락처 전체 목록')
        print('4. 연락처 이름 삭제')
        return input('menu\n')

    app = Controller()
    while 1:
        menu = print()
        if menu =='1':
            app.register(input('이름\n'),
                         input('전화번호\n'),
                         input('이메일\n'),
                         input('주소\n'))
        if menu =='2':
            print(app.search(input('name')))
        if menu =='3':
            result = app.list()
            print('\n'.join(str(item)) for
                  item in result)
        if menu =='4':
            app.remove(input('name'))
        elif menu =='0':
            break