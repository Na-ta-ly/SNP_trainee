from typing import Optional


class Dessert:
    def __init__(self, name: Optional[str] = None, calories: Optional[int | float] = 0):
        self.name = name
        self.calories = calories

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = str(name)

    @property
    def calories(self) -> int:
        return self.__calories

    @calories.setter
    def calories(self, calories: int) -> None:
        if isinstance(calories, (int, float)):
            self.__calories = calories
        else:
            self.__calories = 0
            print('calories should be int or float, so it was set to 0')

    def is_healthy(self) -> bool:
        if self.__calories < 200:
            return True
        return False

    @staticmethod
    def is_delicious() -> bool:
        return True
