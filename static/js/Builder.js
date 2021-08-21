window.addEventListener("DOMContentLoaded",function(){
    get_project_template("de")
})


//Load Template 
//This function loads clients template
function get_project_template(id){
    //compiled url 
    var template_compiled_url = "/builder/get-project-template/KPTNDRRKNP2GIT72QZFFLF96FM42GU06.html/"
    
    //view to add
    var preview_page = document.getElementById("preview-page")

    //send an http request using a function in (cummunications.js)
    POST_REQUEST(template_compiled_url, null, function(response) {
        setTimeout(function(){
            preview_page.innerHTML = response
        },1000)
        
    })
}