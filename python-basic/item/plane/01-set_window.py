
#飞机大战-新建一个窗口

import pygame

def main():

	#创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)

	#创建一个和窗口大小的图片，来充当背景　
	background = pygame.image.load("./feiji/background.png").convert()

	#把背景图片放到窗口中显示
	while True:
		
		#设定需要显示的背景图
		screen.blit(background,(0,0))

		#更新显示的内容
		pygame.display.update()

if __name__ == "__main__":
	main()
help(main)
