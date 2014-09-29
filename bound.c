private double bound() { 
	boolean found= false; // Was bound found?I.e.,is last item partial 
	double boundVal= -1; // Value of upper bound 
	int n= items.length; // Number of items in problem 
	newProfit= currProfit; // Set new prof as current prof at this node 
	newWgt= currWgt; 
	ppartItem= k+1;; //// Go to next lower level,, tryy to pput in soln 
	while (partItem < n && !found) { // More items & haven’t found partial
		if (newWgt + items[partItem].weight <= capacity) { // If fits 
			newWgt += items[partItem].weight; // Update new wgt, prof 
			newProfit += items[partItem].profit; // by adding item wgt,prof 
			y[partItem]= 1; // Update curr soln to show item k is in it
		} else { // Current item only fits partially 
			boundVal= newProfit + (capacity – newWgt)*items[partItem].profit/items[partItem].weight;} // C// Compute upper bound bd b asedd on partitial fit
			found= true; b l partItem++; // Go to next item and try to put in sack 
		} if (found) { // If we have fractional soln for last item in sack
			partItem--; // Back up to prev item, which is fully in sack 
			return boundVal; // Return the upper bound 
		} else { 
			return newProfit;// Return profit including last item 
		}
	}