$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$('#myTabs a:first').tab('show') // Select first tab
$('#myTabs a:second').tab('show') // Select first tab
$('#myTabs a:third').tab('show') // Select first tab
$('#myTabs a:fourth').tab('show') // Select first tab
