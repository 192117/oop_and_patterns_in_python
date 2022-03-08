E_INT, E_FLOAT, E_STR = "INT", "FLOAT", "STR"

class EventGet:

    def __init__(self, value):
        self.kind = {int:E_INT, float:E_FLOAT, str:E_STR}[value]
        self.value = None


class EventSet:

    def __init__(self, value):
        self.kind = {int:E_INT, float:E_FLOAT, str:E_STR}[type(value)]
        self.value = value


class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):

    def handle(self, obj, event):
        if event.kind == E_INT:
            if event.value is None:
                return obj.integer_field
            else:
                obj.integer_field = event.value
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):

    def handle(self, obj, event):
        if event.kind == E_FLOAT:
            if event.value is None:
                return obj.float_field
            else:
                obj.float_field = event.value
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):

    def handle(self, obj, event):
        if event.kind == E_STR:
            if event.value is None:
                return obj.string_field
            else:
                obj.string_field = event.value
        else:
            return super().handle(obj, event)