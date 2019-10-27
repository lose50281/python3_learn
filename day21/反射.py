class Tech:
    def __init__(self):
        pass

    @classmethod
    def course(cls):
        print('老师选课')

    @staticmethod
    def examine():
        print('检查作业')

    @staticmethod
    def check():
        print('检查记录')


a = input('>>>')

if hasattr(Tech, a):
    getattr(Tech, a)()

elif hasattr(Tech, a):
    getattr(Tech, a)
