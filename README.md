# query_bili_fans_num
获取B站粉丝数小工具

## 打包为exe执行文件方法
1、首先`pip install -r requirements.txt`安装必要的依赖包</br>
2、使用`pyinstaller --add-data=".\datasets;pyecharts\datasets\." --add-data=".\templates;pyecharts\render\templates\." -F FN.py -w -i 33.ico
`指令将项目打包成exe执行文件,即”打包.txt“文件内的指令</br>

## 工具使用方法
1、主界面<br/>
![321](https://user-images.githubusercontent.com/88483039/185784001-e22c2476-bc04-42fb-9956-4fa35d0b565c.png)
<br></br>
2、用户存储界面</br>
![123](https://user-images.githubusercontent.com/88483039/185783893-6ca251cb-9258-4b99-817a-a3a6eecc3f4b.png)
<br></br>
3、自动生成的可视化界面
![456](https://user-images.githubusercontent.com/88483039/185784092-f44434d1-14cb-4c09-b64f-c434e2c90182.png)
