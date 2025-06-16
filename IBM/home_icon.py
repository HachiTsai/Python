
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_home_icon_png(output_filename='home_icon.png', width=300, height=300):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 定義顏色
    home_color = (0, 51, 102)     # 深藍色
    roof_color = (220, 100, 50)   # 橙紅色
    
    # 繪製房子主體
    house_width = 200
    house_height = 150
    house_left = (width - house_width) // 2
    house_bottom = height - 50
    
    # 繪製房子基座
    draw.rectangle([
        house_left, 
        house_bottom - house_height, 
        house_left + house_width, 
        house_bottom
    ], fill=home_color, outline=(100,100,100), width=3)
    
    # 繪製屋頂
    roof_points = [
        (house_left, house_bottom - house_height),  # 左下
        (house_left + house_width // 2, house_bottom - house_height - 50),  # 頂點
        (house_left + house_width, house_bottom - house_height)  # 右下
    ]
    draw.polygon(roof_points, fill=roof_color, outline=(150,50,50), width=3)
    
    # 繪製門
    door_width = 50
    door_height = 80
    draw.rectangle([
        house_left + (house_width - door_width) // 2, 
        house_bottom - door_height, 
        house_left + (house_width + door_width) // 2, 
        house_bottom
    ], fill=(180,180,180), outline=(100,100,100), width=2)
    
    # 繪製門把
    draw.ellipse([
        house_left + (house_width + door_width) // 2 - 10, 
        house_bottom - door_height // 2 - 10, 
        house_left + (house_width + door_width) // 2, 
        house_bottom - door_height // 2
    ], fill=(50,50,50))
    
    # 繪製窗戶
    window_width = 40
    window_height = 40
    draw.rectangle([
        house_left + house_width - window_width - 20, 
        house_bottom - house_height + 20, 
        house_left + house_width - 20, 
        house_bottom - house_height + 20 + window_height
    ], fill=(200,230,255), outline=(100,100,100), width=2)
    
    # 添加陰影效果
    shadow = Image.new('RGBA', image.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rectangle([0, height-10, width, height], fill=(0,0,0,50))
    
    # 將陰影疊加到原圖
    image = Image.alpha_composite(image, shadow)
    
    # 保存圖像
    image.save(output_filename)
    print(f"首頁圖標已成功保存為 {output_filename}")

# 生成首頁圖標PNG
create_home_icon_png()
