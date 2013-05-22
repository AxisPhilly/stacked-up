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

// APP
var app = app || {};

app.getChartData = function(school_pk, grade) {
  $.when(
    $.ajax({
      url: '/api/v1/school_curricula/' + school_pk + '/?format=json&grade=' + grade
    }),
    $.ajax({
      dataType: 'json',
      url: '/static/data/pssa.json'
    })
  ).then(function(schoolInfo, districtInfo) {
    var schoolScores = app.formatPSSASchoolData(JSON.parse(schoolInfo[0].curriculum.pssa_test_scores));
    var districtScores = districtInfo[0][grade];
    if(schoolScores.read.length > 1) {
      app.createChart(schoolScores, districtScores, 'read', 'reading-scores', 'reading-chart-title');
      app.createChart(schoolScores, districtScores, 'math', 'math-scores', 'math-chart-title');
    }
  });
};

app.formatPSSASchoolData = function(scores) {
  var fScores = {
    "read": [],
    "math": []
  };

  for(var i=0; i<scores.length; i++) {
    fScores.read.push(scores[i].read_combined_percent);
    fScores.math.push(scores[i].math_combined_percent);
  }

  return fScores;
};

app.createChart = function(schoolScores, districtScores, subject, container, titleContainer) {
  var chart = new CanvasJS.Chart(container, {
    title: {
      fontSize: 12
    },
    theme: "theme2",
    axisX: {
      // we are cheating here and using the month value as the
      // second part of the school year in the x label
      valueFormatString: "YYYY-MM",
      lineThickness: 0,
      labelFontSize: 0,
      tickThickness: 0,
      tickLength: 0
    },
    axisY: {
      valueFormatString: "#'%'",
      lineThickness: 0,
      labelFontSize: 12
    },
    toolTip: {
      shared: true,
      borderColor: "#ffffff"
    },
    data: [
      {
        type: "line",
        markerSize: 5,
        color: "#aaa",
        lineThickness: 1,
        name: "District",
        dataPoints: [
          {x: new Date(2008,08,1), y: districtScores[subject][0]},
          {x: new Date(2009,09,1), y: districtScores[subject][1]},
          {x: new Date(2010,10,1), y: districtScores[subject][2]},
          {x: new Date(2011,11,1), y: districtScores[subject][3]}
        ]
      },
      {
        type: "line",
        markerSize: 5,
        color: "#1fb4fc",
        lineThickness: 1,
        name: "School",
        dataPoints: [
          {x: new Date(2008,08,01), y: schoolScores[subject][0]},
          {x: new Date(2009,09,01), y: schoolScores[subject][1]},
          {x: new Date(2010,10,01), y: schoolScores[subject][2]},
          {x: new Date(2011,11,01), y: schoolScores[subject][3]}
        ]
      }
    ]
  });
  chart.render();

  var sub = subject === "read" ? "Reading" : "Mathematics";
  $('#' + titleContainer).html('<div class="chart-caption">PSSA ' + sub + ' Scores</div>');
};

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
