
import os
from PIL import Image, ImageDraw, ImageFont

def create_profile_name_png(name, output_filename='profile_name.png', width=800, height=200):
    # 創建一個白色背景的圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建一個可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體（確保你的系統有這些字體，否則會拋出錯誤）
    try:
        # 嘗試使用不同的現代字體
        font = ImageFont.truetype("Arial", 60)  # Windows系統常見字體
    except IOError:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)  # Linux系統
        except IOError:
            font = ImageFont.load_default()  # 如果找不到字體，使用默認字體
    
    # 設定文字顏色為深藍色
    text_color = (0, 51, 102)  # 深藍色
    
    # 在左上角繪製名字
    draw.text((20, 20), name, font=font, fill=text_color)
    
    # 可選：添加底線效果
    text_width = draw.textlength(name, font=font)
    draw.line([(20, 80), (20 + text_width, 80)], fill=text_color, width=3)
    
    # 保存圖像
    image.save(output_filename)
    print(f"圖像已成功保存為 {output_filename}")

# 使用範例
create_profile_name_png("YOUR NAME")
create_profile_name_png("HachiTSAI")