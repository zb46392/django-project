$(document).ready(function(){
  setTimeout(function(){
    $.ajax({
      url:"/vj10",
      type: "GET",
      success: function(data){
        var button = $("<button>").append("Click ME!");
        $("#html_string").html(data.template);
        $("#html_string").append(button);

        button.bind({
          click: function(){
            $.ajax({
              url: "/vj10",
              type: "GET",
              success: function(data){
                var age = "Age: " + data.stan.age;
                var height = "Height: " + data.stan.height;
                var birthplace = "Birthplace: " + data.stan.birthplace;

                $("#html_string").append($("<br>"));
                $("#html_string").append($("<p>").append(age));
                $("#html_string").append($("<br>"));
                $("#html_string").append($("<p>").append(height));
                $("#html_string").append($("<br>"));
                $("#html_string").append($("<p>").append(birthplace));
                $("#html_string").append($("<br>"));
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
  }, 2000);

});
