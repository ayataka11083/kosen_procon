import re
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

# 分割データの読み込み
q = input("ファイル名 >>")
n = int(input("重ね合わせ数 >>"))
soundQ = AudioSegment.from_file("D:\高専プロコンサンプルデータ\問題データ\sample_Q_E01\{}.wav".format(q),"wav")
#numpy配列に変換
dataQ = np.array(soundQ.get_array_of_samples())

list2 =[]
for j in range(44):
    # 読みデータの読み込み:英語
    soundE = AudioSegment.from_file("D:\高専プロコンサンプルデータ\読みデータ\E{:0>2g}.wav".format(j+1),"wav")
    #numpy配列に変換
    dataE = np.array(soundE.get_array_of_samples())
    #最も一致率の高い開始位置を探索
    list1 =[]
    for k in range(int(len(dataQ)/1000)):
        #開始位置をスライド
        dataE = np.roll(dataE,k)
        #配列同士の差の合計
        a = np.sum(np.abs(dataE[:len(dataQ):]-dataQ))
        #リストに追加
        list1.append(a)
    #最も一致率の高い開始位置の要素を配列に追加
    list2.append(min(list1))


    # 読みデータの読み込み:日本語
    soundJ = AudioSegment.from_file("D:\高専プロコンサンプルデータ\読みデータ\J{:0>2g}.wav".format(j+1),"wav")
    #numpy配列に変換
    dataJ = np.array(soundJ.get_array_of_samples())

    #最も一致率の高い開始位置を探索
    list1 =[]
    for k in range(int(len(dataQ)/1000)):
        #開始位置をスライド
        dataJ = np.roll(dataJ,k)
        #配列同士の差の合計
        a = np.sum(np.abs(dataJ[:len(dataQ):]-dataQ))
        #リストに追加
        list1.append(a)
    #最も一致率の高い開始位置の要素を配列に追加
    list2.append(min(list1))
for i in range(n):
    b = (list2.index(min(list2)))/2+1
    if b%2!=0:
        # 読みデータの読み込み:英語
        print("E{:0>2g}".format(b))
        soundE = AudioSegment.from_file("D:\高専プロコンサンプルデータ\読みデータ\E{:0>2g}.wav".format(b),"wav")
        #numpy配列に変換
        dataE = np.array(soundE.get_array_of_samples())

    else:
        print("j{:0>2g}".format(b))
        # 読みデータの読み込み:日本語
        soundE = AudioSegment.from_file("D:\高専プロコンサンプルデータ\読みデータ\J{:0>2g}.wav".format(b),"wav")
        #numpy配列に変換
        dataE = np.array(soundJ.get_array_of_samples())
    c = list2.index(min(list2))
    del list2[c]

