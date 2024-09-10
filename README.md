# fuckSQLBlind
CTF sql盲注日志分析
> 做了道CTF流量分析题，布尔盲注，给我恶心惨了，记录一下利用的脚本。

## 提取布尔判断成功的语句

```
strings logbool.pcapng|grep success > sucess.txt
```
## 处理需要还原的字段
content字段处理下，将需要处理的字段摘取到txt里，准备使用脚本处理。
![image](https://github.com/user-attachments/assets/06c7ecdc-e607-49e9-a9f9-08d560c8650f)
## 脚本还原内容
修改脚本读取txt路径直接输出盲注内容
![image](https://github.com/user-attachments/assets/641467c8-10f6-466d-9c63-f0523f596226)

后续转hex还原压缩包，密码在password字段
![image](https://github.com/user-attachments/assets/6d4e7d58-4839-482f-8f4e-a540c8e00ba8)



