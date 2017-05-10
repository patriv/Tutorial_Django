$(document).ready(function(){

    $("a").click(function(){

        $.ajax(

            {

                url: "hola.txt",

                success: function(result){

                    $("#view").html(result);

                },

                error: function(result){

                    $("#view").html("ERROR");

                }

            });

        });

    });