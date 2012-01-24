$(document).ready(function() {
	$("#Rotator").rotator({
		'items': '.RotatorItem',
		'prev': '#RotatorPrevLink',
		'next': '#RotatorNextLink',
		'visibleCount': 4,
		'changeCount': 2,
		//'hashPrefix': "slide",
		//'autoPlay': true,
		//'easing': "easeOutQuad",
		'keyboardNavigation': true
	});
});