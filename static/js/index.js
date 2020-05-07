// $(function () {
//     echart_map();


//     // echart_map中国地图
//     function echart_map() {

//         var myChart = echarts.init(document.getElementById('chart_map'));

//         var mapName = 'china'
//         var data = []
//         var toolTipData = [];

//         /*获取地图数据*/
//         myChart.showLoading();
//         var mapFeatures = echarts.getMap(mapName).geoJson.features;
//         myChart.hideLoading();
//         var geoCoordMap = {
//             '新疆': [86.61, 40.79],
//             '西藏': [89.13, 30.66],
//             '黑龙江': [128.34, 47.05],
//             '吉林': [126.32, 43.38],
//             '辽宁': [123.42, 41.29],
//             '内蒙古': [112.17, 42.81],
//             '北京': [116.40, 40.40],
//             '宁夏': [106.27, 36.76],
//             '山西': [111.95, 37.65],
//             '河北': [115.21, 38.44],
//             '天津': [117.04, 39.52],
//             '青海': [97.07, 35.62],
//             '甘肃': [103.82, 36.05],
//             '山东': [118.01, 36.37],
//             '陕西': [108.94, 34.46],
//             '河南': [113.46, 34.25],
//             '安徽': [117.28, 31.86],
//             '江苏': [120.26, 32.54],
//             '上海': [121.46, 31.28],
//             '四川': [103.36, 30.65],
//             '湖北': [112.29, 30.98],
//             '浙江': [120.15, 29.28],
//             '重庆': [107.51, 29.63],
//             '湖南': [112.08, 27.79],
//             '江西': [115.89, 27.97],
//             '贵州': [106.91, 26.67],
//             '福建': [118.31, 26.07],
//             '云南': [101.71, 24.84],
//             '台湾': [121.01, 23.54],
//             '广西': [108.67, 23.68],
//             '广东': [113.98, 22.82],
//             '海南': [110.03, 19.33],
//             '澳门': [113.54, 22.19],
//             '香港': [114.17, 22.32]
//         };


//         var GZData = [];


//         $(document).ready(function () {
//             getData();
//         });

//         function getData() {
//             $.ajax({
//                 url: 'test',
//                 data: {},
//                 type: 'POST',
//                 async: false,
//                 dataType: 'json',
//                 success: function (data) {
//                     var element = [
//                         [{
//                             //legname1:[],
//                             name: [],
//                             value: []
//                         }, {
//                             name: [],
//                             value: []
//                         }]
//                     ]
//                     var length = data.name_1.length
//                     console.log(data)
//                     console.log(typeof length)

//                     for (i = 0; i < length; i++) {
//                         var element = [
//                             [{
//                                 //legname1:[],
//                                 name: [],
//                                 value: []
//                             }, {
//                                 name: [],
//                                 value: []
//                             }]
//                         ]
//                         element[0][0].name = data.name_1[i];
//                         element[0][0].value = data.tempreture_1[i];
//                         element[0][1].name = data.name_2[i];
//                         element[0][1].value = data.tempreture_2[i];
//                         GZData = GZData.concat(element);
//                     }

//                     console.log(GZData);
//                     var convertData = function (dataa) {
//                         var res = [];
//                         for (var i = 0; i < dataa.length; i++) {
//                             var dataItem = dataa[i];
//                             var fromCoord = geoCoordMap[dataItem[0].name];
//                             var toCoord = geoCoordMap[dataItem[1].name];
//                             if (fromCoord && toCoord) {
//                                 res.push({
//                                     fromName: dataItem[0].name,
//                                     toName: dataItem[1].name,
//                                     coords: [fromCoord, toCoord]
//                                 });
//                             }
//                         }
//                         return res;
//                     };

//                     var color = ['#c5f80e'];
//                     var series = [];
//                     [
//                         ['疫苗运输线路', GZData]
//                     ].forEach(function (item, i) {
//                         series.push({
//                             name: item[0],
//                             type: 'lines',
//                             zlevel: 2,
//                             symbol: ['none', 'arrow'],
//                             symbolSize: 10,
//                             effect: {
//                                 show: true,
//                                 period: 6,
//                                 trailLength: 0,
//                                 symbol: 'arrow',
//                                 symbolSize: 5
//                             },
//                             lineStyle: {
//                                 normal: {
//                                     color: color[i],
//                                     width: 1,
//                                     opacity: 0.6,
//                                     curveness: 0.2
//                                 }
//                             },
//                             data: convertData(item[1])
//                         }, {
//                             name: item[0],
//                             type: 'effectScatter',
//                             coordinateSystem: 'geo',
//                             zlevel: 2,
//                             rippleEffect: {
//                                 brushType: 'stroke'
//                             },
//                             label: {
//                                 normal: {
//                                     show: true,
//                                     position: 'right',
//                                     formatter: '{b}'
//                                 }
//                             },
//                             symbol: 'circle',
//                             symbolSize: function (val) {
//                                 return val[2] / 8;
//                             },
//                             itemStyle: {
//                                 normal: {
//                                     color: color[i]
//                                 }
//                             },
//                             data: item[1].map(function (dataItem) {
//                                 return {
//                                     name: dataItem[1].name,
//                                     value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
//                                 };
//                             })
//                         }, {
//                             name: item[0],
//                             type: 'effectScatter',
//                             coordinateSystem: 'geo',
//                             zlevel: 2,
//                             rippleEffect: {
//                                 brushType: 'stroke'
//                             },
//                             label: {
//                                 normal: {
//                                     show: true,
//                                     position: 'right',
//                                     formatter: '{b}'
//                                 }
//                             },
//                             symbol: 'circle',
//                             symbolSize: function (val) {
//                                 return val[2] / 8;
//                             },
//                             itemStyle: {
//                                 normal: {
//                                     color: color[i]
//                                 }
//                             },
//                             data: item[1].map(function (dataItem) {
//                                 return {
//                                     name: dataItem[0].name,
//                                     value: geoCoordMap[dataItem[0].name].concat([dataItem[0].value])
//                                 };
//                             })
//                         });
//                     });
//                     option = {
//                         tooltip: {
//                             trigger: 'item'
//                         },
//                         geo: {
//                             map: 'china',
//                             label: {
//                                 emphasis: {
//                                     show: false
//                                 }
//                             },
//                             roam: true,
//                             itemStyle: {
//                                 normal: {
//                                     borderColor: 'rgba(147, 235, 248, 1)',
//                                     borderWidth: 1,
//                                     areaColor: {
//                                         type: 'radial',
//                                         x: 0.5,
//                                         y: 0.5,
//                                         r: 0.8,
//                                         colorStops: [{
//                                             offset: 0,
//                                             color: 'rgba(175,238,238, 0)' // 0% 处的颜色
//                                         }, {
//                                             offset: 1,
//                                             color: 'rgba(47,79,79, .1)' // 100% 处的颜色
//                                         }],
//                                         globalCoord: false // 缺省为 false
//                                     },
//                                     shadowColor: 'rgba(128, 217, 248, 1)',
//                                     // shadowColor: 'rgba(255, 255, 255, 1)',
//                                     shadowOffsetX: -2,
//                                     shadowOffsetY: 2,
//                                     shadowBlur: 10
//                                 },
//                                 emphasis: {
//                                     areaColor: '#389BB7',
//                                     borderWidth: 0
//                                 }
//                             }
//                         },
//                         series: series
//                     };

//                     // 使用刚指定的配置项和数据显示图表。
//                     myChart.setOption(option);
//                     window.addEventListener("resize", function () {
//                         myChart.resize();
//                     });

//                 },
//                 error: function (msg) {
//                     console.log(msg);
//                     alert('系统发生错误');
//                 }
//             })
//         }


//     }

//     //点击跳转
//     $('#chart_map').click(function () {
//         window.location.href = './page/index.html';
//     });
// });