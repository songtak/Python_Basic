import pandas as pd


class Entity:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self.id

    @id.setter
    def id(self, id): self.id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label


# context (str), fname(str), train(object), test(object), label(str)

"""

"""


class Service:
    def __init__(self):
        self.entity = Entity()  # 자바의 @Autowired Entity entity와 비슷함!

    def new_model(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):  # entity(속성) + service(기능) = 모델 생성
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)
        print(f'트레인의 컴럼: {this.train.columns}')


def print_menu():
    print('0. exit')
    print('1.')
    return input('메뉴선택\n')


app = Controller()
while 1:
    menu = print_menu()
    if menu == '0':
        break;
    if menu == '1':
        app.preprocess('train.csv', 'test.csv')
        break;
