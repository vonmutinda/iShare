function copyUrl() {
    /* Get the text field */
    var copyText = document.getElementById("link");
  
    /* Select the text field */
    copyUrl.select();
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("image URL copied !");
  }