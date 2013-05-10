var app = app || {};

app.displayCharts = function(school_pk, grade) {
  $.ajax({
    url: '/api/v1/school_curricula/' + school_pk + '/?format=json&grade=' + grade,
    success: function(resp) {
      scores = JSON.parse(resp.curriculum.pssa_test_scores);

      var sortedScores = scores.sort(function(a, b){
        return a.year_start - b.year_start;
      });

      app.createChart(sortedScores, 'reading');
      app.createChart(sortedScores, 'math');
    }
  });
};

app.chartMapping = {
  'reading': [
    'read_below_basic_percent',
    'read_basic_percent',
    'read_proficient_percent',
    'read_advanced_percent'
  ],
  'math': [
    'math_below_basic_percent',
    'math_basic_percent',
    'math_proficient_percent',
    'math_advanced_percent'
  ]
};

app.createChart = function(scores, subject) {
  var mapping = app.chartMapping[subject];
  var $container = $('#' + subject + '-scores.scores-container');
  var has_scores = scores.length > 1
  if (has_scores) {
    $container.append('<strong>PSSA scores in ' + subject + ' for this grade at this school for the past 4 years</strong>');
  }
  for(var i=0; i<scores.length; i++) {
    if(scores[i].year_start === 2012) { continue; } // We don't have 2012-13 scores
    var html = 
      "<div class='scores'>" +
        "<span class='year'>" + scores[i].year_start  + "-" + String(scores[i].year_end).slice(2, 4) + "</span>" +
        "<div class='steps'>" +
          "<span class='tooltip' title='Below basic: " + scores[i][mapping[0]] + "%'>" + 
            "<div class='step step1' style='width:" + scores[i][mapping[0]] + "%;'></div>" +
          "</span>" + 
          "<span class='tooltip' title='Basic: " + scores[i][mapping[1]] + "%'>" + 
            "<div class='step step2' style='width:" + scores[i][mapping[1]] + "%;'></div>" + 
          "</span>" + 
          "<span class='tooltip' title='Proficient: " + scores[i][mapping[2]] + "%'>" +
            "<div class='step step3' style='width:" + scores[i][mapping[2]] + "%;'></div>" +
          "</span>" +
          "<span class='tooltip' title='Advanced: " + scores[i][mapping[3]] + "%'>" +
            "<div class='step step4' style='width:" + (scores[i][mapping[3]] - 0.1) + "%;'></div>" +
          "</span>" +
        "</div>" +
      "</div>";
    $container.append(html);
  }
  if (has_scores) { 
    $container.append('<hr>');
  }
  $('.tooltip').tooltipster({
      maxWidth: 250
    });
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