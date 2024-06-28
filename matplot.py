import pandas as pd
import matplotlib.pyplot as plt

# CSV�f�[�^��ǂݍ���
csv_data = """
Time,Signal1,Signal2,Signal3
0,0,1,0
1,1,1,0
2,1,0,0
3,0,0,1
4,0,1,1
5,1,1,1
"""

# pandas��DataFrame�ɕϊ�
from io import StringIO
data = pd.read_csv(StringIO(csv_data))

# �^�C�~���O�`���[�g��`��
plt.figure(figsize=(10, 6))

signals = data.columns[1:]  # 'Time'����������M���̗񖼂��擾

for i, signal in enumerate(signals):
    plt.step(data['Time'], data[signal] + i * 2, where='post', label=signal)

# �O���t�̃^�C�g���ƃ��x����ݒ�
plt.title('Timing Chart')
plt.xlabel('Time')
plt.yticks([i * 2 for i in range(len(signals))], signals)
plt.ylabel('Signal State')
plt.grid(True)
plt.legend(loc='upper right')

# �O���t��\��
plt.show()
