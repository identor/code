package game;

import org.newdawn.slick.*;
import org.newdawn.slick.state.*;

import states.*;

public class Game extends StateBasedGame {
	
	public static final int MENU = 0;
	public static final int PLAY = 1;
	public static final String TITLE = "Game 1.0.13b";
	
	private Play play;
	private Menu menu;

	public Game(String name) {
		super(name);
		play = new Play(PLAY);
		menu = new Menu(MENU);
	}

	@Override
	public void initStatesList(GameContainer gc) throws SlickException {
		// The first state added will be the initial state to display.
		addState(menu);
		addState(play);
	}

	public static void main(String[] args) {
		AppGameContainer appgc;
		try {			
			Game game = new Game(TITLE);
			appgc = new AppGameContainer(game);
			// can be placed on the constructor new Game(TITLE), 1280, 720, false
			appgc.setDisplayMode(1280, 720, false);
			appgc.setIcons(new String[]{"res/icons/I_16.png", "res/icons/I_32.png"});
			appgc.start();
		} catch (SlickException se) {
			se.printStackTrace();
		}
	}

}
