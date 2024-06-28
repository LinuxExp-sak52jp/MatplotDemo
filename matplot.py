import pandas as pd
import matplotlib.pyplot as plt

# CSVデータを読み込む
csv_data = """
Time,Signal1,Signal2,Signal3
0,0,1,0
1,1,1,0
2,1,0,0
3,0,0,1
4,0,1,1
5,1,1,1
"""

# pandasのDataFrameに変換
from io import StringIO
data = pd.read_csv(StringIO(csv_data))

# タイミングチャートを描画
plt.figure(figsize=(10, 6))

signals = data.columns[1:]  # 'Time'列を除いた信号の列名を取得

for i, signal in enumerate(signals):
    plt.step(data['Time'], data[signal] + i * 2, where='post', label=signal)

# グラフのタイトルとラベルを設定
plt.title('Timing Chart')
plt.xlabel('Time')
plt.yticks([i * 2 for i in range(len(signals))], signals)
plt.ylabel('Signal State')
plt.grid(True)
plt.legend(loc='upper right')

# グラフを表示
plt.show()
