# Download_91Porn
91Porn 爬虫，实现看片自由。。。

## Clone后修改如下变量

```python
    # number 6位整数，后三位可以修改，50为一次下多少部片。
    # client_src:下载后保存在本地什么位置。
    number=428330
    number_end=number+50
    client_src="D://资源//"
```

## 待优化
1. 爬下来的是分段的ts文件，可以使用potplayer播放器自动播放。
2. 如果想合并，将combine.bat 移动至存放片子的文件夹双击执行即可，当然这部分可以加入到download_91.py文件中，不想搞了，欢迎提PR。
