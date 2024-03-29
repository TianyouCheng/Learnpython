import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

imdb=keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# 将整数转换回单词
# 一个映射单词到整数索引的词典
word_index=imdb.get_word_index()

# 保留第一个索引
word_index={k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

train_data=keras.preprocessing.sequence.pad_sequences(train_data,
                                                    value=word_index["<PAD>"],
                                                    padding='post',
                                                    maxlen=256)
test_data=keras.preprocessing.sequence.pad_sequences(test_data,
                                                    value=word_index["<PAD>"],
                                                    padding='post',
                                                    maxlen=256)

# 构建模型
vocab_size=10000

model=keras.Sequential()
model.add(keras.layers.Embedding(vocab_size,16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16,activation='relu'))
model.add(keras.layers.Dense(1,activation='sigmoid'))

model.summary()

# 损失函数与优化器
model.compile(optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy'])

# 创建一个验证集
x_val=train_data[:10000]
partial_x_train=train_data[10000:]
y_val=train_labels[:10000]
partial_y_train=train_labels[10000:]

# 训练模型
history=model.fit(partial_x_train,
                partial_y_train,
                epochs=40,
                batch_size=512,
                validation_data=(x_val,y_val),
                verbose=1)

# 评估模型
results=model.evaluate(test_data,test_labels,verbose=2)

# 图表跟踪
history_dict=history.history

acc=history_dict['accuracy']
val_acc=history_dict['val_accuracy']
loss=history_dict['loss']
val_loss=history_dict['val_loss']

epochs=range(1,len(acc)+1)

plt.plot(epochs,loss,'bo',label='Training loss')

plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()