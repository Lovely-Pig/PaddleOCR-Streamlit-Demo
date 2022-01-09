# PaddleOCR Streamlit Demo

> 使用 Streamlit 部署 PaddleOCR 应用

体验地址：<https://share.streamlit.io/lovely-pig/paddleocr-streamlit-demo/app.py>

## 介绍

1. PaddleOCR

   官网

   - <https://github.com/PaddlePaddle/PaddleOCR>

   官方介绍

   > PaddleOCR旨在打造一套丰富、领先、且实用的OCR工具库，助力开发者训练出更好的模型，并应用落地。

2. Streamlit

   官网

   - <https://streamlit.io>
   - <https://github.com/streamlit/streamlit>

   官方介绍

   > The fastest way to build and share data apps in Python.

## 开发步骤

注意：请使用Linux系统进行开发（原因：paddleocr的whl包对Windows的支持不太好）

### 1 创建python环境

```sh
$ conda create --name streamlit python=3.9

# 进入环境
$ conda activate streamlit
```

### 2 安装相关依赖

```sh
$ pip install streamlit

# 以下为安装 paddleocr whl包需要
$ sudo apt install gcc build-essential

$ pip install "paddleocr>=2.0.1"
$ pip install paddlepaddle==2.2.1 -i https://mirror.baidu.com/pypi/simple
```

### 3 运行

```sh
$ streamlit run app.py
```

## 部署

部署方式有以下两种

- 服务器部署
- Streamlit Cloud部署

这里介绍Streamlit Cloud部署，也是本项目的部署方式

### 1 将代码仓库上传到GitHub

### 2 所有python库的依赖都写在`requirements.txt`文件里

```tex
paddleocr>=2.0.1
paddlepaddle==2.2.1 -i https://mirror.baidu.com/pypi/simple
```

### 3 新建`packages.txt`文件

```tex
freeglut3-dev
libgtk2.0-dev
```

### 3 注册Streamlit Cloud

地址：<https://share.streamlit.io>

### 4 新建一个app并关联自己的GitHub仓库

### 5 Congratulation 🎉🎉🎉
