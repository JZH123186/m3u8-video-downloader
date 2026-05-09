import os

output_dir = r"P:\class_video"
os.makedirs(output_dir, exist_ok=True)

with open("urls.txt", "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

for i, url in enumerate(urls, 1):
    output_file = os.path.join(output_dir, f"video_{i}.mp4")
    print(f"正在下载第 {i} 个视频...")

    cmd = f'ffmpeg -i "{url}" -c copy "{output_file}"'
    os.system(cmd)

print("全部完成")