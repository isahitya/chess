import os
from tkinter import *
from PIL import Image,ImageTk
from tkinter import simpledialog
from tkinter import filedialog
import socket

display_width,display_height=600,600
blocksize=int(display_width/8)
leftstripwidth=int(blocksize/4)
topstripheight=int(blocksize/4)
sidepanelwidth=int(blocksize*4)
root=Tk()
root.title("Chess by Sahitya")
root.geometry(str(display_width+leftstripwidth+sidepanelwidth)+"x"+str(display_height+topstripheight))

canvas=Canvas(root,width=display_width,height=display_height)
canvas.pack()
canvas.place(x=leftstripwidth,y=topstripheight)

leftstrip=Canvas(root,width=int(blocksize/4),height=display_height)
leftstrip.pack()
leftstrip.place(x=0,y=topstripheight)

topstrip=Canvas(root,width=display_width,height=topstripheight)
topstrip.pack()
topstrip.place(x=leftstripwidth,y=0)

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(75,75,125)####NOT ACTUALLY BLACK ,had to change it for some reason




#Loading all images from file
lightbishop=ImageTk.PhotoImage(Image.open("lightbishop.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
lightking=ImageTk.PhotoImage(Image.open("lightking.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
lightknight=ImageTk.PhotoImage(Image.open("lightknight.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
lightqueen=ImageTk.PhotoImage(Image.open("lightqueen.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
lightrook=ImageTk.PhotoImage(Image.open("lightrook.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
lightpawn=ImageTk.PhotoImage(Image.open("lightpawn.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
#lightbishop=pygame.transform.scale(pygame.image.load("lightbishop.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#lightknight=pygame.transform.scale(pygame.image.load("lightknight.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#lightking=pygame.transform.scale(pygame.image.load("lightking.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#lightqueen=pygame.transform.scale(pygame.image.load("lightqueen.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#lightrook=pygame.transform.scale(pygame.image.load("lightrook.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#lightpawn=pygame.transform.scale(pygame.image.load("lightpawn.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))

darkbishop=ImageTk.PhotoImage(Image.open("darkbishop.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
darkking=ImageTk.PhotoImage(Image.open("darkking.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
darkknight=ImageTk.PhotoImage(Image.open("darkknight.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
darkqueen=ImageTk.PhotoImage(Image.open("darkqueen.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
darkrook=ImageTk.PhotoImage(Image.open("darkrook.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
darkpawn=ImageTk.PhotoImage(Image.open("darkpawn.png").resize((int(blocksize-blocksize/4),int(blocksize-blocksize/4))))
#darkbishop=pygame.transform.scale(pygame.image.load("darkbishop.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#darkknight=pygame.transform.scale(pygame.image.load("darkknight.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#darkking=pygame.transform.scale(pygame.image.load("darkking.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#darkqueen=pygame.transform.scale(pygame.image.load("darkqueen.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#darkrook=pygame.transform.scale(pygame.image.load("darkrook.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))
#darkpawn=pygame.transform.scale(pygame.image.load("darkpawn.png"),(int(blocksize-blocksize/4),int(blocksize-blocksize/4)))


class block:
	def __init__(self,xpos=None,ypos=None,color=None):
		self.color=color
		self.xpos=xpos
		self.ypos=ypos
		self.piece=None
		self.isHighlighted=False
	def draw(self):
		x,y=self.xpos*blocksize,self.ypos*blocksize
		if self.isHighlighted==True:
			if self.piece!=None:
				canvas.create_rectangle(x,y,x+blocksize,y+blocksize,fill="red")
			else:
				canvas.create_rectangle(x,y,x+blocksize,y+blocksize,fill="blue")
			canvas.create_rectangle(x+5,y+5,x+blocksize-5,y+blocksize-5,fill=self.color)
		else:
			canvas.create_rectangle(x,y,x+blocksize,y+blocksize,fill=self.color)
		if self.piece!=None:
			self.piece.draw(self.xpos,self.ypos)##########DON'T FORGET

class piece:
	def __init__(self,color,oftype,team):
		self.oftype=oftype
		self.color=color
		self.team=team
		self.firstMove=True
	def draw(self,xpos,ypos):
		if self.oftype=="pawn":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightpawn)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkpawn)
			return
		if self.oftype=="bishop":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightbishop)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkbishop)
			return
		if self.oftype=="king":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightking)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkking)
			return
		if self.oftype=="rook":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightrook)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkrook)
			return
		if self.oftype=="queen":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightqueen)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkqueen)
			return
		if self.oftype=="knight":
			if self.team=="bottom":
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=lightknight)
			else:
				canvas.create_image((int(xpos*blocksize)+blocksize/2,int(ypos*blocksize)+blocksize/2),image=darkknight)
			return
	def move(self,selfx,selfy,xpos,ypos):
		self.firstMove=False
		if blockslist[xpos][ypos].piece==None:
			blockslist[xpos][ypos].piece=self=blockslist[selfx][selfy].piece
			blockslist[selfx][selfy].piece=None
		else:
			if blockslist[xpos][ypos].piece.oftype=="king":
				if blockslist[xpos][ypos].piece.team=="bottom":
					print("Top wins")
				else:
					print("Bottom wins")
			blockslist[xpos][ypos].piece=blockslist[selfx][selfy].piece
			blockslist[selfx][selfy].piece=None


	def calculateMoves(self,xpos,ypos):
		moves=[]
		if self.oftype=="pawn":
			if self.firstMove:
				if self.team=="bottom" and ypos>0:
					if(blockslist[xpos][ypos-1].piece==None):
						moves.append((xpos,ypos-1))
						if(blockslist[xpos][ypos-2].piece==None):moves.append((xpos,ypos-2))
					if xpos>0 and blockslist[xpos-1][ypos-1].piece!=None:
						if blockslist[xpos-1][ypos-1].piece.team!=self.team:
							moves.append((xpos-1,ypos-1))
					if xpos<7 and blockslist[xpos+1][ypos-1].piece!=None:
						if blockslist[xpos+1][ypos-1].piece.team!=self.team:
							moves.append((xpos+1,ypos-1))
				if self.team=="top" and ypos<7:
					if(blockslist[xpos][ypos+1].piece==None):
						moves.append((xpos,ypos+1))
						if(blockslist[xpos][ypos+2].piece==None):moves.append((xpos,ypos+2))
					if xpos>0 and blockslist[xpos-1][ypos+1].piece!=None:
						if blockslist[xpos-1][ypos+1].piece.team!=self.team:
							moves.append((xpos-1,ypos+1))
					if xpos<7 and blockslist[xpos+1][ypos+1].piece!=None:
						if blockslist[xpos+1][ypos+1].piece.team!=self.team:
							moves.append((xpos+1,ypos+1))
			else:
				if self.team=="bottom" and ypos>0:
					if(blockslist[xpos][ypos-1].piece==None):moves.append((xpos,ypos-1))
					if xpos>0 and blockslist[xpos-1][ypos-1].piece!=None:
						if blockslist[xpos-1][ypos-1].piece.team!=self.team:
							moves.append((xpos-1,ypos-1))
					if xpos<7 and blockslist[xpos+1][ypos-1].piece!=None:
						if blockslist[xpos+1][ypos-1].piece.team!=self.team:
							moves.append((xpos+1,ypos-1))
				if self.team=="top" and ypos<7:
					if(blockslist[xpos][ypos+1].piece==None):moves.append((xpos,ypos+1))
					if xpos>0 and blockslist[xpos-1][ypos+1].piece!=None:
						if blockslist[xpos-1][ypos+1].piece.team!=self.team:
							moves.append((xpos-1,ypos+1))
					if xpos<7 and blockslist[xpos+1][ypos+1].piece!=None:
						if blockslist[xpos+1][ypos+1].piece.team!=self.team:
							moves.append((xpos+1,ypos+1))
		if self.oftype=="rook" or self.oftype=="queen":
			if xpos>0:
				p=xpos-1
				while(p>=0):
					if blockslist[p][ypos].piece==None:
						moves.append((p,ypos))
						p-=1
						continue
					if blockslist[p][ypos].piece.team==self.team:
						break
					if blockslist[p][ypos].piece.team!=self.team:
						moves.append((p,ypos))
						break
			if xpos<7:
				p=xpos+1
				while(p<=7):
					if blockslist[p][ypos].piece==None:
						moves.append((p,ypos))
						p+=1
						continue
					if blockslist[p][ypos].piece.team==self.team:
						break
					if blockslist[p][ypos].piece.team!=self.team:
						moves.append((p,ypos))
						break
			if ypos>0:
				p=ypos-1
				while(p>=0):
					if blockslist[xpos][p].piece==None:
						moves.append((xpos,p))
						p-=1
						continue
					if blockslist[xpos][p].piece.team==self.team:
						break
					if blockslist[xpos][p].piece.team!=self.team:
						moves.append((xpos,p))
						break
			if ypos<7:
				p=ypos+1
				while(p<=7):
					if blockslist[xpos][p].piece==None:
						moves.append((xpos,p))
						p+=1
						continue
					if blockslist[xpos][p].piece.team==self.team:
						break
					if blockslist[xpos][p].piece.team!=self.team:
						moves.append((xpos,p))
						break

		if self.oftype=="bishop" or self.oftype=="queen":
			p,q=xpos-1,ypos-1
			while(p>=0 and q>=0):
					if blockslist[p][q].piece==None:
						moves.append((p,q))
						p-=1
						q-=1
						continue
					if blockslist[p][q].piece.team==self.team:
						break
					if blockslist[p][q].piece.team!=self.team:
						moves.append((p,q))
						break
			p,q=xpos+1,ypos+1
			while(p<=7 and q<=7):
					if blockslist[p][q].piece==None:
						moves.append((p,q))
						p+=1
						q+=1
						continue
					if blockslist[p][q].piece.team==self.team:
						break
					if blockslist[p][q].piece.team!=self.team:
						moves.append((p,q))
						break
			p,q=xpos+1,ypos-1
			while(p<=7 and q>=0):
					if blockslist[p][q].piece==None:
						moves.append((p,q))
						p+=1
						q-=1
						continue
					if blockslist[p][q].piece.team==self.team:
						break
					if blockslist[p][q].piece.team!=self.team:
						moves.append((p,q))
						break
			p,q=xpos-1,ypos+1
			while(p>=0 and q<=7):
					if blockslist[p][q].piece==None:
						moves.append((p,q))
						p-=1
						q+=1
						continue
					if blockslist[p][q].piece.team==self.team:
						break
					if blockslist[p][q].piece.team!=self.team:
						moves.append((p,q))
						break
		if self.oftype=="knight":
			p,q=xpos-2,ypos-1

			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos-2,ypos+1
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos+2,ypos-1
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos+2,ypos+1
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos-1,ypos+2
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))

			p,q=xpos+1,ypos+2
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos-1,ypos-2
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))
			p,q=xpos+1,ypos-2
			if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):moves.append((p,q))

		if self.oftype=="king":
			for p in range(xpos-1,xpos+2):
				for q in range(ypos-1,ypos+2):
					if p!=xpos or q!=ypos:
						if((p>=0 and p<=7 and q>=0 and q<=7) and (blockslist[p][q].piece==None or blockslist[p][q].piece.team!=self.team)):
							if self.team=="bottom":
								if checkIfUnderAttack(p,q,"top")==False:
									moves.append((p,q))
							if self.team=="top":
								if checkIfUnderAttack(p,q,"bottom")==False:
									moves.append((p,q))




		return moves


def checkIfUnderAttack(xpos,ypos,underAttackBy):#by which team
	for i in range(0,7+1):
		for j in range(0,7+1):
			if blockslist[i][j].piece!=None and blockslist[i][j].piece.team==underAttackBy and blockslist[i][j].piece.oftype!="king":
				moves=blockslist[i][j].piece.calculateMoves(i,j)
				for each in moves:
					if each[0]==xpos and each[1]==ypos:
						return True
	return False




def saveGame(savefilename="chess_save_game"):
	global chance
	savefilename=simpledialog.askstring("Input","Enter name for save file",parent=root)
	try:
		savefile=open(savefilename+".save","w")
	except:
		return
	savefile.write(chance+'\n')
	for i in range(0,7+1):
		for j in range(0,7+1):
			if blockslist[i][j].piece!=None:
				team=blockslist[i][j].piece.team
				piecetype=blockslist[i][j].piece.oftype
				if blockslist[i][j].piece.firstMove==True:
					firstMove="True"
				else: firstMove="False"
				savefile.write(str(i)+":"+str(j)+":"+team+":"+piecetype+":"+firstMove+'\n')
	savefile.write("topmoves"+'\n')
	topMoves=toplistbox.get(0,END)
	for each in topMoves:
		savefile.write(each+'\n')
	savefile.write("bottommoves"+'\n')
	bottomMoves=bottomlistbox.get(0,END)
	for each in bottomMoves:
		savefile.write(each+'\n')


def loadGame(savedGameName="chess_save_game"):
	global chance,topturncanvas,bottomturncanvas
	savedGameName=filedialog.askopenfilename(parent=root,initialdir=os.getcwd(),title="Select your save file to load",filetypes=[("Save files",'.save')])
	try:
		loadfile=open(savedGameName,"r")
	except:
		return
	for i in range(0,7+1):
		for j in range(0,7+1):
			blockslist[i][j].piece=None
			blockslist[i][j].isHighlighted=False
	strings=loadfile.read().splitlines()
	chance=strings[0]
	print(chance)
	i=1
	while(i<len(strings)):
		if strings[i]=='topmoves':
			i+=1
			break
		xpos,ypos,team,piecetype,firstMove=strings[i].split(':')
		print(str(xpos)+" "+str(ypos)+" "+team+" "+piecetype+" "+firstMove)
		if firstMove=="True":
			fm=True
		else :
			fm=False
		blockslist[int(xpos)][int(ypos)].piece=piece("green",piecetype,team)
		blockslist[int(xpos)][int(ypos)].piece.firstMove=fm
		i+=1

	toplistbox.delete(0,END)
	bottomlistbox.delete(0,END)
	while(i<len(strings)):
		if strings[i]=='bottommoves':
			i+=1
			break
		toplistbox.insert(END,strings[i])
		i+=1
	while(i<len(strings)):
		bottomlistbox.insert(END,strings[i])
		i+=1

	for i in range(0,7+1):
		for j in range(0,7+1):
			blockslist[i][j].draw()
	displayChanceBoard(chance)



def displayChanceBoard(chance):
	if chance=="top":
		topturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="SpringGreen4")
		topturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="It's your turn",font=("Verdana bold",int(blocksize/4)))
		bottomturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="gold3")
		bottomturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="Wait for your turn",font=("Verdana bold",int(blocksize/4)))
	if chance=="bottom":
		bottomturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="SpringGreen4")
		bottomturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="It's your turn",font=("Verdana bold",int(blocksize/4)))
		topturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="gold3")
		topturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="Wait for your turn",font=("Verdana bold",int(blocksize/4)))





color=0
blockslist=[[block() for  x in range(0,8)] for y in range(0,8)]
for i in range(0,8):
	if color==0:color=1
	else: color=0
	for j in range(0,8):
		if color==1:
			blockslist[i][j]=block(i,j,"seagreen")
			color=0
		else:
			blockslist[i][j]=block(i,j,"lavender")
			color=1

for i in range(0,8):
	blockslist[i][1].piece=piece(green,"pawn","top")
for i in range(0,8):
	blockslist[i][6].piece=piece(red,"pawn","bottom")


blockslist[0][0].piece=piece(green,"rook","top")
blockslist[7][0].piece=piece(green,"rook","top")
blockslist[0][7].piece=piece(green,"rook","bottom")
blockslist[7][7].piece=piece(green,"rook","bottom")

blockslist[1][0].piece=piece(green,"knight","top")
blockslist[6][0].piece=piece(green,"knight","top")
blockslist[1][7].piece=piece(green,"knight","bottom")
blockslist[6][7].piece=piece(green,"knight","bottom")


blockslist[2][0].piece=piece(green,"bishop","top")
blockslist[5][0].piece=piece(green,"bishop","top")
blockslist[2][7].piece=piece(green,"bishop","bottom")
blockslist[5][7].piece=piece(green,"bishop","bottom")

blockslist[3][0].piece=piece(green,"queen","top")
blockslist[3][7].piece=piece(green,"queen","bottom")
blockslist[4][0].piece=piece(green,"king","top")
blockslist[4][7].piece=piece(green,"king","bottom")



selected=None
chance="bottom"
moveToSend='nothing'

#def getMoveString(currentx,currenty,destx,desty,piece,capture=False):
#	piecetype=''
#	captureString=''
#	if capture==True:captureString='x'
#	if piece.oftype=="king":
#		piecetype="K"
#	if piece.oftype=="rook":
#		piecetype="R"
#	if piece.oftype=="knight":
#		piecetype="N"
#	if piece.oftype=="pawn":
#		piecetype="P"
#	if piece.oftype=="bishop":
#		piecetype="B"
#	if piece.oftype=="queen":
#		piecetype="Q"
#	return piecetype+letters[currentx]+str(currenty+1)+captureString+letters[destx]+str(desty+1)


def getMoveString(currentx,currenty,destx,desty,piece,capture=False):
	piecetype=''
	captureString=''
	currentfile=letters[currentx]
	destinationfile=letters[destx]
	currentrank=str(8-currenty)
	destinationrank=str(8-desty)
	if capture==True:captureString='x'
	if piece.oftype=="king":
		piecetype="K"
	if piece.oftype=="rook":
		piecetype="R"
	if piece.oftype=="knight":
		piecetype="N"
	if piece.oftype=="pawn":
		piecetype=""
		if capture==True:
			currentrank=''
		else:
			currentrank=''
			currentfile=''

	if piece.oftype=="bishop":
		piecetype="B"
		if capture==True:
			currentrank=''
			currentfile=''
	if piece.oftype=="queen":
		piecetype="Q"
		currentrank=''
		currentfile=''

	return piecetype+currentfile+currentrank+captureString+destinationfile+destinationrank

def checkForCheckmate():
		global chance,me
		for i in range(0,7+1):
			for j in range(0,7+1):
				if blockslist[i][j].piece!=None:
					if blockslist[i][j].piece.oftype=="king" and blockslist[i][j].piece.team!=chance:
						king=blockslist[i][j].piece
						kxpos,kypos=i,j
		check=False
		totalOppMoves=[]
		for i in range(0,7+1):
			for j in range(0,7+1):
				if blockslist[i][j].piece!=None:
					if blockslist[i][j].piece.team==chance:
						oppMoves=blockslist[i][j].piece.calculateMoves(i,j)
						totalOppMoves+=oppMoves
						for each in oppMoves:
							if each[0]==kxpos and each[1]==kypos:
								if chance=="top":attackBy="bottom"
								else: attackBy="top"
								if checkIfUnderAttack(i,j,attackBy)==False:
									threatx,threaty=i,j
									check=True
		if check==False:return False
		blockable=False
		threatMoves=blockslist[threatx][threaty].piece.calculateMoves(threatx,threaty)
		threatPath=[]
		kingRelPos=''#King's relative position to threat
		if kypos<threaty:kingRelPos+="top"
		if kypos==threaty :pass
		if kypos>threaty :kingRelPos+="bottom"
		if kxpos<threatx:kingRelPos+="left"
		if kxpos==threatx :pass
		if kxpos>threatx :kingRelPos+="right"

		for each in threatMoves:
			if kingRelPos=="top":
				if each[0]==kxpos and each[1]<threaty and each[1]!=kypos:
					threatPath.append(each)
			if kingRelPos=="topleft":
				if each[0]<threatx and each[0]!=kxpos and each[1]<threaty:
					threatPath.append(each)
			if kingRelPos=="topright":
				if each[0]>threatx and each[0]!=kxpos and each[1]<threaty:
					threatPath.append(each)
			if kingRelPos=="left":
				if each[1]==kypos and each[0]!=kxpos and each[0]<threatx:
					threatPath.append(each)
			if kingRelPos=="right":
				if each[1]==kypos and each[0]!=kxpos and each[0]>threatx:
					threatPath.append(each)
			if kingRelPos=="bottomright":
				if each[1]>threaty and each[0]>threatx and each[0]!=kxpos:
					threatPath.append(each)
			if kingRelPos=="bottomleft":
				if each[1]>threaty and each[0]<threatx and each[0]!=kxpos:
					threatPath.append(each)
			if kingRelPos=="bottom":
				if each[1]>threaty and each[0]==kxpos and each[1]!=kypos:
					threatPath.append(each)

		totalMyMoves=[]
		for i in range(0,7+1):
			for j in range(0,7+1):
				if blockslist[i][j].piece!=None:
					if blockslist[i][j].piece.team!=chance and blockslist[i][j].piece.oftype!="king":
						myMoves=blockslist[i][j].piece.calculateMoves(i,j)
						totalMyMoves+=myMoves

		for each in totalMyMoves:
			for compareTo in threatPath:
				if each[0]==compareTo[0] and each[1]==compareTo[1]:
					blockable=True
					break
		if blockable==True and blockslist[threatx][threaty].piece.oftype!="knight":check=False

		if check==False:return False
		kingMoves=king.calculateMoves(kxpos,kypos)
		if len(kingMoves)==0:
			return True#All possible moves are under attack
		return False






def moveAccToString(move):
	global chance
	print("move acc to string:"+move)
	selfxpos,selfypos,destxpos,destypos=move.split(',')
	selfxpos=int(selfxpos)
	selfypos=int(selfypos)
	destxpos=int(destxpos)
	destypos=int(destypos)
	capture=False
	piece=blockslist[selfxpos][selfypos].piece
	blockslist[selfxpos][selfypos].piece.firstMove=False
	if blockslist[destxpos][destypos].piece==None:
		blockslist[destxpos][destypos].piece=self=blockslist[selfxpos][selfypos].piece
		blockslist[selfxpos][selfypos].piece=None
	else:
		capture=True
		if blockslist[destxpos][destypos].piece.oftype=="king":
			if blockslist[destxpos][destypos].piece.team=="bottom":
				print("Top wins")
			else:
				print("Bottom wins")
		blockslist[destxpos][destypos].piece=blockslist[selfxpos][selfypos].piece
		blockslist[selfxpos][selfypos].piece=None
	if chance=="top":chance="bottom"
	else: chance="top"
	canvas.delete(ALL)
	for x in range(0,8):#############################DON'T forget to delete all canvas elements-DONE
		for y in range(0,8):
			blockslist[x][y].draw()
	topturncanvas.delete(ALL)
	bottomturncanvas.delete(ALL)
	displayChanceBoard(chance)
	if me=="top":bottomlistbox.insert(END,getMoveString(selfxpos,selfypos,destxpos,destypos,piece,capture))
	else: toplistbox.insert(END,getMoveString(selfxpos,selfypos,destxpos,destypos,piece,capture))


def boardAction(event):
				global chance,selected,moveToSend,me
				if me!=chance:return
				moves=[]
				somethingMoved=False
				x,y=event.x,event.y
				xpos,ypos=int(x/blocksize),int(y/blocksize)
				if(xpos>7 or ypos>7):return
				if checkForCheckmate():
					print("Check Mate")
				if blockslist[xpos][ypos].piece!=None and blockslist[xpos][ypos].piece.team!=chance:
					if blockslist[xpos][ypos].isHighlighted==False:
						pass
					if blockslist[xpos][ypos].isHighlighted==True:
						#SOME CODEEEEEE to Move the piece
						if selected.piece.team=="top":
							toplistbox.insert(END,getMoveString(selected.xpos,selected.ypos,xpos,ypos,selected.piece,True))
						else:
							bottomlistbox.insert(END,getMoveString(selected.xpos,selected.ypos,xpos,ypos,selected.piece,True))
						selected.piece.move(selected.xpos,selected.ypos,xpos,ypos)
						moveToSend=str(selected.xpos)+","+str(selected.ypos)+","+str(xpos)+","+str(ypos)
						print("String prepared,not yet sent:"+moveToSend)
						selected=None
						if chance=="bottom":chance="top"
						else: chance="bottom"
						for x in range(0,8):
							for y in range(0,8):
								blockslist[x][y].isHighlighted=False
						del moves[:]
				elif(selected==None):
					if blockslist[xpos][ypos].piece!=None:
						selected=blockslist[xpos][ypos]
						for x in range(0,8):
							for y in range(0,8):
								blockslist[x][y].isHighlighted=False
						moves=blockslist[xpos][ypos].piece.calculateMoves(xpos,ypos)
						#CODE TO SET HIGHLIGHTED TRUE
						for each in moves:
							blockslist[each[0]][each[1]].isHighlighted=True
				else:

					if blockslist[xpos][ypos].isHighlighted==True:
						#SOME CODEEEEEE to Move the piece
						if selected.piece.team=="top":
							toplistbox.insert(END,getMoveString(selected.xpos,selected.ypos,xpos,ypos,selected.piece))
						else:
							bottomlistbox.insert(END,getMoveString(selected.xpos,selected.ypos,xpos,ypos,selected.piece))
						selected.piece.move(selected.xpos,selected.ypos,xpos,ypos)
						moveToSend=str(selected.xpos)+","+str(selected.ypos)+","+str(xpos)+","+str(ypos)
						print("String prepared not sent"+moveToSend)
						selected=None
						if chance=="bottom":chance="top"
						else: chance="bottom"
						for x in range(0,8):
							for y in range(0,8):
								blockslist[x][y].isHighlighted=False
						del moves[:]

					else:
						if blockslist[xpos][ypos].piece==None:
							del moves[:]
							for x in range(0,8):
								for y in range(0,8):
									blockslist[x][y].isHighlighted=False
							selected=None
						else:#Piece is not none and not a move
							selected=blockslist[xpos][ypos]
							for x in range(0,8):
								for y in range(0,8):
									blockslist[x][y].isHighlighted=False
							moves=blockslist[xpos][ypos].piece.calculateMoves(xpos,ypos)
							#CODE TO SET HIGHLIGHTED TRUE
							for each in moves:
								blockslist[each[0]][each[1]].isHighlighted=True



				#Coding related to displaying pieces and blocks
				canvas.delete(ALL)
				for x in range(0,8):#############################DON'T forget to delete all canvas elements-DONE
					for y in range(0,8):
						blockslist[x][y].draw()
				topturncanvas.delete(ALL)
				bottomturncanvas.delete(ALL)
				displayChanceBoard(chance)




######################################################


letters=['a','b','c','d','e','f','g','h']
for i in range(0,7+1):
	topstrip.create_text(((i*blocksize)+blocksize/2,topstripheight/2),text=letters[i])

for i in range(0,7+1):
	leftstrip.create_text((leftstripwidth/2,int(i*blocksize)+blocksize/2),text=str(8-i))



listboxwidth=int(blocksize*0.75)
listboxheight=int(blocksize*1.25)
listboxxpos=int(leftstripwidth+display_width+(blocksize*2.5))

toplistboxscrollbar=Scrollbar(root)
toplistboxscrollbar.pack(side=RIGHT,fill=Y)
toplistboxscrollbar.place(x=listboxxpos+listboxwidth,y=int(display_height/4),width=20,height=listboxheight)
toplistbox=Listbox(root,yscrollcommand=toplistboxscrollbar.set)
toplistbox.pack()
toplistbox.place(x=listboxxpos,y=int(display_height/4),width=listboxwidth,height=listboxheight)
toplistboxscrollbar.config(command=toplistbox.yview)

bottomlistboxscrollbar=Scrollbar(root)
bottomlistboxscrollbar.pack(side=RIGHT,fill=Y)
bottomlistboxscrollbar.place(x=listboxxpos+listboxwidth,y=int(display_height*3/4),width=20,height=listboxheight)
bottomlistbox=Listbox(root)
bottomlistbox.pack()
bottomlistbox.place(x=listboxxpos,y=int(display_height*3/4),width=int(blocksize*0.75),height=listboxheight)
bottomlistboxscrollbar.config(command=bottomlistbox.yview)


topturncanvas=Canvas(root,width=int(blocksize*2),height=int(blocksize))
topturncanvas.pack()
topturncanvas.place(x=int(listboxxpos-(blocksize*2)-blocksize/4),y=int(display_height/4))
topturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="gold3")
topturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="Wait for your turn",font=("Verdana bold",int(blocksize/4)))

bottomturncanvas=Canvas(root,width=int(blocksize*2),height=int(blocksize))
bottomturncanvas.pack()
bottomturncanvas.place(x=int(listboxxpos-(blocksize*2)-blocksize/4),y=int(display_height*3/4))
bottomturncanvas.create_rectangle(0,0,int(blocksize*2),int(blocksize),fill="SpringGreen4")
bottomturncanvas.create_text((blocksize,int(blocksize/2)),width=int(blocksize*2),text="It's your turn!",font=("Verdana bold",int(blocksize/4)))

player1Label=Label(root,text="Player 1",fg="darkgreen",font=("Verdana bold",int(blocksize/4)))
player1Label.pack()
player1Label.place(x=int(listboxxpos-(blocksize*2)-blocksize/4),y=int((display_height/4)-(blocksize/2)))
topmoveslabel=Label(root,text="Moves History",font=("Verdana bold",int(blocksize/9)))
topmoveslabel.pack()
topmoveslabel.place(x=listboxxpos,y=int((display_height/4)-(blocksize/5)))

player2Label=Label(root,text="Player 2",fg="darkgreen",font=("Verdana bold",int(blocksize/4)))
player2Label.pack()
player2Label.place(x=int(listboxxpos-(blocksize*2)-blocksize/4),y=int((display_height*3/4)-(blocksize/2)))
bottommoveslabel=Label(root,text="Moves History",font=("Verdana bold",int(blocksize/9)))
bottommoveslabel.pack()
bottommoveslabel.place(x=listboxxpos,y=int((display_height*3/4)-(blocksize/5)))

saveButton=Button(root,text="save",command=saveGame)
saveButton.pack()
saveButton.place(x=display_width+int(blocksize*2),y=10)
loadButton=Button(root,text="load",command=loadGame)
loadButton.pack()
loadButton.place(x=display_width+int(blocksize*3),y=10)


for x in range(0,8):#############################DON'T forget to delete all canvas elements-DONE
	for y in range(0,8):
		blockslist[x][y].draw()

canvas.bind("<Button-1>",boardAction)


s=socket.socket()
port=12345
s.connect(('127.0.0.1',port))

request="connection"
s.send(request.encode())
me=s.recv(1024)
print("me=="+me.decode())
me=me.decode()
chance=s.recv(1024)
print("chance=="+chance.decode())
chance=chance.decode()
serverChance=chance

def checkOppResponse():
	global chance,moveToSend,serverChance
	if serverChance==me:
		if moveToSend=="nothing":
			#print("Sent :nothing")
			s.sendall("nothing".encode())
		else:
			s.sendall(("move:"+moveToSend).encode())
			print("Move sent :"+moveToSend)
			moveToSend="nothing"
			if serverChance=="top":serverChance="bottom"
			else: serverChance="top"
	else:
		data=s.recv(1024)
		data=data.decode()
		if data=="nothing" or data=="nothingnothing":
			pass
			#print("Recieved :"+data)
		elif (data.split(":")[0]=="move"):
			#print("Recieved :"+data)
			moveAccToString((data.split(':'))[1])
			serverChance=me
	root.after(50,checkOppResponse)


root.after(50,checkOppResponse)
root.mainloop()
