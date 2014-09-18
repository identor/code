package order;

import java.util.Arrays;
import java.util.List;

public class OrderedIntList {
	private List<Integer> list;
	
	public OrderedIntList(Integer... elements) {
		list = Arrays.asList(elements);
	}
	
	public List<Integer> getList() {
		return this.list;
	}
	
	public static void main(String[] args) {
		OrderedIntList oil = new OrderedIntList(1, 3, 4, 5);
		System.out.printf("class: %s%n", oil.list.getClass());
		System.out.printf("nums: %s%n", oil.list);
	}
}
