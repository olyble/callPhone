
# callPhoneBoom
思路：通过爬取使用「莆田系医院」这一营销组件的企业,
我们可以得到数以万计真实企业的网址。
并通过程序模拟浏览，可以将攻击信息给到这些企业。最终达到「电话攻击」的目的。


## 声明
本项目仅供学习交流使用，勿作商业或非法用途。

所有用户个人行为与本项目无关。

## 爬取接口
感谢xdq2005adam提供的爬取脚本catchad

得益于此脚本，你可以本地运行爬取更多地址放入api.txt中，来增加威力


我上网的时候找到这个项目，发现不能用了，于是修改了一些内容，新增几个功能。
第一，无头模式，不用每次打开窗口。
第二，限制同时运行的线程数，这样就可以一边玩游戏，一遍愉快的轰炸别人了！
第三，莆田系页面元素有改变，原来的基本用不了，我重新修改为现在能用，时间是2024年11月18日，截止这个时候，可以正常使用这个元素。
第四，额，不知道说啥，感谢作者的构想，其实我只懂一点点python，所以做了一点微不足道的修改。
使用我的版本请运行test1.py

## 使用教程
1. 下载
    ```shell script
     $ git clone https://github.com/olyble/callPhoneBoom.git
    ```
2. 安装 Selenium
   ```shell script
   $ pip3 install selenium
   ```
   安装 Selenium 之后，**需要安装对应浏览器的 Driver** ，参见 Selenium 文档 [1.3 节](https://selenium-python.readthedocs.io/installation.html#drivers)。 
    >Seleium 具体的介绍及使用方法可参见 [Selenium 文档](https://selenium-python.readthedocs.io)。

3. 配置

  在main.py中填入需要轰炸的手机号
  
<!--     配置文件为`config.py`，参数说明如下：
   ```python
   """
   攻击对象信息
   """ 
   target = { 
       "phone": "13012345678",             # 手机号
       "name": "小小明",                    # 姓名
       "email": "xx@xx.xx",                # 邮箱
       "address": "宇宙银河太阳系地球村",     # 地址
       "comment": "你好 不会～"             # 留言信息
   }
   
   """
   参数设置
   """
   settings = {
       "times": 100,                 # 攻击次数
       "timeout": 5,                 # 超时
       "driver":webdriver.Firefox(), # 使用的 driver
   }
   ``` -->
   
   
  使用DrissionPage已合并到main2.只用使用set.py设置环境就可以使用

测试阶段建议大家吧api.txt 里面的网站先只保留几个做个测试再跑，要不然一次性弹出来。
问题一：手机号在哪里 改啊？ 没找到配置文件config.py
跑起来只会打开和关闭网站，并没有输入 电话号码欸。
所以 希望博主大大能够补充一下 运行步骤呢 就差最后一步输入 电话号码卡住了呜呜。 selenium 和浏览器组件弄了好久 感谢博主！！！！
图片一    ![]([https://res.cloudinary.com/dxl1idlr5/image/upload/v1675247958/2023/02/ce181419ab91f325ac208e188904538a.png](https://private-user-images.githubusercontent.com/109078329/313204687-67f12993-3b62-4fb2-83d7-9b19974e3f59.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTIzMzMxNTcsIm5iZiI6MTcxMjMzMjg1NywicGF0aCI6Ii8xMDkwNzgzMjkvMzEzMjA0Njg3LTY3ZjEyOTkzLTNiNjItNGZiMi04M2Q3LTliMTk5NzRlM2Y1OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQwNVQxNjAwNTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZTA0NDBlN2RhYTdkMTIxZjA1MjRiYjcyM2NiOWY4OWNiNzFiZjNkYTc5Y2YxNmUxNzhmNTBlNDJlZWFhZTNkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.54QEzKojTqByWB9rGS5MF5Ee836zBSBEnQEBfFi_o_o))
 图片二    ![]([https://res.cloudinary.com/dxl1idlr5/image/upload/v1675247958/2023/02/ce181419ab91f325ac208e188904538a.png](https://private-user-images.githubusercontent.com/109078329/313204705-2385e169-2318-4b7d-a5c4-3e48079cc103.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTIzMzMxNTcsIm5iZiI6MTcxMjMzMjg1NywicGF0aCI6Ii8xMDkwNzgzMjkvMzEzMjA0NzA1LTIzODVlMTY5LTIzMTgtNGI3ZC1hNWM0LTNlNDgwNzljYzEwMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQwNVQxNjAwNTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNDBlNmJlYTc2NWViZmExZGI2YWQzYTE2NDBlNmQ0ZDJlNGI4OTc5MzA1YmZjMzQ5MzkwZTZlZjJkYzgwODZkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.LkaS9HyGqTqTSpHDaL93Kr2BEPd60MgH5tWtjduh40k))


4. 运行程序
    ```shell script
    $ python3 main.py
    ```
5. Enjoy!

    运行截图：
    
    ![](https://res.cloudinary.com/dxl1idlr5/image/upload/v1675247958/2023/02/ce181419ab91f325ac208e188904538a.png)

## 目录说明


## TODO
1. 使用 PyQt5 实现用户界面。
2. 定时任务。
3. 使用 「HTTP 请求」替代「模拟浏览」。
4. 跳过验证码
5. 封装docker


## 许可
MIT
