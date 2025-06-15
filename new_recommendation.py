import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_recommendations_png(recommendations, output_filename='new_recommendation.png', width=1000, height=600):
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
    name_color = (20, 100, 150)         # 亮藍色
    text_color = (70, 70, 70)           # 深灰色
    quote_color = (150, 150, 150)       # 引號灰色
    
    # 繪製標題
    draw.text((50, 30), "Recommendations", font=title_font, fill=title_color)
    
    # 推薦信參數
    start_y = 120
    line_height = 40
    quote_symbol_size = 30
    
    # 繪製推薦信
    for i, recommendation in enumerate(recommendations):
        # 計算垂直位置
        y = start_y + i * (line_height * 4)
        
        # 創建引號圖標
        quote_icon = Image.new('RGBA', (quote_symbol_size, quote_symbol_size), color=(0,0,0,0))
        quote_draw = ImageDraw.Draw(quote_icon)
        # 修正字型載入方式，避免 OSError
        try:
            quote_font = ImageFont.truetype("arial.ttf", quote_symbol_size)
        except OSError:
            try:
                quote_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", quote_symbol_size)
            except OSError:
                try:
                    quote_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", quote_symbol_size)
                except OSError:
                    quote_font = ImageFont.load_default()
        quote_draw.text((0,0), '"', font=quote_font, fill=quote_color)
        
        # 貼上引號圖標
        image.paste(quote_icon, (50, y), quote_icon)
        
        # 繪製推薦信內容
        draw.multiline_text(
            (50 + quote_symbol_size + 10, y), 
            recommendation['text'], 
            font=recommendation_text_font, 
            fill=text_color,
            spacing=5
        )
        
        # 繪製推薦人名字和職位
        recommender_text = f"- {recommendation['name']}, {recommendation['position']}"
        draw.text(
            (50 + quote_symbol_size + 10, y + line_height * 2), 
            recommender_text, 
            font=recommendation_name_font, 
            fill=name_color
        )
    
    # 添加裝飾性底部線
    draw.line([(30, height-10), (width-30, height-10)], fill=(200,200,200), width=2)
    
    # 保存圖像
    image.save(output_filename)
    print(f"推薦信圖像已成功保存為 {output_filename}")

# 現有推薦信列表
existing_recommendations = [
    {
        'text': 'Exceptional skills in industrial automation\nand impressive problem-solving abilities.',
        'name': 'Dr. Tanaka',
        'position': 'Senior Industrial Engineer'
    },
    {
        'text': 'Outstanding communication skills\nand deep understanding of PLC systems.',
        'name': 'Michael Chen',
        'position': 'Automation Project Manager'
    }
]

# 新增推薦信
new_recommendation = {
    'text': 'Remarkable potential in AI-driven industrial\nautomation with strong technical expertise.',
    'name': 'Emily Rodriguez',
    'position': 'AI Innovation Director'
}

# 將新推薦信加入現有列表
full_recommendations = existing_recommendations + [new_recommendation]

# 生成推薦信PNG
create_recommendations_png(full_recommendations)
