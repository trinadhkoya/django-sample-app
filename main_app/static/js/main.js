/**
 * Created by trinadhkoya on 15/03/17.
 */

$('button').on('click', function (event) {
    console.log("entered");
    event.preventDefault();
    console.log("what's inside");
    var element = $(this);
    console.log(element)

    $.ajax({
        url: '/like_treasure/',
        type: 'GET',
        data: {treasure_id: element.attr("data-id")},
        success: function (response) {
            console.log(response)
            element.html(' ' + response);
        }

    });

    console.log("END");
});