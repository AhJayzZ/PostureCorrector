![H1K7_ThQC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/f0c11f0e-fb62-43f0-be46-0578af54eba5)# 坐姿矯正辨識系統 (PostureCorrector)

## 介紹 Introduction
日常生活中，因需要長時間久坐於電腦前，而又沒有注意到坐姿不正的問題，時間久了會導致肌肉神經壓迫，引發如脊椎側彎與骨盆前傾等問題。於是希望透過本專題可以幫助辨識使用者目前的坐姿，並即時提出矯正建議。


---
## 研究目的 Purpose
透過嵌入式系統的監測姿勢提醒，**解決現代人久坐，姿勢不良導致頸椎僵直、脊椎側彎...等一系列腰椎疾病的問題**
![S140hh3QR](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/1b090c96-a566-40c9-8c21-bb434802394d)

---
## 使用流程 Usage
- Step 0. 啟動坐姿辨識系統
- Step 1. 開始坐姿辨識
- Step 2. 坐姿不良提醒
![rkC532nXA](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/5c36f6d2-238e-40f0-88a8-b3d6f4ebefbd)

---
## 展示影片 Demo
https://github.com/AhJayzZ/PostureCorrector/assets/61458156/178440bc-e4c6-4d47-99b8-6b7ddda5e235

---
## 實現 Implement

- ### Part 1.資料集 Dataset
    - #### 1.資料蒐集 Data Collection
        - 1.使用手機拍攝1500張、開發版(WEI)版拍攝150張圖片
        - 2.透過自製Python資料分類程式加快蒐集資料集的蒐集與分類
          ![rJZUR3h7R](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/42e80a4b-8400-45ed-86b9-15e59ea9aa7d)

    - #### 2.資料前處理 Data Preprocessing
        為了控制輸出模型大小與開發版規格，將圖片灰階化與縮放圖片尺寸至96x96來進行資料集的前處理
      ![SyPsanh7A](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/55e2bb7b-f54a-42ef-b28c-e201820b6e63)     
        - 圖像灰階化(Gray Scale)
            ![H1K7_ThQC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/889e6cf9-0123-4f6a-ae88-5cd3c3c83c0b)

        - 圖像縮小取樣(Down sample)   
            ![S1tgu627C](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/f83eaca4-0d9c-40fd-be86-27a0915fbae5)

- ### Part 2.模型訓練 Model Training
    - #### 架構 Architeture
        採用CNN模型神經網路架構結合Max Pooling層壓縮特徵，而後將模型張量(tensor)進行展平(Flatten)送至稠密層(Dense)進行特徵融合，最後透過Adaptive Moment Estimation(Adam)優化器對模型訓練進行優化。
        ![r1Hm16hQA](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/dd40c764-6c68-44fd-bb04-06788ace9011)

    - #### 準確率 Accuracy
        在```epoch=10```與```batch_size=5```的情況下，模型最終準確率```accuracy=0.9906```(99.06%)與驗證準確率```val_accuracy=0.9592```(95.92%)
        ![BkIX-p3m0](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/c5d4075f-17c2-47aa-833f-8b4300e50bd5)

    - #### 混淆矩陣 Confusion Matrices
        ![Hk6lNp2mC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/56b32ae8-16ec-41e7-8763-85d59d0ed401)

- ### Part 3.模型轉換 Model Conversion
    - #### Step 1.TFLiteConverter轉換keras_model 成 tfilite 模型
        ![ry8HSpnm0](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/c83c263b-6afa-41bf-b087-e6114aaf14c4)

    - #### Step 2.生成tflite模型
        ![HJBLrp2mR](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/51528bab-489a-430c-95bb-8b890dc07453)

- ### Part 4.載入模型 Load Model
    - #### Step 1.利用xxd將.tflite 轉換成 model.h
        ( xxd : 將文件以16進制的方式轉換出來 )
        ![SkuO8p3X0](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/370e1b56-38f8-42a0-9998-320ba65e82eb)

    - #### Step 2.生成tflite模型
        ![HJBLrp2mR](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/6b239853-0825-4a96-acbf-4b0098f2fe09)

- ### Part 5.更新模型 Reload Model
    ![SkKtPT2QC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/1eb707f1-9610-4316-b55b-221c9e40e9a9)

---
## 開發環境 Enviroment
- ### 開發環境 Enviroment
    - 開發版: Synopsis ARC EM9D RA6000 EVK
    
- ### 執行環境 Runtime
    - 語言: Python 3.7.8
    - 包管理工具: pip 21.1.2
    
---
## 結果 Result
![HJcyPThX0](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/2d66724f-a941-414e-ac7e-9c10766d5332)

![ryMZD6nXA](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/bb4e6e75-d824-4cf7-a7a6-b88d4f9cf95f)

![HkrfDT370](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/bc099781-5cad-45f6-b364-62bd98eafa0e)

---
## 其餘 Others
![HyhDFp2QA](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/132f0730-fa08-4340-8b6a-ffec1a6566c8)

![BJVSDp3QC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/6c5d0e8a-d24f-452d-942a-69414973c13e)

![BJVSDp3QC](https://github.com/AhJayzZ/PostureCorrector/assets/61458156/130765da-cfb6-464e-8f23-d1765c0e1ba6)
