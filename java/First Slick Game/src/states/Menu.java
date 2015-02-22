package states;

import org.lwjgl.input.Mouse;
import org.newdawn.slick.*;
import org.newdawn.slick.gui.*;
import org.newdawn.slick.state.*;

public class Menu extends BasicGameState {
	
	MouseOverArea play;
	MouseOverArea exit;
	String p;
	private int state;
	
	public Menu(int state) {
		this.state = state;
	}

	@Override
	public void init(GameContainer gc, StateBasedGame sbg)
			throws SlickException {
		//SpriteSheet ss = new SpriteSheet("res/buttons/menuSet.png", 140, 50);
		//play = new MouseOverArea(gc, ss.getSubImage(0, 0), 50, 100);
		//exit = new MouseOverArea(gc, ss.getSubImage(0, 2), 50, 175);
		play = new MouseOverArea(gc, new Image("res/buttons/2/play.png"), 50, 640);
		exit = new MouseOverArea(gc, new Image("res/buttons/2/exit.png"), 200, 640);
		//play.setMouseDownImage(ss.getSubImage(0, 1));
		//exit.setMouseDownImage(ss.getSubImage(0, 3));
		play.setMouseDownImage(new Image("res/buttons/2/playPressed.png"));
		exit.setMouseDownImage(new Image("res/buttons/2/exitPressed.png"));
		p = "No input yet...";
	}

	@Override
	public void render(GameContainer gc, StateBasedGame sbg, Graphics g)
			throws SlickException {
		g.setAntiAlias(true);
		g.drawImage(new Image("/res/screen.jpg"), 0, 0);
		play.render(gc, g);
		exit.render(gc, g);
		
		g.drawString(p, 50, 50);
	}

	@Override
	public void update(GameContainer gc, StateBasedGame sbg, int delta)
			throws SlickException {
		play.setInput(gc.getInput());
		exit.setInput(gc.getInput());
		
		if (gc.getInput().isKeyPressed(Input.KEY_ESCAPE)) {
			System.exit(0);
		} else if (gc.getInput().isKeyPressed(Input.KEY_P)) {
			sbg.enterState(game.Game.PLAY);
		}
		
		if (play.isMouseOver()) {
			p = "mouse over play!";
			if (Mouse.isButtonDown(0)) {
				sbg.enterState(game.Game.PLAY);
			}
		} else if (exit.isMouseOver()) {
			p = "mouse over exit!";
			if (Mouse.isButtonDown(0)) {
				System.exit(0);
			}
		} else {
			p = "No input";
		}
		
	}

	@Override
	public int getID() {
		return state;
	}
}
