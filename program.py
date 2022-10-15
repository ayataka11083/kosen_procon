import re
from pydub import AudioSegment
import numpy as np

# 分割データの読み込み
q = input("ファイル名 >>")
n = int(input("重ね合わせ数 >>"))
rate = 100
soundQ = AudioSegment.from_file("C:\高専プロコンサンプルデータ\問題データ\Q\{}.wav".format(q),"wav")
#numpy配列に変換
dataQ = np.array(soundQ.get_array_of_samples())

#読み札リスト
list3 = ["あe","あj","いe","いj","うe","うj","えe","えj","おe","おj","かe","かj","きe","きj","くe","くj","けe","けj","こe","こj","さe","さj","しe","しj","すe","すj","せe","せj","そe","そj","たe","たj","ちe","ちj","つe","つj","てe","てj","とe","とj","なe","なj","にe","にj","ぬe","ぬj","ねe","ねj","のe","のj","はe","はj","ひe","ひj","ふe","ふj","へe","へj","ほe","ほj","まe","まj","みe","みj","むe","むj","めe","めj","もe","もj","やe","やj","ゆe","ゆj","よe","よj","らe","らj","りe","りj","るe","るj","れe","れj","ろe","ろj","わe","わj"]

#除外リスト
listdel =[]
for i in range(n):
    list2 =[]
    for j in range(44):
        # 読みデータの読み込み:英語
        soundE = AudioSegment.from_file("C:\高専プロコンサンプルデータ\読みデータ\E{:0>2g}.wav".format(j+1),"wav")
        #numpy配列に変換
        dataE = np.array(soundE.get_array_of_samples())
        #既出のデータを除外
        for p in range(i):
            if (j == listdel[p])&(i>0):
                dataE = dataE+np.full(len(dataE),10000)
        #最も一致率の高い開始位置を探索
        list1 =[]
        for k in range(int(len(dataQ)/rate)):
            if len(dataQ)*2 > len(dataE):
                dataE = np.append(dataE,dataQ[len(dataQ)*2-len(dataE):len(dataQ):])
            #配列同士の差の合計
            a = np.sum(np.abs(dataQ[::rate]-dataE[k*rate:len(dataQ)+k*rate:rate]))    
            #リストに追加
            list1.append(a)
        #最も一致率の高い開始位置の要素を配列に追加
        list2.append(min(list1))

        # 読みデータの読み込み:日本語
        soundJ = AudioSegment.from_file("C:\高専プロコンサンプルデータ\読みデータ\J{:0>2g}.wav".format(j+1),"wav")
        #numpy配列に変換
        dataJ = np.array(soundJ.get_array_of_samples())
        #既出のデータを除外
        for p in range(i):
            if (j == listdel[p])&(i>0):
                dataJ = dataJ+np.full(len(dataJ),10000)
        #最も一致率の高い開始位置を探索
        list1 =[]
        for k in range(int(len(dataQ)/rate)):
            if len(dataQ)*2 > len(dataE):
                dataJ = np.append(dataJ,dataQ[len(dataQ)*2-len(dataJ):len(dataQ):])
            #配列同士の差の合計
            a = np.sum(np.abs(dataQ[::rate]-dataJ[k*rate:len(dataQ)+k*rate:rate]))
            #リストに追加
            list1.append(a)
        #最も一致率の高い開始位置の要素を配列に追加
        list2.append(min(list1))

    b=list2.index(min(list2))
    print(list3[b])

    if b%2 == 0:
        # 読みデータの読み込み:英語
        soundE = AudioSegment.from_file("C:\高専プロコンサンプルデータ\読みデータ\E{:0>2g}.wav".format(b/2+1),"wav")
        #numpy配列に変換
        dataE = np.array(soundE.get_array_of_samples())
        #最も一致率の高い開始位置を探索
        list1 =[]
        for k in range(int(len(dataQ)/rate)):
            if len(dataQ)*2 > len(dataE):
                dataE = np.append(dataE,dataQ[len(dataQ)*2-len(dataE):len(dataQ):])
            #配列同士の差の合計を要素ごとにスライドして求める
            a = np.sum(np.abs(dataQ[::rate]-dataE[k*rate:len(dataQ)+k*rate:rate]))
            #リストに追加
            list1.append(a)
        c = list1.index(min(list1))
        #合成
        dataQ = dataQ[::]-dataE[c:len(dataQ)+c:]
        #削除リストにインデックスを追加
        listdel.append(b/2)
    else:
         # 読みデータの読み込み:日本語
        soundJ = AudioSegment.from_file("C:\高専プロコンサンプルデータ\読みデータ\J{:0>2g}.wav".format((b+1)/2),"wav")
        #numpy配列に変換
        dataJ = np.array(soundJ.get_array_of_samples())
        #最も一致率の高い開始位置を探索
        list1 =[]
        for k in range(int(len(dataQ)/rate)):
            if len(dataQ)*2 > len(dataE):
                dataJ = np.append(dataJ,dataQ[len(dataQ)*2-len(dataJ):len(dataQ):])
            #配列同士の差の合計を要素ごとにスライドして求める
            a = np.sum(np.abs(dataQ[::rate]-dataJ[k*rate:len(dataQ)+k*rate:rate]))
            #リストに追加
            list1.append(a)
        c = list1.index(min(list1))
        #合成
        dataQ = dataQ[::]-dataJ[c:len(dataQ)+c:]
        #削除リストにインデックスを追加
        listdel.append((b+1)/2-1)




