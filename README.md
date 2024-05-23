# 坐姿矯正辨識系統 (PostureCorrector)

## 介紹 Introduction
日常生活中，因需要長時間久坐於電腦前，而又沒有注意到坐姿不正的問題，時間久了會導致肌肉神經壓迫，引發如脊椎側彎與骨盆前傾等問題。於是希望透過本專題可以幫助辨識使用者目前的坐姿，並即時提出矯正建議。


---
## 研究目的 Purpose
透過嵌入式系統的監測姿勢提醒，**解決現代人久坐，姿勢不良導致頸椎僵直、脊椎側彎...等一系列腰椎疾病的問題**
![image](https://hackmd.io/_uploads/S140hh3QR.png)
    

---
## 使用流程 Usage
- Step 0. 啟動坐姿辨識系統
- Step 1. 開始坐姿辨識
- Step 2. 坐姿不良提醒
![image](https://hackmd.io/_uploads/rkC532nXA.png)

---
## 展示影片 Demo
https://github.com/AhJayzZ/PostureCorrector/assets/61458156/178440bc-e4c6-4d47-99b8-6b7ddda5e235

---
## 實現 Implement

- ### Part 1.資料集 Dataset
    - #### 1.資料蒐集 Data Collection
        - 1.使用手機拍攝1500張、開發版(WEI)版拍攝150張圖片
        - 2.透過自製Python資料分類程式加快蒐集資料集的蒐集與分類
        ![image](https://hackmd.io/_uploads/rJZUR3h7R.png)

    - #### 2.資料前處理 Data Preprocessing
        為了控制輸出模型大小與開發版規格，將圖片灰階化與縮放圖片尺寸至96x96來進行資料集的前處理
    ![image](https://hackmd.io/_uploads/SyPsanh7A.png)
        - 圖像灰階化(Gray Scale)
            ![image](https://hackmd.io/_uploads/H1K7_ThQC.png)
        - 圖像縮小取樣(Down sample)   
            ![image](https://hackmd.io/_uploads/S1tgu627C.png)


- ### Part 2.模型訓練 Model Training
    - #### 架構 Architeture
        採用CNN模型神經網路架構結合Max Pooling層壓縮特徵，而後將模型張量(tensor)進行展平(Flatten)送至稠密層(Dense)進行特徵融合，最後透過Adaptive Moment Estimation(Adam)優化器對模型訓練進行優化。
        ![image](https://hackmd.io/_uploads/r1Hm16hQA.png)

    - #### 準確率 Accuracy
        在```epoch=10```與```batch_size=5```的情況下，模型最終準確率```accuracy=0.9906```(99.06%)與驗證準確率```val_accuracy=0.9592```(95.92%)
        ![image](https://hackmd.io/_uploads/BkIX-p3m0.png)
        
    - #### 混淆矩陣 Confusion Matrices
        ![image](https://hackmd.io/_uploads/Hk6lNp2mC.png)

- ### Part 3.模型轉換 Model Conversion
    - #### Step 1.TFLiteConverter轉換keras_model 成 tfilite 模型
        ![image](https://hackmd.io/_uploads/ry8HSpnm0.png)

    - #### Step 2.生成tflite模型
        ![image](https://hackmd.io/_uploads/HJBLrp2mR.png)

- ### Part 4.載入模型 Load Model
    - #### Step 1.利用xxd將.tflite 轉換成 model.h
        ( xxd : 將文件以16進制的方式轉換出來 )
        ![image](https://hackmd.io/_uploads/SkuO8p3X0.png)


    - #### Step 2.生成tflite模型
        ![image](https://hackmd.io/_uploads/HJBLrp2mR.png)

- ### Part 5.更新模型 Reload Model
    ![image](https://hackmd.io/_uploads/SkKtPT2QC.png)


---
## 開發環境 Enviroment
- ### 開發環境 Enviroment
    - 開發版: Synopsis EVL
    - 開發環境: Linux Ubuntu 20.04
    
- ### 執行環境 Runtime
    - 語言: Python 3.7.8
    - 包管理工具: pip 21.1.2
    
---
## 結果 Result
![image](https://hackmd.io/_uploads/HJcyPThX0.png)

![image](https://hackmd.io/_uploads/ryMZD6nXA.png)

![image](https://hackmd.io/_uploads/HkrfDT370.png)


---
## 其餘 Others
![image](https://hackmd.io/_uploads/HyhDFp2QA.png)

![image](https://hackmd.io/_uploads/Hy-PK63mC.png)

![image](https://hackmd.io/_uploads/BJVSDp3QC.png)
