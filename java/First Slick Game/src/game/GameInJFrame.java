package game;

import java.awt.BorderLayout;
import java.io.File;

import javax.swing.JFrame;

import org.lwjgl.LWJGLUtil;
import org.newdawn.slick.CanvasGameContainer;
import org.newdawn.slick.SlickException;

public class GameInJFrame {
	
	public static void main(String[] args) throws SlickException {
		/** 
		 * Setting the properties for LWJGl and 
		 * JInput and as value we added a path to 
		 * the "present working DIR". 
		 **/
		System.setProperty("org.lwjgl.librarypath", 
				new File(new File(System.getProperty("user.dir"), "lib/native"),
				LWJGLUtil.getPlatformName()).getAbsolutePath());
		System.setProperty("net.java.games.input.librarypath",
				System.getProperty("org.lwjgl.librarypath"));
		
		CanvasGameContainer canvas = new CanvasGameContainer(new Game("Game 1"));
		canvas.getContainer().setAlwaysRender(true);
		canvas.setBounds(20, 20, 400, 400);
		JFrame f = new JFrame("With JFrame");
		f.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		//newFrame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		f.setSize(1280, 720);
		f.setLayout(new BorderLayout());
		f.add(canvas, BorderLayout.CENTER);
		f.add(new javax.swing.JLabel("Title"), BorderLayout.NORTH);
		f.setVisible(true);
		canvas.start();
	}
	
	
}
