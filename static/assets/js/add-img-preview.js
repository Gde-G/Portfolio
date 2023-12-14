$(function () {
    $(document).on("change", ".upload-img", function () {
        var uploadFile = $(this);
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

        if (/^image/.test(files[0].type)) { // only image file
            var reader = new FileReader(); // instance of the FileReader
            reader.readAsDataURL(files[0]); // read the local file

            reader.onloadend = function () { // set image data as background of div
                //alert(uploadFile.closest(".upimage").find('.imagePreview').length);
                uploadFile.closest(".testi-img-portada").find('.testi-img-preview-portada').css("background-image", "url(" + this.result + ")");
                uploadFile.closest(".testi-img-portada").find('.testi-img-portada-border').css("display", "none");
            }
        }

    });
});

$(function () {
    $(document).on("change", ".upload-img", function () {
        
        var uploadFile = $(this);
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

        if (/^image/.test(files[0].type)) { // only image file
            var reader = new FileReader(); // instance of the FileReader
            reader.readAsDataURL(files[0]); // read the local file
            
            reader.onloadend = function () { // set image data as background of div
                //alert(uploadFile.closest(".upimage").find('.imagePreview').length);
                console.log(reader.result)
                uploadFile.closest(".project-img-portada").find('.project-img-preview-portada').css("background-image", "url(" + this.result + ")");
                uploadFile.closest(".project-img-portada").find('.project-img-portada-border').css("display", "none");
            }
        }

    });
});