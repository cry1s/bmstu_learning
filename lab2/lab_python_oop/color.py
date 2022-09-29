class Color:
    def __init__(self):
        self._color = None

    @property
    def colorproperty(self):
        # getter
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        # setter
        self._color = value