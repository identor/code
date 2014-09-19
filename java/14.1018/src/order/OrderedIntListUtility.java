package order;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;

public class OrderedIntListUtility {
	public static OrderedIntList common(OrderedIntList... lists) {
		HashSet<Integer> commonList = new HashSet<Integer>(lists[0].getList());
		for (OrderedIntList list: lists) {
			commonList.retainAll(new HashSet<Integer>(list.getList()));
		}
		Integer[] commonArray = new Integer[commonList.size()];
		commonList.toArray(commonArray);
		return new OrderedIntList(commonArray);
	}
	
	public static OrderedIntList replaceAll(OrderedIntList list, 
			OrderedIntList sublist, OrderedIntList newList) {
		return list;
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
		OrderedIntList commonList = common(list1, list2, list3);
		int[] subsequence = findSubsequenceIndices(list1, list3); 
		System.out.printf("nums: %s%n", commonList.getList());
		System.out.printf("indices: %s%n",	Arrays.toString(subsequence));
	}
}
