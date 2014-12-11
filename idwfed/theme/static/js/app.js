$(document).foundation();
$(document).ready(function() {    
	$("#nav-about").on("click", function(){
		$("#about-nav").slideToggle();
		$(this).toggleClass("active");
	});
});