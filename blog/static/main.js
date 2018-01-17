$(document).ready(() => {

  /* add_like_to_post */

  /* outputSquare Hover */
  jQuery(document).ready(function($) {
    $('.outputSquare').fadeIn(250, "swing");
  })

  /* outputSquare Hover */
  $(document).on('mouseenter', '.singlepost', event => {
    $(event.currentTarget).closest('.singlepost').animate({
      'opacity': '1'
    }, 100);
  })
  $(document).on('mouseleave', '.singlepost', event => {
    $(event.currentTarget).closest('.singlepost').animate({
      'opacity': '0.85'
    }, 100);
  })

  /* NAV BAR SCRIPTS */
  /* PLUS */
  /* Add goal function */
  $('.createList').on('click', () => {
    /*$('.outputSquare').fadeToggle(200, "swing");*/
  })
  /* Animated Nav Link */
  $('.createList').on('mouseenter', () => {
    $('.createList').animate({
      fontSize: '14.3px'
    }, 200);
  })
  $('.createList').on('mouseleave', () => {
    $('.createList').animate({
      fontSize: '14px'
    }, 200);
  })

  /* CROSS */
  /* Remove goal function */
  $('#removePost').on('click', function(e) {
    if (confirm("Are you sure about DELETING your post?")) {
      $('#outputTable').children().remove()
    } else {
      e.preventDefault();
    }
  })
  /* Animated Nav Link */
  $('.removeGoals').on('mouseenter', () => {
    $('.removeGoals').animate({
      fontSize: '14.3px'
    }, 200);
  })
  $('.removeGoals').on('mouseleave', () => {
    $('.removeGoals').animate({
      fontSize: '14px'
    }, 200);
  })

  /* TOGGLE */
  /* Toggle function */
  $('.toggleGoals').on('click', () => {
    $('.outputSquare').fadeToggle();
  })
  /* Animated Nav Link */
  $('.toggleGoals').on('mouseenter', () => {
    $('.toggleGoals').animate({
      fontSize: '15px'
    }, 200);
  })
  $('.toggleGoals').on('mouseleave', () => {
    $('.toggleGoals').animate({
      fontSize: '14px'
    }, 200);
  })

  /* LOGO HOVER CREATOR NAME */
  /* MOUSEENTER */
  $('.navbar-brand').on('mouseenter', () => {
      $('.createList').hide()
    })
    .on('mouseenter', () => {
      $('.removeGoals').hide()
    })
    .on('mouseenter', () => {
      $('.toggleGoals').hide()
    })
    .on('mouseenter', () => {
      $('.appearingTextCreator').show()
    })
    /* MOUSELEAVE */
    .on('mouseleave', () => {
      $('.appearingTextCreator').hide()
    })
    .on('mouseleave', () => {
      $('.createList').show()
    })
    .on('mouseleave', () => {
      $('.removeGoals').show()
    })
    .on('mouseleave', () => {
      $('.toggleGoals').show()
    })

  /* OUTPUT (MANIPULATING) SCRIPTS */
  /* PROCESSING INPUT */
  $('#userInputButton').on('click', () => {
    /* Save input in variable. Clear and hide form */
    var goal = $("#userInput").val();
    $("#userInput").val("");
    $('.inputSquare').hide();
    /* Display output area containing empty table. Add goals as row in table. */
    $('.outputSquare').show();
    $('#outputTable').append('<tr><td>' + new Date().toLocaleDateString() + '</td><td>' +
      (goal) + '</td><td><div class="btn-toolbar" role="toolbar"><button id="buttonFinished" class="btn-group btn-group-sm btn-success" role="group" type="button"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button><button id="buttonRemove" class="btn-group btn-group-sm btn-danger" role="group" type="button"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></button></div></td></tr>');
  })

  /* Enter key-functionality */
  $('#userInput').keypress(function(e) {
    if (e.which == 13) { //Enter key pressed
      $('#userInputButton').click(); //Trigger #userInputButton click event
    }
  });


  /* buttonFinished (Checkmark-icon) */
  $(document).on('click', '#buttonFinished', event => {
    $(event.currentTarget).parent().parent().parent().css("text-decoration", "line-through")
    $(event.currentTarget).parent().parent().parent().fadeTo('slow', 0.7, function() {});
    $(event.currentTarget).remove(); /* Remove checkmark-icon */
  })

  jQuery(document).ready(function($) {
    document.getElementById("likeForm").submit();

    })
});
