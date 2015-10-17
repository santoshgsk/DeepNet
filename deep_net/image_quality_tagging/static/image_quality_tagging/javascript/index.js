function validateAndSubmit() {
    console.log("Hello World")
    var img_wall_checked = jQuery("input[name=img_wall]:checked").val();
    var img_spacious_checked = jQuery("input[name=img_spacious]:checked").val();
    var img_cleanliness_checked = jQuery("input[name=img_cleanliness]:checked").val();
    var img_windows_size_checked = jQuery("input[name=img_windows_size]:checked").val();
    var img_flat_overall_checked = jQuery("input[name=img_flat_overall]:checked").val();

    if(!img_wall_checked){
        alert('Please select option for question 1');
    }
    else if(!img_spacious_checked){
        alert('Please select option for question 2');
    }
    else if(!img_cleanliness_checked){
        alert('Please select option for question 3');
    }
    else if(!img_windows_size_checked){
        alert('Please select option for question 4');
    }
    else if(!img_flat_overall_checked){
        alert('Please select option for question 5');
    }
    if(img_wall_checked && img_spacious_checked && img_cleanliness_checked && img_windows_size_checked && img_flat_overall_checked){
        document.getElementById("image_upload_form").submit();
    }
}
