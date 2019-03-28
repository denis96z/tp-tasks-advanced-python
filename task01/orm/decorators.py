def entity(table: str = None):
    def _table_name(clazz):
        return clazz.__name__ if table is None else table

    def _wrapper(clazz):
        class Wrapper(clazz):
            def __init__(self):
                setattr(self, "__table", _table_name(clazz))

        return Wrapper

    return _wrapper
