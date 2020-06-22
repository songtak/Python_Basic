class Model:
    def __init__(self):
        self._num1 = 0      # self는 this의 의미
        self._num2 = 0      # __init__ 안에 있는 것은 필드임
        self._opcode = ''   #싱글쿼터 추천

        # 언더바 두개는 private
        # 언더바 하나는 protect
        # 여기에 은닉화 한거

        @property
        def num1(self) -> int: return self._num1
        @num1.setter
        def num1(self, num1): self._num1 = num1
        @property
        def num2(self) -> int: return self._num1
        @num2.setter
        def num2(self, num2): self._num2 = num2
        @property
        def opcode(self) -> str: return self._opcode
        @opcode.setter
        def opcode(self, opcode): self._opcode = opcode


