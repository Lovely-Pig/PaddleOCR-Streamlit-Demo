# PaddleOCR & Streamlit

> 使用Streamlit部署PaddleOCR应用

## 部署步骤

注意：请使用Linux系统进行部署（原因：paddleocr的whl包对Windows的支持不太好）

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
