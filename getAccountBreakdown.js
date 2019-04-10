(function getAccountBreakdown() {
	var acct_breakdown = [];
	var status, number;
	var els = document.evaluate("//div[@class[contains(., 'SRTALEAdAccountOverviewWidget')]]//span[text()='Ad Account Statuses']/../../div[2]/div[1]//div[text()='Active' or text()='Disabled' or text()='Inactive']/../../../div[position()>1]", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
	for (i=0;i<els.snapshotLength;i++){
		status = els.snapshotItem(i).children[0].innerText;
		number = els.snapshotItem(i).children[1].innerText;
		acct_breakdown.push([status,number]);
	}
	acct_breakdown.forEach(function(v,i,arr) {
		arr[i][1] = "("+v[1]+")";
		arr[i] = arr[i].join(" ");
	});
	acct_breakdown = acct_breakdown.join(", ");
	alert(acct_breakdown);
})();
