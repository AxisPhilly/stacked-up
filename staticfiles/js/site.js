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
      url: '/static/data/pssa.json'
    })
  ).then(function(schoolInfo, districtInfo) {
    var schoolScores = app.formatPSSASchoolData(JSON.parse(schoolInfo[0].curriculum.pssa_test_scores));
    var districtScores = JSON.parse(districtInfo[0][grade]);
    console.log(schoolScores);
    console.log(districtScores);
    console.log(districtInfo);
    if(schoolScores.read.length > 1) {
      app.createChart(schoolScores, districtScores, 'read', 'reading-scores');
      app.createChart(schoolScores, districtScores, 'math', 'math-scores');
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

app.createChart = function(schoolScores, districtScores, subject, container) {
  $('#' + container).addClass('scores-container');
  var chart = new CanvasJS.Chart(container, {  
    title: {
      text: "PSSA " + subject + " combined percent scores",
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
      valueFormatString: "#'%'"
    },
    toolTip: {
      shared: true
    },
    data: [
      {
        type: "line",
        lineThickness: 2,
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
        lineThickness: 2,
        name: "School",
        dataPoints: [
          {x: new Date(2008,08,01), y: schoolScores[subject][0]},
          {x: new Date(2009,09,01), y: schoolScores[subject][1]},
          {x: new Date(2010,10,01), y: schoolScores[subject][2]},
          {x: new Date(2011,11,01), y: schoolScores[subject][3]},
        ]
      }
    ]
  });
  chart.render();
};

// jQuery global instatiations
$(document).ready(function() 
  { 
    $("#matched-grade-curricula").tablesorter({ 
      widgets: ['zebra'],
      sortList: [[2,0],[1,0],[4,0]]        
    });
    $(".tablesorter").tablesorter({ 
      widgets: ['zebra']
    });
    $('.tooltip').tooltipster({
      maxWidth: 250
    });
  } 
);

// Search

$(document).ready(function() {
  var schoolObjects;

  $.ajax({
    url: '/api/v1/schools/?format=json',
    success: function(resp) {
      setupAutoComplete(resp);
    },
    select: function(event, ui) {

    }
  });

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
    $difference.next('td').removeClass('notEnough unknown').addClass('enough');
  }
  else {
    $difference.next('td').removeClass('enough unknown').addClass('notEnough');
  }
  if (currentDifference > 0) {
    return;
  }
  var materialPk = $difference.attr('data-material-pk');
  // Locate the container of the shortfall info
  var $shortfallDetail = $(needed).parents('.tablesorter').next('.shortfall-detail');
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
              // TODO Make sure we get the right price
              price = Number(resp.prices[0].value);
              prices[materialKey] = price;
              shortfallCost += price * (diff * -1);
              $shortfallCost.html(numberWithCommas(shortfallCost.toFixed(2)));
            }
          });
      }
    }
    $shortfallCount.html(shortfallCount);
    $shortfallCost.html(numberWithCommas(shortfallCost.toFixed(2)));
  });
});
