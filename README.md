

![B7759C97-3BD3-4ABA-94AD-4A9E2EFA11BB_1_201_a](https://blogsources-1305284863.file.myqcloud.com/images/B7759C97-3BD3-4ABA-94AD-4A9E2EFA11BB_1_201_a.jpeg)

# Tongji-AutoGetScore

一个简单、方便、易于使用的成绩查询与监测app

支持几乎所有平台

## 免费下载

- [Windows](https://cineaworks-1305284863.cos.accelerate.myqcloud.com/tongji-AutoGetScore-new/1.0.0/Tongji-AutoGetScore-Windows-amd64.zip)

- [macOS(双平台通用)](https://cineaworks-1305284863.cos.accelerate.myqcloud.com/tongji-AutoGetScore-new/1.0.0/Tongji-AutoGetScore-macOS-Universal.dmg)

- Linux等其他平台：请前往GitHub下载源代码直接使用

**GitHub项目地址**

[Cinea4678/Tongji-AutoGetScore-new](https://github.com/Cinea4678/Tongji-AutoGetScore-new)



## 手动运行

*前提条件：已经安装Python 3.6～3.10（暂不推荐3.11，因为项目使用的自编译库fastgm-whl还未来得及适配3.11）*

手动运行时，您需要先clone代码到本地。

```bash
git clone https://github.com/Cinea4678/Tongji-AutoGetScore-new.git
cd Tongji-AutoGetScore-new
```

如果GitHub不可用，可以使用作者的私有反代服务器

```bash
git clone https://www.cinea.com.cn/git/tongji-autogetscore-new.git
cd tongji-autogetscore-new
```

接下来，安装依赖（在大多数linux平台上，你可能需要使用pip3）

```bash
pip install -r requirements.txt 
```

最后，运行即可。（在大多数linux平台上，你可能需要使用python3）

```bash
python Tongji-AutoGetScore.py 
```


