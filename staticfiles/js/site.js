// Utilities
if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// jQuery global instatiations
$(document).ready(function()
  {
    $("#matched-grade-curricula").tablesorter({
      widgets: ['zebra'],
      sortList: [[2,0],[1,0],[4,0]]
    });
    $(".tablesorter").tablesorter({
      sortList: [[0,0]]
    });
    $('.tooltip').tooltipster({
      maxWidth: 250
    });
  }
);

// Search

var schoolObjects;

function setupAutoComplete(resp) {
  schoolObjects = resp.objects;
  var sourceList = [];

  for(var i=0; i<schoolObjects.length; i++) {
    sourceList.push(schoolObjects[i].name);
  }

  $("#search").autocomplete({
    source: sourceList,
    minLength: 2,
    delay: 0
  });
}

$.ajax({
  url: '/api/v1/schools/?format=json',
  success: function(resp) {
    setupAutoComplete(resp);
  }
});

$("#search").on("autocompleteselect", function(event, ui) {
  var school;

  for(var i=0; i<schoolObjects.length; i++) {
    if(schoolObjects[i].name === ui.item.value) {
      school = schoolObjects[i];
      break;
    }
  }

  window.location = '/school/' + school.school_code;
});

// Create data binding for "change assumptions" feature

var prices = prices || {};
$('.needed-material input').on('change', function() {
  var needed = this;
  var $difference = $(needed).parent().next('.material-difference');
  var $container = $(needed).parents('.tablesorter');
  // What's the difference between input value and the original value?
  var calc = Number(needed.value - needed.defaultValue);
  var originalDifference = $difference.attr('data-original-difference');
  // Compute the current difference for that material
  var currentDifference = originalDifference - calc;
  $difference.html(currentDifference);
  if (currentDifference >= 0) {
    $difference.next('td').removeClass('notEnough').addClass('enough')
    .find('.icon').html('1');
  }
  else {
    $difference.next('td').removeClass('enough').addClass('notEnough')
    .find('.icon').html('-1');
  }
  if (currentDifference > 0) {
    return;
  }
  var materialPk = $difference.attr('data-material-pk');
  // Locate the container of the shortfall info
  var $shortfallDetail = $container.next('.shortfall-detail');
  var $shortfallCost = $shortfallDetail.find('.shortfall-cost');
  var $shortfallCount = $shortfallDetail.find('.shortfall-count');
  var shortfallCount = 0;
  var shortfallCost = 0;
  $container.find('.material-difference').each(function(){
    var diff = this.innerHTML.trim();
    if (diff < 0) {
      // Increase the shortfall count by subtracting the negative diff
      shortfallCount = shortfallCount - diff;
      var materialPk = $(this).attr('data-material-pk');
      var materialKey = 'key' + materialPk;
      // If we have the price, get it
      var price;
      if(prices[materialKey]) {
        price = prices[materialKey];
        shortfallCost += price * (diff * -1);
      }
      // Otherwise go get it
      else {
          $.ajax({
            url: '/api/v1/learning_material/' + materialPk,
            success: function(resp){
              if(resp.prices.length > 1) {
                for (var i = resp.prices.length - 1; i >= 0; i--) {
                  if(resp.prices[i].types.length > 1) {
                    for (var j = resp.prices[i].types.length - 1; j >= 0; j--) {
                      if(resp.prices[i].types[j].name == school_type) {
                        price = Number(resp.prices[i].value);
                        return;
                      }
                    }
                  }
                }
              } else {
                price = Number(resp.prices[0].value);
              }
              prices[materialKey] = price;
              shortfallCost += price * (diff * -1);
              $shortfallCost.html('$' + numberWithCommas(shortfallCost.toFixed(2)));
            }
          });
      }
    }
    $shortfallCount.html(shortfallCount);
    $shortfallCost.html('$' + numberWithCommas(shortfallCost.toFixed(2)));
    $shortfallCount.addClass('changed');
    $shortfallCost.addClass('changed');
    window.setTimeout(function() {
      $shortfallCount.removeClass('changed');
      $shortfallCost.removeClass('changed');
    }, 600);
  });
});
