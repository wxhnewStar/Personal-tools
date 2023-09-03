![image-20220308131511217](C:\Users\shainvol\Documents\Typora files\图库\6-装饰模式\image-20220308131511217.png)

![image-20220308153727987](C:\Users\shainvol\Documents\Typora files\图库\12-单例模式\image-20220308153727987.png)

![截屏2020-07-26 下午2.45.02](/Users/smart/Library/Application Support/typora-user-images/截屏2020-07-26 下午2.45.02.png)


![a275a6af7625b354123c5062466e4b67.png](en-resource://database/713:1)



![截屏2020-07-28 上午10.28.47](/Users/smart/Library/Application Support/typora-user-images/截屏2020-07-28 上午10.28.47.png)


![image-20220714153622735](D:/Typora files/C-工作/C1-论文/ORAM/22-6/image-20220714153622735.png)


![f6387f0780e8ff703929853383ccd503.png](https://img-blog.csdnimg.cn/img_convert/f6387f0780e8ff703929853383ccd503.png)

![55_1](images/055_1.png)

# 提取出来的规则：
1. 如果含有 .. 代表已经是调整过的了，不需要再调整
2. 如果没有 .. 且此时绝对路径中有 typora files 这个文件夹关键字
   1. 此时需要将绝对路径中的 typora files 之前的替换成 ..
3. 如果没有 .. 且此时绝对路径中没有 typora files 这个文件夹关键字
   1. 如果含有 http 关键字，是网络图片，无需处理
   2. 其他情况，属于极少数的老图片，需要手动处理