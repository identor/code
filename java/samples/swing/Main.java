import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;

import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Component;

class Main extends JFrame implements ActionListener {
	JButton[] buttons;

	Main(String name) {
		this.setSize(400, 100);
		this.setLayout(new FlowLayout());
		this.add(new JLabel("Hello: " + name));
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		this.buttons = new JButton[5];

		buttons[0] = new JButton("1");
		buttons[1] = new JButton("2");
		buttons[2] = new JButton("3");
		buttons[3] = new JButton("4");
		buttons[4] = new JButton("5");

		for (int i = 0; i < buttons.length; i++) {
			this.add(buttons[i]);
			buttons[i].addActionListener(this);
		}
	}

	public static void main(String[] args) {
		Main main = new Main("Irvin");
		main.show();
	}

	@Override
	public void actionPerformed(ActionEvent evt) {
		if (buttons[0] == evt.getSource()) {
			System.out.println("Hello");
		}

		if (buttons[1] == evt.getSource()) {
			System.out.println("Hello");
		}

		if (buttons[2] == evt.getSource()) {
			System.out.println("Hello");
		}

		if (buttons[3] == evt.getSource()) {
			System.out.println("Hello");
		}

		if (buttons[4] == evt.getSource()) {
			System.out.println("Hello");
		}
	}
}