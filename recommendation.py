import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_recommendations_png(recommendations, output_filename='recommendations.png', width=1000, height=600):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體
    try:
        title_font = ImageFont.truetype("Arial", 40)
        recommendation_name_font = ImageFont.truetype("Arial", 25)
        recommendation_text_font = ImageFont.truetype("Arial", 18)
    except IOError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            recommendation_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
            recommendation_text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except IOError:
            title_font = ImageFont.load_default()
            recommendation_name_font = ImageFont.load_default()
            recommendation_text_font = ImageFont.load_default()
    
    # 定義顏色
    title_color = (0, 51, 102)          # 深藍色
    background_highlight = (240, 248, 255)  # 淡藍色背景
    name_color = (20, 100, 150)         # 亮藍色
    text_color = (50, 50, 50)           # 深灰色
    quote_color = (200, 200, 200)       # 引號灰色
    
    # 繪製標題
    draw.text((50, 30), "Professional Recommendations", font=title_font, fill=title_color)
    
    # 推薦信參數
    start_y = 120
    card_height = 180
    card_padding = 20
    
    # 創建引號圖標（移出循環外）
    try:
        quote_font = ImageFont.truetype("arial.ttf", 40)
    except OSError:
        try:
            quote_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 40)
        except OSError:
            try:
                quote_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            except OSError:
                quote_font = ImageFont.load_default()
    quote_text = '"'
    
    # 繪製推薦信卡片
    for i, recommendation in enumerate(recommendations):
        # 計算卡片位置
        y = start_y + i * (card_height + card_padding)
        
        # 繪製卡片背景
        card_bbox = [50, y, width-50, y+card_height]
        draw.rectangle(card_bbox, fill=background_highlight, outline=(220,220,220), width=1)
        
        quote_bbox = draw.textbbox((0,0), quote_text, font=quote_font)
        quote_width = quote_bbox[2] - quote_bbox[0]
        quote_height = quote_bbox[3] - quote_bbox[1]
        
        # 繪製引號
        draw.text(
            (card_bbox[0] + 20, card_bbox[1] + 20), 
            quote_text, 
            font=quote_font, 
            fill=quote_color
        )
        
        # 繪製推薦信內容
        draw.multiline_text(
            (card_bbox[0] + 70, card_bbox[1] + 30), 
            recommendation['text'], 
            font=recommendation_text_font, 
            fill=text_color,
            spacing=5
        )
        
        # 繪製推薦人信息
        recommender_text = f"{recommendation['name']}"
        position_text = f"{recommendation['position']}"
        
        # 推薦人名字
        draw.text(
            (card_bbox[0] + 70, card_bbox[1] + card_height - 50), 
            recommender_text, 
            font=recommendation_name_font, 
            fill=name_color
        )
        
        # 推薦人職位
        draw.text(
            (card_bbox[0] + 70, card_bbox[1] + card_height - 20), 
            position_text, 
            font=recommendation_text_font, 
            fill=text_color
        )
    
    # 保存圖像
    image.save(output_filename)
    print(f"推薦信圖像已成功保存為 {output_filename}")

# 客製化推薦信列表
recommendations = [
    {
        'text': 'A remarkable engineer with exceptional\nskills in industrial automation and\nAI integration technologies.',
        'name': 'Dr. Emily',
        'position': 'Chief Technology Officer, Global Automation Inc.'
    },
    {
        'text': 'Demonstrates outstanding problem-solving\nabilities and innovative approach to\nindustrial control systems design.',
        'name': 'Michael Rodriguez',
        'position': 'Senior Automation Architect, TechSolutions LLC'
    },
    {
        'text': 'Exceptional communication skills and\ndeep technical expertise in PLC and\nDCS implementation strategies.',
        'name': 'Carlos Wang',
        'position': 'Director of Engineering, IndustrialNet Solutions'
    }
]

# 生成推薦信PNG
create_recommendations_png(recommendations)
