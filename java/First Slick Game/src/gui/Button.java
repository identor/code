package gui;

import org.newdawn.slick.Image;
import org.newdawn.slick.geom.Shape;
import org.newdawn.slick.gui.ComponentListener;
import org.newdawn.slick.gui.GUIContext;
import org.newdawn.slick.gui.MouseOverArea;

public class Button extends MouseOverArea {

	public Button(GUIContext container, Image image, int x, int y) {
		super(container, image, x, y);
		// TODO Auto-generated constructor stub
	}
	
	public Button(GUIContext container, Image image, int x, int y, ComponentListener listener) {
		super(container, image, x, y, listener);
	}
	
	public Button(GUIContext container, Image image, int x, int y, int width, int height)  {
		super(container, image, x, y, width, height);
	}
	
	public Button(GUIContext container, Image image, int x, int y, int width, int height, ComponentListener listener) {
		super(container, image, x, y, width, height);
	}
	
	public Button(GUIContext container, Image image, Shape shape) {
		super(container, image, shape);
	}

}
