package order;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class OrderedIntListUtility {
	public static OrderedIntList common(OrderedIntList... lists) {
		List<Integer> commonList = new ArrayList<Integer>(lists[0].getList());
		for (OrderedIntList list: lists) {
			commonList.retainAll(new HashSet<Integer>(list.getList()));
		}
		Integer[] commonArray = new Integer[commonList.size()];
		commonList.toArray(commonArray);
		return new OrderedIntList(commonArray);
	}
	
	public static void main(String[] args) {
		OrderedIntList list1 = new OrderedIntList(1, 3, 4, 5);
		OrderedIntList list2 = new OrderedIntList(10, 3, 4, 5);
		OrderedIntList list3 = new OrderedIntList(1, 3, 40, 5);
		OrderedIntList commonList = common(list1, list2, list3);
		System.out.printf("nums: %s%n", commonList.getList());
	}
}
