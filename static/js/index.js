/*
I loved Virgil's Dribble shot and decided to remake
it with some SVG animations :) I didn't really want
to recreate the curvy line since I believe straight
lines are more accurate. Sorry Virgil, I might make
them curvy one day :)! With a bit of time on my 
hands I could make it even more detailed.
I hope you like it and post some feedback on how to
make this better :)!

Don't forget to check out the original at
http://goo.gl/0aKiS0

Kudos Virgil!*/


$(document).ready(function () {
    getemp();
});

function getemp() {
    $.ajax({
        url: 'temp',
        data: {},
        type: 'POST',
        async: false,
        dataType: 'json',
        success: function (data) {
            var length = data.tempreture_1.length

            var stepX = 77 / 14;
            console.log(data);

            var chart_2_y = [];
            for (i = 0; i < length; i++) {
                chart_2_y.push(data.tempreture_1[i])
            }
            //TODO 更新温度数值到指定范围内的映射
            function point(x, y) {
                x: 0;
                y: 0;
            }
            /* DRAW GRID */
            function drawGrid(graph) {
                var graph = Snap(graph);
                var g = graph.g();
                g.attr('id', 'grid');
                for (i = 0; i <= stepX + 2; i++) {
                    var horizontalLine = graph.path(
                        "M" + 0 + "," + stepX * i + " " +
                        "L" + 77 + "," + stepX * i);
                    horizontalLine.attr('class', 'horizontal');
                    g.add(horizontalLine);
                };
                for (i = 0; i <= 14; i++) {
                    var horizontalLine = graph.path(
                        "M" + stepX * i + "," + 38.7 + " " +
                        "L" + stepX * i + "," + 0)
                    horizontalLine.attr('class', 'vertical');
                    g.add(horizontalLine);
                };
            }
            drawGrid('#chart-2');

            function drawLineGraph(graph, points, container, id) {


                var graph = Snap(graph);


                /*END DRAW GRID*/

                /* PARSE POINTS */
                var myPoints = [];
                var shadowPoints = [];

                function parseData(points) {
                    for (i = 0; i < points.length; i++) {
                        var p = new point();
                        var pv = points[i] / 100 * 40;
                        p.x = 83.7 / points.length * i + 1;
                        p.y = 40 - pv;
                        if (p.x > 78) {
                            p.x = 78;
                        }
                        myPoints.push(p);
                    }
                }

                var segments = [];

                function createSegments(p_array) {
                    for (i = 0; i < p_array.length; i++) {
                        var seg = "L" + p_array[i].x + "," + p_array[i].y;
                        if (i === 0) {
                            seg = "M" + p_array[i].x + "," + p_array[i].y;
                        }
                        segments.push(seg);
                    }
                }

                function joinLine(segments_array, id) {
                    var line = segments_array.join(" ");
                    var line = graph.path(line);
                    line.attr('id', 'graph-' + id);
                    var lineLength = line.getTotalLength();

                    line.attr({
                        'stroke-dasharray': lineLength,
                        'stroke-dashoffset': lineLength
                    });
                }



                function showValues() {
                    var val1 = $(graph).find('.h-value');
                    var val2 = $(graph).find('.percentage-value');
                    val1.addClass('visible');
                    val2.addClass('visible');
                }

                function drawPolygon(segments, id) {
                    var lastel = segments[segments.length - 1];
                    var polySeg = segments.slice();
                    polySeg.push([78, 38.4], [1, 38.4]);
                    var polyLine = polySeg.join(' ').toString();
                    var replacedString = polyLine.replace(/L/g, '').replace(/M/g, "");

                    var poly = graph.polygon(replacedString);
                    var clip = graph.rect(-80, 0, 80, 40);
                    poly.attr({
                        'id': 'poly-' + id,
                        //'clipPath':'url(#clip)'
                        'clipPath': clip
                    });
                    clip.animate({
                        transform: 't80,0'
                    }, 1300, mina.linear);
                }
                parseData(points);

                createSegments(myPoints);
                // calculatePercentage(points, container);
                joinLine(segments, id);

                drawPolygon(segments, id);


                /*$('#poly-'+id).attr('class','show');*/

                /* function drawPolygon(segments,id){
                  var polySeg = segments;
                  polySeg.push([80,40],[0,40]);
                  var polyLine = segments.join(' ').toString();
                  var replacedString = polyLine.replace(/L/g,'').replace(/M/g,"");
                  var poly = graph.polygon(replacedString);
                  poly.attr('id','poly-'+id)
                }
                drawPolygon(segments,id);*/
            }
            // drawLineGraph('#chart-1', chart_1_y, '#graph-1-container', 2);
            drawLineGraph('#chart-2', chart_2_y, '#graph-2-container', 2);
        }
    })
}