
function showModal() {
    $("#popup").css("display", "block"); 
}

function hideModal() {
     $("#popup").css("display", "none"); 
}

function init() {
    console.log("List page");

    // hook events 
    $("#btnCreate").click(showModal);
    $(".closePopup").click(hideModal);
}


window.onload = init;