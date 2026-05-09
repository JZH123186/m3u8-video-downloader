# m3u8-video-downloader
基于 ffmpeg 的 m3u8 批量下载与转 mp4 工具
# m3u8 批量下载工具

这是一个基于 Python + ffmpeg 的 m3u8 视频流批量下载与 MP4 转换工具。

---

## 🚀 功能特点

- 支持批量下载 m3u8 视频链接
- 自动将 m3u8 转换为 MP4 格式
- 支持通过文本文件批量导入链接
- 自动分类输出视频文件
- 脚本简单，易于使用

---

## 📦 环境要求

- Python 3.x
- ffmpeg（需配置到环境变量）

ffmpeg 下载地址：
https://ffmpeg.org/download.html

---

## 📁 项目结构

m3u8-downloader/ │ ├
── batch.py        # 主程序 ├
── urls.txt        # m3u8链接列表（一行一个） └

---

## ⚙️ 使用方法

### 1️⃣ 添加视频链接

在 `urls.txt` 中写入 m3u8 链接（每行一个）：

https://example.com/video1.m3u8
https://example.com/video2.m3u8

2️⃣ 运行脚本
Bash
python batch.py

3️⃣ 输出结果
下载完成的视频会保存到：
Plain text
P:\class_video

🧠 工作原理
使用 ffmpeg 读取 m3u8 视频流，并自动下载并合并为 MP4 文件。

⚠️ 注意事项
部分 m3u8 链接可能会过期
某些视频需要有效 token 或 referer
请确保 ffmpeg 已正确安装

📌 作者说明
本项目用于学习 Python 自动化与视频处理技术。

🔥 后续优化方向
图形界面版本（GUI）
多线程下载提升速度
下载失败自动重试
视频自动命名优化
