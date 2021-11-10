# USTC自动打卡

python + selenium 实现USTC自动打卡，防止忘记打卡

only work on linux

### 依赖

- python
- selenium
- crontab

### 运行方式

``` shell
make
```

### TODO list

- 完善逻辑
- 无论打卡成功还是失败都会自动发送邮件给指定邮箱
- crontab实现自动化打卡
- 可能会出现的验证码，需要一个简单的CNN来处理