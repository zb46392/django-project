$(document).ready(function(){
  $.post('', {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
    function(data){
      var body = $(document.body);
      var img = $("<img>", {
        src: data.yapi.imageUrl
      });

      var title = $("<p>", {class: 'text-center'}).append(data.yapi.title);

      var table = $("<table>", {
        class: "table table-striped table-bordered"
      });
      var tableHead = $("<thead>");
      tableHead.append($("<th>").append("Date"));
      tableHead.append($("<th>").append("Day"));
      tableHead.append($("<th>").append("Weather"));
      var tableBody = $("<tbody>");

      $.each(data.yapi.forecast, function(index, f){
        var tableRow = $("<tr>");
        tableRow.append($("<td>").append(f.date));
        tableRow.append($("<td>").append(f.day));
        tableRow.append($("<td>").append(f.text));
        tableBody.append(tableRow);
      });

      table.append(tableHead);
      table.append(tableBody);
      
      body.append(img);
      body.append(title);
      body.append(table);
    });
});
