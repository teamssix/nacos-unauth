# nacos-unauth
2020年12月29日，Nacos官方在github发布的issue中披露Alibaba Nacos 存在一个由于不当处理User-Agent导致的未授权访问漏洞 。通过该漏洞，攻击者可以进行任意操作，包括创建新用户并进行登录后操作。

# 漏洞影响范围
> Nacos <= 2.0.0-ALPHA.1

# 使用
```
git clone https://github.com/teamssix/nacos-unauth.git

cd nacos-unauth

python3 nacos-unauth.py url
```

```
eg: python3 nacos-unauth.py www.example.com
```

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
