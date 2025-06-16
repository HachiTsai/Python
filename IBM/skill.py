import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_skills_png(skills, output_filename='skills.png', width=1000, height=400):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體
    try:
        title_font = ImageFont.truetype("Arial", 40)
        skill_font = ImageFont.truetype("Arial", 20)
    except IOError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            skill_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except IOError:
            title_font = ImageFont.load_default()
            skill_font = ImageFont.load_default()
    
    # 定義顏色
    title_color = (0, 51, 102)  # 深藍色
    text_color = (50, 50, 50)   # 深灰色
    
    # 繪製標題
    draw.text((50, 30), "Skills", font=title_font, fill=title_color)
    
    # 技能圖標參數
    icon_size = 100
    icon_spacing = 50
    start_y = 120
    
    # 繪製技能圖標和名稱
    for i, skill in enumerate(skills):
        # 計算圖標位置
        x = 50 + i * (icon_size + icon_spacing)
        
        # 創建技能圖標（模擬）
        icon = Image.new('RGBA', (icon_size, icon_size), color=skill['color'])
        icon_draw = ImageDraw.Draw(icon)
        
        # 在圖標中心繪製技能縮寫或圖示
        try:
            abbr_font = ImageFont.truetype("arial.ttf", 40)
        except OSError:
            try:
                abbr_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 40)
            except OSError:
                try:
                    abbr_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
                except OSError:
                    abbr_font = ImageFont.load_default()
        abbr_width = icon_draw.textlength(skill['abbr'], font=abbr_font)
        # 使用 textbbox 取得高度
        abbr_bbox = icon_draw.textbbox((0, 0), skill['abbr'], font=abbr_font)
        abbr_height = abbr_bbox[3] - abbr_bbox[1]
        icon_draw.text(
            ((icon_size - abbr_width) / 2, (icon_size - abbr_height) / 2), 
            skill['abbr'], 
            font=abbr_font, 
            fill=(255, 255, 255, 255)
        )
        
        # 為圖標添加陰影效果
        icon = icon.filter(ImageFilter.GaussianBlur(2))
        
        # 將圖標貼到主圖像
        image.paste(icon, (x, start_y), icon)
        
        # 繪製技能名稱
        draw.text(
            (x + icon_size // 2 - draw.textlength(skill['name'], font=skill_font) // 2, 
             start_y + icon_size + 10), 
            skill['name'], 
            font=skill_font, 
            fill=text_color
        )
    
    # 保存圖像
    image.save(output_filename)
    print(f"技能圖像已成功保存為 {output_filename}")

# 技能列表（包括之前的和新增的技能）
skills = [
    {
        'name': 'DCS Design',
        'abbr': 'DCS',
        'color': (0, 120, 200)  # 藍色
    },
    {
        'name': 'PLC Programming',
        'abbr': 'PLC',
        'color': (220, 100, 50)  # 橙色
    },
    {
        'name': 'Japanese',
        'abbr': '日本',
        'color': (100, 200, 100)  # 綠色
    },
    {
        'name': 'AI Automation',
        'abbr': 'AI',
        'color': (150, 50, 200)  # 紫色
    },
    {
        'name': 'Industrial IoT',
        'abbr': 'IoT',
        'color': (255, 180, 0)  # 黃色
    }
]

# 生成技能PNG
create_skills_png(skills)
