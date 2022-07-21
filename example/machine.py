from PIL import Image, ImageDraw
class Machine():
	def __init__(self,IDVALUE):
		super(Machine, self).__init__()
		self.IDVALUE = IDVALUE
	def first_load(self):		
		im = Image.new('RGB', (500, 300), (128, 128, 128))
		draw = ImageDraw.Draw(im)
		draw.rectangle((10, 10, 50,50), fill=(0, 192, 192), outline=(255, 255, 255))
		im.save("./static/"+self.IDVALUE+'.jpg', quality=95)
	def click(self,x,y):
		print(x,y)
		if x>20 and x<140 and y>20 and y<110:
			im = Image.new('RGB', (500, 300), (128, 128, 128))
			draw = ImageDraw.Draw(im)
			draw.rectangle((10, 10, 50,50), fill=(0, 192, 192), outline=(0, 0, 0))
			im.save("./static/"+self.IDVALUE+'.jpg', quality=95)
