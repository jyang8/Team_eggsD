$('#myTabs a').click(function (e) {
	e.preventDefault()
	    $(this).tab('show')
	    })

    $('#myTabs a[href="#1"]').tab('show') // Select tab by name
