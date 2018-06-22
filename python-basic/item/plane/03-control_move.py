
#飞机大战-显示玩家飞机,检测键盘,控制玩家移动

import pygame
import time
from pygame.locals import *

#面向对象，定义一个飞机类
class Heroplane(object):
	def __init__(self,screen):

		#定义对象的初始位置
		self.x = 230
		self.y = 600

		#初始化窗口大小
		self.screen = screen

		#保存一个飞机的图片名字
		self.ImageName = "./feiji/hero.gif"
		#在窗口里生成一个飞机图片
		self.image = pygame.image.load(self.ImageName).convert()

		#保存飞机射出的子弹
		self.Bullet = []

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	def moveLeft(self):
		self.x -= 10
	def moveRight(self):
		self.x += 10
	def moveUp(self):
		self.y -= 10
	def moveDown(self):
		self.y += 10
		
def key_control(player_temp):
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
				player_temp.moveLeft()
			#判断按键是否是d或者right
			elif event.key == K_d or event.key == K_RIGHT:
				player_temp.moveRight()
			#判断按键是否是space
			elif event.key == K_SPACE:
				print("space")
			elif event.key == K_w or event.key == K_UP:
				player_temp.moveUp()
			elif event.key == K_s or event.key == K_DOWN:
				player_temp.moveDown()
	
def main():

	#创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
	#显示背景
	background = pygame.image.load("./feiji/background.png")
	#创建了一个玩家对象
	player = Heroplane(screen)
	while True:
		
		screen.blit(background,(0,0))	
		#更新显示的内容
		player.display()
		key_control(player)
		pygame.display.update()
		#延时，避免程序cpu飙升
		time.sleep(0.01)

if __name__ == "__main__":
	main()
