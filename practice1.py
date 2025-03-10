#youtubeのpython超入門コース（pythonの復讐）
#python3 practice1.pyで実行

#文字表示
print("good morning")

#変数
#変数には""いらない
#変数名は数字から始められない、_以外の記号を使うことができない
num = 1
print(num)

#データ型...pthonは自動でデータ型が分類される（動的）
int01 = 1
string01 = "hello"
print(type(int01))
print(type(string01))

a = 1
b = 2
bool01 = (a < b)
print(type(bool01))

#リスト
a = [["sato","suzuki"],"takahashi"]
a[1] = "tanaka"
print(a[0][0])
print(a[0])
print(a[1])

#演算子
x = 10
y = 2
z = 10
n = 15
print(x / y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)
print(x <= 5 and x <= 12)
print(y == 2 or z == 2)

n += 10
print(n)

#条件分岐(インデントをずらすことに注意)
age = 18
if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")

for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    print(i)

#for文のネスト
for m in range(3):
    for j in range(3):
        print(i, j, sep="-")

arr = [2,4,6,8,10]
sum = 0
for i in arr:
    sum += i
print(sum)

#関数
#引数のみ

#関数を定義する
def say_hello1():
    print("hello world")
#関数を呼び出す
say_hello1()

#引数あり
def say_hello2(greeting):
    print(greeting)
#greetingという引数に"hello world"を渡す
say_hello2("hello world")

#関数の代入
hello = say_hello2
hello("goodmornig")

#引数を二つ作ってみる
def add(num01,num02):
    print(num01 + num02)
add(6,2)

#関数の結果はreturnで返すことができる
def add(num01,num02):
    return(num01 + num02)
print(add(7,3))

#演習問題
def average(av01,av02,av03):
    return((av01 + av02 + av03)/3)
print(average(9,4,2))

#クラス
#アトリビュート...クラス内で定義された変数
#メソッド...クラス内で定義された関数(引数に必ずselfと記述することが必要)
#以下演習問題で同一のクラスが出てくるためコメントアウト
'''
class Student:
    #初期化メソッド
    def __init__(self,name):
        self.name = name

    def avg(self,math,english):
        print((math + english)/2)
#インスタンス化
#インスタンス... クラスから作られた具体的なオブジェクト(データ（属性）とそのデータに対する処理（メソッド）をひとまとめにしたもの)
a001 = Student("sato")
a001.avg(80,70)

#アトリビュートを表示
print(a001.name)

a002 = Student("tanaka")
print(a002.name)
'''

#演習問題
class Student:
    def __init__(self,name):
        self.name = name

    def caluculate_avg(self,date):
        sum = 0

        for num in date:
            sum += num
        
        avg = sum/len(date)
        return avg
    
    def judge(self,avg):
        if (avg >= 60):
            result="passed"
        else:
            result="failed"
        return result
    
a001 = Student("sato")
date = [70,65,50,90,30]
avg = a001.caluculate_avg(date)
result = a001.judge(avg)

print(avg)
print(a001.name+" "+result)
