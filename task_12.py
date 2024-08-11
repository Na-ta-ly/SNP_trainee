from typing import Optional
from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: Optional[str] = None,
                 calories: Optional[int] = 0,
                 flavor: Optional[str] = None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self) -> str:
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor: str) -> None:
        self.__flavor = str(flavor)

    def is_delicious(self) -> bool:
        if self.flavor == 'black licorice':
            return True
        return False
