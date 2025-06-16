import os
from PIL import Image, ImageDraw, ImageFont

def create_navigation_bar_png(output_filename='nav_bar.png', width=1200, height=100):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 定義導航欄選項
    nav_options = ['About', 'Project Details', 'Skills', 'Recommendations']
    
    # 選擇字體
    try:
        # 嘗試使用現代字體
        font = ImageFont.truetype("Arial", 30)
    except IOError:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        except IOError:
            font = ImageFont.load_default()
    
    # 定義顏色
    text_color = (0, 51, 102)  # 深藍色
    hover_color = (255, 0, 0)  # 懸停時的紅色
    
    # 計算每個選項的間距
    spacing = width // (len(nav_options) + 1)
    
    # 繪製導航欄選項
    for i, option in enumerate(nav_options):
        # 計算文字位置
        x = spacing * (i + 1)
        y = height // 2

        # 使用 textbbox 取得文字寬高
        bbox = draw.textbbox((0, 0), option, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # 文字位置居中
        text_x = x - text_width // 2
        text_y = y - text_height // 2

        # 繪製文字
        draw.text((text_x, text_y), option, font=font, fill=text_color)

        # 模擬懸停效果（加粗和底線）
        # 繪製模擬的懸停底線
        line_y = text_y + text_height + 5
        draw.line(
            [(text_x, line_y), (text_x + text_width, line_y)], 
            fill=hover_color, 
            width=3
        )
    
    # 添加裝飾性底部線
    draw.line([(0, height-2), (width, height-2)], fill=(200,200,200), width=2)
    
    # 保存圖像
    image.save(output_filename)
    print(f"導航欄圖像已成功保存為 {output_filename}")

# 生成導航欄PNG
create_navigation_bar_png()
