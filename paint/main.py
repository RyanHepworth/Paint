import customtkinter as ctk 
from draw_surface import DrawSurface
from toolpanel import ToolPanel

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry('800x600')
		self.title('')
		self.iconbitmap('images/empty.ico')
		ctk.set_appearance_mode('light')

		# data
		self.color_string = ctk.StringVar(value='000')
		self.brush_float = ctk.DoubleVar(value=0.5)
		self.erase_bool = ctk.BooleanVar()
	
		# widgets 
		self.draw_surface = DrawSurface(self, self.color_string, self.brush_float, self.erase_bool)
		ToolPanel(self, self.brush_float, self.color_string, self.erase_bool, self.clear_canvas)
		self.erase_bool.set(False)

		# mouse wheel event
		self.bind('<MouseWheel>', self.adjust_brush_size)


		self.mainloop()

	def clear_canvas(self):
		self.draw_surface.delete('all')

		
	def adjust_brush_size(self, event):
		# this has the same effect and is what i did
		# direction = -0.5 if event.delta < 0 else 0.5
		# new_brush_size = self.brush_float.get() + 0.05 * direction
		# self.brush_float.set(new_brush_size)
		# if new_brush_size < 0.2:
		# 	self.brush_float.set(0.2)
		# if new_brush_size > 1:
		# 	self.brush_float.set(1)

		direction = int(event.delta / abs(event.delta))
		new_brush_size = self.brush_float.get() + 0.05 * direction
		new_brush_size = max(0.2, min(1, new_brush_size))
		self.brush_float.set(new_brush_size)


if __name__ == '__main__':
	App()