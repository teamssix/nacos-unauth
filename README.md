# nacos-unauth
在 Nacos <= 2.0.0-ALPHA.1 版本中存在一个由于不当处理User-Agent导致的未授权访问漏洞 。通过该漏洞，攻击者可以进行任意操作，包括创建新用户并进行登录后操作。

# 使用
```
python3 nacos-unauth.py url

eg: python3 nacos-unauth.py www.example.com
```

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
