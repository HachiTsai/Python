import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_popup_png(output_filename='popup.png', width=500, height=300):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體
    try:
        title_font = ImageFont.truetype("Arial", 30)
        message_font = ImageFont.truetype("Arial", 20)
    except IOError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
            message_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except IOError:
            title_font = ImageFont.load_default()
            message_font = ImageFont.load_default()
    
    # 定義顏色
    background_color = (240, 248, 255)  # 淡藍色背景
    border_color = (0, 51, 102)         # 深藍色邊框
    title_color = (0, 51, 102)          # 深藍色標題
    message_color = (50, 50, 50)        # 深灰色消息
    button_color = (20, 100, 150)       # 亮藍色按鈕
    
    # 繪製彈出框背景
    popup_rect = [50, 50, width-50, height-50]
    draw.rectangle(popup_rect, fill=background_color, outline=border_color, width=3)
    
    # 繪製勾選圖示
    def draw_checkmark(draw, x, y, size=60, color=(20, 100, 150)):
        # 繪製勾選標記
        draw.line(
            [(x, y+size/2), (x+size/3, y+size)], 
            fill=color, width=8
        )
        draw.line(
            [(x+size/3, y+size), (x+size, y)], 
            fill=color, width=8
        )
    
    # 在彈出框中心繪製勾選圖示
    draw_checkmark(draw, width/2 - 30, 100)
    
    # 繪製標題
    title_text = "Recommendation Submitted"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(
        ((width - title_width) / 2, 180), 
        title_text, 
        font=title_font, 
        fill=title_color
    )
    
    # 繪製確認消息
    message_text = "Thank you for leaving a recommendation!"
    message_bbox = draw.textbbox((0, 0), message_text, font=message_font)
    message_width = message_bbox[2] - message_bbox[0]
    draw.text(
        ((width - message_width) / 2, 230), 
        message_text, 
        font=message_font, 
        fill=message_color
    )
    
    # 繪製確認按鈕
    button_text = "OK"
    try:
        button_font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        try:
            button_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
        except OSError:
            try:
                button_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
            except OSError:
                button_font = ImageFont.load_default()
    button_bbox = draw.textbbox((0, 0), button_text, font=button_font)
    button_width = button_bbox[2] - button_bbox[0]
    button_height = button_bbox[3] - button_bbox[1]
    
    button_rect = [
        width/2 - 50, 
        height - 100, 
        width/2 + 50, 
        height - 100 + 50
    ]
    
    # 繪製按鈕背景
    draw.rectangle(button_rect, fill=button_color, outline=(10,50,100), width=2)
    
    # 繪製按鈕文字
    draw.text(
        (width/2 - button_width/2, height - 85), 
        button_text, 
        font=button_font, 
        fill=(255,255,255)
    )
    
    # 添加陰影效果
    image = image.filter(ImageFilter.GaussianBlur(1))
    
    # 保存圖像
    image.save(output_filename)
    print(f"彈出框已成功保存為 {output_filename}")

# 生成推薦確認彈出框PNG
create_popup_png()
