# Baidu Fanyi

## Description
A Simple SDK for Baidu Translate  (unofficial)

一个简单的用于调用百度翻译api的包。

## Usage

```python
from baidufanyi import BaiduFanyi # 注意大小写

APPID = "your appid"
APPKEY = "your appkey"
# APPID 与 APPKEY 可在百度翻译开放平台获取，标准版可免费使用
fanyi = BaiduFanyi(APPID, APPKEY)

print(fanyi.translate("hello world", fromLang="auto", toLang="zh")) 
# fromLang 和 toLang 格式请查阅百度翻译api文档

```

## Features

1. 支持多行，自动合并

2. 简单易用，立即上手

3. 支持多种语言的设置
