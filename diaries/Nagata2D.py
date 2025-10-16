from diaries.AbstractDiary import AbstractDiary

class Nagata2D(AbstractDiary):

    def get_date(self):
        return "2029-12-31"

    def get_summary(self):
        return "未来の大晦日"

    def get_author(self):
        return "Nagata2"