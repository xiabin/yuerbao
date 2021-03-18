###

### 背景
老婆使用了育儿宝4年多，里面太多相册和视频，现在育儿宝要关停表示遗憾，虽然其提供了下载网站，但是还是很不方便，所以写了个爬虫进行视频和照片的爬取

### 常用操作
生成依赖
```
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```
注意 --encoding=utf8 为使用utf8编码，不然可能会报UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 406: illegal multibyte sequence 的错误。

--force 强制执行，当 生成目录下的requirements.txt存在时覆盖。
安装依赖
```
pip install -r requirements.txt
```
### 操作说明

1. 安装环境建议使用conda作为开发环境
2. 登录网站 https://www.yuerbao.com/m/yuerbao/download.html 获取sessionid 然后在代码中配置，然后执行脚本
注意session有有效期，大概30分钟，失败后，记录页数重新在爬取。
3. 爬取脚本
爬取视频
```
 scrapy crawl videos 
```
爬取照片
```
 scrapy crawl videos 
```


### 有问题欢迎微信联系沟通
![wechat](http://qiniu-xb-temp.xiazixun.com/WechatI.jpeg?imageView2/2/w/300)