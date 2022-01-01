# PaddleOCR & Streamlit

> 使用Streamlit部署PaddleOCR应用

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

### 2 
