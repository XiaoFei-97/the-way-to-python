
#飞机大战-显示玩家飞机,检测键盘

import pygame
import time
from pygame.locals import *

def main():

	#创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)

	#创建一个和窗口大小的图片，来充当背景　
	background = pygame.image.load("./feiji/background.png").convert()

	#创建一个飞机图片
	player = pygame.image.load("./feiji/hero1.png")

	#把背景图片放到窗口中显示
	while True:
		
		#设定需要显示的背景图
		screen.blit(background,(0,0))
		screen.blit(player,(230,500))
	
		#获取事件，如按键
		for event in pygame.event.get():
			
			#判断是否点击类退出按钮
			if event.type == QUIT:
				print("exit")
				exit()
			#判断是否按下了键
			elif event.type == KEYDOWN:
				#判断按键是否是a或者left
				if event.key == K_a or event.key == K_LEFT:
					print("left")
				#判断按键是否是d或者right
				elif event.key == K_d or event.key == K_RIGHT:
					print("right")
				#判断按键是否是space
				elif event.key == K_SPACE:
					print("space")
				elif event.key == K_w or event.key == K_UP:
					print("up")
				elif event.key == K_s or event.key == K_DOWN:
					print("down")

		#更新显示的内容
		pygame.display.update()

		#延时，避免程序cpu飙升
		time.sleep(0.01)

if __name__ == "__main__":
	main()
