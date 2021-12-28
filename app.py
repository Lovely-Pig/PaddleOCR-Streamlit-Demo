import streamlit as st

from ocr import detect, recognize
from utils import bytes_to_numpy, numpy_to_pic

st.write("""
# PaddleOCR Streamlit

this is a demo

---
""")


def main():
    # 上传图片
    uploaded_file = st.sidebar.file_uploader('请选择一张图片', type=['png', 'jpg', 'jpeg'])
    print('uploaded_file:', uploaded_file)

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # 转换格式
        img = bytes_to_numpy(bytes_data, channels='RGB')

        option_task = st.sidebar.radio('请选择要执行的任务', ('查看原图', '文本检测', '文本识别'))
        if option_task == '查看原图':
            st.image(img, caption='原图')
        elif option_task == '文本检测':
            im_show = detect(img)
            st.image(im_show, caption='文本检测后的图片')
        elif option_task == '文本识别':
            option_mode = st.sidebar.radio('请选择图片输出的模式', (0, 1))
            im_show = recognize(img, output_mode=option_mode)
            st.image(im_show, caption='文本识别后的图片')


main()
