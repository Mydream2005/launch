import json


class jsonIO:

    def __init__(self):
        self.is_data = False
        self.data = []

    def jsoninput(self, filename) -> list:
        try:
            with open(filename, "r", encoding="utf8") as f:
                self.data = json.load(f)
                self.is_data = True
        except Exception as e:
            print(e)
            self.is_data = False
            self.data = []
        return self.data

    def jsonoutput(self, filename, data):
        if not data in self.data:
            self.data.append(data)
        else:
            print('重复数据：', data)
        f = open(filename, "w", encoding="utf-8")
        json.dump(self.data, f, indent=4)
        f.close()

    def json_delete(self, filename, data):
        print(data)
        if not data in self.data:
            print("要删除的数据不存在")
            return
        self.data.remove(data)
        print(self.data)
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)


def main():
    filename = r'D:\ProgrameData\ProjectCode\PyQT5\test0324.json'
    data = {
        'name': 'Ms.Wang',
        'id': '10003'
    }

    IO = jsonIO()
    print(IO.jsoninput(filename))

    IO.jsonoutput(filename, data)
    print(IO.data)

    IO.json_delete(filename, data)
    print(IO.data)


if __name__ == '__main__':
    main()
