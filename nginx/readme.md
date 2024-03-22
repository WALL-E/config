# 分流代码说明文档

运行环境是OpenResty, 默认配置了三个mock服务来进行测试。

## 关键点-1

为了保证所有的请求body内容全部缓存到内存里，不要写入到磁盘，否则 `ngx.req.get_body_data()` 会调用失败
```
client_body_buffer_size 8k;
client_max_body_size 8k;
```

## 关键点-2

设置分流的字段

```
local value = json_data.apiUrl
```

## 关键点-3

分流支持两种类型，一种是数值，一种是字符串

```
local digest
if type(value) == "number" then
    digest = value
elseif type(value) == "string" then
    digest = ngx.crc32_short(value)
else
    return ngx.exit(0)
end
```

## 关键点-4

有两个默认转发策略

```
set $target '127.0.0.1:8080';
```

```
local mod = digest % 3
if mod == 0 then
    ngx.var.target = "127.0.0.1:8080"
elseif mod == 1 then
    ngx.var.target = "127.0.0.1:8081"
else
    ngx.var.target = "127.0.0.1:8082"
end
```

## 关键点-5

需要优化的关键代码

```
// Todo: 只截取字符串的关键部分进行计算
digest = ngx.crc32_short(value)
```
