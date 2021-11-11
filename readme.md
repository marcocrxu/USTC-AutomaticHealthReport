# USTC自动打卡

python + selenium 实现USTC自动打卡，防止忘记打卡

only work on linux

### 依赖

- python
- selenium
- crontab

### 运行方式

``` shell
# 执行一次
make
# 定时执行
systemctl start cronie.service
systemctl enable cronie.service
export EDITOR=vim
crontab -e
```

输入（在每天11:30执行脚本打卡）

```
30 11 * * * python pre_folder/main.py > pre_folder/log.txt
```

### TODO list

- 完善逻辑
- 无论打卡成功还是失败都会自动发送邮件给指定邮箱    Done
- crontab实现自动化打卡                        Done
- 可能会出现的验证码，需要一个简单的CNN来处理
- 完善路径问题