# OpenCV 프로젝트 구조

```
11_opencv/
│
├── data/
│   ├── images/
│   │   └── charles.jpg
│   ├── weights/
│   │   └── mmod_human_face_detector.dat
│   ├── train/
│   │   ├── angry/
│   │   ├── happy/
│   │   └── ...
│   └── test/
│       ├── angry/
│       ├── happy/
│       └── ...
│
├── models/
│   └── emotion_model.h5
│
├── src/
│   ├── predict_emotion.py
│   ├── validation_emotion_HOG.py
│   └── validation_emotion.py
│
└── requirements.txt
```

## 디렉토리 설명

- **`data/`**: 데이터 파일들을 저장하는 디렉토리
  - **`images/`**: 테스트용 이미지 파일들
  - **`weights/`**: 사전 훈련된 모델 가중치 파일들
  - **`train/`**: 훈련용 감정 데이터셋 (클래스별 폴더)
  - **`test/`**: 테스트용 감정 데이터셋 (클래스별 폴더)

- **`models/`**: 훈련된 감정 분류 모델 저장

- **`src/`**: 소스 코드 파일들
  - **`predict_emotion.py`**: 감정 예측 메인 스크립트
  - **`validation_emotion_HOG.py`**: HOG 기반 검증 스크립트
  - **`validation_emotion.py`**: CNN 기반 검증 스크립트

- **`requirements.txt`**: 프로젝트 의존성 패키지 목록

## data set site
[FER-2013](https://www.kaggle.com/datasets/msambare/fer2013?select=test) 

