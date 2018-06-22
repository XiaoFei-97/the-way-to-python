
#飞机大战-显示玩家飞机,检测键盘,控制玩家移动，控制玩家射击，显示敌机

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
		self.bullet_list = []
	
	#显示飞机的影像
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
	#飞机左移
	def moveLeft(self):
		self.x -= 10
	#飞机右移
	def moveRight(self):
		self.x += 10
	#飞机上移
	def moveUp(self):
		self.y -= 10
	#飞机下移
	def moveDown(self):
		self.y += 10
	def shoot(self):
		#这里的self.x,self.y是指飞机的位置
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class Enemy(object):
	def __init__(self,screen):

		#定义对象的初始位置
		self.x = 0
		self.y = 0

		#初始化窗口大小
		self.screen = screen

		#保存一个飞机的图片名字
		self.ImageName = "./feiji/enemy-1.gif"
		#在窗口里生成一个飞机图片
		self.image = pygame.image.load(self.ImageName).convert()

		#保存飞机射出的子弹
		self.bullet_list = []
	
	#显示飞机的影像
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		#for bullet in self.bullet_list:
			#bullet.display()
			#bullet.move()

	#飞机左移
	def moveLeft(self):
		self.x -= 10
	#飞机右移
	def moveRight(self):
		self.x += 10
	#飞机上移
	def moveUp(self):
		self.y -= 10
	#飞机下移
	def moveDown(self):
		self.y += 10
	def shoot(self):
		#这里的self.x,self.y是指飞机的位置
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))


class Bullet(object):
	def __init__(self,screen,x,y):
		self.x = x+40 
		self.y = y-20 
		self.screen = screen
		self.name = "./feiji/bullet-3.gif"
		self.image = pygame.image.load(self.name).convert()
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	def move(self):
		self.y -= 5
		
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
				print("left")
				player_temp.moveLeft()
			#判断按键是否是d或者right
			elif event.key == K_d or event.key == K_RIGHT:
				print("right")
				player_temp.moveRight()
			#判断按键是否是space
			elif event.key == K_SPACE:
				print("space")
				player_temp.shoot()
			elif event.key == K_w or event.key == K_UP:
				print("up")
				player_temp.moveUp()
			elif event.key == K_s or event.key == K_DOWN:
				print("down")
				player_temp.moveDown()
	
def main():

	#1.创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
	#2.显示背景
	background = pygame.image.load("./feiji/background.png")
	#3.创建了一个玩家对象
	player = Heroplane(screen)
	#4.创建一个敌机
	enemy = Enemy(screen)
	while True:
		
		screen.blit(background,(0,0))	
		#更新显示的内容
		player.display()
		enemy.display()
		key_control(player)
		pygame.display.update()
		#延时，避免程序cpu飙升
		time.sleep(0.01)

if __name__ == "__main__":
	main()
