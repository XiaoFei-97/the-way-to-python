
#飞机大战-显示玩家飞机,检测键盘,控制玩家移动，控制玩家射击，显示敌机，优化子弹越界，敌机移动,敌机发动攻击，优化抽取基类,飞机爆炸

import pygame
import time
from pygame.locals import *
import random

#创建一个飞机的基类
class Baseplane(object):
	def __init__(self,screen,x,y,image_name):

		#定义对象的初始位置
		self.x = x
		self.y = y

		#初始化窗口大小
		self.screen = screen

		#保存一个飞机的图片名字
		self.ImageName = image_name
		#在窗口里生成一个飞机图片
		self.image = pygame.image.load(self.ImageName).convert()

		#保存飞机射出的子弹
		self.bullet_list = []
		self.hit = False #表示是否要爆炸
		self.bomb_list = []
		self.__create_images() #调用这个方法向bomb_list添加图片
		self.image_index = 0
		self.image_num = 0
	def __create_images(self):
		self.bomb_list.append(pygame.image.load("./feiji/heroup_n1.png"))
		self.bomb_list.append(pygame.image.load("./feiji/heroup_n2.png"))
		self.bomb_list.append(pygame.image.load("./feiji/heroup_n3.png"))
		self.bomb_list.append(pygame.image.load("./feiji/heroup_n4.png"))

	#显示飞机的影像
	def display(self):
		#如果被击中，显示爆炸效果
		if self.hit == True:
			self.screen.blit(self.bomb_list[self.image_index],(self.x,self.y))
			self.image_num += 1
				if self.image_num == 7:
					self.image_num = 0
					self.image_index += 1
				if self.image_index > 3:
					time.sleep(1)
					exit() #游戏退出
		else:
			self.screen.blit(self.image,(self.x,self.y))
		#不管玩家是否被击中，都要显示发射出去的子弹
		for bullet in self.bullet_list:
			bullet.display()
		bullet.move()
		if bullet.judget(): #判断子弹是否越界
			self.bullet_list.remove(bullet)

#面向对象，定义一个飞机类
class Heroplane(Baseplane):
	def __init__(self,screen):
		Baseplane.__init__(self,screen,230,600,"./feiji/hero.gif")
	
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

class Enemy(Baseplane):
	def __init__(self,screen):

		Baseplane.__init__(self,screen,0,0,"./feiji/enemy-1.gif")

		#控制敌机的方向
		self.direction = "right"
	
	def move(self):
		if self.direction == "right":
			self.x += 5
		elif self.direction == "left":
			self.x -= 5
		if self.x > 400:
			self.direction = "left"
		if self.x <0:
			self.direction = "right"
	def shoot(self):
		#这里的self.x,self.y是指飞机的位置
		random_num = random.randint(1,100)
		if random_num == 28 or random_num == 50:
			self.bullet_list.append(Enemy_Bullet(self.screen,self.x,self.y))

class Basebullet(object):
	def display(self):		
		self.screen.blit(self.image,(self.x,self.y))
class Bullet(Basebullet):
	def __init__(self,screen,x,y):
		self.x = x+40 
		self.y = y-20 
		self.screen = screen
		self.name = "./feiji/bullet-3.gif"
		self.image = pygame.image.load(self.name).convert()
	def move(self):
		self.y -= 5
	def judget(self):
		if self.y<0:
			return True
		else:
			return False

class Enemy_Bullet(Basebullet):
	def __init__(self,screen,x,y):
		self.x = x+25 
		self.y = y+40 
		self.screen = screen
		self.name = "./feiji/bullet-1.gif"
		self.image = pygame.image.load(self.name).convert()
	def move(self):
		self.y += 5
	def judget(self):
		if self.y>852:
			return True
		else:
			return False

		
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
		enemy.shoot()
		enemy.move()
		key_control(player)
		pygame.display.update()
		#延时，避免程序cpu飙升
		time.sleep(0.01)

if __name__ == "__main__":
	main()
