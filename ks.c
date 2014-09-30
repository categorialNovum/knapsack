public void knapsack() { 
int n= items.length; // Number of items in problem 
do { // While upper bound < known soln,backtrack
	while (bound() <= solutionProfit) { 
		while (k != 0 && y[k] != 1) // Back up while item k not in sack 
			k--; // to find last object in knapsack 
		if ( k == 0)) //If at root,, we’re done. Return.
			return; 
		y[k]= 0; // Else take k out of soln (R branch) 
		currWgt -= items[k].weight; // Reduce soln wgt by k’s wgt 
		currProfit -= items[k].profit; // Reduce soln profit by k’s prof
	} 			// Back to while(), recompute bound 
	currWgt= newWgt; // Reach here if bound> soln profit 
	currProfit= newProfit; // and we may have new soln. 
	k= partItem; // Set tree level k to last, possibly partial item in greedy solution

	if (k == n) { 				// If we’ve reached leaf node, have 
		solutionProfit= currProfit; // actual soln, not just bound 
		System.arraycopy(y, 0, x, 0, y.length); 	// Copy soln into array x 
		k= n-1; 					// Back up to prev tree level, which may leave solution
	} else // Else not at leaf, just have bound 
		y[k]= 0; // Take last item k out of soln 
	} while (true); // Infinite loop til backtrack to k=0 
}