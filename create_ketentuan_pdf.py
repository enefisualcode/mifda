from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from PIL import Image
from pathlib import Path

source = Path(r'C:/Users/ASUS/AppData/Local/Temp/codex-clipboard-e7c5eb88-2c60-4779-a6f3-0f5440a7f843.png')
out = Path('output/pdf/ketentuan-ppdb-mi-mifda-2026-2027.pdf')
out.parent.mkdir(parents=True, exist_ok=True)
page_w, page_h = A4
image = Image.open(source).convert('RGB')
iw, ih = image.size
margin = 24
scale = min((page_w - margin * 2) / iw, (page_h - margin * 2) / ih)
dw, dh = iw * scale, ih * scale
c = canvas.Canvas(str(out), pagesize=A4)
c.setFillColor(colors.white)
c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
c.drawImage(ImageReader(image), (page_w-dw)/2, (page_h-dh)/2, dw, dh, preserveAspectRatio=True, mask='auto')
c.setTitle('Ketentuan PPDB MI MIFTAHUL HUDA 2026-2027')
c.save()
print(out)
