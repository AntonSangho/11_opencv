import tensorflow as tf

import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten, BatchNormalization

# 훈련 데이터 제너레이터

train_generator = ImageDataGenerator(

    rotation_range=10,

    zoom_range=0.2,

    horizontal_flip=True,

    rescale=1/255

)

train_dataset = train_generator.flow_from_directory(

    directory='../data/train',  # 직접 경로 사용

    target_size=(48, 48),

    class_mode='categorical',

    batch_size=16,

    shuffle=True,

    seed=10

)

# ... (모델 정의 및 훈련 코드) ...

# 모델 저장

network.save('./models/emotion_model.h5')  # 직접 경로 사용

print("모델이 저장되었습니다!")
