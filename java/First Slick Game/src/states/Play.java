package states;

import org.newdawn.slick.*;
import org.newdawn.slick.state.*;
import org.newdawn.slick.tiled.TiledMap;
import org.newdawn.slick.geom.*;

public class Play extends BasicGameState {
	
	Image i;
	private TiledMap map;
	private int updateCounter = 0;
	private int[] originalTileID = new int[16];
	float posX = 0, posY = 0;
	Point center;
	Point cTile;
	int mouseX, mouseY;
	int state;
	int xRend, yRend;
	int rendSkip;
	Animation goingRight, goingLeft, goingUp, goingDown, a;
	private Rectangle r;
	
	public Play(int state) {
		this.state = state;
	}

	@Override
	public void init(GameContainer gc, StateBasedGame sbg)
			throws SlickException {
		i = new Image(this.getClass().getResourceAsStream("/res/alien.png"), "alien", false);
		map = new TiledMap("res/testRes.tmx", "res");
		center = new Point(gc.getWidth()/2, gc.getHeight()/2);
		cTile = new Point(center.getX()/32, center.getY()/32);
		/*pokemon char
		SpriteSheet s = new SpriteSheet("res/bHNorm.png", 96/3, 128/4);
		 
		a = new Animation(s, 150);
		a.setAutoUpdate(false);
		a.setCurrentFrame(3);
		
		goingUp = new Animation(s, 0,0,2,0, true, 150, false);
		goingDown = new Animation(s, 0,1,2,1, true, 150, false);
		goingLeft = new Animation(s, 0,2,2,2, true, 150, false);
		goingRight = new Animation(s, 0,3,2,3, true, 150, false);
		**/

		SpriteSheet s = new SpriteSheet("res/hero.png", 64, 64);
		a = new Animation(s, 150);
		a.setAutoUpdate(false);
		a.setCurrentFrame(17);
		
		goingUp = new Animation(s, 0,0,8,0, true, 150, false);
		goingDown = new Animation(s, 0,2,8,2, true, 150, false);
		goingLeft = new Animation(s, 0,1,8,1, true, 150, false);
		goingRight = new Animation(s, 0,3,8,3, true, 150, false);
		
		xRend = 300;
		yRend = -100;
		
		rendSkip=0;
		
		for (int i = 0; i < originalTileID.length; i++) {
			switch (i/4) {
			case 0: originalTileID[i] = 777 + i%4; break;
			case 1: originalTileID[i] = 777 + 64 + i%4; break;
			case 2: originalTileID[i] = 777 + 128 + i%4; break;
			case 3: originalTileID[i] = 777 + 192 + i%4; break;
			}
		}
		cTile.setY((int)((center.getY()-yRend)/32));
		cTile.setX((int)((center.getX()-xRend)/32));
		
		r = new Rectangle(center.getX()-32, center.getY()-32, 64, 64);
		
	}

	@Override
	public void render(GameContainer gc, StateBasedGame sbg, Graphics g)
			throws SlickException {
		
		map.render(xRend, yRend, 0);
		map.render(xRend, yRend, 1);
		//g.drawRect((center.getX()-a.getWidth()/2), (center.getY()-a.getHeight()/2), 32, 32);
		g.draw(r);
		g.drawAnimation(a, (center.getX()-a.getWidth()/2), (center.getY()-a.getHeight()/2));
		map.render(xRend, yRend, 2);
		map.render(xRend, yRend, 3);
		map.render(xRend, yRend, 4);
		map.render(xRend, yRend, 5);
		
		g.resetTransform();

		g.drawString("Point (x, y): ", 50, 50);
		g.drawString("Camera (x, y): ", 41, 75);
		g.drawString("Pos (x, y): ", 68, 100);
		g.drawString("(" + mouseX + "," + mouseY + ")", 175, 50);
		g.drawString("(" + xRend + "," + yRend + ")", 175, 75);
		g.drawString(map.getTileId((int) cTile.getX(), (int) cTile.getY(), 5)+"", 200, 175);
		g.drawString("(" + (int)cTile.getX() + "," + (int)cTile.getY() + ")", 175, 100);
		//map.render(1400, 0);
		
		
	}

	@Override
	public void update(GameContainer gc, StateBasedGame sbg, int delta)
			throws SlickException {
		mouseX = gc.getInput().getAbsoluteMouseX();
		mouseY = gc.getInput().getAbsoluteMouseY();
		int collisionID = map.getTileId((int)cTile.getX(), (int)cTile.getY(), 5);
		boolean collided = collisionID == 5317;
		
		if (gc.getInput().isKeyPressed(Input.KEY_ESCAPE)) {
			sbg.enterState(game.Game.MENU);
		}
		
		int nRendSkip = 2;
		if (gc.getInput().isKeyDown(Input.KEY_DOWN)) {
			a=goingDown;
			a.update(delta);
			collisionID = map.getTileId((int)cTile.getX(), (int)(center.getY()-(yRend-delta))/32, 6);
			collided = collisionID == 5317;
			if (rendSkip == 0) {
				yRend-=delta;
				cTile.setY((int)((center.getY()-yRend)/32));			 
				while (collided) {
					yRend+=delta*2;
					cTile.setY((int)((center.getY()-yRend)/32));
					collisionID = map.getTileId((int)cTile.getX(), (int)(center.getY()-(yRend-delta))/32, 6);
					collided = collisionID == 5317;
				}
			} else if (rendSkip > nRendSkip) {
				rendSkip = -1;
			}
			rendSkip++;
		} else if (gc.getInput().isKeyDown(Input.KEY_UP)) {
			a=goingUp;
			a.update(delta);
			collisionID = map.getTileId((int)cTile.getX(), (int)(center.getY()-(yRend+delta))/32, 6);
			collided = collisionID == 5317;
			if (rendSkip == 0) {
				yRend+=delta;
				cTile.setY((int)((center.getY()-yRend)/32)); 
				while (collided) {
					yRend-=delta*2;
					cTile.setY((int)((center.getY()-yRend)/32));
					collisionID = map.getTileId((int)cTile.getX(), (int)(center.getY()-(yRend+delta))/32, 6);
					collided = collisionID == 5317;
				}
			} else if (rendSkip > nRendSkip) {
				rendSkip = -1;
			}
			rendSkip++;
		} else if (gc.getInput().isKeyDown(Input.KEY_LEFT)) {
			a=goingLeft;
			a.update(delta);
			collisionID = map.getTileId((int)(center.getX()-(xRend+delta))/32, (int)cTile.getY(), 6);
			collided = collisionID == 5317;
			if (rendSkip == 0) {
				xRend+=delta;
				cTile.setX((int)((center.getX()-xRend)/32));
				while (collided) {
					xRend-=delta*2;
					cTile.setX((int)((center.getX()-xRend)/32));
					collisionID = map.getTileId((int)(center.getX()-(xRend+delta))/32, (int)cTile.getY(), 6);
					collided = collisionID == 5317;
				}
			} else if (rendSkip > nRendSkip) {
				rendSkip = -1;
			}
			rendSkip++;
		} else if (gc.getInput().isKeyDown(Input.KEY_RIGHT)) {
			a=goingRight;
			a.update(delta);
			collisionID = map.getTileId((int)(center.getX()-(xRend-delta))/32, (int)cTile.getY(), 6);
			collided = collisionID == 5317;
			if (rendSkip == 0) {
				xRend-=delta;
				cTile.setX((int)((center.getX()-xRend)/32));
				while (collided) {
					xRend+=delta*2;
					cTile.setX((int)((center.getX()-xRend)/32));
					collisionID = map.getTileId((int)(center.getX()-(xRend-delta))/32, (int)cTile.getY(), 6);
					collided = collisionID == 5317;
				}
			} else if (rendSkip > nRendSkip) {
				rendSkip = -1;
			}
			rendSkip++;
		} else if(gc.getInput().isKeyPressed(Input.KEY_C)) {
			sbg.mouseClicked(0, (int)center.getX(), (int)center.getY(), 0);
		} else {			
			a.setCurrentFrame(0);
		}
		
		updateCounter += delta;
		if (updateCounter > 1000) {
			// swap the tile every second
			updateCounter -= 1000;
			int currentTileID = map.getTileId(23, 15, 0);
			if (currentTileID != originalTileID[0]) {
				for (int i = 0; i < originalTileID.length; i++) {
					map.setTileId(23+i%4, 15+i/4, 0, originalTileID[i]);
				}
			}
			else {
				for (int i = 0; i < originalTileID.length; i++) {
					map.setTileId(23+i%4, 15+i/4, 0, originalTileID[i] - 4);
				}
			}
		}
	}

	@Override
	public int getID() {
		return state;
	}
}
