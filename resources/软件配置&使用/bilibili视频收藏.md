---
aliases: 
tags: []
date created: 2022-07-10 17:29:12
date modified: 2022-07-10 17:50:47
---

# bilibili视频收藏

## 1 PC 端

下载视频, 一般来说有很多**哔哩哔哩的辅助插件**可以完成这个任务.

## 2 Android 端

缓存视频默认存储位置为 `Andriod(系统文件)/data/tv.danmaku.bili/download`
默认格式音画分离, 不能直接用于收藏, 需要格式转换.

!!! note "据说"
    文件夹名称为 av 号, `audio.m4s` 和 `video.m4s` 分别为声音和画面.
    可以分别修改后缀名为 mp4, 并手动通过 PR 合并.

这里主要使用软件 [bili2mp4](https://github.com/bitdust/bili2mp4), 它是托管在 GitHub 上面的开源项目

1. 把缓存的文件夹复制到电脑上
2. 将文件夹拖放到 `bili2mp4.exe` 图标上
3. 转换后的视频将出现在 `bili2mp4_output` 文件夹内

> 使用的时候发现有的视频会转化失败
