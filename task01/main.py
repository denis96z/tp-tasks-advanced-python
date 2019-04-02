from orm.decorators import entity


@entity(table="table01")
class MyTable:
    id: int
    pass


def main():
    print(type(MyTable.id))
    pass


if __name__ == "__main__":
    main()
