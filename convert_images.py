import os
from PIL import Image

# 图片目录
img_dir = r"C:\Users\17594\my-blog\src\content\blog\关于过零检测与可控硅的实际应用"

# 支持的图片格式
supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.webp', '.gif', '.tiff'}

for filename in os.listdir(img_dir):
    ext = os.path.splitext(filename)[1].lower()
    if ext in supported_formats:
        filepath = os.path.join(img_dir, filename)

        # 跳过已经是 PNG 的文件
        if ext == '.png':
            print(f"跳过（已是PNG）: {filename}")
            continue

        try:
            img = Image.open(filepath)

            # 构建新文件名（改为.png）
            new_name = os.path.splitext(filename)[0] + '.png'
            new_path = os.path.join(img_dir, new_name)

            img.save(new_path, format='PNG')
            print(f"转换成功: {filename} -> {new_name}")

            # 如果原文件不是PNG，删除原文件
            if ext != '.png':
                os.remove(filepath)
                print(f"  删除原文件: {filename}")

        except Exception as e:
            print(f"转换失败: {filename} - {e}")

print("\n完成！")