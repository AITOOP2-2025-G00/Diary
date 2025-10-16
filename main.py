from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.Nagata2D import Nagata2D

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NagataniDiary(),
    Nagata2D(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()