# 此工具用于获取本机出口IP地址以及查询ip地址的所在地。
### demo地址：https://ip.iuhui.site  （1核1G，请勿压测）(原域名：ip.newb.ga已经凉凉）
### 1.环境python 2.7 和 django 1.11.X
### 2.安装
#### 1) git clone https://github.com/yubinhong/ip.git
#### 2) git submodule update --init --recursive
#### 3）pip install -r requirements.txt
#### 4) python manage.py runserver 0.0.0.0:8000

### 用法
#### 1.默认访问为获取本机出口IP地址以及所在地
#### curl https://ip.teatea.ga

#### 2.添加ip参数可以查询其他ip地址
#### curl https://ip.teatea.ga/?ip=114.114.114.114

### 捐赠地址
![](https://res.cloudinary.com/dc6pgic7p/image/upload/v1553325075/weixin.jpg)
![](https://res.cloudinary.com/dc6pgic7p/image/upload/v1553241343/zhifubao.png)

### 感谢
感谢[lionsoul2014](https://github.com/lionsoul2014/ip2region) 提供的ip数据以及工具
### License
MIT
