$(document).ready(function(){
  setTimeout(function(){
    $.ajax({
      url:"/ajax",
      type: "GET",
      success: function(data){
        $("#html_string").html(data.template)

        $.ajax({
          url:"/vj10ajax01",
          type: "GET",
          success: function(data){
            button = null;// get button froma data

            button.bind({
              click: function(){
                $.ajax({
                  url: "/vj10ajax02",
                  type: "GET",
                  success: function(data){
                    // ispis podataka (dob, visina, mjesto rodjenja)
                  },
                  error: function(xhr, errmessage, err){
                    console.log(errmessage);
                  }
                });
              }
            });
          },
          error: function(xhr, errmessage, err){
            console.log(errmessage);
          }
        });
      },
      error: function(xhr, errmessage, err){
        console.log(errmessage);
      }
    });
  }, 2000);

});
