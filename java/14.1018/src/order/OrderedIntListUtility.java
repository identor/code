package order;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

public class OrderedIntListUtility {
	private static OrderedIntList toOrderedIntList(Collection<Integer> collection) {
		Integer[] array = new Integer[collection.size()];
		collection.toArray(array);
		return new OrderedIntList(array);
	}

	public static OrderedIntList common(OrderedIntList... lists) {
		HashSet<Integer> commonList = new HashSet<Integer>(lists[0].getList());
		for (OrderedIntList list: lists) {
			commonList.retainAll(new HashSet<Integer>(list.getList()));
		}
		return toOrderedIntList(commonList);
	}
	
	public static OrderedIntList replaceAll(OrderedIntList list, 
			OrderedIntList sublist, OrderedIntList newList) {
		List<Integer> replaced = new ArrayList<Integer>(list.getList().size());
		replaced.addAll(list.getList());
		replaced.removeAll(sublist.getList());
		replaced.addAll(newList.getList());
		return toOrderedIntList(replaced);
	}
	
	private static int[] toIntArray(Collection<Integer> collection) {
		int[] indices = new int[collection.size()];
		Iterator<Integer> iterator = collection.iterator();
		for (int i = 0; iterator.hasNext(); i++) {
			indices[i] = iterator.next();
		}
		return indices;
	}
	
	public static int[] findSubsequenceIndices(OrderedIntList list,
			OrderedIntList sublist) {
		final int NOT_FOUND = -1;
		HashSet<Integer> set = new HashSet<Integer>();
		for (Integer i: sublist.getList()) {
			for (int j = 0; j < list.getList().size(); j++) {
				int occurence = list.getList().get(j) == i ? j : -1;
				set.add(occurence);
			}
		}
		set.remove(NOT_FOUND);
		return toIntArray(set);
	}
	
	/*
	 * Tests
	 */
	public static void main(String[] args) {
		OrderedIntList list1 = new OrderedIntList(1, 3, 4, 5, 5, 5);
		OrderedIntList list2 = new OrderedIntList(10, 3, 3, 3, 3, 4, 5);
		OrderedIntList list3 = new OrderedIntList(1, 3, 40, 5);
		OrderedIntList list4 = new OrderedIntList(1, 2, 3, 4);
		OrderedIntList list5 = new OrderedIntList(3, 4);
		OrderedIntList list6 = new OrderedIntList(6, 7);
		OrderedIntList commonList = common(list1, list2, list3);
		OrderedIntList replaced = replaceAll(list4, list5, list6);
		int[] subsequence = findSubsequenceIndices(list1, list3); 
		System.out.printf("nums: %s%n", commonList.getList());
		System.out.printf("replaced: %s%n", replaced.getList());
		System.out.printf("indices: %s%n",	Arrays.toString(subsequence));
	}
}
