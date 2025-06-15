
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_about_me_png(name, profile_text, output_filename='aboutme.png', width=800, height=400):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體
    try:
        # 嘗試使用不同的現代字體
        title_font = ImageFont.truetype("Arial", 40)
        text_font = ImageFont.truetype("Arial", 20)
    except IOError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except IOError:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
    
    # 創建模擬的圓形頭像（如果沒有實際圖片）
    avatar_size = 150
    avatar = Image.new('RGBA', (avatar_size, avatar_size), color=(200, 200, 200, 255))
    avatar_draw = ImageDraw.Draw(avatar)
    
    # 在頭像上繪製一些簡單的剪影效果
    avatar_draw.ellipse([20, 20, 130, 130], fill=(150, 150, 150, 255))
    
    # 為頭像添加模糊陰影效果
    avatar = avatar.filter(ImageFilter.GaussianBlur(3))
    
    # 將頭像貼到主圖像
    image.paste(avatar, (50, 50), avatar)
    
    # 設定文字顏色
    title_color = (0, 51, 102)  # 深藍色
    text_color = (50, 50, 50)   # 深灰色
    
    # 在圖像上繪製名字
    draw.text((250, 70), name, font=title_font, fill=title_color)
    
    # 繪製個人簡介文字（支持多行）
    draw.multiline_text(
        (250, 130), 
        profile_text, 
        font=text_font, 
        fill=text_color,
        spacing=5,
        align='left'
    )
    
    # 保存圖像
    image.save(output_filename)
    print(f"圖像已成功保存為 {output_filename}")

# 使用範例
create_about_me_png(
    name="王小明", 
    profile_text="熱愛程式設計的軟體工程師\n專注於Python和Web開發\n擁有3年開發經驗\n目標成為全端工程師"
)
create_about_me_png(
    name="Hachi.TSAI",
    profile_text="Passionate Industrial Control Software Engineer\nFocused on DCS and PLC Design\nProficient in Japanese Communication\nAspiring AI Industrial Automation Specialist"
)