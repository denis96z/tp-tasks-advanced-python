from orm.decorators import entity


@entity(table="table01")
class MyTable:
    pass


def main():
    print(MyTable().__table)
    pass


if __name__ == "__main__":
    main()
