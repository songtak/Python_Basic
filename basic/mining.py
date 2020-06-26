from dataclasses import dataclass


@dataclass
class Model:
    def __init__(self):
        context:str
        fname:str
        target:str

    @property
    def context(self) -> str: return self._context
    @context.getter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.getter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target
    @target.getter
    def target(self, target): self._target = target


class Service:
    def __init__(self):
        pass

class Controller:
    def __init__(self):
        pass
