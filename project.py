
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_projects_png(projects, output_filename='projects.png', width=1000, height=500):
    # 創建白色背景圖像
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    
    # 創建可以在圖像上繪圖的對象
    draw = ImageDraw.Draw(image)
    
    # 選擇字體
    try:
        title_font = ImageFont.truetype("Arial", 40)
        project_title_font = ImageFont.truetype("Arial", 25)
        project_desc_font = ImageFont.truetype("Arial", 18)
    except IOError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            project_title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
            project_desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except IOError:
            title_font = ImageFont.load_default()
            project_title_font = ImageFont.load_default()
            project_desc_font = ImageFont.load_default()
    
    # 定義顏色
    title_color = (0, 51, 102)      # 深藍色
    project_title_color = (20, 100, 150)  # 亮藍色
    project_desc_color = (70, 70, 70)     # 深灰色
    
    # 繪製標題
    draw.text((50, 30), "Project Details", font=title_font, fill=title_color)
    
    # 項目參數
    start_y = 120
    line_height = 40
    
    # 繪製項目詳情
    for i, project in enumerate(projects):
        # 計算垂直位置
        y = start_y + i * (line_height * 3)
        
        # 繪製項目編號和標題
        project_header = f"{i+1}. {project['title']}"
        draw.text((50, y), project_header, font=project_title_font, fill=project_title_color)
        
        # 繪製項目描述（支持多行）
        draw.multiline_text(
            (50, y + line_height), 
            project['description'], 
            font=project_desc_font, 
            fill=project_desc_color,
            spacing=5
        )
        
        # 繪製技術棧
        tech_text = f"Technologies: {', '.join(project['technologies'])}"
        draw.text((50, y + line_height * 2), tech_text, font=project_desc_font, fill=project_desc_color)
    
    # 添加裝飾性底部線
    draw.line([(30, height-10), (width-30, height-10)], fill=(200,200,200), width=2)
    
    # 保存圖像
    image.save(output_filename)
    print(f"項目詳情圖像已成功保存為 {output_filename}")

# 項目列表
projects = [
    {
        'title': 'Industrial Automation Dashboard',
        'description': 'Developed a comprehensive IoT dashboard\nfor real-time industrial equipment monitoring\nand predictive maintenance.',
        'technologies': ['Python', 'DCS', 'IoT', 'React']
    },
    {
        'title': 'AI-Powered PLC Optimization',
        'description': 'Implemented machine learning algorithms\nto enhance PLC performance and\nreduce operational inefficiencies.',
        'technologies': ['AI', 'Machine Learning', 'PLC', 'TensorFlow']
    },
    {
        'title': 'Japanese Industrial Communication Platform',
        'description': 'Created a multilingual communication\nplatform for international industrial\ncollaboration and knowledge sharing.',
        'technologies': ['Japanese', 'WebSocket', 'Node.js', 'Internationalization']
    }
]

# 生成項目詳情PNG
create_projects_png(projects)
